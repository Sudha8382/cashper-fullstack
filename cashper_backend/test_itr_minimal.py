"""Minimal ITR test"""
import requests

url = "http://localhost:8000/api/retail-services/itr-filing"

# Only required fields
data = {
    "fullName": "TestName",
    "email": "test@t.com",
    "phone": "9999999999",
    "panNumber": "TEST",
    "aadhaarNumber": "123456789012",
    "dateOfBirth": "1990-01-01",
    "employmentType": "Salaried",
    "annualIncome": "500000",
    "itrType": "ITR-1",
    "address": "TestAddr",
    "city": "Delhi",
    "state": "Delhi",
    "pincode": "110001"
}

print(f"Sending: {data}")

try:
    response = requests.post(url, data=data, timeout=10)
    print(f"\nStatus: {response.status_code}")
    print(f"Response: {response.text[:500]}")
except Exception as e:
    print(f"Exception: {e}")
    import traceback
    traceback.print_exc()
