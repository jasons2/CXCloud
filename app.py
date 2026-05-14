from creds import client_id, client_secret
import requests

def get_hardware(bearer_token: str, customer_id: str) -> list:
    url = f"https://apix.cisco.com/cs/api/v2/inventory/hardware?customerId={customer_id}"

    payload = None

    headers = { "Accept": "application/json" }

    response = requests.request('GET', 
                                url, 
                                headers=headers, 
                                data = payload)

    return response.text.encode('utf8') 


def get_customer_details(bearer_token: str) -> str:
    ### Get Customer Details

    url = "https://apix.cisco.com/cs/api/v2/customer-info/customer-details"

    # Define the headers
    headers = {
        "Accept": "application/json",
        'Authorization': 'Bearer {bearer_token}'
    }

    try:
        # Perform the GET request
        response = requests.get(url, 
                                headers=headers)
        
        # Check for HTTP errors
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return response.text.encode('utf8')


def get_bearer_token(client_id: str, client_secret: str) -> str:

    url = "https://id.cisco.com/oauth2/default/v1/token"

    # The data dictionary handles the application/x-www-form-urlencoded encoding
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    try:
        response = requests.post(url, 
                                 data=payload)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return response.json()['access_token']


def main():
    bearer_token= get_bearer_token(client_id, client_secret)

    # Print results from get customer details function
    print(get_customer_details(bearer_token))

if __name__ == "__main__":
    main()