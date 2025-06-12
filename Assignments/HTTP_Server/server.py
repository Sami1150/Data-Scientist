import socket
import json
import re
import threading
from typing import List, Dict, Optional

HOST: str = '127.0.0.1'
PORT: int = 8000
ITEMS_PATH: str = '/items'
shutdown_event = threading.Event()

def loadData() -> List[Dict[str, object]]:
    """
    Load data from data.json file.
    Each item has keys: 'id' (int) and 'name' (str).
    """
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def get_item_by_id(items: List[Dict[str, object]], item_id: int) -> Optional[Dict[str, object]]:
    for item in items:
        if item.get("id") == item_id:
            return item
    return None

def handle_client(client_socket: socket.socket) -> None:
    http_request: str = client_socket.recv(1024).decode('utf-8')
    

    pattern: str = r'^(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD) (\S+) HTTP/'
    match = re.search(pattern, http_request)

    if not match:
        response = "HTTP/1.1 400 Bad Request\r\nConnection: close\r\n\r\n"
        client_socket.sendall(response.encode())
        client_socket.close()
        return

    method: str = match.group(1)
    request_path: str = match.group(2)
    items: List[Dict[str, object]] = loadData()

    if method != 'GET':
        response_body = json.dumps({"error": "Method Not Allowed"})
        response = (
            "HTTP/1.1 405 Method Not Allowed\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "Connection: close\r\n\r\n" + response_body
        )

    elif request_path == ITEMS_PATH:
        response_body = json.dumps(items)
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "Connection: close\r\n\r\n" + response_body
        )

    elif re.fullmatch(rf"{ITEMS_PATH}/\d+", request_path):
        try:
            item_id: int = int(request_path.split("/")[-1])
            item: Optional[Dict[str, object]] = get_item_by_id(items, item_id)
            if item:
                response_body = json.dumps(item)
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: application/json\r\n"
                    f"Content-Length: {len(response_body)}\r\n"
                    "Connection: close\r\n\r\n" + response_body
                )
            else:
                response_body = json.dumps({"error": "Item Not Found"})
                response = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: application/json\r\n"
                    f"Content-Length: {len(response_body)}\r\n"
                    "Connection: close\r\n\r\n" + response_body
                )
        except ValueError:
            response = "HTTP/1.1 400 Bad Request\r\nConnection: close\r\n\r\n"

    else:
        response_body = json.dumps({"error": "Not Found"})
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "Connection: close\r\n\r\n" + response_body
        )

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def start_server() -> None:
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[*] Server running on http://{HOST}:{PORT}")

    try:
        while not shutdown_event.is_set():
            server_socket.settimeout(1.0)
            try:
                client_socket, addr = server_socket.accept()
                print(f"[+] Connected by {addr}")
                handle_client(client_socket)
            except socket.timeout:
                continue
    except Exception as e:
        print(f"[!] Server error: {e}")
    except KeyboardInterrupt as e:
        server_socket.close()
        print("[*] Server shut down.")
    finally:
        server_socket.close()
        print("[*] Server shut down.")

# Start server in a background thread (safe for Jupyter)
server_thread = threading.Thread(target=start_server)
server_thread.start()
