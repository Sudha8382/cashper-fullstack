"""
Test script to verify insurance user isolation is working correctly.
Users should only see their own insurance applications, not others'.
"""

import os
import sys
import requests
import json
from datetime import datetime

# Add the backend directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

# Base URL for API
BASE_URL = "http://localhost:8000/api"

# Test users
TEST_USER_1 = {
    "email": "test_insurance_user1@gmail.com",
    "password": "Test@12345",
    "fullName": "Insurance Test User 1"
}

TEST_USER_2 = {
    "email": "test_insurance_user2@gmail.com",
    "password": "Test@12345",
    "fullName": "Insurance Test User 2"
}

ADMIN_USER = {
    "email": "admin@payloan.com",
    "password": "Admin@123",
}

def signup_user(user_data):
    """Sign up a new user"""
    try:
        response = requests.post(
            f"{BASE_URL}/auth/signup",
            json=user_data
        )
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✓ User registered: {user_data['email']}")
            return result.get("user", {}).get("_id") or result.get("userId") or "created"
        else:
            print(f"✗ Failed to signup user {user_data['email']}: {response.status_code}")
            print(f"  Response: {response.text}")
            return None
    except Exception as e:
        print(f"✗ Error signing up user: {e}")
        return None

def login_user(email, password):
    """Login a user and get token"""
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"email": email, "password": password}
        )
        if response.status_code in [200, 201]:
            result = response.json()
            token = result.get("access_token")
            user_id = result.get("user", {}).get("_id") or result.get("userId")
            if token:
                print(f"✓ User logged in: {email}")
                return token, user_id
            else:
                print(f"✗ No token in response for {email}")
                return None, None
        else:
            print(f"✗ Failed to login {email}: {response.status_code}")
            print(f"  Response: {response.text}")
            return None, None
    except Exception as e:
        print(f"✗ Error logging in: {e}")
        return None, None

def submit_health_insurance(token, user_name, user_email):
    """Submit a health insurance application"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "name": user_name,
            "email": user_email,
            "phone": "9876543210",
            "age": "35",
            "coverage": "₹5L",
            "planType": "individual",
            "existingConditions": "None",
            "address": "Test Address",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560001"
        }
        
        response = requests.post(
            f"{BASE_URL}/health-insurance/application/submit",
            headers=headers,
            data=data
        )
        
        if response.status_code in [200, 201]:
            result = response.json()
            app_id = result.get("id")
            app_number = result.get("applicationNumber")
            user_id = result.get("userId")
            print(f"✓ Health Insurance submitted by {user_name}")
            print(f"  App ID: {app_id}, App Number: {app_number}, User ID: {user_id}")
            return app_id, user_id
        else:
            print(f"✗ Failed to submit health insurance: {response.status_code}")
            print(f"  Response: {response.text}")
            return None, None
    except Exception as e:
        print(f"✗ Error submitting health insurance: {e}")
        return None, None

def submit_motor_insurance(token, user_name, user_email):
    """Submit a motor insurance application"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "name": user_name,
            "email": user_email,
            "phone": "9876543210",
            "age": "35",
            "vehicleType": "car",
            "registrationNumber": f"KA01{user_name[-1:]}000",
            "makeModel": "Toyota Fortuner",
            "manufacturingYear": "2020",
            "vehicleValue": "2500000",
            "policyType": "comprehensive",
            "address": "Test Address",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560001"
        }
        
        response = requests.post(
            f"{BASE_URL}/motor-insurance/application/submit",
            headers=headers,
            data=data
        )
        
        if response.status_code in [200, 201]:
            result = response.json()
            app_id = result.get("id")
            app_number = result.get("applicationNumber")
            user_id = result.get("userId")
            print(f"✓ Motor Insurance submitted by {user_name}")
            print(f"  App ID: {app_id}, App Number: {app_number}, User ID: {user_id}")
            return app_id, user_id
        else:
            print(f"✗ Failed to submit motor insurance: {response.status_code}")
            print(f"  Response: {response.text}")
            return None, None
    except Exception as e:
        print(f"✗ Error submitting motor insurance: {e}")
        return None, None

def submit_term_insurance(token, user_name, user_email):
    """Submit a term insurance application"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "name": user_name,
            "email": user_email,
            "phone": "9876543210",
            "age": "35",
            "gender": "male",
            "occupation": "IT Professional",
            "annualIncome": "₹10L",
            "coverage": "₹50L",
            "term": "20",
            "smokingStatus": "no",
            "address": "Test Address",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560001",
            "nomineeRelation": "Spouse"
        }
        
        response = requests.post(
            f"{BASE_URL}/term-insurance/application/submit",
            headers=headers,
            data=data
        )
        
        if response.status_code in [200, 201]:
            result = response.json()
            app_id = result.get("id")
            app_number = result.get("applicationNumber")
            user_id = result.get("userId")
            print(f"✓ Term Insurance submitted by {user_name}")
            print(f"  App ID: {app_id}, App Number: {app_number}, User ID: {user_id}")
            return app_id, user_id
        else:
            print(f"✗ Failed to submit term insurance: {response.status_code}")
            print(f"  Response: {response.text}")
            return None, None
    except Exception as e:
        print(f"✗ Error submitting term insurance: {e}")
        return None, None

def get_health_insurance_applications(token, user_name):
    """Get health insurance applications for a user"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{BASE_URL}/health-insurance/application/all",
            headers=headers
        )
        
        if response.status_code == 200:
            apps = response.json()
            print(f"✓ Health Insurance applications retrieved for {user_name}: {len(apps)} applications")
            return apps
        else:
            print(f"✗ Failed to get health insurance applications: {response.status_code}")
            return []
    except Exception as e:
        print(f"✗ Error getting health insurance applications: {e}")
        return []

def get_motor_insurance_applications(token, user_name):
    """Get motor insurance applications for a user"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{BASE_URL}/motor-insurance/application/all",
            headers=headers
        )
        
        if response.status_code == 200:
            apps = response.json()
            print(f"✓ Motor Insurance applications retrieved for {user_name}: {len(apps)} applications")
            return apps
        else:
            print(f"✗ Failed to get motor insurance applications: {response.status_code}")
            return []
    except Exception as e:
        print(f"✗ Error getting motor insurance applications: {e}")
        return []

def get_term_insurance_applications(token, user_name):
    """Get term insurance applications for a user"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{BASE_URL}/term-insurance/application/all",
            headers=headers
        )
        
        if response.status_code == 200:
            apps = response.json()
            print(f"✓ Term Insurance applications retrieved for {user_name}: {len(apps)} applications")
            return apps
        else:
            print(f"✗ Failed to get term insurance applications: {response.status_code}")
            return []
    except Exception as e:
        print(f"✗ Error getting term insurance applications: {e}")
        return []

def main():
    print("=" * 80)
    print("INSURANCE USER ISOLATION TEST")
    print("Testing that users only see their own insurance applications")
    print("=" * 80)
    
    # Signup users
    print("\n1. SIGNING UP TEST USERS")
    print("-" * 80)
    user1_id = signup_user(TEST_USER_1)
    user2_id = signup_user(TEST_USER_2)
    
    # Login users
    print("\n2. LOGGING IN TEST USERS")
    print("-" * 80)
    token1, user1_auth_id = login_user(TEST_USER_1["email"], TEST_USER_1["password"])
    token2, user2_auth_id = login_user(TEST_USER_2["email"], TEST_USER_2["password"])
    
    if not token1 or not token2:
        print("\n✗ Failed to login users. Cannot proceed with tests.")
        return False
    
    # Submit insurance applications
    print("\n3. SUBMITTING INSURANCE APPLICATIONS")
    print("-" * 80)
    
    print("\nUser 1 submitting Health Insurance:")
    h1_id, h1_user = submit_health_insurance(token1, TEST_USER_1["fullName"], TEST_USER_1["email"])
    
    print("\nUser 1 submitting Motor Insurance:")
    m1_id, m1_user = submit_motor_insurance(token1, TEST_USER_1["fullName"], TEST_USER_1["email"])
    
    print("\nUser 1 submitting Term Insurance:")
    t1_id, t1_user = submit_term_insurance(token1, TEST_USER_1["fullName"], TEST_USER_1["email"])
    
    print("\nUser 2 submitting Health Insurance:")
    h2_id, h2_user = submit_health_insurance(token2, TEST_USER_2["fullName"], TEST_USER_2["email"])
    
    print("\nUser 2 submitting Motor Insurance:")
    m2_id, m2_user = submit_motor_insurance(token2, TEST_USER_2["fullName"], TEST_USER_2["email"])
    
    print("\nUser 2 submitting Term Insurance:")
    t2_id, t2_user = submit_term_insurance(token2, TEST_USER_2["fullName"], TEST_USER_2["email"])
    
    # Test isolation
    print("\n4. TESTING USER ISOLATION")
    print("-" * 80)
    
    print("\nUser 1 retrieving applications:")
    h1_apps = get_health_insurance_applications(token1, TEST_USER_1["fullName"])
    m1_apps = get_motor_insurance_applications(token1, TEST_USER_1["fullName"])
    t1_apps = get_term_insurance_applications(token1, TEST_USER_1["fullName"])
    
    print("\nUser 2 retrieving applications:")
    h2_apps = get_health_insurance_applications(token2, TEST_USER_2["fullName"])
    m2_apps = get_motor_insurance_applications(token2, TEST_USER_2["fullName"])
    t2_apps = get_term_insurance_applications(token2, TEST_USER_2["fullName"])
    
    # Verify isolation
    print("\n5. VERIFICATION RESULTS")
    print("-" * 80)
    
    all_pass = True
    
    # Health Insurance
    print("\nHEALTH INSURANCE ISOLATION:")
    if len(h1_apps) == 1 and h1_apps[0].get("userId") == h1_user:
        print("✓ User 1 sees only their health insurance application")
    else:
        print(f"✗ User 1 health insurance isolation failed: {len(h1_apps)} apps")
        all_pass = False
    
    if len(h2_apps) == 1 and h2_apps[0].get("userId") == h2_user:
        print("✓ User 2 sees only their health insurance application")
    else:
        print(f"✗ User 2 health insurance isolation failed: {len(h2_apps)} apps")
        all_pass = False
    
    # Motor Insurance
    print("\nMOTOR INSURANCE ISOLATION:")
    if len(m1_apps) == 1 and m1_apps[0].get("userId") == m1_user:
        print("✓ User 1 sees only their motor insurance application")
    else:
        print(f"✗ User 1 motor insurance isolation failed: {len(m1_apps)} apps")
        all_pass = False
    
    if len(m2_apps) == 1 and m2_apps[0].get("userId") == m2_user:
        print("✓ User 2 sees only their motor insurance application")
    else:
        print(f"✗ User 2 motor insurance isolation failed: {len(m2_apps)} apps")
        all_pass = False
    
    # Term Insurance
    print("\nTERM INSURANCE ISOLATION:")
    if len(t1_apps) == 1 and t1_apps[0].get("userId") == t1_user:
        print("✓ User 1 sees only their term insurance application")
    else:
        print(f"✗ User 1 term insurance isolation failed: {len(t1_apps)} apps")
        all_pass = False
    
    if len(t2_apps) == 1 and t2_apps[0].get("userId") == t2_user:
        print("✓ User 2 sees only their term insurance application")
    else:
        print(f"✗ User 2 term insurance isolation failed: {len(t2_apps)} apps")
        all_pass = False
    
    # Final result
    print("\n" + "=" * 80)
    if all_pass:
        print("✓ ALL TESTS PASSED - Insurance user isolation is working correctly!")
        print("  - Users can only see their own applications")
        print("  - Each application has correct userId")
    else:
        print("✗ SOME TESTS FAILED - Please review the output above")
    print("=" * 80)
    
    return all_pass

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n✗ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
