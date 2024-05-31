from rabbitmq_manager import RabbitMQManager
from database_manager import mongodb
from datetime import timedelta
import datetime
import time
from email_manager import email_manager


class main:
    def __init__(self) -> None:
        self.rabbitmq_queue = RabbitMQManager()
        self.database_manager = mongodb()
        self.email_manager = email_manager()
        self.rabbitmq_status_list = []
        self.database_status_list = []

    def check_queue_size(self):
        self.rabbitmq_queue.send_message()

    def check_time_status(self):
        self.current_time = datetime.datetime.now().second  # change second to min

        if self.current_time % 5 in [0, 5]:
            print("5 min completed")
            self.rabbitmq_status_list.append(self.rabbitmq_queue.reconnect())
            self.database_status_list.append(self.database_manager.reconnect())
        print(self.current_time)
        print("len", len(self.rabbitmq_status_list), len(self.database_status_list))

        if len(self.rabbitmq_status_list) > 2 and len(self.database_status_list) > 2:
            print(self.rabbitmq_status_list[0], self.database_status_list[0])
            a = self.rabbitmq_status_list.pop(0)
            b = self.database_status_list.pop(0)
            print(a, b)

        elif (
            len(self.rabbitmq_status_list) == 2 and len(self.database_status_list) == 2
        ):
            print(all(self.rabbitmq_status_list), all(self.database_status_list))
            
            if not True in self.rabbitmq_status_list:
                self.email_manager.send_email()
                self.rabbitmq_status_list = []
            else:
                if self.rabbitmq_queue.check_queue_lenght():
                    self.email_manager.send_email()
                    
            if not True in self.database_status_list:
                self.email_manager.send_email()
                self.database_status_list = []
                


main = main()

# main.check_queue_size()


while True:
    main.check_time_status()

    time.sleep(1)
