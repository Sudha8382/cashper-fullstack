"""
Create a test user for API testing
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def create_test_user():
    print("Creating test user...")
    
    response = requests.post(
        f"{BASE_URL}/api/auth/register",
        json={
            "fullName": "Insurance Test User",
            "email": "insurance.test@example.com",
            "password": "Test@12345",
            "confirmPassword": "Test@12345",
            "phone": "9123456789",
            "agreeToTerms": True
        }
    )
    
    print(f"Status Code: {response.status_code}")
    
    try:
        data = response.json()
        print(f"Response:\n{json.dumps(data, indent=2)}")
        
        if response.status_code == 200 or response.status_code == 201:
            print("\n✅ Test user created successfully!")
            return True
        elif "already exists" in str(data).lower():
            print("\n✅ Test user already exists!")
            return True
        else:
            print("\n❌ Failed to create test user")
            return False
    except Exception as e:
        print(f"Response Text: {response.text}")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        create_test_user()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to backend server!")
        print(f"   Please ensure the backend is running at {BASE_URL}")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
