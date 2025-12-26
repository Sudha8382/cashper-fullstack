"""
Quick Test Script for PAN Services APIs
Tests: Individual PAN, HUF PAN Applications
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/retail-services"

print("=" * 80)
print("Testing PAN Services APIs".center(80))
print("=" * 80)

# Test 1: Individual PAN Application
print("\n1. Testing Individual PAN Application...")
individual_pan_data = {
    "fullName": "Test Individual PAN User",
    "fatherName": "Test Father Name",
    "dateOfBirth": "1995-06-15",
    "email": "test.individual.pan@example.com",
    "phone": "8888888888",
    "aadhaarNumber": "234567890123",
    "gender": "male",
    "category": "individual",
    "applicationType": "new",
    "address": "Test PAN Address, Near Main Road",
    "city": "Chennai",
    "state": "Tamil Nadu",
    "pincode": "600001"
}

try:
    response = requests.post(f"{BASE_URL}/individual-pan", json=individual_pan_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Individual PAN Application Submitted Successfully!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  Applicant: {individual_pan_data['fullName']}")
        print(f"  Status: {result['status']}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 2: HUF PAN Application
print("\n2. Testing HUF PAN Application...")
huf_pan_data = {
    "hufName": "Test HUF Family Name",
    "kartaName": "Test Karta Name",
    "kartaPAN": "KLMNO3456P",
    "email": "test.huf.pan@example.com",
    "phone": "8888888887",
    "dateOfFormation": "2020-01-01",
    "hufMembers": 4,
    "address": "Test HUF Address, Family House",
    "city": "Pune",
    "state": "Maharashtra",
    "pincode": "411001"
}

try:
    response = requests.post(f"{BASE_URL}/huf-pan", json=huf_pan_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ HUF PAN Application Submitted Successfully!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  HUF Name: {huf_pan_data['hufName']}")
        print(f"  Karta: {huf_pan_data['kartaName']}")
        print(f"  Status: {result['status']}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test: Get PAN Applications
print("\n3. Testing Get PAN Applications...")
try:
    # Individual PAN
    response = requests.get(f"{BASE_URL}/applications?service_type=individual-pan")
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Individual PAN Applications: {result['total']}")
    
    # HUF PAN
    response = requests.get(f"{BASE_URL}/applications?service_type=huf-pan")
    if response.status_code == 200:
        result = response.json()
        print(f"✓ HUF PAN Applications: {result['total']}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

print("\n" + "=" * 80)
print("PAN Services API Testing Complete!".center(80))
print("=" * 80)
