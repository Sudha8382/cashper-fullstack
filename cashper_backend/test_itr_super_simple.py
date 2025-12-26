"""Very simple ITR test without files"""
import requests

url = "http://localhost:8000/api/retail-services/itr-filing"

data = {
    "full_name": "T",
    "email": "a@b.c",
    "phone": "9999999999",
    "pan_number": "TEST",
    "aadhaar_number": "111111111111",
    "date_of_birth": "2000-01-01",
    "employment_type": "Salaried",
    "annual_income": "100000",
    "itr_type": "ITR-1",
    "address": "Addr",
    "city": "City",
    "state": "State",
    "pincode": "111111"
}

print("Sending minimal data...")
try:
    response = requests.post(url, data=data, timeout=30)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:500]}")
except requests.exceptions.Timeout:
    print("Request timed out - backend might be processing or crashed")
except Exception as e:
    print(f"Error: {e}")
