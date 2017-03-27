import requests
import json
import time

path = 'http://localhost:'
servers = ['8080', '8090']

def is_server_overload(request):
    if request.status_code != 200:
        return True
    data = json.loads(request.text)
    if data['load'] >= 90.0:
        return True
    return False


def main():
    current_server = 0
    while True:
        time.sleep(1)
        try:
            r = requests.get(path+servers[current_server])
            print r.status_code, r.text
            if is_server_overload(r):
                print 'Server', current_server, 'failed to respond, trying another server...'
                current_server = (current_server + 1) % 2
        except requests.ConnectionError:
            print 'Server', current_server, 'failed to respond, trying another server...'
            current_server = (current_server + 1) % 2

main()
