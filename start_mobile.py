#!/usr/bin/env python3
"""Serve the static page on the local network so a phone can open it."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import socket
import sys


PROJECT_DIR = Path(__file__).resolve().parent
PORT = 8766


class PageHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_DIR), **kwargs)

    def log_message(self, format_string, *args):
        print(f"[page] {self.address_string()} - {format_string % args}")


def local_ip() -> str | None:
    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(("192.0.2.1", 80))
        address = probe.getsockname()[0]
        return address if not address.startswith("127.") else None
    except OSError:
        return None
    finally:
        probe.close()


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", PORT), PageHandler)
    address = local_ip()
    print("梅间一卦手机预览服务已启动。")
    print(f"本机浏览器：http://127.0.0.1:{PORT}/")
    if address:
        print(f"同一 Wi-Fi 下的手机访问：http://{address}:{PORT}/")
    else:
        print(f"请在同一 Wi-Fi 下，将电脑局域网 IP 填入：http://电脑IP:{PORT}/")
    print("请保持此窗口开启；按 Ctrl+C 停止服务。")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n手机预览服务已停止。")
    finally:
        server.server_close()


if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        print(f"无法启动手机预览服务：{error}", file=sys.stderr)
        raise SystemExit(1) from error
