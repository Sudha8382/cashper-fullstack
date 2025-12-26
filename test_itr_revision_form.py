"""Test ITR Revision Form Submission"""
import requests
import json
from datetime import datetime

# Test data - mimicking form submission
test_data = {
    "fullName": "Raj Kumar",
    "email": "raj@example.com",
    "phone": "9876543210",
    "panNumber": "ABCDE1234F",
    "assessmentYear": "2023-24",
    "itrType": "ITR-2",
    "acknowledgmentNumber": "123456789012345",
    "originalFilingDate": "2024-01-15",
    "revisionReason": "Correction of income details and deduction claims",
    "address": "123 Main Street, Building A",
    "city": "Delhi",
    "state": "Delhi",
    "pincode": "110001"
}

# Test 1: Try without files (should fail)
print("=" * 60)
print("TEST 1: Form submission without authentication (should fail)")
print("=" * 60)

response = requests.post(
    "http://localhost:8000/api/retail-services/itr-revision",
    data=test_data
)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

print("\n" + "=" * 60)
print("TEST 2: Trying with valid token...")
print("=" * 60)

# First need to login
login_data = {
    "email": "admin@cashper.ai",
    "password": "admin@123"
}

login_response = requests.post(
    "http://localhost:8000/api/users/login",
    json=login_data
)

if login_response.status_code == 200:
    login_result = login_response.json()
    token = login_result.get("access_token")
    print(f"Login successful! Token: {token[:20]}...")
    
    # Now try with token
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Create form data with files
    files = {
        "originalITR": ("sample.txt", "Sample Original ITR", "text/plain"),
        "acknowledgmentReceipt": ("receipt.txt", "Sample Receipt", "text/plain")
    }
    
    # Combine form data and files
    form_data = test_data.copy()
    
    response = requests.post(
        "http://localhost:8000/api/retail-services/itr-revision",
        data=form_data,
        files=files,
        headers=headers
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
else:
    print(f"Login failed: {login_response.status_code}")
    print(f"Response: {login_response.text}")
