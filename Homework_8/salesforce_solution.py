import requests
import json
import configparser

# Load configuration
config = configparser.ConfigParser()
config.read('salesforceconfig.ini')

# Prepare OAuth2 request data
auth_url = f"{config['OAUTH']['base_url']}/services/oauth2/token"
auth_data = {
    'grant_type': config['OAUTH']['grant_type'],
    'client_id': config['OAUTH']['client_id'],
    'client_secret': config['OAUTH']['client_secret'],
    'username': config['OAUTH']['username'],
    'password': config['OAUTH']['password'] + config['OAUTH']['security_token']
}

# Get the access token
auth_response = requests.post(auth_url, data=auth_data)
auth_response.raise_for_status()  # Check for errors in request
access_token = auth_response.json().get('access_token')

# Retrieve Account data using the access token
query_url = f"{config['OAUTH']['base_url']}/services/data/v55.0/query/?q=SELECT+NAME+,+ID+,+BillingAddress+FROM+ACCOUNT"
headers = {'Authorization': f'Bearer {access_token}'}
account_response = requests.get(query_url, headers=headers)

# Output the response as a byte stream
print(account_response.content)
