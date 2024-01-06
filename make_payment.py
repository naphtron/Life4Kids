import get_mpesa_token
from datetime import datetime
import requests
import os
import base64 
import json
from dotenv import load_dotenv
from get_mpesa_token import getAccessToken

load_dotenv()

def initiate_payment(amount,phone_number,session_id):
    #headers
    access_token = getAccessToken()
    if access_token:
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }
        BusinessShortCode = 174379
        Timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        Passkey = os.getenv('Passkey')
        Password = base64.b64encode((str(BusinessShortCode) + Passkey + str(Timestamp)).encode('utf8')).decode()
        TransactionType = 'CustomerPayBillOnline'
        Amount = int(amount)
        PartyA = int(phone_number[1:])
        PhoneNumber = int(phone_number[1:])
        CallBackURL = 'https://016f-196-250-209-182.ngrok-free.app/'
        acc_ref = "Life4Kids"
        TransactionDesc = "Donation"
        request_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

        payload = {
        "BusinessShortCode": BusinessShortCode,
        "Password": Password,
        "Timestamp": Timestamp,
        "TransactionType": TransactionType,
        "Amount": Amount,
        "PartyA": PartyA,
        "PartyB": BusinessShortCode,
        "PhoneNumber":PhoneNumber ,
        "CallBackURL": CallBackURL,
        "AccountReference": acc_ref,
        "TransactionDesc": TransactionDesc 
        }

        
        res = requests.post(request_url, headers=headers, json=payload)
        # response.raise_for_status()
        print(res.json())
        return res.json()
    
    else:
        return "Error 🤦‍♂️"




###################

# import requests

# ​
# payload = {
#     "BusinessShortCode": 174379,
#     "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwMTA2MDgxNDA5",
#     "Timestamp": "20240106081409",
#     "TransactionType": "CustomerPayBillOnline",
#     "Amount": 1,
#     "PartyA": 254707479652,
#     "PartyB": 174379,
#     "PhoneNumber": 254707479652,
#     "CallBackURL": "https://mydomain.com/path",
#     "AccountReference": "CompanyXLTD",
#     "TransactionDesc": "Payment of X" 
#   }
# ​
# response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
# print(response.text.encode('utf8'))