"""
Quick Test Script for ITR Services APIs
Tests: ITR Filing, ITR Revision, ITR Notice Reply
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/retail-services"

print("=" * 80)
print("Testing ITR Services APIs".center(80))
print("=" * 80)

# Test 1: ITR Filing
print("\n1. Testing ITR Filing Service...")
itr_filing_data = {
    "fullName": "Test User ITR Filing",
    "email": "test.itr@example.com",
    "phone": "9999999999",
    "panNumber": "ABCDE1234F",
    "aadhaarNumber": "123456789012",
    "dateOfBirth": "1990-01-01",
    "employmentType": "salaried",
    "annualIncome": "500000",
    "itrType": "ITR-1",
    "hasBusinessIncome": False,
    "hasCapitalGains": False,
    "hasHouseProperty": False,
    "address": "Test Address Line 1, Near Landmark",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001"
}

try:
    response = requests.post(f"{BASE_URL}/itr-filing", json=itr_filing_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ ITR Filing Application Submitted Successfully!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  Status: {result['status']}")
        
        # Test GET
        app_id = result['applicationId']
        get_response = requests.get(f"{BASE_URL}/itr-filing/{app_id}")
        if get_response.status_code == 200:
            print(f"✓ Retrieved ITR Filing Application: {get_response.json()['applicantName']}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 2: ITR Revision
print("\n2. Testing ITR Revision Service...")
itr_revision_data = {
    "fullName": "Test User ITR Revision",
    "email": "test.revision@example.com",
    "phone": "9999999998",
    "panNumber": "PQRST5678Z",
    "aadhaarNumber": "987654321098",
    "acknowledgementNumber": "123456789012345",
    "originalFilingDate": "2023-07-31",
    "reasonForRevision": "Need to include additional income from freelancing work that was not reported in original ITR filing",
    "address": "Test Address for Revision, Landmark Area",
    "city": "Delhi",
    "state": "Delhi",
    "pincode": "110001"
}

try:
    response = requests.post(f"{BASE_URL}/itr-revision", json=itr_revision_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ ITR Revision Application Submitted Successfully!")
        print(f"  Application ID: {result['applicationId']}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 3: ITR Notice Reply
print("\n3. Testing ITR Notice Reply Service...")
itr_notice_data = {
    "fullName": "Test User Notice Reply",
    "email": "test.notice@example.com",
    "phone": "9999999997",
    "panNumber": "UVWXY9012A",
    "noticeNumber": "CPC/NOTICE/2024/TEST123",
    "noticeDate": "2024-11-01",
    "noticeSubject": "Form 26AS Mismatch",
    "noticeDescription": "Received notice from Income Tax Department regarding mismatch between TDS shown in Form 26AS and the amount claimed in ITR. Need to submit clarification with supporting documents.",
    "address": "Test Notice Address, IT Department Road",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560001"
}

try:
    response = requests.post(f"{BASE_URL}/itr-notice-reply", json=itr_notice_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ ITR Notice Reply Application Submitted Successfully!")
        print(f"  Application ID: {result['applicationId']}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test: Get All Applications
print("\n4. Testing Get All ITR Applications...")
try:
    response = requests.get(f"{BASE_URL}/applications")
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Retrieved {result['total']} total applications")
        
        # Filter ITR applications
        itr_apps = [app for app in result['applications'] if 'itr' in app['serviceType'].lower()]
        print(f"  ITR Related Applications: {len(itr_apps)}")
    else:
        print(f"✗ Failed: {response.status_code}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

print("\n" + "=" * 80)
print("ITR Services API Testing Complete!".center(80))
print("=" * 80)
