import requests
import json

# API endpoint
endpoint_url = "https://api.discord.gx.games/v1/direct-fulfillment"

# Base URL for formatting
base_url = "https://discord.com/billing/partner-promotions/1180231712274387115/"

# Initialize an empty list to store tokens
tokens = []

# Iterate over 250 partner IDs
for i in range(250):
    # Change the partner ID for each request
    partner_id = f"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b944ca158891b7851b8{i:03d}"

    # Prepare the payload
    payload = {"partnerUserId": partner_id}

    try:
        # Send a POST request to the API endpoint
        response = requests.post(endpoint_url, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the token is in the response JSON, adjust accordingly
            token = response.json().get('token')
            
            # Store the token in the list
            tokens.append(token)

            # Save the token in the specified format to a text file
            with open("tokens2.txt", "a") as txt_file:
                txt_file.write(f"{base_url}{token} \n")  # Add a space after each entry
        else:
            print(f"Request {i + 1} failed. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Tokens have been saved to tokens.txt")
