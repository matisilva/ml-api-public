
import settings
import kafka
import redis
import serializers

########################################################################
# COMPLETAR AQUI: Crear conexion a redis y asignarla a la variable "db".
########################################################################
redis_client = None

kafka_producer = None

kafka_consumer = None
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
        pass

    try:
        client.create_partitions({
            settings.KAFKA_TOPIC: kafka.admin.new_partitions.NewPartitions(settings.KAFKA_PARTITIONS)
        })
    except kafka.errors.InvalidPartitionsError:
        pass
