# Bases de Datos - Entrega 4 🎉

¡Hola! A continuación unas pequeñas cosas sobre el script realizado para esta entrega :D

## Estructura del repositorio 🌱

```bash
├───clases
│   ├───__init__.py
│   ├───Consulta.py
│   ├───ListaConsultas.py
│   ├───G0.py
│   ├───G1.py
│   ├───G2.py
│   ├───G3.py
│   ├───D1.py
│   └───P1.py
│
├───consultas
│   ├───__init__.py
│   ├───G0.py
│   ├───G1.py
│   ├───G2.py
│   ├───G3.py
│   ├───D1.py
│   └───P1.py
│ 
├───lista_consultas.py
├───main.py
└───valores.py
```

## Para correr script 🍀
```
python main.py grupoXX
```
O también es posible:
* Especificar grupo como número
```
python main.py XX
```
* No especificar grupo (se pedirá por consola después)
```
python main.py
```

## Una vez en main.py... 😊
* Se revisarán los distintos testcases:
  * **G0**: en la ruta `/messages?id1=XX&id2=YY`
  * **G1**: en la ruta `/messages` y `/messages/id`
  * **G2**: en la ruta `/users` y `/users/id`
  * **G3**: en la ruta `/text-search`
  * **P1**: en la ruta `/messages` con `POST`
  * **D1**: en la ruta `/message/id` o `/messages/id` con `DELETE`
  
 ## Testcases listos 🌳🌿🌳
 * Se creó (si ya no estaba creada :D) una carpeta con el nombre `grupoXX`, donde `XX` es el número del grupo ingresado al principio.
 * Dentro de esta carpeta habrá una subcarpeta con el formato `dd-mm-aa hh-mm-ss`, que corresponde a la hora del día en donde se abrió el script :D
 * Dentro de esta subcarpeta habrán dos archivos:
    * `resumen.py`: Con información complementaria de las distintas consultas sobre la api del grupo o de otras cosas que pueden ser útiles para revisar :D 
    * `comentarios.txt`: Con dos partes:
      * **Comentarios por test**: se incluye una lista con el nombre de la consulta, el resultado (`true`, `false` o `none`), el puntaje y algunos eventuales comentarios.
      * **Notas para la planilla**: En esta es posible copiar y pegar los puntos, para eso se copia la fila del texto, luego en la planilla se selecciona la primera con puntaje en la fila del grupo, y se pega :D
        Esta tiene la estructura:
        ```
        |__G0__|_____G1_____|____G2____|____________________G3____________________|___P1___|___D1___|
        |_1_|_2|__1_|_2_|_3_|_1_|_2_|_3|__1_|_2_|_3_|_4_|_5_|_6_|_7_|_8_|_9_|10|11|___1_|_2|__1_|_2_|
          2   2   2   2   3   2   2   3   2   2   2   2   2   2   2   2   2   2   4   6   6   3   3	
  
      ```

      
¡Eso! Pueden preguntarme cualquier cosa c:
¡Mucho éxito y ánimo con lo que queda de semestreeeee!
😊🍀🎉😄🌱🎊🌳

