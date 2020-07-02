# GET mensajes que cumplan con filtro de text-search

ruta = "/text-search"

consulta = {
    "G3.1": None,
    "G3.2": {},
    "G3.3": {
            	"desired": ["P NP", "Pokemon"]
            },
    "G3.4": {
            	"required": ["quiero jugar", "Bai"]
            },
    "G3.5": {
            	"forbidden":   ["Pokemon", "Megaman", "Espero",
                                "Buena", "Hola", "Cambio", "despido",
                                "Feliz", "tiempo", "cancion", "hablar",
                                "cuento", "bases", "bai", "respecto",
                                "completo", "tal", "algo", "estas",
                                "viste", "Konnichiwa", "mal", "ayuda",
                                "niño", "tarea", "profe"]
            },
    "G3.6": {
            	"userId": 1
            },
    "G3.7": {
            	"required": ["Pasó algo."],
            	"userId": 2
            },
    "G3.8": {
            	"required": ["Te cuento que"],
            	"forbidden":   ["feliz", "despido", "partido",
                                "pronto", "mal", "bai"]
            },
    "G3.9": {
            	"userId": 2,
            	"forbidden": ["despido", "bien"]
            },
    "G3.10": {
            	"desired": []
            },
    "G3.11": {
            	"userId": 2,
            	"forbidden": ["pingüino"],
            	"desired": ["origami"],
            	"required": ["Pasó algo."]
            }
}
