from clases.Consulta import *

class P1(Consulta):
    def __init__(self, nombre, documento=None, ruta="/messages"):#p
        Consulta.__init__(self, ruta)
        #if id is None:
        #    self.esperar = True
        self.documento = documento
        self.done = False
        self.nombre = nombre
        self.json_grupo = None
        self.ids_iniciales = None
        self.ids_despues = None
        self.largo_inicial = None
        self.largo_despues = None
        self.respuesta = None


    def mensaje(self):
        if self.respuesta:
            return f"{self.nombre}: {self.respuesta}"
        else:
            if self.permitido and type(self.largo_inicial) == int and type(self.largo_despues) == int and self.largo_inicial >= self.largo_despues:
                self._mensaje = f"El mensaje debería poder ingresarse, pero la cantidad de mensajes no aumentó"
            elif not self.permitido and type(self.largo_inicial) == int and type(self.largo_despues) == int and self.largo_inicial != self.largo_despues:

                self._mensaje = f"El mensaje no debería poder ingresarse, pero la cantidad de mensajes es distinta"
                return f"{self.nombre}: {self.respuesta} {self._mensaje}"


    def escribir(self, nombre_archivo="D1.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            with open(nombre_carpeta + f"/{nombre_archivo}", "a") as archivo:# + datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
                #""
                string = f'''
{"#"*((80-len(self.nombre) - 2)//2)} {self.nombre} {"#"*(80 - len(self.nombre) - 2 - ((80-len(self.nombre) - 2)//2))}
"{self.nombre}": {'{'}
    "consulta": {self.documento},
    "respuesta": {self.respuesta},
    "json_grupo": {self.json_grupo},
    "json_api": {self.json_api},
    "ids_encontradas_antes": {self.ids_iniciales},
    "ids_encontradas_despues": {self.ids_despues},
    "largo_ids_encontradas_antes": {self.largo_inicial},
    "largo_ids_encontradas_despues": {self.largo_despues},
    "se_deberia_poder_agregar": {self.permitido}
{'},'}
                '''
                archivo.write(string)#r

    def correr(self):
        try:

            cargando = threading.Thread(target=self.animate)
            cargando.start()

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
                consulta = f"{self.ruta}"
                uno = Consulta.requests_post(self.api + consulta, json=self.documento)#ge
                respuesta_api = Consulta.encontrar(uno.json())
                self.json_api = respuesta_api
                se_puede = respuesta_api[0]["success"]
                self.permitido = se_puede
                dos = Consulta.requests_post(self.grupo + consulta, json=self.documento)
                try:
                    self.json_grupo = dos.json()
                except:
                    pass
                #respuesta_grupo = Consulta.encontrar(dos.json())
                if None:
                    pass
                else:
                    self.ids_despues = self.ids_disponibles()
                    self.largo_despues = len(self.ids_despues)
                    if se_puede and self.largo_despues > self.largo_inicial:
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
