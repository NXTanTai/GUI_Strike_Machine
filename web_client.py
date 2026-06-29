import asyncio
import json
import logging
import logging.handlers
import multiprocessing
import os
import socket
import sys
import threading
from datetime import datetime
from pathlib import Path
import httpx

MACHINE_ID     = "machine_#1"          # "machine_a" | "machine_b" | "machine_c"
CENTRAL_URL    = "http://192.168.1.100:9000"  # IP + port của Central Server
PUSH_INTERVAL  = 0.5                  # giây — push lên server mỗi 0.5s

def _get_local_ip() -> str:
    """Lấy IP LAN của máy hiện tại."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "unknown"

def _setup_logger() -> logging.Logger:
    log_dir = Path("WebLog")
    log_dir.mkdir(exist_ok=True)

    date_str = datetime.now().strftime("%d-%m-%Y")
    log_file  = log_dir / f"log_client_{date_str}.log"

    logger = logging.getLogger("web_client")
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

    logging.getLogger("httpx").setLevel(logging.CRITICAL)
    logging.getLogger("httpcore").setLevel(logging.CRITICAL)

    return logger

_plc_data: dict = {}
_local_ip: str  = _get_local_ip()


async def _queue_reader(queue: multiprocessing.Queue) -> None:
    loop   = asyncio.get_event_loop()
    logger = logging.getLogger("web_client")

    while True:
        try:
            data = await loop.run_in_executor(None, queue.get)
            _plc_data.update(data)
        except (EOFError, OSError):
            logger.warning("PLC queue closed.")
            break
        except Exception as e:
            logger.error("Queue read error: %s", e)
            await asyncio.sleep(0.1)

async def _push_loop(logger: logging.Logger) -> None:
    """
    Push data lên Central Server định kỳ.
    Dùng httpx.AsyncClient với timeout ngắn — không block nếu server mất.
    """
    url     = f"{CENTRAL_URL.rstrip('/')}/data"
    headers = {"Content-Type": "application/json"}

    _last_fail  = False
    _fail_count = 0

    async with httpx.AsyncClient(timeout=2.0) as client:
        while True:
            await asyncio.sleep(PUSH_INTERVAL)

            if not _plc_data:
                continue

            payload = {
                "machine_id": MACHINE_ID,
                "ip":         _local_ip,
                "data":       _plc_data.copy(),
            }

            try:
                resp = await client.post(url, content=json.dumps(payload), headers=headers)
                resp.raise_for_status()

                if _last_fail:
                    logger.info("Reconnected to central server: %s", CENTRAL_URL)
                    _last_fail  = False
                    _fail_count = 0

            except httpx.ConnectError:
                _fail_count += 1
                if not _last_fail or _fail_count % 60 == 0:
                    logger.warning(
                        "Cannot connect to central server: %s (attempt %d)",
                        CENTRAL_URL, _fail_count,
                    )
                _last_fail = True

            except httpx.TimeoutException:
                logger.warning("Push timeout — central server slow or unreachable.")

            except httpx.HTTPStatusError as e:
                logger.error("Central server returned error: %s", e)

            except Exception as e:
                logger.error("Push error: %s", e)


def run_web_client(queue: multiprocessing.Queue) -> None:
    """
    Entry point — gọi từ main.py giống như run_web_server.

    Ví dụ trong main.py:
        from web_client import run_web_client
        p = multiprocessing.Process(target=run_web_client, args=(plc_queue,))
        p.start()
    """
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")

    logger = _setup_logger()
    logger.info(
        "Web client starting — machine_id=%s  ip=%s  central=%s",
        MACHINE_ID, _local_ip, CENTRAL_URL,
    )

    async def _main() -> None:
        asyncio.create_task(_queue_reader(queue))
        await _push_loop(logger)

    try:
        asyncio.run(_main())
    except Exception as e:
        logger.critical("Web client crashed: %s", e)