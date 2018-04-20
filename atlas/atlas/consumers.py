from channels.generic.websocket import WebsocketConsumer
import json

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaiiids')

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        self.send(text_data=json.dumps({
            'message': message
        }))

    def notification_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
