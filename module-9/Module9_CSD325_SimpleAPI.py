
# Scott Macioce
# Module 9 - Joke API Program
# Purpose: Connect to a simple API and retrieve a random joke

import requests

# URL for a simple joke API
url = "https://official-joke-api.appspot.com/random_joke"

# Make a request
response = requests.get(url)

# Check connection
if response.status_code == 200:
    print("Connection successful!")
else:
    print("Failed to connect. Status code:", response.status_code)

# Print the raw JSON
print("\nRaw JSON Response:")
print(response.json())

# Nicely format the joke
data = response.json()
print("\nFormatted Joke:")
print(f"{data['setup']} - {data['punchline']}")
