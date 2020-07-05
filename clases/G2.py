from clases.Consulta import *

class G2(Consulta):
    def __init__(self, nombre, id=None, ruta="/users", listo=None):
        Consulta.__init__(self, ruta)
        #if id is None:
        #    self.esperar = True
        self.id = id
        self.done = False
        self.nombre = nombre
        self.atributos = True
        self.estado = None
        if id is None:
            self._puntos = 3
        else:
            self._puntos = 2 # self._puntos = 2 #self._puntos = 2

    def escribir(self, nombre_archivo="G2.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            with open(nombre_carpeta + f"/{nombre_archivo}", "a") as archivo:# + datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
                #""#bcbm
                string = f'''
{"#"*((80-len(self.nombre) - 2)//2)} {self.nombre} {"#"*(80 - len(self.nombre) - 2 - ((80-len(self.nombre) - 2)//2))}
"{self.nombre}": {'{'}
    "id_del_usuario": {self.id},
    "respuesta": {self.respuesta},
    "todos_los_atributos": {self.atributos},
    "atributos_encontrados": {self.atributos_encontrados},
    "json_grupo_adaptado": {self.json_grupo_adaptado if self.json_grupo_adaptado in [None, False] else [int(float(i["uid"])) for i in self.json_grupo_adaptado if str(i["uid"]).isnumeric() or str(i["uid"]).replace(".", "").isnumeric()]},
    "json_api": {self.json_api if self.json_api in [None, False] else [int(float(i["uid"])) for i in self.json_api if str(i["uid"]).isnumeric() or str(i["uid"]).replace(".", "").isnumeric()]},

    "json_grupo_original": {self.json_grupo_original},

{'},'}
                '''
                archivo.write(string)#r


    def correr(self):
        try:

            #if self.esperar:
            #    self.inicio = datetime.now()
            #    print(self.inicio)
            cargando = threading.Thread(target=self.animate)
            cargando.start()

            resultado = self._correr()
            self.respuesta = resultado
            self.done = True
            self.estado = resultado#True
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{'id = ' + str(self.id) if self.id is not None else 'Todos los usuarios'}]   ")
            print()
        except SeDemora:
            #print("hola")
            self.done = True
            resultado = False
            self.respuesta = resultado
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{'id = ' + str(self.id) if self.id is not None else 'Todos los usuarios'}]   ")
            print()
        except (KeyboardInterrupt, SystemExit):
            self.done = True
            cargando.clear()

        return resultado


    def _correr(self):
        try:
            #https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-runningd

            if self.id is None:
                self.esperar = True
                uno = Consulta.requests_get(self.api + self.ruta, timeout=(10, 10))
                respuesta_api = Consulta.encontrar_2(uno.json())
                self.json_api = respuesta_api
                dos = Consulta.requests_get(self.grupo + self.ruta, timeout=(10, 10))
                self.json_grupo_original = dos.json()
                respuesta_grupo = Consulta.encontrar_2(self.json_grupo_original)
                self.json_grupo_adaptado = respuesta_grupo
                if not respuesta_api and not respuesta_grupo:
                    return True
                elif respuesta_api and not respuesta_grupo:
                    return False
                elif not respuesta_api and respuesta_grupo:
                    return False
                else:
                    self.todos_atributos_2(respuesta_grupo)
                    largo = len(respuesta_grupo)
                    contador = 0
                    for i in range(len(respuesta_grupo)):
                        if str(respuesta_grupo[i]["uid"]).replace(".", "").isnumeric() and 1 <= int(str(respuesta_grupo[i]["uid"]).replace(".", "")) <= 43:
                            contador += 1
                    if contador >= 43:
                        return True
                    if largo >= 2:
                        return True
                    return False


            else:
                consulta = f"{self.ruta}/{self.id}"
                uno = Consulta.requests_get(self.api + consulta)
                a = uno.json()
                respuesta_api = Consulta.encontrar_2(a)
                self.json_api = respuesta_api
                dos = Consulta.requests_get(self.grupo + consulta)
                a = dos.json()
                self.json_grupo_original = a
                respuesta_grupo = Consulta.encontrar_2(a)
                self.json_grupo_adaptado = respuesta_grupo
                if type(respuesta_grupo) == list:
                    self.json_grupo_adaptado = [self.json_grupo_adaptado[0]]
                if not respuesta_api and not respuesta_grupo:
                    return True
                elif respuesta_api and not respuesta_grupo:
                    return False
                elif not respuesta_api and respuesta_grupo:
                    return False
                else:
                    self.todos_atributos_2(respuesta_grupo)
                    elemento = respuesta_grupo[0]
                    uid = elemento.get("uid")
                    if uid and uid == self.id:
                        return True
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

        except Exception as e:
            print(e)
            self.done = True
            return False
