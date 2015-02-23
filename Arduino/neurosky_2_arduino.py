import socket
import json
from copy import copy
ser = serial.Serial('COM9', 9600, timeout=1);
        
sock = socket.socket()
sock.connect(("127.0.0.1", 13854))
msg = json.dumps({"enableRawOutput": False, "format": "Json"})

def handle_msg(msg):
    try:
        j = json.loads(msg)
        if 'blinkStrength' in j.keys():
            print(j)
            send_msg_2_arduino("turn led on");
    except Exception as e:
        pass

def send_msg_2_arduino(msg):
    ser.write(msg);


#sock.send(bytes(msg,"UTF-8"))
sock.send(msg)

pool = ""

while True:
    pool = pool + sock.recv(1024).decode("ascii")
    for i,c in enumerate(copy(pool)):
        if c == '\r':
            msg = pool[0:i]
            pool = pool[i+1:]
            handle_msg(msg)
ser.close();
    
