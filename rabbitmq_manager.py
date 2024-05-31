from constant import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
    RABBITMQ_PASSWORD,
    RABBIT_QUEUE_NAME,
    RABBIT_EXCHANGE_NAME,
    RABBIT_ROUTING_KEY,
)
import pika
import time
import random
from queue import Queue


class RabbitMQManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        # logger.info(f"RabbitMQManager Called")

        # Queue to store msgs
        self.rabbitmq_queue = Queue(maxsize=500)
        self.running = True

        # RabbitMQ Connection
        self.credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        self.parameters = pika.ConnectionParameters(
            RABBITMQ_HOST, credentials=self.credentials
        )

    def reconnect(self):
        connected = False
        time.sleep(1)
        try:
            # logger.info("Reconnecting and publishing")
            self.connection = pika.BlockingConnection(self.parameters)
            self.channel = self.connection.channel()
            connected = True
        except Exception:
            # logger.info(f"Exception in reconnect_and_publish {traceback.print_exc()}")
            time.sleep(0.1)
            pass
        return connected


    def message_count(self):
        return False
    
    def message_count_(self):
        print(self.message_queue.method.message_count)

    def send_message(self):
        connection = pika.BlockingConnection(self.parameters)

        channel = connection.channel()

        self.message_queue = channel.queue_declare(queue=RABBIT_QUEUE_NAME)

        employee__id = 1

        while True:

            message = f"sending message id: {employee__id}"

            channel.basic_publish(exchange="", routing_key="letterbox", body=message)

            print(f"send message: {message}")
            time.sleep(random.randint(1, 4))

            employee__id += 1
            self.message_count_()
