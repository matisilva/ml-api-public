# -*- coding: utf-8 -*-
import os

# API
API_DEBUG = True

# KAFKA
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'service_topic')
KAFKA_SERVER_HOST = os.getenv('KAFKA_SERVER_HOST', 'kafka')
KAFKA_SERVER_PORT = os.getenv('KAFKA_SERVER_PORT', 29092)
KAFKA_SERVERS = ['{}:{}'.format(KAFKA_SERVER_HOST, KAFKA_SERVER_PORT)]
KAFKA_PARTITIONS = 10
KAFKA_REPLICATION_FACTOR = 1


# REDIS
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT =os.getenv('REDIS_PORT', 6379)
REDIS_DB =os.getenv('REDIS_DB', 0)