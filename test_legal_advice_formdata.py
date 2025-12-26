import requests

url = "http://127.0.0.1:8000/api/business-services/legal-advice"

# Test data with FormData
data = {
    "name": "Test User",
    "email": "test@example.com",
    "phone": "1234567890",
    "companyName": "Test Company",
    "legalIssueType": "Contract Dispute",
    "caseDescription": "This is a test case description that needs legal advice.",
    "urgency": "High",
    "address": "123 Test Street, Test Area",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001",
    "companyPAN": "AAAAA1234A"
}

try:
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
    if 'response' in locals():
        print(f"Response text: {response.text}")
