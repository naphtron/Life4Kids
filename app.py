from flask import Flask, request
from dotenv import load_dotenv
from make_payment import initiate_payment
import os

load_dotenv()

app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    if text == '':
        response  = "CON Welcome to Life4Kids Donations\n"
        response += "1. Make a Donation \n"
        response += "2. Check Donation History"
    elif text == '1':
        response = "CON Enter Amount You Wish To Donate\n"
    elif text.startswith('1*'):
        amount = text.split('*')[1]
        response = initiate_payment(amount, phone_number, session_id)
    elif text == '2':
        response = "END This is your phone number " + phone_number

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT'))