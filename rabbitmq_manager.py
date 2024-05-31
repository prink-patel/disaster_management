from constant import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
    RABBITMQ_PASSWORD,
    RABBIT_QUEUE_NAME,
    RABBIT_EXCHANGE_NAME,
    RABBIT_ROUTING_KEY,
    RABBIT_QUEUE_MAX_SIZE
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

    def check_queue_lenght(self):
        try:
            self.queue = self.channel.queue_declare(queue=RABBIT_QUEUE_NAME, passive=True)
            self.channel.queue_bind(queue=self.queue.method.queue, exchange=RABBIT_EXCHANGE_NAME, routing_key=RABBIT_ROUTING_KEY)
            message_count = self.queue.method.message_count

            if message_count >= RABBIT_QUEUE_MAX_SIZE:
                return False
        except Exception as e:
            print(e)
            return False
