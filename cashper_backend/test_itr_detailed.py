"""Test with proper boolean"""
import requests

url = "http://localhost:8000/api/retail-services/itr-filing"

data = {
    "fullName": "Test User",
    "email": "test@test.com",
    "phone": "9999999999",
    "panNumber": "TEST123",
    "aadhaarNumber": "123456789012",
    "dateOfBirth": "1990-01-01",
    "employmentType": "Salaried",
    "annualIncome": "500000",
    "itrType": "ITR-1",
    "hasBusinessIncome": "false",  # String for form data
    "hasCapitalGains": "false",
    "hasHouseProperty": "false",
    "address": "TestAddr",
    "city": "Delhi",
    "state": "Delhi",
    "pincode": "110001"
}

try:
    response = requests.post(url, data=data, timeout=10)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print(f"✅ SUCCESS: {response.json()}")
    else:
        print(f"❌ Error: {response.text}")
        print(f"Headers: {response.headers}")
except Exception as e:
    print(f"Exception: {e}")
