import json
import pika


def publish(method, body):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            "rabbitmq", 5672, "/", pika.PlainCredentials("guest", "guest")
        )
    )
    channel = connection.channel()
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="likes", body=json.dumps(body), properties=properties
    )
