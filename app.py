from model import cargar_datos_entrenamiento, entrenar_modelo
from flask import Flask, render_template, request

app = Flask(__name__)

# Importa las funciones definidas en model.py

# Cargar datos de entrenamiento y entrenar el modelo al iniciar la aplicación
sintomas, diagnosticos, tratamientos = cargar_datos_entrenamiento()
modelo = entrenar_modelo(sintomas, diagnosticos)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/procesar', methods=['POST'])
def procesar():
    # Obtener los síntomas seleccionados por el usuario desde el formulario
    sintomas_usuario = request.form.getlist('sintomas')

    # Realizar una predicción con el modelo
    diagnosticos_sugeridos = []

    for i, sintomas_enfermedad in enumerate(sintomas):
        # Verificar si los síntomas del usuario coinciden con los síntomas de una enfermedad
        if set(sintomas_usuario).issubset(sintomas_enfermedad):
            diagnosticos_sugeridos.append(diagnosticos[i])

    # Mostrar los diagnósticos sugeridos al usuario
    return render_template('resultado.html', diagnosticos=diagnosticos_sugeridos)


if __name__ == "__main__":
    app.run(debug=True)
