from clases.Consulta import *
from datetime import datetime

class D1(Consulta):
    def __init__(self, nombre, id=None, ruta="/messages"):#p
        Consulta.__init__(self, ruta)
        #if id is None:
        #    self.esperar = True
        self.id = id
        self.done = False
        self.nombre = nombre
        self.largo_inicial, self.largo_despues = None, None
        self.ids_iniciales, self.ids_despues = None, None
        self.esta = None
        self._mensaje = ""
        self._puntos = 3

    def mensaje(self):
        if self.respuesta:
            return f"{self.nombre}: {self.respuesta} [{self.puntos()} puntos]"
        else:
            if self.esta and type(self.largo_inicial) == int and type(self.largo_despues) == int and self.largo_inicial <= self.largo_despues:
                self._mensaje = f"El mensaje de id={self.id} está en la lista, pero la cantidad de mensajes no es menor"
            elif not self.esta and type(self.largo_inicial) == int and type(self.largo_despues) == int and self.largo_inicial != self.largo_despues:

                self._mensaje = f"El mensaje de id={self.id} no está en la lista, pero la cantidad de mensajes es distinta"
        return f"{self.nombre}: {self.respuesta} [{self.puntos()} puntos] {self._mensaje}"


    def escribir(self, nombre_archivo="D1.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            with open(nombre_carpeta + f"/{nombre_archivo}", "a") as archivo:# + datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
                #""
                string = f'''
{"#"*((80-len(self.nombre) - 2)//2)} {self.nombre} {"#"*(80 - len(self.nombre) - 2 - ((80-len(self.nombre) - 2)//2))}
"{self.nombre}": {'{'}
    "id_mensaje": {self.id},
    "respuesta": {self.respuesta},
    "json_grupo": {self.json_grupo},
    "ids_encontradas_antes": {self.ids_iniciales},
    "ids_encontradas_despues": {self.ids_despues},
    "largo_ids_encontradas_antes": {self.largo_inicial},
    "largo_ids_encontradas_despues": {self.largo_despues},
    "se_deberia_poder_borrar": {self.esta}
{'},'}
                '''
                archivo.write(string)#r

    def correr(self):
        try:

            cargando = threading.Thread(target=self.animate)
            cargando.start()

            resultado = self._correr()
            self.respuesta = resultado
            if self.respuesta is False:
                self.ruta = "/message"
            resultado = self._correr()
            self.respuesta = resultado
            self.done = True
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [De {self.largo_inicial} a {self.largo_despues} mensajes]  ")
            print()
        except SeDemora:
            #print("hola")
            self.done = True
            resultado = False
            self.respuesta = resultado
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{'id = ' + str(self.id) if self.id is not None else 'Todos los mensajes'}]   ")
            print()
        except (KeyboardInterrupt, SystemExit):
            self.done = True
            cargando.clear()

        self.respuesta = resultado
        return resultado


    def _correr(self):
        try:
            #https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-runningd
            if None:
                pass
            else:
                self.ids_iniciales = self.ids_disponibles()
                self.largo_inicial = len(self.ids_iniciales)
                if self.id is None:
                    self.id = sorted(list(self.ids_iniciales))[-1]
                    ''' # """"
                    self.done = True
                    sys.stdout.write("\r... ")#po
                    sys.stdout.flush()
                    print("La id que fue eliminada al principio no existía, así que otro test para probarla!")
                    print("Las siguientes ids fueron encontradas:")
                    print(" ".join((str(i) for i in sorted(list(self.ids_iniciales)))))
                    print("A continuación puede elegir una de la lista, o puede presionar ENTER para saltarse esta consulta:")
                    print("[Importante: Idealmente elegir una id mayor a 220 :D (si la hay) para así no borrar ids que pueden ser respuestas de otras consultas!]")
                    entrada = input(">> ")
                    while (not entrada.isnumeric()) and entrada != "" and (((int(entrada) not in self.ids_inciales))):
                        print("No se pudo entender la entrada :O puede intentarlo nuevamente :D")
                        entrada = input(">> ")
                    if entrada == "":
                        print("saltando consulta...")
                        return True#True
                    self.id = int(entrada)
                    print(f"mid elegida: {self.id} ({'no ' if not self.id in self.ids_iniciales else ''}está en la lista)")#y})")
                    self.done = False
                    cargando = threading.Thread(target=self.animate)#TT
                    cargando.start()'''
                consulta = f"{self.ruta}/{self.id}"
                se_puede = self.id in self.ids_iniciales
                self.esta = se_puede
                dos = Consulta.requests_delete(self.grupo + consulta)
                try:
                    self.json_grupo = dos.json()
                except:
                    self.json_grupo = {}
                #respuesta_grupo = Consulta.encontrar(dos.json())
                if None:
                    pass
                else:
                    self.ids_despues = self.ids_disponibles()
                    self.largo_despues = len(self.ids_despues)
                    if se_puede and self.largo_despues < self.largo_inicial:
                        return True
                    elif not se_puede and self.largo_despues == self.largo_inicial:
                        return True
                    else:
                        return False
            return False

        except requests.exceptions.ReadTimeout:
            self.done = True
            sys.stdout.write(f"\r¿Listo? {self.nombre}")
            print()
            print("    " + "_"*48)
            print("    Al parecer algo sucede con las consultas que ")
            print("    entregan todos los mensajes                  ")
            print("    A continuación se dan distintas opciones     ")
            print("    para resolver, resolverlo ahora o más tarde: ")
            print('''
    [0] Revisar código ahora -> Está correcto
    [1] Revisar código ahora -> Está incorrecto
    [2] Revisar código más tarde
            ''')
            entrada = input("    >> ")
            while entrada.strip() not in ["0", "1", "2"]:
                print("    No se reconoció la entrada")
                entrada = input("    >> ")
            print("    " + "_"*48)
            if entrada.strip() == "0":
                resultado = True#ye#TTTT
                return True
            elif entrada.strip() == "1":
                resultado = False
                return False
            else:
                resultado = None
                return None

        except:
            self.done = True
            return False
