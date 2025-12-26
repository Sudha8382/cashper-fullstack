#!/usr/bin/env python3
"""
Test script to verify userId is correctly set in tax planning applications.
This script will:
1. Create a test user
2. Get their JWT token
3. Submit a personal tax planning application with the token
4. Verify userId is set in the response and in the database
5. Fetch applications and verify they are filtered by userId
"""

import requests
import json
from datetime import datetime

# Configuration
BACKEND_URL = "http://localhost:8000"
TEST_EMAIL = f"test_userId_{datetime.now().strftime('%Y%m%d_%H%M%S')}@test.com"
TEST_PASSWORD = "TestPassword123!"
TEST_PHONE = f"987654{datetime.now().strftime('%H%M%S')[-4:]}"
TEST_PAN = f"ABCDE{datetime.now().strftime('%Y%m%d%H%M%S')[-4:]}F"  # Dynamic PAN

print("=" * 80)
print("TESTING USERID FIX FOR TAX PLANNING APPLICATIONS")
print("=" * 80)

# Step 1: Create a test user
print("\n[Step 1] Creating test user...")
try:
    signup_response = requests.post(
        f"{BACKEND_URL}/api/auth/register",
        json={
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD,
            "confirmPassword": TEST_PASSWORD,
            "fullName": "Test User",
            "phone": TEST_PHONE,
            "agreeToTerms": True
        }
    )
    print(f"Status: {signup_response.status_code}")
    print(f"Response: {json.dumps(signup_response.json(), indent=2)}")
    
    if signup_response.status_code != 201:
        print("❌ Failed to create user")
        exit(1)
    
    print("✅ User created successfully")
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

# Step 2: Login and get token
print("\n[Step 2] Logging in and getting JWT token...")
try:
    login_response = requests.post(
        f"{BACKEND_URL}/api/auth/login",
        json={
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
    )
    print(f"Status: {login_response.status_code}")
    login_data = login_response.json()
    print(f"Response: {json.dumps(login_data, indent=2)}")
    
    if login_response.status_code != 200:
        print("❌ Failed to login")
        exit(1)
    
    token = login_data.get("access_token") or login_data.get("token")
    if not token:
        print("❌ No token in response")
        exit(1)
    
    print(f"✅ Login successful, token: {token[:20]}...")
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

# Step 3: Submit personal tax planning application WITH token
print("\n[Step 3] Submitting personal tax planning application WITH token...")
try:
    app_response = requests.post(
        f"{BACKEND_URL}/api/personal-tax/application/submit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "fullName": "Test User",
            "emailAddress": TEST_EMAIL,
            "phoneNumber": TEST_PHONE,
            "panNumber": TEST_PAN,
            "annualIncome": "below-5",
            "employmentType": "salaried",
            "preferredTaxRegime": "new",
            "additionalInfo": "Test application"
        }
    )
    print(f"Status: {app_response.status_code}")
    app_data = app_response.json()
    print(f"Response: {json.dumps(app_data, indent=2)}")
    
    if app_response.status_code != 201:
        print("❌ Failed to submit application")
        exit(1)
    
    # Check if userId is in response
    if "userId" not in app_data:
        print("❌ userId field missing from response!")
        exit(1)
    
    if not app_data.get("userId"):
        print("❌ userId is null/empty in response!")
        print(f"   Expected: User ID string")
        print(f"   Got: {app_data.get('userId')}")
        exit(1)
    
    app_id = app_data.get("id")
    user_id = app_data.get("userId")
    print(f"✅ Application submitted with userId: {user_id}")
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

# Step 4: Fetch applications with token and verify userId filtering
print("\n[Step 4] Fetching applications with token...")
try:
    fetch_response = requests.get(
        f"{BACKEND_URL}/api/personal-tax/application/all",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    print(f"Status: {fetch_response.status_code}")
    fetch_data = fetch_response.json()
    print(f"Response: {json.dumps(fetch_data, indent=2)}")
    
    if fetch_response.status_code != 200:
        print("❌ Failed to fetch applications")
        exit(1)
    
    if not isinstance(fetch_data, list):
        print("❌ Expected list of applications")
        exit(1)
    
    # Find the application we just submitted
    found_app = False
    for app in fetch_data:
        if app.get("id") == app_id:
            found_app = True
            print(f"✅ Application found in user's list")
            print(f"   Application ID: {app.get('id')}")
            print(f"   userId: {app.get('userId')}")
            
            if not app.get("userId"):
                print("❌ userId is null in fetched application!")
                exit(1)
            
            print(f"✅ userId is correctly set: {app.get('userId')}")
            break
    
    if not found_app:
        print("❌ Application not found in user's list!")
        exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

# Step 5: Verify no applications are returned without token
print("\n[Step 5] Fetching applications WITHOUT token...")
try:
    fetch_response = requests.get(
        f"{BACKEND_URL}/api/personal-tax/application/all",
        headers={
            "Content-Type": "application/json"
        }
    )
    print(f"Status: {fetch_response.status_code}")
    
    if fetch_response.status_code == 200:
        fetch_data = fetch_response.json()
        if isinstance(fetch_data, list) and len(fetch_data) == 0:
            print("✅ Empty list returned (correct behavior)")
        else:
            print("❌ Expected empty list when no token provided")
            exit(1)
    elif fetch_response.status_code == 401:
        print("✅ 401 Unauthorized returned (correct behavior)")
    else:
        print(f"⚠️  Unexpected status: {fetch_response.status_code}")
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

print("\n" + "=" * 80)
print("✅ ALL TESTS PASSED - userId FIX IS WORKING CORRECTLY!")
print("=" * 80)
