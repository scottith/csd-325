# Scott Macioce
# Module 9 - Astronaut API Program
# Purpose: Connect to an API, retrieve data, and display it formatted

import requests

# URL for the astronaut API
url = "http://api.open-notify.org/astros.json"

# Make a request to the API
response = requests.get(url)

# Check if the connection was successful
if response.status_code == 200:
    print("Connection successful!")
else:
    print("Failed to connect. Status code:", response.status_code)

# Print the raw JSON response (no formatting)
print("\nRaw JSON Response:")
print(response.json())

# Now format the output nicely
data = response.json()
print("\nFormatted Astronaut Data:")
print(f"There are {data['number']} astronauts in space:")
for astronaut in data['people']:
    print(f" - {astronaut['name']} on {astronaut['craft']}")
