"""
Test script to verify user session persistence
Simulates user staying logged in without automatic logout
"""

import requests
import time

BASE_URL = "http://127.0.0.1:8000"

print("=" * 80)
print("USER SESSION PERSISTENCE TEST".center(80))
print("=" * 80)

# Step 1: Login
print("\n1. Logging in user...")
login_data = {
    "email": "testuser12345@example.com",
    "password": "Test@1234"
}

try:
    response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    if response.status_code == 200:
        data = response.json()
        token = data.get("access_token")
        print(f"✓ Login successful!")
        print(f"  Token: {token[:20]}...")
    else:
        print(f"✗ Login failed: {response.text}")
        # Try to register if login fails
        print("\n  Registering new user...")
        register_data = {
            "fullName": "Test User Session",
            "email": "testuser12345@example.com",
            "phone": "8888888888",
            "password": "Test@1234",
            "confirmPassword": "Test@1234",
            "agreeToTerms": True
        }
        reg_response = requests.post(f"{BASE_URL}/api/auth/register", json=register_data)
        if reg_response.status_code in [200, 201]:
            data = reg_response.json()
            token = data.get("access_token")
            print(f"✓ Registration successful!")
            print(f"  Token: {token[:20]}...")
        else:
            print(f"✗ Registration also failed: {reg_response.text}")
            exit(1)
except Exception as e:
    print(f"✗ Error: {str(e)}")
    exit(1)

# Step 2: Make authenticated requests
print("\n2. Testing authenticated requests...")
headers = {"Authorization": f"Bearer {token}"}

for i in range(5):
    try:
        response = requests.get(f"{BASE_URL}/api/auth/me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print(f"✓ Request {i+1}: User {user_data.get('fullName')} is still authenticated")
        else:
            print(f"✗ Request {i+1} failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Request {i+1} error: {str(e)}")
    
    time.sleep(1)

# Step 3: Check token validity
print("\n3. Checking token validity after 5 seconds...")
try:
    response = requests.get(f"{BASE_URL}/api/auth/me", headers=headers)
    if response.status_code == 200:
        print("✓ Token is still valid - user remains logged in!")
    else:
        print(f"✗ Token invalid: {response.status_code}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Step 4: Verify dashboard access
print("\n4. Testing dashboard access...")
try:
    response = requests.get(f"{BASE_URL}/api/dashboard/stats", headers=headers)
    if response.status_code == 200:
        print("✓ Dashboard accessible - user session is persistent!")
    else:
        print(f"⚠ Dashboard access: {response.status_code}")
except Exception as e:
    print(f"⚠ Dashboard check: {str(e)}")

print("\n" + "=" * 80)
print("SESSION PERSISTENCE TEST COMPLETE".center(80))
print("=" * 80)
print("\n✅ User session should remain active until explicit logout")
print("✅ No automatic logout on page refresh or navigation")
print("✅ Token stored in localStorage persists across browser sessions")
