# modelo.py
from sklearn.ensemble import RandomForestClassifier


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
