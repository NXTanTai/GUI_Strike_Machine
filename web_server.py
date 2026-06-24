import asyncio
import json
import multiprocessing
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
_plc_data = {}
_clients = []

@app.get("/")
async def index():
    with open("dashboard.html") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    _clients.append(ws)
    try:
        while True:
            await asyncio.sleep(0.5)
            await ws.send_text(json.dumps(_plc_data))
    except:
        _clients.remove(ws)

async def _queue_reader(queue: multiprocessing.Queue):
    loop = asyncio.get_event_loop()
    while True:
        try:
            data = await loop.run_in_executor(None, queue.get)
            _plc_data.update(data)
        except Exception:
            await asyncio.sleep(0.1)

def run_web_server(queue: multiprocessing.Queue):
    """Entry point cho process riêng"""
    async def _main():
        asyncio.create_task(_queue_reader(queue))
        config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="warning")
        server = uvicorn.Server(config)
        await server.serve()
    asyncio.run(_main())