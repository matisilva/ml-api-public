# -*- coding: utf-8 -*-

########################################################################
# COMPLETAR AQUI: Crear conexion a redis y asignarla a la variable "db".
########################################################################
db = None
########################################################################


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
    prediction = None
    score = None

    #################################################################
    # COMPLETAR AQUI: Crearemos una tarea para enviar a procesar.
    # Una tarea esta definida como un diccionario con dos entradas:
    #     - "id": será un hash aleatorio generado con uuid4 o
    #       similar, deberá ser de tipo string.
    #     - "text": texto que se quiere procesar, deberá ser de tipo
    #       string.
    # Luego utilice rpush de Redis para encolar la tarea.
    #################################################################
    raise NotImplementedError
    #################################################################

    # Iterar hasta recibir el resultado
    while True:
        #################################################################
        # COMPLETAR AQUI: En cada iteración tenemos que:
        #     1. Intentar obtener resultados desde Redis utilizando
        #        como key nuestro "job_id".
        #     2. Si no obtuvimos respuesta, dormir el proceso algunos
        #        milisegundos.
        #     3. Si obtuvimos respuesta, extraiga la predicción y el
        #        score para ser devueltos como salida de esta función.
        #################################################################
        raise NotImplementedError
        #################################################################

    return prediction, score
