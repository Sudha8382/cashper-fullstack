"""Simple test for ITR Revision endpoint"""
import requests
import json

# Try to hit the endpoint
url = "http://localhost:8000/api/retail-services/itr-revision"

print("Testing ITR Revision endpoint...")
print(f"URL: {url}\n")

# Test data
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

try:
    # Try without token first
    print("1. Testing without authentication (should fail)...")
    response = requests.post(url, data=test_data, timeout=5)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:200]}\n")
except Exception as e:
    print(f"   Error: {e}\n")

try:
    # Try with token
    print("2. Testing with authentication...")
    token = "test-token"  # We'll update this after login
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, data=test_data, headers=headers, timeout=5)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:200]}\n")
except Exception as e:
    print(f"   Error: {e}\n")

print("Test complete!")
