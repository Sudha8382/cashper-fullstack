import requests
import json

# First, let's try to register a new user
base_url = "http://localhost:8000/api/auth"

print("="*60)
print("Testing Authentication Flow")
print("="*60)

# Step 1: Register a new user
print("\n1. Registering a new test user...")
register_url = f"{base_url}/register"
register_data = {
    "fullName": "Test User",
    "email": "testuser@example.com",
    "password": "Test@1234",
    "confirmPassword": "Test@1234",
    "phone": "9876543210",
    "agreeToTerms": True
}

try:
    response = requests.post(register_url, json=register_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("✅ Registration successful!")
    elif response.status_code == 400:
        print("⚠️  User might already exist, trying to login...")
except Exception as e:
    print(f"❌ Registration error: {str(e)}")

# Step 2: Try to login
print("\n2. Attempting to login...")
login_url = f"{base_url}/login"
login_data = {
    "email": "testuser@example.com",
    "password": "Test@1234"
}

try:
    response = requests.post(login_url, json=login_data)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Login successful!")
        print(f"Access Token: {data.get('access_token', 'N/A')[:50]}...")
        print(f"User: {json.dumps(data.get('user', {}), indent=2)}")
    else:
        print(f"❌ Login failed: {response.json()}")
except Exception as e:
    print(f"❌ Login error: {str(e)}")

print("\n" + "="*60)
