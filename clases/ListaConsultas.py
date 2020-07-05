from clases.G0 import *
from clases.G1 import *
from clases.G2 import *
from clases.G3 import *
from clases.P1 import *
from clases.D1 import *
from clases.Consulta import *
import requests
import threading
import time
import sys
from datetime import datetime

class ListaConsultas:
    def __init__(self, n_grupo=0, ruta="/", api="https://iic2413-2020-1-api.herokuapp.com", grupo="http://localhost:5000"):
        self.g0 = []
        self.g1 = []
        self.g2 = []
        self.g3 = []
        self.p1 = []
        self.d1 = []
        self.api = api
        self.grupo = grupo
        self.listos = []
        self.skip = []
        self.numero = 0
        self.n_grupo = n_grupo
        #self.largo_inicial, self.largo_despues = "?", "?"

    def animate(self):
        datetime.now()
        while self.numero < 220:
            sys.stdout.write('\rCargando [' + '*'*int(self.numero*0.1) + ' '*int((220-self.numero)*0.1) + ']')
            sys.stdout.flush()
            time.sleep(1)

    def ids_disponible(self):
        print("Preparando todo...")
        try:
            dos = requests.get(f"{self.grupo}/messages", timeout=10)
            respuesta_grupo = Consulta.encontrar(dos.json())
            #print(respuesta_grupo)
            #print(dos.json())
            if respuesta_grupo:
                ids = [int(i["mid"]) for i in respuesta_grupo if str(i["mid"]).replace(".", "").isnumeric() and 1 <= int(i["mid"]) <= 220]
                self.listos.append(True)
                atributos = [i.strip().lower() for i in respuesta_grupo[0]]
                encontrados = True
                for i in ["mid", "message", "sender", "receptant", "lat", "long", "date"]:
                    if i.strip().lower() not in atributos:
                        encontrados = False
                self.listos.append(encontrados)
                self.listos.append(atributos)
                return ids
        except:
            pass

        try:
            ids = []
            cargando = threading.Thread(target=self.animate)
            cargando.start()
            for i in range(1, 221):
                self.numero = i
                dos = requests.get(f"{self.grupo}/messages/{i}", timeout=4)
                dos = Consulta.encontrar(dos.json())
                j = dos[0]["mid"]
                if str(j).replace(".", "").isnumeric() and 1 <= int(j) <= 220:
                    ids.append(int(j))
            return ids
        except:
            return False

    def cargar_g0(self):
        import consultas.G0 as g0
        for i in g0.consulta:
            id1, id2 = list((g0.consulta[i]["id1"], g0.consulta[i]["id2"]))
            consulta = G0(i, id1, id2)
            self.g0.append(consulta)

    def correr_g0(self):
        for i in self.g0:
            i.correr()


    def guardar_g0(self, ahora=None, nombre_archivo="G0.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            if not ahora:
                ahora = datetime.now()

            ahora = 'G0 ' + str((ahora).strftime('%d/%m/%y %H:%M:%S'))#()#))
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write(f'''
{"#"*80}
{"#"*80}
{"#"*((80-len(ahora)-2)//2)} {ahora} {"#"*(80 - 2 - len(ahora) - (80-len(ahora)-2)//2)}
{"#"*80}
{"#"*80}

{ahora.replace("/", "_").replace(":", "_").replace(" ", "__")} = {"{"}
                ''')
            for i in self.g0:
                i.escribir(nombre_archivo)
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write('''
}
''')


    def cargar_g1(self):
        import consultas.G1 as g1
        for i in g1.consulta:
            consulta = G1(i, g1.consulta[i])
            self.g1.append(consulta)

    def correr_g1(self):
        for i in self.g1:
            i.correr()



    def guardar_g1(self, ahora=None, nombre_archivo="G1.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            if not ahora:
                ahora = datetime.now()

            ahora = 'G1 ' + str((ahora).strftime('%d/%m/%y %H:%M:%S'))#()#))
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write(f'''
{"#"*80}
{"#"*80}
{"#"*((80-len(ahora)-2)//2)} {ahora} {"#"*(80 - 2 - len(ahora) - (80-len(ahora)-2)//2)}
{"#"*80}
{"#"*80}

{ahora.replace("/", "_").replace(":", "_").replace(" ", "__")} = {"{"}
                ''')
            for i in self.g1:
                i.escribir(nombre_archivo)
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write('''
}
''')

    def guardar_g2(self, ahora=None, nombre_archivo="G2.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            if not ahora:
                ahora = datetime.now()

            ahora = 'G2 ' + str((ahora).strftime('%d/%m/%y %H:%M:%S'))#()#))
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write(f'''
{"#"*80}
{"#"*80}
{"#"*((80-len(ahora)-2)//2)} {ahora} {"#"*(80 - 2 - len(ahora) - (80-len(ahora)-2)//2)}
{"#"*80}
{"#"*80}

{ahora.replace("/", "_").replace(":", "_").replace(" ", "__")} = {"{"}
                ''')
            for i in self.g2:
                i.escribir(nombre_archivo)
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write('''
}
''')






    def cargar_g2(self):
        import consultas.G2 as g2
        for i in g2.consulta:
            consulta = G2(i, g2.consulta[i])
            self.g2.append(consulta)

    def correr_g2(self):
        for i in self.g2:
            i.correr()

    def cargar_g3(self):
        import consultas.G3 as g3
        for i in g3.consulta:
            busqueda = g3.consulta[i]
            consulta = G3(i, busqueda)
            self.g3.append(consulta)

    def correr_g3(self):
        for i in self.g3:
            i.correr()

    def guardar_g3(self, ahora=None, nombre_archivo="G3.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            if not ahora:
                ahora = datetime.now()

            ahora = 'G3 ' + str((ahora).strftime('%d/%m/%y %H:%M:%S'))#()#))
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write(f'''
{"#"*80}
{"#"*80}
{"#"*((80-len(ahora)-2)//2)} {ahora} {"#"*(80 - 2 - len(ahora) - (80-len(ahora)-2)//2)}
{"#"*80}
{"#"*80}

{ahora.replace("/", "_").replace(":", "_").replace(" ", "__")} = {"{"}
                ''')
            for i in self.g3:
                i.escribir(nombre_archivo)
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write('''
}
''')

    def cargar_p1(self):
        import consultas.P1 as p1
        for i in p1.consulta:
            documento = p1.consulta[i]
            consulta = P1(i, documento)
            self.p1.append(consulta)

    def correr_p1(self):
        for i in self.p1:
            i.correr()

    def guardar_p1(self, ahora=None, nombre_archivo="P1.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            if not ahora:
                ahora = datetime.now()

            ahora = 'P1 ' + str((ahora).strftime('%d/%m/%y %H:%M:%S'))#()#))
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write(f'''
{"#"*80}
{"#"*80}
{"#"*((80-len(ahora)-2)//2)} {ahora} {"#"*(80 - 2 - len(ahora) - (80-len(ahora)-2)//2)}
{"#"*80}
{"#"*80}

{ahora.replace("/", "_").replace(":", "_").replace(" ", "__")} = {"{"}
                ''')
            for i in self.p1:
                i.escribir(nombre_archivo)
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write('''
}
''')


    def cargar_d1(self):
        import consultas.D1 as d1
        for i in d1.consulta:
            id = d1.consulta[i]
            consulta = D1(i, id)
            self.d1.append(consulta)

    def correr_d1(self):
        algun_encontrado = False # ytr
        algun_no_encontrado = False
        for i in self.d1[:len(self.d1)]: # -1]:
            i.correr()
        '''
            if i.esta:
                algun_encontrado = True
            elif not i.esta:
                algun_no_encontrado = True # False
        if algun_encontrado:
            self.d1.pop(-1)
        else:
            self.d1[-1].correr()
            self.d1[0] = self.d1.pop(-1) # self.d1[0] = self.d1.pop(-1) # self.d1[0] = self.d1.pop(-1) self.d1[0] = self.d1.pop(-1)
        '''

    def guardar_d1(self, ahora=None, nombre_archivo="D1.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            if not ahora:
                ahora = datetime.now()

            ahora = 'D1 ' + str((ahora).strftime('%d/%m/%y %H:%M:%S'))#()#))
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write(f'''
{"#"*80}
{"#"*80}
{"#"*((80-len(ahora)-2)//2)} {ahora} {"#"*(80 - 2 - len(ahora) - (80-len(ahora)-2)//2)}
{"#"*80}
{"#"*80}

{ahora.replace("/", "_").replace(":", "_").replace(" ", "__")} = {"{"}
                ''')
            for i in self.d1:
                i.escribir(nombre_archivo)
            with open(nombre_carpeta + f"/{nombre_archivo}", "a", encoding="utf-8") as archivo:
                archivo.write('''
}
''')

    def cargar(self):
        for i in [self.cargar_g0, self.cargar_g1, self.cargar_g2,
                self.cargar_g3, self.cargar_p1, self.cargar_d1]:
            i()

    def correr(self):
        for i in [self.correr_g0, self.correr_g1, self.correr_g2,
                    self.correr_g3, self.correr_p1, self.correr_d1]:
            i()

    def guardar(self, ahora=None, nombre_archivo="resumen.py"):
        if ahora is None:
            ahora = datetime.now()
        for i in [self.guardar_g1, self.guardar_g2, self.guardar_g0,
                    self.guardar_g3, self.guardar_d1, self.guardar_p1]:
            i(ahora, nombre_archivo)

        self.resumir(ahora)

    def resumir(self, ahora=None, nombre_archivo="comentarios.txt"):
        if ahora is None:
            ahora = datetime.now()
        if Consulta.guarda:
            nombre_archivo = Consulta.nombre_archivo + "/" + nombre_archivo
        with open(f"{nombre_archivo.replace('.py', '.txt')}", "w", encoding="utf-8") as archivo:#")#gh
            puntos = []
            for i in [self.g0, self.g1, self.g2, self.g3, self.p1, self.d1]:
                for j in i:
                    archivo.write(j.mensaje() + "\n")
                    # puntos.append(j.puntos())
                    decimales = str(j.puntos())[str(j.puntos()).find("."):]
                    if len(decimales) - 1 == decimales.count("0"):
                        numero = str(int(j.puntos()))
                    else:
                        numero = str(j.puntos()).replace(".", ",")
                    puntos.append(numero)
            # print(puntos)
            archivo.write('''\nPuntos en Planilla (se puede copiar y pegar la fila :D):
|__G0__|_____G1_____|____G2____|____________________G3____________________|___P1___|___D1___|
|_1_|_2|__1_|_2_|_3_|_1_|_2_|_3|__1_|_2_|_3_|_4_|_5_|_6_|_7_|_8_|_9_|10|11|___1_|_2|__1_|_2_|''')
            archivo.write('\n  ' + " 	".join(puntos))
            # 1	2	31	234
            
            '''
archivo.write(' ' '\nPuntos en Planilla (se puede copiar y pegar la fila :D):
____________________________________________________________________________________________
|__G0__|_____G1_____|____G2____|____________________G3____________________|___P1___|___D1___|
|_1_|_2|__1_|_2_|_3_|_1_|_2_|_3|__1_|_2_|_3_|_4_|_5_|_6_|_7_|_8_|_9_|10|11|___1_|_2|__1_|_2_|
  ' ' ')
            archivo.write('\n  ' + " 	".join(puntos))
            # 1	2 31 234
'''
