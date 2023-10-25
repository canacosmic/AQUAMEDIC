# modelo.py
from sklearn.ensemble import RandomForestClassifier

# Aqui es donde clasifico cada sintoma segun su categoría

# sintomas de comportameinto
sintomas_comportamiento = [
    "Inactivity",
    "Erratic swimming",
    "Sluggishness",
    "Weight loss",
    "Loss of color or appetite",
    "Bloating or swelling in the body",
    "Abnormal swimming",
    "Darting",
    "Flashing",
    "Gasping for air",
    "Unusually bulging of one or both eyes",
    "Fish struggles to swim, may float with head tipped down, or have difficulty surfacing, no balance, etc. May occur after eating",
    "Sudden abnormal behavior"
]


# sintomas de excremento
sintomas_excremento = [
    "String of feces hanging from fish",
]

# sintomas del cuerpo
sintomas_body = [
    "Grayish-white film on skin",
    "White or gray fungus on eyes",
    "Bluish-white film on body",
    "Reddened areas on body",
    "Small dark spots on fins and body",
    "Red or bloody gills",
    "Cloudy white appearance to one or both eyes",
    "Reddening on or under skin"
]


# sintomas de las aleetas
sintomas_fins = [
    "Damaged fins",
    "Ragged or decaying fins",
    "Small white spots that get larger over time, possibly with black streaks"
]

# sintomas de las branquias
sintomas_branquias = [
    "Yellow to gray patches on gills",
    "Strained breathing caused by gill damage",
    "Difficulty breathing due to gill damage"
]

# sintomas de la cabeza
sintomas_cabeza = [
    "Tissue on the head may be eaten away",
    "Swelling of head",
    "Bulging eyes",
    "Scratching, white salt-like spots starting on the head and spreading over the whole body, rapid breathing, cloudiness on eyes or fins",
    "Scratching, small worms hanging from the body",
    "Scratching, green to brown lice (up to an inch) visible on the skin",
    "Small yellow to white spots dusting the skin",
    "Small holes or eroding pits appearing in the head"
]


def cargar_datos_entrenamiento():
    tabla_de_datos = [
        {"symptoms": ["Síntoma 1", "Síntoma 2"],
            "diagnosis": "Enfermedad A", "treatment": "Tratamiento A"},
        {"symptoms": ["Síntoma 3", "Síntoma 4"],
            "diagnosis": "Enfermedad B", "treatment": "Tratamiento B"},
        # Agregar más datos
    ]
    sintomas = [entry["symptoms"] for entry in tabla_de_datos]
    diagnosticos = [entry["diagnosis"] for entry in tabla_de_datos]
    tratamientos = [entry["treatment"] for entry in tabla_de_datos]
    return sintomas, diagnosticos, tratamientos


def entrenar_modelo(sintomas, diagnosticos):
    modelo = RandomForestClassifier()
    modelo.fit(sintomas, diagnosticos)
    return modelo
