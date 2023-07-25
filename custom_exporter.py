from prometheus_client import start_http_server, Gauge
import time
import os

APP_PORT=8000
MAC_ADDRESS=os.getenv('MAC_ADDRESS')
g = Gauge('uptime_seconds', 'Description of gauge', ['mac_address'])

def process_request(t):
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        g.labels(mac_address=MAC_ADDRESS).set(uptime_seconds)

if __name__ == '__main__':
    start_http_server(APP_PORT)
    print("Server is running on port", APP_PORT)
    print("MAC Address: ", MAC_ADDRESS)
    while True:
        process_request(time.time())
        time.sleep(15)
