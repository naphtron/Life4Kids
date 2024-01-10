import africastalking
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = os.getenv('USERNOMBRE')
        self.api_key = os.getenv('API_KEY')
        print(self.api_key)
        print(self.username)

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, recipients, message):
        # Set the numbers you want to send to in international format
        self.recipients = [str(recipients)]

        # Set your message
        self.message = str(message)

        # Set your shortCode or senderId
        sender = "shortCode or senderId"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(self.message, self.recipients)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))

# SMS().send("+254715702887","Hello")
# if __name__ == '__main__':
#     SMS().send()