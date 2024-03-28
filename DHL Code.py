import http.client
import urllib.parse
import json
import csv
import time

# Your API key and secret
api_key = 'Your_API_Key_Here'

# Define the CSV file path
csv_file_path = "DHL status.csv"

# Function to make the API request with retry logic
def make_api_request(number, retries=10, delay=5.1):
    for attempt in range(retries):
        params = urllib.parse.urlencode({
            'trackingNumber': number,
            'service': 'express'
        })

        headers = {
            'Accept': 'application/json',
            'DHL-API-Key': api_key
        }

        connection = http.client.HTTPSConnection("api-eu.dhl.com")
        connection.request("GET", "/track/shipments?" + params, headers=headers)
        response = connection.getresponse()
        data = json.loads(response.read())
        
        if 'shipments' in data:
            return data  # Return data if 'shipments' is present
        else:
            print(f"Retry {attempt + 1}/{retries} for tracking number {number}")
            time.sleep(delay)

    return None

# Prepare the CSV file header
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tracking Number', 'Final Status', 'Timestamp'])

# Input tracking numbers
tracking_numbers = []
failed_tracking_numbers = []  # To keep track of failed tracking numbers
print("Please paste tracking numbers separated by line breaks, when done press enter twice:")
while True:
    number = input().strip()
    if number:
        tracking_numbers.append(number)
    else:
        break

# Process each tracking number
for number in tracking_numbers:
    data = make_api_request(number)
    if data and 'shipments' in data:
        final_status = data['shipments'][0]['status']['status']
        final_timestamp = data['shipments'][0]['status']['timestamp']
        print(f"Final Status: {final_status} at {final_timestamp}")
    else:
        print(f"Failed to retrieve data for tracking number {number}")
        final_status = "Data not received"
        final_timestamp = ""
        failed_tracking_numbers.append(number)

    # Write to the CSV file regardless of success or failure
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number, final_status, final_timestamp])

# Summarize what needs manual review
if failed_tracking_numbers:
    print("\nPlease manually review the following tracking numbers as their data was not retrieved:")
    for num in failed_tracking_numbers:
        print(num)
