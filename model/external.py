
import settings
import kafka
import redis
import serializers

########################################################################
# COMPLETAR AQUI: Crear conexion a redis y asignarla a la variable "db".
########################################################################
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)

kafka_producer = kafka.KafkaProducer(
   value_serializer=serializers.serialize_json,
   bootstrap_servers=settings.KAFKA_SERVERS,
)

kafka_consumer = kafka.KafkaConsumer(
    settings.KAFKA_TOPIC,
    value_deserializer=serializers.deserialize_json,
    bootstrap_servers=settings.KAFKA_SERVERS,
    auto_offset_reset='earliest',
    group_id=settings.KAFKA_TOPIC
)
########################################################################

def startup():
    # Create or setup topic with respective partiions
    client = kafka.KafkaAdminClient(bootstrap_servers=settings.KAFKA_SERVERS)
    try:
        client.create_topics(
            [kafka.admin.NewTopic(
                name=settings.KAFKA_TOPIC,
                num_partitions=settings.KAFKA_PARTITIONS,
                replication_factor=settings.KAFKA_REPLICATION_FACTOR)
            ],
            validate_only=False
        )
    except kafka.errors.TopicAlreadyExistsError:
        client.create_partitions({
            settings.KAFKA_TOPIC: kafka.admin.new_partitions.NewPartitions(settings.KAFKA_PARTITIONS)
        })