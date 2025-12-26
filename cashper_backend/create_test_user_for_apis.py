"""
Create a test user for API testing
"""
import requests
import json

BASE_URL = "http://localhost:8000"

# Test user details
test_user = {
    "fullName": "Test User",
    "email": "test@example.com",
    "phone": "9876543210",
    "password": "Test@123",
    "confirmPassword": "Test@123"
}

print("Creating test user...")
response = requests.post(f"{BASE_URL}/api/auth/signup", json=test_user)

if response.status_code == 201:
    print(f"✅ Test user created successfully!")
    print(f"Email: {test_user['email']}")
    print(f"Password: {test_user['password']}")
elif response.status_code == 400:
    print(f"ℹ️ User might already exist. Trying to login...")
    
    login_data = {
        "email": test_user["email"],
        "password": test_user["password"]
    }
    
    response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    
    if response.status_code == 200:
        print(f"✅ Login successful!")
        token = response.json().get("access_token")
        print(f"Token: {token[:20]}...")
    else:
        print(f"❌ Login failed: {response.json()}")
else:
    print(f"❌ Failed to create user: {response.json()}")
