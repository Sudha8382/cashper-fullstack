import requests
import json

url = "http://127.0.0.1:8000/api/business-services/legal-advice"

# Test data
data = {
    "name": "Test User",
    "email": "test@example.com",
    "phone": "1234567890",
    "company_name": "Test Company",
    "legal_issue_type": "Contract Dispute",
    "case_description": "This is a test case description that needs legal advice.",
    "urgency": "High",
    "address": "123 Test Street, Test Area",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001",
    "company_pan": "AAAAA1234A"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
    print(f"Response text: {response.text if 'response' in locals() else 'No response'}")
