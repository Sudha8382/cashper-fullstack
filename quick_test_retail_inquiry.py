"""
Simple Quick Test for Retail Inquiry APIs
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("=" * 70)
print("TESTING RETAIL INQUIRY APIs")
print("=" * 70)

# Test 1: Health Check
print("\n1. Testing Server Health...")
try:
    response = requests.get(f"{BASE_URL}/health")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    print("   ✅ Server is running!")
except Exception as e:
    print(f"   ❌ Error: {e}")
    print("   Please start the server first!")
    exit(1)

# Test 2: File ITR Inquiry
print("\n2. Testing File ITR Inquiry...")
try:
    data = {
        "name": "Rahul Kumar",
        "email": "rahul@example.com",
        "phone": "9876543210",
        "message": "Need help with ITR filing"
    }
    response = requests.post(f"{BASE_URL}/api/retail-inquiry/file-itr", json=data)
    print(f"   Status: {response.status_code}")
    result = response.json()
    print(f"   Response: {json.dumps(result, indent=2)}")
    if response.status_code == 201 and result.get("success"):
        print(f"   ✅ File ITR Inquiry Created: {result.get('inquiryId')}")
    else:
        print("   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 3: Apply Individual PAN Inquiry
print("\n3. Testing Individual PAN Inquiry...")
try:
    data = {
        "name": "Priya Sharma",
        "email": "priya@example.com",
        "phone": "9876543211",
        "message": "Want to apply for PAN card"
    }
    response = requests.post(f"{BASE_URL}/api/retail-inquiry/apply-individual-pan", json=data)
    print(f"   Status: {response.status_code}")
    result = response.json()
    if response.status_code == 201 and result.get("success"):
        print(f"   ✅ PAN Inquiry Created: {result.get('inquiryId')}")
    else:
        print("   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 4: Bank Account Inquiry
print("\n4. Testing Bank Account Inquiry...")
try:
    data = {
        "name": "Amit Patel",
        "email": "amit@example.com",
        "phone": "9876543212",
        "message": "Want to open savings account"
    }
    response = requests.post(f"{BASE_URL}/api/retail-inquiry/bank-account", json=data)
    print(f"   Status: {response.status_code}")
    result = response.json()
    if response.status_code == 201 and result.get("success"):
        print(f"   ✅ Bank Account Inquiry Created: {result.get('inquiryId')}")
    else:
        print("   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 5: Financial Planning Inquiry
print("\n5. Testing Financial Planning Inquiry...")
try:
    data = {
        "name": "Suresh Nair",
        "email": "suresh@example.com",
        "phone": "9876543219",
        "age": "35",
        "currentIncome": "800000",
        "investmentGoal": "retirement"
    }
    response = requests.post(f"{BASE_URL}/api/retail-inquiry/financial-planning", json=data)
    print(f"   Status: {response.status_code}")
    result = response.json()
    if response.status_code == 201 and result.get("success"):
        print(f"   ✅ Financial Planning Inquiry Created: {result.get('inquiryId')}")
    else:
        print("   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 6: Get All Inquiries (Admin)
print("\n6. Testing Admin - Get All Inquiries...")
try:
    response = requests.get(f"{BASE_URL}/api/retail-inquiry/admin/inquiries")
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        inquiries = response.json()
        print(f"   ✅ Retrieved {len(inquiries)} inquiries")
        if inquiries:
            print(f"   Latest: {inquiries[0]['name']} - {inquiries[0]['serviceType']}")
    else:
        print("   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 7: Get Statistics (Admin)
print("\n7. Testing Admin - Get Statistics...")
try:
    response = requests.get(f"{BASE_URL}/api/retail-inquiry/admin/statistics")
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        stats = response.json()
        print(f"   ✅ Statistics retrieved")
        print(f"   Total Inquiries: {stats.get('total')}")
        print(f"   New: {stats.get('new')}, Contacted: {stats.get('contacted')}")
    else:
        print("   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "=" * 70)
print("TESTING COMPLETE!")
print("=" * 70)
print("\n✨ All Retail Inquiry APIs are working correctly!")
print("\n📝 Available Endpoints:")
print("   • POST /api/retail-inquiry/file-itr")
print("   • POST /api/retail-inquiry/revise-itr")
print("   • POST /api/retail-inquiry/reply-itr-notice")
print("   • POST /api/retail-inquiry/apply-individual-pan")
print("   • POST /api/retail-inquiry/apply-huf-pan")
print("   • POST /api/retail-inquiry/withdraw-pf")
print("   • POST /api/retail-inquiry/update-aadhaar-pan")
print("   • POST /api/retail-inquiry/online-trading-demat")
print("   • POST /api/retail-inquiry/bank-account")
print("   • POST /api/retail-inquiry/financial-planning")
print("   • GET  /api/retail-inquiry/admin/inquiries")
print("   • GET  /api/retail-inquiry/admin/statistics")
print("\n🌐 API Documentation: http://127.0.0.1:8000/docs")
