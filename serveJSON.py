from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyServer(BaseHTTPRequestHandler):
    pump=0
    caudal=0
    valve=0
    humidity=0
    temperature=0
    volume=0

    def do_GET(self):
        if '/action' in self.path :
            if 'opt=1' in self.path:
                if MyServer.pump==0:
                    MyServer.pump=1
                else:
                    MyServer.pump=0
                    
            elif 'opt=2' in self.path:
                MyServer.caudal+=1
            elif 'opt=3' in self.path:
                if MyServer.valve==0:
                    MyServer.valve=1
                else:
                    MyServer.valve=0
            elif 'opt=4' in self.path:
                MyServer.humidity+=1
            elif 'opt=5' in self.path:
                MyServer.temperature+=1
            elif 'opt=6' in self.path:
                MyServer.volume+=1

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {'pump': self.pump, 'caudal':self.caudal, 'valve': self.valve, 'humidity': self.humidity, 'temperature':self.temperature, 'volume':self.volume}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())
            
        else:
            self.send_error(404)

def run():
    print('Starting server...')
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, MyServer)
    print('Server started!')
    httpd.serve_forever()

if __name__ == '__main__':
    run()