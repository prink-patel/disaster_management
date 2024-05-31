from datetime import timedelta
import datetime
import boto3
# from constants import AWS_REGION, AWS_SES_ACCESS_KEY, AWS_SES_SECRET_KEY, RECEIVER_LIST, SENDER_EMAIL

class email_manager:
    def __init__(self) -> None:
        self.rebbitmq_previous_time_status = datetime.datetime.now().second
        self.database_previous_time_status = datetime.datetime.now().second
        
    def rabbitmq_send_email(self):
        print("second",self.rebbitmq_previous_time_status-datetime.datetime.now().second)
        if datetime.datetime.now().second-self.rebbitmq_previous_time_status >= 1:
            print("*"*10)
            print("send email for rabbitmq")
            self.rebbitmq_previous_time_status = datetime.datetime.now().second
        else:
            print("no need to send email rab")
        print("time", self.rebbitmq_previous_time_status, self.database_previous_time_status)
            
    def database_send_email(self):   
        if self.database_previous_time_status-datetime.datetime.now().second >= 1:
            print("*"*10)
            print("send email for database")
            self.database_previous_time_status = datetime.datetime.now().second
        
        else:
            print("no need to send email data")
        print("time", self.rebbitmq_previous_time_status, self.database_previous_time_status)
        
        
# class MailNotifier:
#     def __init__(self) -> None:
#         # self.client = boto3.client('ses', region_name='us-east-1', aws_access_key_id=AWS_SES_ACCESS_KEY, aws_secret_access_key=AWS_SES_SECRET_KEY)
#         pass

#     def send_mail(self, subject, body):
#         print(f"{subject}: {body}")
#         return
#         response = self.client.send_email(
#             Destination={
#                 'ToAddresses': RECEIVER_LIST,
#             },
#             Message={
#                 'Body': {
#                     'Text': {
#                         'Charset': 'UTF-8',
#                         'Data': body,
#                     },
#                 },
#                 'Subject': {
#                     'Charset': 'UTF-8',
#                     'Data': subject,
#                 },
#             },
#             Source=SENDER_EMAIL,
#         )
#         return response