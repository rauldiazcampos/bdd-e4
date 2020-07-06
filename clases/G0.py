from clases.Consulta import *

class G0(Consulta):
    def __init__(self, nombre, id1=None, id2=None, ruta="/messages"):
        Consulta.__init__(self, ruta)
        #if id is None:
        #    self.esperar = True
        self.id1 = id1
        self.id2 = id2
        self.done = False
        self.nombre = nombre
        self._puntos = 2

    def escribir(self, nombre_archivo="G0.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            with open(nombre_carpeta + f"/{nombre_archivo}", "a") as archivo:# + datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
                #""#bcbm
                # print(self.json_grupo_adaptado)
                string = f'''
{"#"*((80-len(self.nombre) - 2)//2)} {self.nombre} {"#"*(80 - len(self.nombre) - 2 - ((80-len(self.nombre) - 2)//2))}
"{self.nombre}": {'{'}
    "id1": {self.id1},
    "id2": {self.id2},
    "respuesta": {self.respuesta},
    "todos_los_atributos": {self.atributos},
    "atributos_encontrados": {self.atributos_encontrados},
    "json_grupo_adaptado": {self.json_grupo_adaptado if self.json_grupo_adaptado in [None, False] else [int(float(i["mid"])) for i in self.json_grupo_adaptado if "mid" in i and str(i["mid"]).isnumeric() or "mid" in i and str(i["mid"]).replace(".", "").isnumeric()]},
    "json_api": {self.json_api if self.json_api in [None, False] else [int(float(i["mid"])) for i in self.json_api if "mid" in i and str(i["mid"]).isnumeric() or "mid" in i and str(i["mid"]).replace(".", "").isnumeric()]},

    "json_grupo_original": {self.json_grupo_original},

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
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [id1 = {self.id1} id2 = {self.id2}]   ")
            print()
        except SeDemora:
            #print("hola")
            self.done = True
            resultado = False
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{'id = ' + str(self.id) if self.id is not None else 'Todos los mensajes'}]   ")
            print()
        except (KeyboardInterrupt, SystemExit):
            self.done = True
            cargando.clear()

        return resultado


    def _correr(self):
        try:
            #https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-runningd

            if None:
                pass


            else:
                consulta = f"{self.ruta}?id1={self.id1}&id2={self.id2}"
                uno = Consulta.requests_get(self.api + consulta)
                respuesta_api = Consulta.encontrar(uno.json())
                self.json_api = respuesta_api
                dos = Consulta.requests_get(self.grupo + consulta)
                self.json_grupo_original = dos.json()
                respuesta_grupo = Consulta.encontrar(self.json_grupo_original)
                self.json_grupo_adaptado = respuesta_grupo
                if not respuesta_api and not respuesta_grupo:
                    return True
                elif respuesta_api and not respuesta_grupo:
                    return False
                elif not respuesta_api and respuesta_grupo:
                    return False
                else:
                    ids_encontrados = set([int(i["mid"]) for i in respuesta_api])
                    self.todos_atributos(respuesta_grupo)
                    ids = set()
                    for elemento in respuesta_grupo:
                        mid = elemento.get("mid")
                        if str(mid).replace(".", "").isnumeric():
                            mid = int(float(str(mid)))
                            if mid in Consulta.ids:
                                if mid not in ids_encontrados:
                                    return False
                                else:
                                    ids.add(mid)
                    largo = len((ids_encontrados - ids).union(ids - ids_encontrados).intersection(Consulta.ids))

                    if largo >= 1:
                        return False #if i in
                    return True#tYu#tRUE#FalsetRUE
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
