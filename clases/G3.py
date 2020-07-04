from clases.Consulta import *

class G3(Consulta):
    def __init__(self, nombre, busqueda=None, ruta="/text-search"):
        Consulta.__init__(self, ruta)
        #if id is None:
        #    self.esperar = Truye
        self.busqueda = busqueda
        self.done = False
        self.nombre = nombre
        self.json_api = None
        self.json_grupo_original = None
        self.json_grupo_adaptado = None
        self.json_api_mayus = None
        self.json_api_tilde = None
        self.json_api_mayus_tilde = None
        self.filtros_busqueda = []
        self.completo = True
        if nombre == "G3.11":
            self._puntos = 4
        else:
            self._puntos = 2

    def puntos(self):
        if self.respuesta:
            if self.completo:
                return self._puntos
            else:
                return self._puntos / 2
        return 0

    def mensaje(self):
        if not self.atributos:
            self._mensaje = "Faltan atributos por mostrar"
        if self.respuesta:
            return f"{self.nombre}: {self.respuesta} {self._mensaje}{self.filtros_busqueda}"
        else:
            return f"{self.nombre}: {self.respuesta} {self._mensaje}"#"


    def escribir(self, nombre_archivo="G3.py"):
        if Consulta.guarda:
            nombre_carpeta = Consulta.nombre_archivo
            with open(nombre_carpeta + f"/{nombre_archivo}", "a") as archivo:# + datetime.now().strftime('%d-%m-%y_%H-%M-%S'))
                #""#bcb
                string = f'''
{"#"*((80-len(self.nombre) - 2)//2)} {self.nombre} {"#"*(80 - len(self.nombre) - 2 - ((80-len(self.nombre) - 2)//2))}
"{self.nombre}": {'{'}
    "busqueda": {self.busqueda},
    "respuesta": {self.respuesta},
    "acepta_no_incluir_parametros": {self.completo},
    "puntos": {self.puntos()},
    "todos_los_atributos": {self.atributos},
    "atributos_encontrados": {self.atributos_encontrados},
    "json_grupo_adaptado": {self.json_grupo_adaptado if self.json_grupo_adaptado in [None, False] else [int(float(i["mid"])) for i in self.json_grupo_adaptado if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]},
    "json_api": {self.json_api if self.json_api in [None, False] else [int(float(i["mid"])) for i in self.json_api if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]},
    "json_api_mayusculas": {self.json_api_mayus if self.json_api_mayus in [None, False] else [int(float(i["mid"])) for i in self.json_api_mayus if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]},
    "json_api_tildes": {self.json_api_tilde if self.json_api_tilde in [None, False] else [int(float(i["mid"])) for i in self.json_api_tilde if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]},
    "json_api_mayus_tildes": {self.json_api_mayus_tilde if self.json_api_mayus_tilde in [None, False] else [int(float(i["mid"])) for i in self.json_api_mayus_tilde if str(i["mid"]).isnumeric() or str(i["mid"]).replace(".", "").isnumeric()]},


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
            if not self.respuesta:
                resultado = self._correr(de_nuevo=True)
                if resultado:
                    self.respuesta = resultado
                    self.completo = False
            self.done = True#jiib.strip()
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{', '.join([i for i in self.busqueda]) if self.busqueda else self.busqueda}]   ")
            print()
        except SeDemora:
            #print("hola")
            self.done = True
            resultado = False
            sys.stdout.write(f"\r¡Listo! {self.nombre}: {resultado} [{self.busqueda}]   ")
            print()
        except (KeyboardInterrupt, SystemExit):
            self.done = True
            cargando.clear()

        return resultado


    def _correr(self, de_nuevo=False):
        try:
            if de_nuevo:
                for i in ["desired", "forbidden", "required"]:
                    if i not in self.busqueda:
                        self.busqueda[i] = []
        except:
            return False
        try:
            #https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-runningd
            if self.busqueda == None or self.busqueda == {}:
                consulta = f"{self.ruta}"
                if self.busqueda is None:
                    uno = Consulta.requests_get(self.api + consulta, timeout=10)
                else:
                    uno = Consulta.requests_get(self.api + consulta, json=self.busqueda, timeout=10)

                respuesta_api = Consulta.encontrar(uno.json())

                if self.busqueda is None:
                    dos = Consulta.requests_get(self.grupo + consulta, timeout=10)
                else:
                    dos = Consulta.requests_get(self.grupo + consulta, json=self.busqueda, timeout=10)
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
                    self.todos_atributos(respuesta_grupo)
                    largo = len(respuesta_grupo)
                    contador = 0
                    for i in range(len(respuesta_grupo)):
                        if str(respuesta_grupo[i]["mid"]).replace(".", "").isnumeric() and 1 <= int(str(respuesta_grupo[i]["mid"]).replace(".", "")) <= 220:
                            contador += 1
                    if contador >= 100:
                        return True
                    if largo >= 2:
                        return True
                    return False


            else:
                consulta = f"{self.ruta}"
                uno = Consulta.requests_get(self.api + consulta, json=self.busqueda)
                tres_mayus = Consulta.requests_get(self.api + consulta + "-2/True/False", json=self.busqueda, timeout=10)
                tres_tilde = Consulta.requests_get(self.api + consulta + "-2/False/True", json=self.busqueda, timeout=10)
                tres_mayus_tilde = Consulta.requests_get(self.api + consulta + "-2/True/True", json=self.busqueda, timeout=10)
                respuesta_api = Consulta.encontrar(uno.json())
                self.json_api = respuesta_api
                dos = Consulta.requests_get(self.grupo + consulta, json=self.busqueda)
                respuesta_api_mayus = Consulta.encontrar(tres_mayus.json())
                respuesta_api_tilde = Consulta.encontrar(tres_tilde.json())
                respuesta_api_mayus_tilde = Consulta.encontrar(tres_mayus_tilde.json())
                self.json_api = respuesta_api
                self.json_api_mayus = respuesta_api_mayus
                self.json_api_tilde = respuesta_api_tilde
                self.json_api_mayus_tilde = respuesta_api_mayus_tilde
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
                    ids_encontrados_mayus = set([int(i["mid"]) for i in respuesta_api_mayus] if respuesta_api_mayus not in [None, False] else [])
                    ids_encontrados_tilde = set([int(i["mid"]) for i in respuesta_api_tilde] if respuesta_api_tilde not in [None, False] else [])
                    ids_encontrados_mayus_tilde = set([int(i["mid"]) for i in respuesta_api_mayus_tilde ] if respuesta_api_mayus_tilde not in [None, False] else [])
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
                    largo_mayus = len((ids_encontrados_mayus - ids).union(ids - ids_encontrados_mayus).intersection(Consulta.ids))
                    largo_tilde = len((ids_encontrados_tilde - ids).union(ids - ids_encontrados_tilde).intersection(Consulta.ids))
                    largo_mayus_tilde = len((ids_encontrados_mayus_tilde - ids).union(ids - ids_encontrados_mayus_tilde).intersection(Consulta.ids))
                    #print(largo)
                    if largo >= 1 and largo_mayus >= 1 and largo_tilde >= 1 and largo_mayus_tilde >= 1:
                        return False #if i in
                    lista = []
                    if largo == 0:
                        lista.append("regular")
                    if largo_mayus == 0:
                        lista.append("case_sensitive")
                    if largo_mayus_tilde == 0:
                        lista.append("case_and_diacritic_sensitive")
                    if largo_tilde == 0:
                        lista.append("diacritic_sensitive")
                    self.filtros_busqueda = lista
                    return True#tYu#tRUE#FalsetRUE
        except requests.exceptions.ReadTimeout:
            self.done = True
            sys.stdout.write(f"\r¿Listo? {self.nombre}")
            print()
            print("    " + "_"*48)
            print("    Al parecer algo sucede Con las consultas que ")
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
