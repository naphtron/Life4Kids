import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

request = ""
######
def getAccessToken(request):
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    req = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(req.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    print(f'Access token{mpesa_access_token}')
    print(f'Validated access token: {validated_mpesa_access_token}')

getAccessToken(request)