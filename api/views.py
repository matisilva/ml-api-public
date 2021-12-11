# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
)
from middleware import model_predict

router = Blueprint('app_name',
                   __name__,
                   template_folder='templates')


@router.route('/', methods=['GET', 'POST'])
def index():
    """
    Esta función renderiza un frontend donde podemos ingresar
    sentencias y obtener una prediccion de su sentimiento.
    """
    context = {
        'text': None,
        'prediction': None,
        'score': None,
        'success': False
    }
    # Obtiene la sentencia ingresada por el usuario en el frontend
    text_data = request.form.get('text_data')

    if text_data:
        #################################################################
        # COMPLETAR AQUI: Envie el texto ingresado para ser procesado
        # por nuestra función model_predict.
        # Luego con los resultados obtenidos, complete el diccionario
        # "context" para mostrar la predicción en el frontend.
        #################################################################
        pass
        #################################################################

    return render_template('index.html', context=context)


@router.route('/feedback', methods=['GET', 'POST'])
def feedback():
    #################################################################
    # OPCIONAL COMPLETAR AQUI: guardar la informacion envianda en un archivo
    # en /src/feedback. Luego podran usar esa informacion para reentrenar
    #################################################################
    context = {
        'text': None,
        'prediction': None,
        'score': None,
        'success': False
    }
    return render_template('index.html', context=context)


@router.route('/predict', methods=['POST'])
def predict():
    """
    Método POST que permite obtener predicciones de analisis de
    sentimiento a partir de oraciones.
    """
    # Respuesta inicial
    rpse = {
        'success': False,
        'prediction': None,
        'score': None
    }

    # Nos aseguramos que el método sea correcto y tengamos datos
    # para procesar
    if request.method == 'POST' and request.args.get('text'):
        #################################################################
        # COMPLETAR AQUI: Extraiga la sentencia a procesar y utilice la
        # función middleware.model_predict para obtener el sentimiento
        # de la misma. Complete los campos de "rpse" con los valores
        # obtenidos.
        #################################################################
        text_data = None
        prediction, score = None, None
        #################################################################
        rpse = {
            "text": text_data,
            "prediction": prediction,
            "score": score,
            "success": True
        }
        return jsonify(rpse)

    return jsonify(rpse), 400
