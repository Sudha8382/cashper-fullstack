"""
Quick Test Script for Document Services APIs
Tests: PF Withdrawal, Document Update (Aadhaar/PAN)
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/retail-services"

print("=" * 80)
print("Testing Document Services APIs".center(80))
print("=" * 80)

# Test 1: PF Withdrawal Application
print("\n1. Testing PF Withdrawal Application...")
pf_withdrawal_data = {
    "fullName": "Test PF Withdrawal User",
    "email": "test.pf@example.com",
    "phone": "6666666666",
    "panNumber": "FGHIJ6789K",
    "uanNumber": "123456789012",
    "employerName": "Test Company Ltd",
    "withdrawalType": "full",
    "withdrawalAmount": 250000.00,
    "withdrawalReason": "Resigned from job after 5 years. Planning higher education abroad. Need EPF funds for course fees and living expenses.",
    "lastWorkingDate": "2024-10-31",
    "address": "Test PF Address, IT Park",
    "city": "Pune",
    "state": "Maharashtra",
    "pincode": "411001"
}

try:
    response = requests.post(f"{BASE_URL}/pf-withdrawal", json=pf_withdrawal_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ PF Withdrawal Application Submitted!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  Applicant: {pf_withdrawal_data['fullName']}")
        print(f"  UAN: {pf_withdrawal_data['uanNumber']}")
        print(f"  Withdrawal Type: {pf_withdrawal_data['withdrawalType']}")
        print(f"  Amount: ₹{pf_withdrawal_data['withdrawalAmount']:,.2f}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 2: Document Update Application
print("\n2. Testing Document Update Application...")
document_update_data = {
    "fullName": "Test Document Update User",
    "email": "test.docupdate@example.com",
    "phone": "6666666665",
    "updateType": "aadhaar",
    "currentAadhaarNumber": "345678901234",
    "currentPANNumber": "MNOPQ7890L",
    "updateReason": "Changed address after relocation from one city to another for job transfer. Need to update residential address in Aadhaar.",
    "newDetails": "New Address: Test New Address, Tech Park Area, Near Metro Station",
    "address": "Test Current Address for Updates",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560001"
}

try:
    response = requests.post(f"{BASE_URL}/document-update", json=document_update_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Document Update Application Submitted!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  Applicant: {document_update_data['fullName']}")
        print(f"  Update Type: {document_update_data['updateType'].upper()}")
        print(f"  Reason: {document_update_data['updateReason'][:50]}...")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test: Get Applications by Status
print("\n3. Testing Get Applications by Status...")
try:
    for status in ["pending", "under-review", "in-progress"]:
        response = requests.get(f"{BASE_URL}/applications?status={status}")
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Status '{status}': {result['total']} applications")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test: Get Specific Service Type Applications
print("\n4. Testing Get Document Service Applications...")
try:
    # PF Withdrawal
    response = requests.get(f"{BASE_URL}/applications?service_type=pf-withdrawal")
    if response.status_code == 200:
        result = response.json()
        print(f"✓ PF Withdrawal Applications: {result['total']}")
    
    # Document Update
    response = requests.get(f"{BASE_URL}/applications?service_type=document-update")
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Document Update Applications: {result['total']}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

print("\n" + "=" * 80)
print("Document Services API Testing Complete!".center(80))
print("=" * 80)
