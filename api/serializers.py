import json


def serialize_json(message):
    return json.dumps(message).encode('utf-8')


def deserialize_json(message):
    return json.loads(message.decode('utf-8'))