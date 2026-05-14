from creds import client_id, client_secret
import requests

# Get Access Token
url = "https://id.cisco.com/oauth2/default/v1/token"

# The data dictionary handles the application/x-www-form-urlencoded encoding
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

try:
    response = requests.post(url, data=payload)
    
    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()
    
    # Print the JSON response
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

bearer_token = response.json()['access_token']

### Get Customer Details

url = "https://apix.cisco.com/cs/api/v2/customer-info/customer-details"

# Define the headers
headers = {
    "Accept": "application/json",
    'Authorization': 'Bearer {bearer_token}'
}

try:
    # Perform the GET request
    response = requests.get(url, headers=headers)
    
    # Check for HTTP errors
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


import sys
sys.exit()

#### Make Request

url = "https://apix.cisco.com/cs/api/v2/inventory/hardware?customerId="

payload = None

headers = { "Accept": "application/json" }

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

