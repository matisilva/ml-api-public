# Despliegue de sistemas predictivos - Práctico 1
> Diplodatos 2019

En este proyecto, construiremos y desplegaremos nuestra propia API que brindará servicios de Machine Learning, en este caso, predicción de sentimientos para oraciones en Español.

La estructura base del proyecto será la siguiente:

```
├── api
│   ├── Dockerfile
│   ├── app.py
│   ├── middleware.py
│   ├── views.py
│   ├── settings.py
│   ├── templates
│   │   └── index.html
│   └── tests
│       └── test_api.py
├── model
│   ├── Dockerfile
│   ├── ml_service.py
│   ├── settings.py
│   └── tests
│       └── test_model.py
├── stress_test
│   └── locustfile.py
├── docker-compose.yml
├── README.md
└── tests
    └── test_integration.py
```

Veamos una descripción rasgos generales de cada modulo:

- api: Contiene todo el código necesario para implementar la interfaz de comunicación entre el usuario y nuestro servicio, está implementada en Flask y utiliza Redis para encolar tareas a ser procesadas por nuestro modelo de Machine Learning.
    - `api/app.py`: Configura y lanza nuestro servicio en Flask.
    - `api/views.py`: Implementa los endpoints de nuestro servicio. En este práctico tenemos que implementar dos endpoints básicos (aunque puede agregar adicionales si usted lo desea)
        - *index*: Encargado de renderizar un frontend en el cual el usuario puede escribir oraciones y obtener el sentimiento de las mismas
        - *predict*: Método POST que recibe un texto y nos devuelve una predicción de sentimiento del mismo. Este endpoint es útil como acceso genérico para integrarse con otras plataformas ya que puede consultarse utilizando algún lenguaje de programación como Python, Java, etc.
    - `api/settings.py`: Contiene las configuraciones generales de nuestra API.
    - `api/templates`: Contiene el frontend de nuestro servicio.
    - `api/tests`: Suite de tests.
- model: Módulo con las funciones necesarias para obtener tareas desde Redis y procesarlas con nuestro modelo de Machine Learning. Una vez obtenidos los resultados, debemos encolarlos para que sean devueltos al usuario. Utilizaremos un modelo de analisis de sentimientos para oraciones en español ya entrenado que puede ser instalado simplemente con pip ([link](https://github.com/aylliote/senti-py)).
    - `model/ml_service.py`: Corre un hilo que se encarga de obtener tareas, procesarlas y devolver una respuesta.
    - `model/settings.py`: Configuraciones generales para nuestro modelo.
    - `model/tests`: Suite de tests.
- tests: Contiene tests de integración para validar que nuestro servicio funciona correctamente end-to-end, partiendo desde el punto de entrada (api) hasta el procesamiento y obtención de resultados (model).

Su tarea será completar con el código correspondiente donde sea requerido en los diferentes módulos del proyecto. Puede validar si su funcionamiento es el esperado ejecutando los tests ya brindados.
