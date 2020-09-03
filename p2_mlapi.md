# Despliegue de sistemas predictivos - Práctico 2
> Diplodatos 2019

En esta segunda iteración, vamos a continuar trabajando en nuestra API para predicción de sentimientos en oraciones, profundizando e implementando lo siguiente:

1. Testing de stress con *Locust*
2. Monitoreo con *EKL*
3. Scaling de servicios
4. Obtener y almacenar feedback de usuarios
5. Usar traefik como un DNS resolver y descubrir sus features

## 1. Testing de stress con *Locust*

Para esta tarea deberá modificar el archivo `locustfile.py` en la carpeta `stress_test`.

- Cree al menos un test de uso del endpoint `index` de nuestra API para evaluar su comportamiento frente a un gran número de usuarios.

- Cree al menos un test de uso del endpoint `predict` de nuestra API para evaluar su comportamiento frente a un gran número de usuarios.

- Detalle en un reporte las especificaciones de hardware del servidor donde está desplegado su servicio y compare los resultados obtenidos para diferentes números de usuarios.

- (Opcional) Reemplace el actual procesamiento de datos secuencial en `ml_service.py` por procesamiento en batches. ¿Nota alguna mejora?

## 2. Monitoreo con *EKL*

Si bien la propuesta es ElasticSearch Kibana y Logstash para mejor entendimiento usaremos tecnologías similares. En este punto se deberá instanciar un stack compuesto de los siguientes servicios:
  - *mongodb*: Para dar soporte de base de datos a graylog en la gestión de usuarios y configuraciones
  - *elasticsearch*: Para el almacenamiento persistente de los datos a ser procesados. En este caso serán logs de salida de los contenedores.
  - *graylog*: Responsable de la gestión de elasticsearch. Creará nuestros indices rotativos con persistencia configurable y además nos permitirá hacer preproceso en la ingestión de datos. Su driver de ingestión de datos nos permitirá conectar la salida de los contenedores de manera nativa.
  - *grafana*: Herramienta que utilizaremos para la creación de dashboards para visualización. Elegida por su versatilidad y fácil entendimiento.

Una vez realizadas las configuraciones iniciales para completar la tarea será necesario enviar los logs al stack instanciado y visualizar dashboards de actividad donde se pueda ver en tiempo real las siguientes estadísticas.

- *req/min* que está recibiendo nuestra API
- *histograma de actividad* diferenciando cuales dieron respuesta positiva y cuales negativa.
- *alerta de errores* al recibir más de 10 request con codigo de error (>=400) en un minuto

*AYUDA*: Aqui (https://docs.graylog.org/en/3.1/pages/installation/docker.html) encontrarán la informacion al respecto de como levantar el stack propuesto. Los pasos para la configuración inicial serán explicados en el teórico. Ademas deberán agregar los prints necesarios para poder ingestar los datos minimos que necesitan para su dashboard.

## 3. Scaling de servicios

El objetivo aqui es duplicar nuestra capacidad de respuesta instanciando un "worker" más en nuestra infraestructura. Para ello deberíamos aumentar la cantidad de réplicas que tenemos del contenedor *model* y visualizar las mejoras en grafana usando nuestro cliente locust para exigir la carga. Para ello deberán utilizar el comando `docker-compose scale <SERVICE>=<#INSTANCES>`

## 4. Obtener y almacenar feedback de usuarios
En las views de nuestro proyecto deberán completar el endpoint para feedback y permitir al usuario así acusar una respuesta incorrecta. Almacenar en un csv todos estos reportes para una futura retroalimentación.

## (Opcional) 5. Usar traefik como un DNS resolver y descubrir sus features
Entre las muchas funcionalidades que traefik tiene integradas podemos encontrar un balanceador de carga con resoluciones DNS.
El desafío propuesto es poder utilizar traefik y descubrir sus funcionalidades integrandolo en nuestro proyecto. Las tareas a realizarse son:

- Descargar e instanciar mediante docker run la imagen [containous/whoami](https://hub.docker.com/r/containous/whoami) y entender la información que esta nos brinda. Dentro de esa información identificar el valor que nos permita conocer la IP del contenedor. Esto sera util para más adelante.
- Levantar al menos 2 servicios (uno con nuestra API y otro sirviendo la imagen pública containous/whoami) y visualizarlos en el dashboard de traefik. Verificar también el acceso mediante el DNS http://my.own.api.localhost y http://my.own.whoami.localhost respectivamente.
- Una vez desplegados los dos servicios, generar réplicas para nuestro servicio whoami con el comando `docker-compose scale whoami=3` y acceder a http://my.own.whoami.localhost para verificar el balanceo de carga entre los distintos contenedores notando las diferentes IP's de contenedores que reciban nuestra petición.

*AYUDA*: Aqui (https://docs.traefik.io/user-guides/docker-compose/basic-example/) encontrarán un ejemplo sencillo de uso de traefik incluso con la imagen containous/whoami.
