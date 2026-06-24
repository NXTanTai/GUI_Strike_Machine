import asyncio
import json
import logging
import multiprocessing
import os
import re
import subprocess
import sys
import threading
from datetime import datetime
from pathlib import Path

import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
_plc_data = {}
_clients  = []

def _setup_logger() -> logging.Logger:
    log_dir = Path("WebLog")
    log_dir.mkdir(exist_ok=True)

    date_str  = datetime.now().strftime("%d-%m-%Y")
    log_file  = log_dir / f"log_web_{date_str}.log"

    logger = logging.getLogger("web_server")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    fmt = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger

@app.get("/")
async def index():
    with open("dashboard.html", encoding="utf-8") as f:
        return HTMLResponse(f.read(), headers={"Content-Type": "text/html; charset=utf-8"})

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    _clients.append(ws)
    logger = logging.getLogger("web_server")
    logger.info("Client connected: %s", ws.client)
    try:
        while True:
            await asyncio.sleep(0.5)
            await ws.send_text(json.dumps(_plc_data))
    except Exception:
        logger.warning("Client disconnected: %s", ws.client)
        _clients.remove(ws)

async def _queue_reader(queue: multiprocessing.Queue):
    loop   = asyncio.get_event_loop()
    logger = logging.getLogger("web_server")
    while True:
        try:
            data = await loop.run_in_executor(None, queue.get)
            _plc_data.update(data)
        except Exception as e:
            logger.error("Queue read error: %s", e)
            await asyncio.sleep(0.1)

def _start_cloudflare(logger: logging.Logger):
    try:
        proc = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", "http://localhost:8000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for line in proc.stdout:
            match = re.search(r'https://[a-z0-9\-]+\.trycloudflare\.com', line)
            if match:
                logger.info("Dashboard URL: %s", match.group())
    except FileNotFoundError:
        logger.error("cloudflared not found — run: winget install Cloudflare.cloudflared")
    except Exception as e:
        logger.error("Cloudflare tunnel error: %s", e)

def run_web_server(queue: multiprocessing.Queue):
    if sys.stdout is None:
        sys.stdout = open(os.devnull, 'w')
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w')

    logger = _setup_logger()
    logger.info("Web server starting...")

    threading.Thread(
        target=_start_cloudflare,
        args=(logger,),
        daemon=True
    ).start()

    async def _main():
        asyncio.create_task(_queue_reader(queue))
        config = uvicorn.Config(
            app,
            host="0.0.0.0",
            port=8000,
            log_config=None,
            log_level="critical",
        )
        server = uvicorn.Server(config)
        logger.info("Uvicorn listening on port 8000")
        await server.serve()

    try:
        asyncio.run(_main())
    except Exception as e:
        logger.critical("Web server crashed: %s", e)