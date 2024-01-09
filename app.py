from flask import Flask, request, jsonify
from dotenv import load_dotenv
from make_payment import initiate_payment
from datetime import datetime
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
        response = f"END You will receive a confirmation message KES{amount} Donation"
    elif text == '2':
        response = " END To be implemented " + phone_number

    return response
@app.route('/callback')
def handle_callback():
    content_type = request.headers.get('Content-Type')

    if content_type and content_type.startswith('application/json'):
        try:
            data = request.json
            # Process the JSON data as needed
            ResultCode = data['Body']['stkCallback']['ResultCode']
            ResultDesc = data['Body']['stkCallback']['ResultDesc']
            Items = data['Body']['stkCallback']['CallbackMetadata']['Item']
            if ResultCode == 0:
                amount = Items[0]['Value']
                mpesa_receipt_number = Items[1]['Value']
                transaction_date = datetime.strptime(Items[2]['Value'])
                phone_number = Items[3]['Value']

            else:
                print(f"Result Code: {ResultCode}\n")
                print(f"Result Desc: {ResultDesc}")

            print("Received JSON data:", data)
            return jsonify(data)
        except Exception as e:
            print(f"Error processing JSON data: {e}")
            return jsonify({'status': 'error', 'message': 'Invalid JSON data'}), 400
    else:
        return jsonify({'status': 'error', 'message': 'Unsupported Content-Type'}), 415


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT'))