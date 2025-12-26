import requests
import json

# Test login endpoint
url = "http://localhost:8000/api/auth/login"

# Test with sample credentials
test_data = {
    "email": "test@example.com",
    "password": "Test@1234"
}

print("Testing login endpoint...")
print(f"URL: {url}")
print(f"Request data: {json.dumps(test_data, indent=2)}")
print("-" * 50)

try:
    response = requests.post(url, json=test_data)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Response Body: {response.text}")
    
    if response.status_code == 500:
        print("\n⚠️ 500 Internal Server Error detected!")
        print("Check the backend terminal/logs for detailed error traceback")
        
except Exception as e:
    print(f"Error making request: {str(e)}")
