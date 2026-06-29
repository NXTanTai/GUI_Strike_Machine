import asyncio
import json
import logging
import logging.handlers
import os
import sys
from datetime import datetime
from pathlib import Path

import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, FileResponse
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK

app = FastAPI()
_all_data: dict[str, dict] = {}

def _setup_logger() -> logging.Logger:
    log_dir = Path("WebLog")
    log_dir.mkdir(exist_ok=True)

    date_str = datetime.now().strftime("%d-%m-%Y")
    log_file  = log_dir / f"log_central_{date_str}.log"

    logger = logging.getLogger("central_server")
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

    logging.getLogger("websockets").setLevel(logging.CRITICAL)
    logging.getLogger("websockets.protocol").setLevel(logging.CRITICAL)
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)

    return logger

class ConnectionManager:
    def __init__(self):
        self._lock    = asyncio.Lock()
        self._clients: set[WebSocket] = set()

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        async with self._lock:
            self._clients.add(ws)

    async def disconnect(self, ws: WebSocket) -> None:
        async with self._lock:
            self._clients.discard(ws)

    async def broadcast(self, data: str) -> None:
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

@app.get("/favicon.png")
async def favicon():
    return FileResponse(
        os.path.join(os.path.dirname(__file__), "icons", "strike_machine.png"),
        media_type="image/png",
    )

@app.get("/")
async def index():
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard_central.html")
    try:
        with open(html_path, encoding="utf-8") as f:
            return HTMLResponse(f.read())
    except FileNotFoundError:
        return HTMLResponse(f"<h2>dashboard_central.html không tìm thấy tại: {html_path}</h2>", status_code=404)

@app.post("/data")
async def receive_data(payload: dict):
    """
    Nhận data từ web_client.py trên mỗi máy Strike.
    Payload: { "machine_id": "machine_a", "ip": "192.168.1.10", "data": {...} }
    """
    logger     = logging.getLogger("central_server")
    machine_id = payload.get("machine_id")
    ip         = payload.get("ip", "unknown")
    data       = payload.get("data", {})

    if not machine_id:
        return {"error": "missing machine_id"}

    if machine_id not in _all_data:
        logger.info("New machine connected: %s (%s)", machine_id, ip)

    _all_data[machine_id] = {"_ip": ip, **data}

    if manager.count > 0:
        await manager.broadcast(json.dumps(_all_data))

    return {"ok": True}

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    logger    = logging.getLogger("central_server")
    await manager.connect(ws)
    client_id = str(ws.client)
    logger.info("Dashboard connected: %s  (total: %d)", client_id, manager.count)

    try:
        await ws.send_text(json.dumps(_all_data))
    except Exception:
        pass

    try:
        while True:
            try:
                await asyncio.wait_for(ws.receive_text(), timeout=30)
            except asyncio.TimeoutError:
                pass  # keepalive — không làm gì

    except (WebSocketDisconnect, ConnectionClosedOK):
        logger.info("Dashboard disconnected normally: %s", client_id)

    except ConnectionClosedError as e:
        logger.warning("Dashboard lost (timeout): %s — %s", client_id, e)

    except Exception as e:
        logger.error("WebSocket error [%s]: %s", client_id, e)

    finally:
        await manager.disconnect(ws)
        logger.info("Dashboard removed: %s  (remaining: %d)", client_id, manager.count)

_reload_clients: set[WebSocket] = set()

@app.websocket("/hot-reload")
async def hot_reload_ws(ws: WebSocket):
    await ws.accept()
    _reload_clients.add(ws)
    try:
        await ws.receive_text()
    except Exception:
        pass
    finally:
        _reload_clients.discard(ws)

async def _broadcast_reload():
    dead = set()
    for ws in _reload_clients:
        try:
            await ws.send_text("reload")
        except Exception:
            dead.add(ws)
    _reload_clients -= dead

def main():
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")

    logger = _setup_logger()
    logger.info("Central server starting on port 9000...")

    try:
        class HtmlWatcher(FileSystemEventHandler):
            def __init__(self, loop):
                self._loop = loop
            def on_modified(self, event):
                if str(event.src_path).endswith(".html"):
                    asyncio.run_coroutine_threadsafe(_broadcast_reload(), self._loop)

        async def _start_with_watcher():
            loop = asyncio.get_event_loop()
            observer = Observer()
            observer.schedule(HtmlWatcher(loop), path=".", recursive=False)
            observer.start()
            logger.info("Hot reload enabled — edit dashboard_central.html and save")

            config = uvicorn.Config(
                app, host="0.0.0.0", port=9000,
                log_config=None, log_level="critical",
                ws_ping_interval=30, ws_ping_timeout=60,
            )
            server = uvicorn.Server(config)
            logger.info("Uvicorn listening on :9000")
            await server.serve()

        asyncio.run(_start_with_watcher())

    except ImportError:
        logger.info("watchdog not installed — hot reload disabled")
        logger.info("Install: pip install watchdog")

        config = uvicorn.Config(
            app, host="0.0.0.0", port=9000,
            log_config=None, log_level="critical",
            ws_ping_interval=30, ws_ping_timeout=60,
        )
        uvicorn.run(app, host="0.0.0.0", port=9000, log_level="critical")


if __name__ == "__main__":
    main()