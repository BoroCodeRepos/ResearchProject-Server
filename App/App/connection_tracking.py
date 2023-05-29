from socket import *
from threading import *
from http.client import *
from App.settings import DEVICE_TOKEN, SERVER_PORT, DEVICE_SERVER_PORT, CONNECTION_TRACKING_STOP_EVENT
from time import sleep

def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def device_disconnect(KEY, MAC, HOST):
    head = {'Content-type': 'application/x-www-form-urlencoded'}
    body = f"KEY={KEY}&MAC={MAC}&IP={HOST}"
    conn = HTTPConnection(host=get_ip(), port=SERVER_PORT)
    conn.request("POST", "/device/disconnect/", body, head)
    return conn.getresponse()

def ConnectionTracking(HOST, MAC):
    CONNECTION_TRACKING_STOP_EVENT.clear()
    thread = Thread(target=ConnectionTrackingThread, args=(HOST, MAC))
    thread.start()

def ConnectionTrackingThread(HOST, MAC):
    conn = HTTPConnection(host=HOST, port=DEVICE_SERVER_PORT, timeout=1)
    while True:
        if CONNECTION_TRACKING_STOP_EVENT.is_set():
            break
        try:
            conn.request("GET", "/ping/")
            conn.getresponse()
            sleep(1)
        except timeout:
            if CONNECTION_TRACKING_STOP_EVENT.is_set():
                break
            conn.close()
            device_disconnect(DEVICE_TOKEN, MAC, HOST)
            break
            
    