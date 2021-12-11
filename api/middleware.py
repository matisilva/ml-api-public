# -*- coding: utf-8 -*-
import json
import settings
import serializers
from uuid import uuid4
from retry import retry


def _send_message(text_data):
    #################################################################
    # COMPLETAR AQUI: Crearemos una tarea para enviar a procesar.
    # Una tarea esta definida como un diccionario con dos entradas:
    #     - "id": será un hash aleatorio generado con uuid4 o
    #       similar, deberá ser de tipo string.
    #     - "text": texto que se quiere procesar, deberá ser de tipo
    #       string.
    # Luego utilice kafka_producer para encolar la tarea.
    #################################################################
    from external import redis_client, kafka_producer
    job_id = str(uuid4())
    #################################################################
    return job_id


@retry(ValueError, delay=1, backoff=2, tries=5)
def _receive_response(job_id):
    #################################################################
    # COMPLETAR AQUI: En cada iteración tenemos que:
    #     1. Intentar obtener resultados desde Redis utilizando
    #        como key nuestro "job_id".
    #     2. Si no obtuvimos respuesta, lanzar exception ValueError
    #     3. Si obtuvimos respuesta, extraiga la predicción y el
    #        score para ser devueltos como salida de esta función.
    #     4. Eliminar los resultados de la BD temporal.
    #################################################################
    from external import redis_client, kafka_producer
    prediction, score = None, None
    #################################################################
    return prediction, score


def model_predict(text_data):
    """
    Esta función recibe sentencias para analizar desde nuestra API,
    las encola en Redis y luego queda esperando hasta recibir los
    resultados, qué son entonces devueltos a la API.

    Attributes
    ----------
    text_data : str
        Sentencia para analizar.

    Returns
    -------
    prediction : str
        Sentimiento de la oración. Puede ser uno de: "Positivo",
        "Neutral" o "Negativo".
    score : float
        Valor entre 0 y 1 que especifica el grado de positividad
        de la oración.
    """
    job_id = _send_message(text_data)
    prediction, score = _receive_response(job_id)

    # TODO hacer un decorador para esto
    print(json.dumps({
        "text": text_data,
        "prediction": prediction,
        "score": score
    }))
    return prediction, score
