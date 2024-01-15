from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from make_payment import initiate_payment
from send_sms import SMS
from datetime import datetime
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#instantiate sms object
sendSMS = SMS()

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer)
    phone_number = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    mpesa_receipt_number = db.Column(db.String(15))
    transaction_date = db.Column(db.DateTime)

def get_user_data(phone_number):
    # Query a user by email or username
    donations = Donation.query.filter((Donation.phone_number == phone_number)).all()
    for donation in donations:
        # Return user information as a dictionary
        donation_info = "Donation History\n"
        donation_info += f'Date: {donation.transaction_date.strftime("%d/%m/%Y %H:%M")}\n'
        donation_info += f'Amount: KES{donation.amount}'

        return donation_info
    else:
        return None

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    global session_id
    data = request.get_json()
    session_id = data.get("sessionId", None) 
    #session_id = request.values.get("sessionId", None) 
    service_code = data.get("serviceCode", None)
    #service_code = request.values.get("serviceCode",None)
    phone_number = data.get("phoneNumber", None)
    #phone_number = request.values.get("phoneNumber",None)
    text = data.get("text", "default")
    #text = request.values.get("text","default")
    print(session_id, service_code, phone_number, text)
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
        response = "Your donation history details will be forwarded to you shortly."
        res = get_user_data(f'{str(phone_number)}')
        if res:
            sendSMS.send(f'{str(phone_number)}',res)
            print("Success")
        else:
            sendSMS.send(f'{str(phone_number)}',"You have made no donations yet")
            print("Success: No Dons")
    return response

@app.route('/callback', methods=['POST','GET'])
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
                transaction_date = datetime.strptime(str(Items[3]['Value']),"%Y%m%d%H%M%S")
                phone_number = Items[4]['Value']
                phone_number = f'+{str(phone_number)}'
                message = f"Your KES{int(amount)} donation has been received.\nThank you for supporting Life4Kids 💙"
                sendSMS.send(phone_number,message)
                new_donation = Donation(session_id=session_id, phone_number=phone_number, amount=amount, transaction_date=transaction_date)
                db.session.add(new_donation)
                db.session.commit()
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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT'), debug=True)