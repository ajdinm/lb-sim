from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import psutil
import json
import sys

SERVER_ID = int(sys.argv[1])
PORT_NUMBER = int(sys.argv[2])

def get_cpuload():
    return psutil.cpu_percent()


class RequestHanlder(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = dict()
        response['server'] = SERVER_ID
        response['load'] = get_cpuload()
        self.wfile.write(json.dumps(response))
        return


def main():
    try:
        server = HTTPServer(('', PORT_NUMBER), RequestHanlder)
        print 'Started server', SERVER_ID, 'on port', PORT_NUMBER
        server.serve_forever()
    
    except KeyboardInterrupt:
        print 'Shutting down...'
        server.socket.close()
main()
    
