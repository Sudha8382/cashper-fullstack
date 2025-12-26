#!/usr/bin/env python3
"""
End-to-end test: Verify that userId is correctly set and filtering works
This test simulates:
1. User A creates an account and submits a tax application
2. User B creates an account and submits a tax application
3. Verify User A only sees their own application
4. Verify User B only sees their own application
"""

import requests
import json
from datetime import datetime

BACKEND_URL = "http://localhost:8000"

def create_test_user(email, fullName, phone, password):
    """Create a test user and return token"""
    response = requests.post(
        f"{BACKEND_URL}/api/auth/register",
        json={
            "email": email,
            "password": password,
            "confirmPassword": password,
            "fullName": fullName,
            "phone": phone,
            "agreeToTerms": True
        }
    )
    if response.status_code != 201:
        raise Exception(f"User creation failed: {response.json()}")
    
    token = response.json().get("access_token")
    user_id = response.json()["user"]["id"]
    return token, user_id

def submit_tax_application(token, fullName, email, phone, pan):
    """Submit a tax planning application with the given token"""
    response = requests.post(
        f"{BACKEND_URL}/api/personal-tax/application/submit",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "fullName": fullName,
            "emailAddress": email,
            "phoneNumber": phone,
            "panNumber": pan,
            "annualIncome": "below-5",
            "employmentType": "salaried",
            "preferredTaxRegime": "new",
            "additionalInfo": f"Test app for {fullName}"
        }
    )
    if response.status_code != 201:
        raise Exception(f"Application submission failed: {response.json()}")
    
    return response.json()

def get_user_applications(token):
    """Get all applications for the user (filtered by userId)"""
    response = requests.get(
        f"{BACKEND_URL}/api/personal-tax/application/all",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    if response.status_code != 200:
        raise Exception(f"Get applications failed: {response.json()}")
    
    return response.json()

print("=" * 80)
print("END-TO-END TEST: Multi-User Isolation")
print("=" * 80)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Create User A
print(f"\n[User A] Creating account...")
email_a = f"user_a_{timestamp}@test.com"
phone_a = f"990000{timestamp[-4:]}"
pan_a = "AAAAA1111F"  # Format: ABCDE1234F (5 letters + 4 digits + 1 letter)

token_a, user_id_a = create_test_user(
    email=email_a,
    fullName="User A",
    phone=phone_a,
    password="TestPass123!"
)
print(f"✅ User A created: {user_id_a}")

# Create User B
print(f"\n[User B] Creating account...")
email_b = f"user_b_{timestamp}@test.com"
phone_b = f"991111{timestamp[-4:]}"
pan_b = "BBBBB2222F"  # Format: ABCDE1234F (5 letters + 4 digits + 1 letter)

token_b, user_id_b = create_test_user(
    email=email_b,
    fullName="User B",
    phone=phone_b,
    password="TestPass123!"
)
print(f"✅ User B created: {user_id_b}")

# User A submits application
print(f"\n[User A] Submitting tax application...")
app_a = submit_tax_application(
    token=token_a,
    fullName="User A",
    email=email_a,
    phone=phone_a,
    pan=pan_a
)
print(f"✅ User A application submitted: {app_a['id']}")
print(f"   userId in response: {app_a['userId']}")

if app_a['userId'] != user_id_a:
    print(f"❌ FAIL: userId mismatch! Expected {user_id_a}, got {app_a['userId']}")
    exit(1)

# User B submits application
print(f"\n[User B] Submitting tax application...")
app_b = submit_tax_application(
    token=token_b,
    fullName="User B",
    email=email_b,
    phone=phone_b,
    pan=pan_b
)
print(f"✅ User B application submitted: {app_b['id']}")
print(f"   userId in response: {app_b['userId']}")

if app_b['userId'] != user_id_b:
    print(f"❌ FAIL: userId mismatch! Expected {user_id_b}, got {app_b['userId']}")
    exit(1)

# Verify User A sees only their application
print(f"\n[User A] Fetching their applications...")
apps_a = get_user_applications(token_a)
print(f"   Applications found: {len(apps_a)}")

if len(apps_a) != 1:
    print(f"❌ FAIL: User A should see 1 application, got {len(apps_a)}")
    exit(1)

if apps_a[0]['id'] != app_a['id']:
    print(f"❌ FAIL: User A's application ID mismatch")
    exit(1)

print(f"✅ User A correctly sees only their own application")
print(f"   Application ID: {apps_a[0]['id']}")
print(f"   userId: {apps_a[0]['userId']}")

# Verify User B sees only their application
print(f"\n[User B] Fetching their applications...")
apps_b = get_user_applications(token_b)
print(f"   Applications found: {len(apps_b)}")

if len(apps_b) != 1:
    print(f"❌ FAIL: User B should see 1 application, got {len(apps_b)}")
    exit(1)

if apps_b[0]['id'] != app_b['id']:
    print(f"❌ FAIL: User B's application ID mismatch")
    exit(1)

print(f"✅ User B correctly sees only their own application")
print(f"   Application ID: {apps_b[0]['id']}")
print(f"   userId: {apps_b[0]['userId']}")

# Verify cross-isolation
print(f"\n[Isolation Verification]")
if app_a['id'] == app_b['id']:
    print(f"❌ FAIL: Applications should have different IDs")
    exit(1)
print(f"✅ User A and User B have different application IDs")

if apps_a[0]['id'] in [app['id'] for app in apps_b]:
    print(f"❌ FAIL: User B can see User A's application!")
    exit(1)
print(f"✅ User B cannot see User A's application")

if apps_b[0]['id'] in [app['id'] for app in apps_a]:
    print(f"❌ FAIL: User A can see User B's application!")
    exit(1)
print(f"✅ User A cannot see User B's application")

print("\n" + "=" * 80)
print("✅ ALL TESTS PASSED - USER ISOLATION IS WORKING CORRECTLY!")
print("=" * 80)
