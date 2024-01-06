from flask import Flask, request
from dotenv import load_dotenv
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
        response += "1. Account number \n"
        response += "2. Account balance"
    elif text == '1*1':
        accountNumber  = "ACC1001"
        response = "END Your account number is " + accountNumber
    elif text == '1*2':
        balance  = "KES 10,000"
        response = "END Your balance is " + balance
    elif text == '2':
        response = "END This is your phone number " + phone_number

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT'))