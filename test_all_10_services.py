"""
Complete Test for ALL 10 Retail Inquiry APIs
Tests every single service endpoint
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(service_name, endpoint, data):
    """Test a single endpoint"""
    print(f"\n{'='*70}")
    print(f"Testing: {service_name}")
    print(f"{'='*70}")
    print(f"Endpoint: POST {endpoint}")
    print(f"Data: {json.dumps(data, indent=2)}")
    
    try:
        response = requests.post(endpoint, json=data, timeout=10)
        print(f"\nStatus Code: {response.status_code}")
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ SUCCESS!")
            print(f"Inquiry ID: {result.get('inquiryId')}")
            print(f"Message: {result.get('message')}")
            return True, result.get('inquiryId')
        else:
            print(f"❌ FAILED - Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False, None
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False, None

# Test data for all 10 services
tests = [
    {
        "name": "File Your ITR",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/file-itr",
        "data": {
            "name": "Rajesh Kumar",
            "email": "rajesh.kumar@example.com",
            "phone": "9876543210",
            "message": "Need help filing ITR for AY 2024-25"
        }
    },
    {
        "name": "Revise Your ITR",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/revise-itr",
        "data": {
            "name": "Priya Sharma",
            "email": "priya.sharma@example.com",
            "phone": "9876543211",
            "message": "Want to revise my ITR filed last month"
        }
    },
    {
        "name": "Reply to ITR Notice",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/reply-itr-notice",
        "data": {
            "name": "Amit Patel",
            "email": "amit.patel@example.com",
            "phone": "9876543212",
            "message": "Received ITR notice u/s 143(1), need assistance"
        }
    },
    {
        "name": "Apply for Individual PAN",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/apply-individual-pan",
        "data": {
            "name": "Sneha Reddy",
            "email": "sneha.reddy@example.com",
            "phone": "9876543213",
            "message": "Want to apply for new PAN card"
        }
    },
    {
        "name": "Apply for HUF PAN",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/apply-huf-pan",
        "data": {
            "name": "Ramesh Singh",
            "email": "ramesh.singh@example.com",
            "phone": "9876543214",
            "message": "Need HUF PAN for my family business"
        }
    },
    {
        "name": "Withdraw Your PF",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/withdraw-pf",
        "data": {
            "name": "Deepak Verma",
            "email": "deepak.verma@example.com",
            "phone": "9876543215",
            "message": "Planning to withdraw PF for home purchase"
        }
    },
    {
        "name": "Update Aadhaar or PAN Details",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/update-aadhaar-pan",
        "data": {
            "name": "Anjali Gupta",
            "email": "anjali.gupta@example.com",
            "phone": "9876543216",
            "message": "Need to update address in Aadhaar and PAN"
        }
    },
    {
        "name": "Online Trading & Demat",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/online-trading-demat",
        "data": {
            "name": "Vikram Mehta",
            "email": "vikram.mehta@example.com",
            "phone": "9876543217",
            "message": "Interested in opening Demat account for equity trading"
        }
    },
    {
        "name": "Bank Account Services",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/bank-account",
        "data": {
            "name": "Pooja Desai",
            "email": "pooja.desai@example.com",
            "phone": "9876543218",
            "message": "Want to open zero-balance savings account"
        }
    },
    {
        "name": "Financial Planning & Advisory",
        "endpoint": f"{BASE_URL}/api/retail-inquiry/financial-planning",
        "data": {
            "name": "Suresh Nair",
            "email": "suresh.nair@example.com",
            "phone": "9876543219",
            "age": "35",
            "currentIncome": "1200000",
            "investmentGoal": "retirement planning"
        }
    }
]

print("="*70)
print("COMPREHENSIVE TEST - ALL 10 RETAIL INQUIRY APIs")
print("="*70)

# Health check
print("\n🏥 Checking Server Health...")
try:
    response = requests.get(f"{BASE_URL}/health")
    if response.status_code == 200:
        print("✅ Server is running and healthy!")
    else:
        print("❌ Server health check failed!")
        print("Please start the backend server first!")
        exit(1)
except:
    print("❌ Cannot connect to server!")
    print("Please start the backend server first!")
    print("Command: cd cashper_backend && python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000")
    exit(1)

# Run all tests
passed = 0
failed = 0
inquiry_ids = []

for test in tests:
    success, inquiry_id = test_endpoint(test["name"], test["endpoint"], test["data"])
    if success:
        passed += 1
        if inquiry_id:
            inquiry_ids.append(inquiry_id)
    else:
        failed += 1

# Test Admin Endpoints
print(f"\n{'='*70}")
print("Testing Admin Endpoints")
print(f"{'='*70}")

# Get all inquiries
print("\n📋 Getting All Inquiries...")
try:
    response = requests.get(f"{BASE_URL}/api/retail-inquiry/admin/inquiries")
    if response.status_code == 200:
        inquiries = response.json()
        print(f"✅ Retrieved {len(inquiries)} total inquiries")
        print(f"Recent inquiries created in this test: {len(inquiry_ids)}")
    else:
        print(f"❌ Failed - Status: {response.status_code}")
except Exception as e:
    print(f"❌ Error: {e}")

# Get statistics
print("\n📊 Getting Statistics...")
try:
    response = requests.get(f"{BASE_URL}/api/retail-inquiry/admin/statistics")
    if response.status_code == 200:
        stats = response.json()
        print(f"✅ Statistics retrieved:")
        print(f"   Total Inquiries: {stats.get('total')}")
        print(f"   New: {stats.get('new')}")
        print(f"   Contacted: {stats.get('contacted')}")
        print(f"   In Progress: {stats.get('inProgress')}")
        print(f"   Converted: {stats.get('converted')}")
        print(f"   Closed: {stats.get('closed')}")
        print(f"\n   By Service Type:")
        for service, count in stats.get('byService', {}).items():
            print(f"   - {service}: {count}")
    else:
        print(f"❌ Failed - Status: {response.status_code}")
except Exception as e:
    print(f"❌ Error: {e}")

# Summary
print(f"\n{'='*70}")
print("TEST SUMMARY")
print(f"{'='*70}")
print(f"\n✅ Passed: {passed}/{len(tests)} endpoints")
print(f"❌ Failed: {failed}/{len(tests)} endpoints")
print(f"📝 Inquiries Created: {len(inquiry_ids)}")

if failed == 0:
    print("\n🎉 ALL TESTS PASSED! All 10 retail inquiry APIs are working perfectly!")
else:
    print("\n⚠️  Some tests failed. Please check the errors above.")

print("\n📚 API Documentation: http://127.0.0.1:8000/docs")
print(f"{'='*70}")
