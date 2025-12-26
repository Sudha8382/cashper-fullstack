import requests
import json

# Test endpoint
url = "http://127.0.0.1:8000/api/personal-loan/apply"

# Sample data
test_data = {
    "fullName": "Test User",
    "email": "test@example.com",
    "phone": "9876543210",
    "loanAmount": "100000",
    "purpose": "education",
    "employment": "salaried",
    "monthlyIncome": "50000",
    "companyName": "Test Company",
    "workExperience": "2",
    "creditScore": "700",
    "panNumber": "ABCDE1234F",
    "aadharNumber": "123456789012",
    "address": "Test Address",
    "city": "Test City",
    "state": "Test State",
    "pincode": "123456"
}

print("Testing POST /api/personal-loan/apply...")
print(f"Payload: {json.dumps(test_data, indent=2)}")
print("-" * 50)

try:
    response = requests.post(url, json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {str(e)}")
    if response.text:
        print(f"Response Text: {response.text}")
