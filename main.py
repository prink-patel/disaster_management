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
        self.email_manager_counter_database = 0
        self.email_manager_counter_rabbit = 0

    def check_queue_size(self):
        self.rabbitmq_queue.send_message()

    def check_time_status_5min(self):
        self.current_time = datetime.datetime.now().second  # change second to min

        if self.current_time % 5 in [0, 5]:
            print("5 min completed")
            self.rabbitmq_status_list.append(self.rabbitmq_queue.reconnect())
            self.database_status_list.append(self.database_manager.reconnect())

            self.check_send_email()

    def check_send_email_status(self):
        print("first", self.rabbitmq_status_list, self.database_status_list)

        if self.rabbitmq_queue.check_queue_lenght():
            print("queue length", self.rabbitmq_queue.check_queue_lenght())
            self.email_manager.rabbitmq_send_email()

        if len(self.rabbitmq_status_list) < 2 and len(self.database_status_list) < 2:
            pass
        else:

            if (
                len(self.rabbitmq_status_list) == 2
                or len(self.database_status_list) == 2
            ):
                if len(self.rabbitmq_status_list) == 2:
                    if True not in self.rabbitmq_status_list:
                        if self.email_manager_counter_rabbit >= 3:
                            self.email_manager.rabbitmq_send_email()
                            self.email_manager_counter_rabbit = 0
                        else:
                            self.email_manager_counter_rabbit += 1
                        self.rabbitmq_status_list = []
                    else:
                        self.email_manager_counter_rabbit = 0
                        
                if len(self.database_status_list) == 2:
                    if True not in self.database_status_list:
                        if self.email_manager_counter_database >= 3:
                            self.email_manager.database_send_email()
                            self.email_manager_counter_database = 0
                        else:
                            self.email_manager_counter_database += 1
                        self.database_status_list = []
                    else:
                        self.email_manager_counter_database = 0
                        
            if len(self.rabbitmq_status_list) > 2:
                for _ in range(len(self.rabbitmq_status_list) - 2):
                    self.rabbitmq_status_list.pop(0)
            if len(self.database_status_list) > 2:
                for _ in range(len(self.database_status_list) - 2):
                    self.database_status_list.pop(0)



main = main()

while True:
    main.check_time_status()

    time.sleep(1)
