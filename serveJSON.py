from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
pattern = r'opt=(\w+)'

class MyServer(BaseHTTPRequestHandler):
    pump=False
    caudal=0
    humidity=0
    temperature=0
    volume=0
    fanIn=False
    fanOut=False
    valve1=False
    valve2=False
    valve3=False    

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        if '/action' in self.path :
            match = re.search(pattern, self.path)
            print(match)
            opt_value = match.group(1)
            print(opt_value)
            
            if opt_value == 'pump':
                MyServer.pump= False if MyServer.pump==1 else True
                    
            elif opt_value == 'caudal':
                MyServer.caudal+=1
            elif opt_value == 'valve1':
                MyServer.valve1= False if MyServer.valve1==1 else True
            elif opt_value ==  'humidity':
                MyServer.humidity+=1
            elif opt_value == 'temperature':
                MyServer.temperature+=1
            elif opt_value == 'volume':
                MyServer.volume+=1
            elif opt_value == 'fanIn':
                MyServer.fanIn= False if MyServer.fanIn==1 else True
            elif opt_value == 'fanOut':
                MyServer.fanOut = False if MyServer.fanOut ==1 else True
            elif opt_value == 'valve2':
                MyServer.valve2 = False if MyServer.valve2==1 else True
            elif opt_value == 'valve3':
                MyServer.valve3 = False if MyServer.valve3==1 else True
                    

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {'pump': self.pump, 
                    'caudal':self.caudal, 
                    'valve1': self.valve1, 
                    'humidity': self.humidity,
                     'temperature':self.temperature,
                     'volume':self.volume,
                     'fanIn':self.fanIn,
                    'fanOut':self.fanOut,
                    'valve2':self.valve2,
                    'valve3': self.valve3
                     }
            print()
            print(data)
            print()
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())
            
        else:
            self.send_error(404)

def run():
    print('Startix server...')
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, MyServer)
    print('Server started!')
    httpd.serve_forever()

if __name__ == '__main__':
    run()