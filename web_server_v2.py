import asyncio
import json
import logging
import logging.handlers
import multiprocessing
import os
import re
import subprocess
import sys
import threading
from datetime import datetime
from pathlib import Path

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK

app = FastAPI()
_plc_data: dict = {}

def _setup_logger() -> logging.Logger:
    log_dir = Path("WebLog")
    log_dir.mkdir(exist_ok=True)

    date_str = datetime.now().strftime("%d-%m-%Y")
    log_file = log_dir / f"log_web_{date_str}.log"

    logger = logging.getLogger("web_server")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    fmt = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger

class ConnectionManager:
    def __init__(self):
        self._lock = asyncio.Lock()
        self._clients: set[WebSocket] = set()

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        async with self._lock:
            self._clients.add(ws)

    async def disconnect(self, ws: WebSocket) -> None:
        async with self._lock:
            self._clients.discard(ws)

    async def broadcast(self, data: str) -> None:
        """Gửi data đến tất cả clients, tự xóa client đã chết."""
        dead: set[WebSocket] = set()
        async with self._lock:
            clients = set(self._clients)

        for ws in clients:
            try:
                await ws.send_text(data)
            except Exception:
                dead.add(ws)

        if dead:
            async with self._lock:
                self._clients -= dead

    @property
    def count(self) -> int:
        return len(self._clients)


manager = ConnectionManager()

@app.get("/")
async def index():
    try:
        with open("dashboard.html", encoding="utf-8") as f:
            return HTMLResponse(
                f.read(), headers={"Content-Type": "text/html; charset=utf-8"}
            )
    except FileNotFoundError:
        return HTMLResponse("<h2>dashboard.html không tìm thấy</h2>", status_code=404)


@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    logger = logging.getLogger("web_server")
    await manager.connect(ws)
    client_id = str(ws.client)
    logger.info("Client connected: %s  (total: %d)", client_id, manager.count)

    try:
        while True:
            await ws.send_text(json.dumps(_plc_data))

            try:
                await asyncio.wait_for(ws.receive_text(), timeout=0.5)
            except asyncio.TimeoutError:
                pass  # Bình thường — client không gửi gì, tiếp tục vòng lặp

    except (WebSocketDisconnect, ConnectionClosedOK):
        logger.info("Client disconnected normally: %s", client_id)

    except ConnectionClosedError as e:
        logger.warning(
            "Client lost (keepalive timeout / network drop): %s — %s",
            client_id, e,
        )

    except Exception as e:
        logger.error("WebSocket unexpected error [%s]: %s", client_id, e)

    finally:
        await manager.disconnect(ws)
        logger.info(
            "Client removed: %s  (remaining: %d)", client_id, manager.count
        )

async def _queue_reader(queue: multiprocessing.Queue) -> None:
    """
    Đọc data từ PLC process qua multiprocessing.Queue.
    Dùng run_in_executor để không block event loop.
    """
    loop = asyncio.get_event_loop()
    logger = logging.getLogger("web_server")

    while True:
        try:
            data = await loop.run_in_executor(None, queue.get)
            _plc_data.update(data)
        except (EOFError, OSError):
            logger.warning("PLC queue closed, stopping queue reader.")
            break
        except Exception as e:
            logger.error("Queue read error: %s", e)
            await asyncio.sleep(0.1)

def _start_cloudflare(logger: logging.Logger) -> None:
    try:
        proc = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", "http://localhost:8000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        for line in proc.stdout:  # type: ignore
            match = re.search(r"https://[a-z0-9\-]+\.trycloudflare\.com", line)
            if match:
                logger.info("Dashboard URL: %s", match.group())
    except FileNotFoundError:
        logger.warning(
            "cloudflared không tìm thấy — cài bằng: winget install Cloudflare.cloudflared"
        )
    except Exception as e:
        logger.error("Cloudflare tunnel error: %s", e)

def run_web_server(queue: multiprocessing.Queue) -> None:
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")

    logger = _setup_logger()
    logger.info("Web server starting...")

    threading.Thread(target=_start_cloudflare, args=(logger,), daemon=True).start()

    async def _main() -> None:
        asyncio.create_task(_queue_reader(queue))

        config = uvicorn.Config(
            app,
            host="0.0.0.0",
            port=8000,
            log_config=None,
            log_level="critical",
            ws_ping_interval=30,   # gửi ping mỗi 30s (mặc định 20s) | Tăng timeout ping để giảm false-positive disconnect 
            ws_ping_timeout=60,    # chờ pong tối đa 60s (mặc định 20s) 
        )
        server = uvicorn.Server(config)
        logger.info("Uvicorn listening on port 8000")
        await server.serve()

    try:
        asyncio.run(_main())
    except Exception as e:
        logger.critical("Web server crashed: %s", e)