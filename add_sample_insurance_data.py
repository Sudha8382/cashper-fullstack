"""
Add sample insurance data to test user
"""

import requests
import json

BASE_URL = "http://localhost:8000"
TEST_EMAIL = "insurance.test@example.com"
TEST_PASSWORD = "Test@12345"

def login():
    """Login and get user token"""
    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json={
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
    )
    
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"Login failed: {response.json()}")
        return None

def add_health_insurance(token):
    """Add health insurance inquiry"""
    print("\n📋 Adding Health Insurance...")
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.post(
        f"{BASE_URL}/api/insurance/health-insurance/inquiry",
        headers=headers,
        json={
            "fullName": "Insurance Test User",
            "email": TEST_EMAIL,
            "phone": "9123456789",
            "dateOfBirth": "1990-01-15",
            "numberOfMembers": 4,
            "coverageAmount": "10 Lakhs",
            "medicalHistory": "No major medical conditions",
            "additionalDetails": "Looking for comprehensive family coverage"
        }
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code in [200, 201]:
        print("✅ Health Insurance added successfully")
    else:
        print(f"❌ Failed: {response.json()}")

def add_motor_insurance(token):
    """Add motor insurance inquiry"""
    print("\n🚗 Adding Motor Insurance...")
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.post(
        f"{BASE_URL}/api/insurance/motor-insurance/inquiry",
        headers=headers,
        json={
            "fullName": "Insurance Test User",
            "email": TEST_EMAIL,
            "phone": "9123456789",
            "vehicleType": "Car",
            "vehicleNumber": "DL01AB1234",
            "vehicleModel": "Honda City",
            "yearOfManufacture": 2020,
            "additionalDetails": "Need comprehensive coverage"
        }
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code in [200, 201]:
        print("✅ Motor Insurance added successfully")
    else:
        print(f"❌ Failed: {response.json()}")

def add_term_insurance(token):
    """Add term insurance inquiry"""
    print("\n💼 Adding Term Insurance...")
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.post(
        f"{BASE_URL}/api/insurance/term-insurance/inquiry",
        headers=headers,
        json={
            "fullName": "Insurance Test User",
            "email": TEST_EMAIL,
            "phone": "9123456789",
            "dateOfBirth": "1990-01-15",
            "annualIncome": "12,00,000",
            "coverageAmount": "50 Lakhs",
            "policyTerm": "20 years",
            "smokingStatus": "No",
            "additionalDetails": "Looking for long-term security"
        }
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code in [200, 201]:
        print("✅ Term Insurance added successfully")
    else:
        print(f"❌ Failed: {response.json()}")

def main():
    print("="*60)
    print("Adding Sample Insurance Data to Test User")
    print("="*60)
    
    token = login()
    if not token:
        print("❌ Cannot proceed without login")
        return
    
    print(f"✅ Logged in successfully")
    
    # Add all types of insurance
    add_health_insurance(token)
    add_motor_insurance(token)
    add_term_insurance(token)
    
    print("\n" + "="*60)
    print("✅ All sample insurance data added!")
    print("You can now run: python test_insurance_management_apis.py")
    print("="*60)

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to backend server!")
        print(f"   Please ensure the backend is running at {BASE_URL}")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
