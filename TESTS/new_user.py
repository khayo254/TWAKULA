import requests

# Define the endpoint URL
url = 'http://localhost:5000/api/users'  # Adjust the URL according to your Flask app's address

# Define the user data
user_data = {
    'username': 'example_user',
    'email': 'example@example.com',
    'password': 'example_password'
}

# Send a POST request to create a new user
response = requests.post(url, json=user_data)

# Check the response status code
if response.status_code == 201:
    print('User created successfully')
else:
    print('Failed to create user:', response.text)
