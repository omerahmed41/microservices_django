import json
import pika
import logging

logger = logging.getLogger(__name__)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "rabbitmq", 5672, "/", pika.PlainCredentials("guest", "guest")
    )
)
channel = connection.channel()
channel.queue_declare(queue="likes")


def callback(ch, method, properties, body):
    print("Received in likes...")
    print(body)
    data = json.loads(body)
    print(data)
    send_email()


def send_email():
    print("Sending email: Dear Omer, thanks for joining us")


channel.basic_consume(queue="likes", on_message_callback=callback, auto_ack=True)
logging.info("Started Consuming...")
print("Started Consuming...")
channel.start_consuming()
