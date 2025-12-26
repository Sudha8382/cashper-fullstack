"""Simple ITR test with error handling"""
import requests

url = "http://localhost:8000/api/retail-services/itr-filing"

data = {
    "fullName": "Test User",
    "email": "test@example.com",
    "phone": "9876543210",
    "panNumber": "ABCDE1234F",
    "aadhaarNumber": "123456789012",
    "dateOfBirth": "1990-01-01",
    "employmentType": "Salaried",
    "annualIncome": "500000",
    "itrType": "ITR-1",
    "hasBusinessIncome": "false",  # sending as string
    "hasCapitalGains": "false",
    "hasHouseProperty": "false",
    "address": "Test Address",
    "city": "Delhi",
    "state": "Delhi",
    "pincode": "110001"
}

try:
    response = requests.post(url, data=data, timeout=5)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
