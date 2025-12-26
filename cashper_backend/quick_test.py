"""Quick API Test - Tests one endpoint to verify APIs are working"""
import requests
import time

BASE_URL = "http://localhost:8000"

print("\n" + "="*60)
print("🧪 QUICK API TEST")
print("="*60)

# Wait a moment for server
time.sleep(2)

# Test Company Registration
print("\n📤 Testing Company Registration API...")
data = {
    "full_name": "Test User",
    "email": "test@example.com",
    "phone": "9876543210",
    "pan_number": "ABCDE1234F",
    "proposed_company_name": "Test Company Pvt Ltd",
    "company_type": "Private Limited",
    "number_of_directors": 2,
    "registration_state": "Maharashtra",
    "address": "Test Address, Mumbai",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001"
}

try:
    response = requests.post(f"{BASE_URL}/api/business-services/company-registration", json=data, timeout=5)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ SUCCESS! Application ID: {result['application_id']}")
        print(f"Company: {result['data']['proposed_company_name']}")
        
        # Test GET endpoint
        print(f"\n📥 Testing GET endpoint...")
        response2 = requests.get(f"{BASE_URL}/api/business-services/company-registration", timeout=5)
        if response2.status_code == 200:
            print(f"✅ GET SUCCESS! Found {response2.json()['count']} applications")
    else:
        print(f"❌ FAILED: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ ERROR: Cannot connect to server. Make sure backend is running on port 8000")
except Exception as e:
    print(f"❌ ERROR: {str(e)}")

print("\n" + "="*60)
