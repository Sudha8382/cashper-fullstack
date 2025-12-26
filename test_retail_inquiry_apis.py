"""
Test Script for Retail Inquiry APIs
Tests all hero section form submission endpoints
"""

import requests
import json
from datetime import datetime

# Base URL
BASE_URL = "http://127.0.0.1:8000/api/retail-inquiry"

# Test data
TEST_INQUIRIES = {
    "file-itr": {
        "name": "Rahul Kumar",
        "email": "rahul.kumar@example.com",
        "phone": "9876543210",
        "message": "I need help filing my ITR for AY 2024-25"
    },
    "revise-itr": {
        "name": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "phone": "9876543211",
        "message": "I need to revise my ITR filed last month"
    },
    "reply-itr-notice": {
        "name": "Amit Patel",
        "email": "amit.patel@example.com",
        "phone": "9876543212",
        "message": "I received an ITR notice and need help responding"
    },
    "apply-individual-pan": {
        "name": "Sneha Reddy",
        "email": "sneha.reddy@example.com",
        "phone": "9876543213",
        "message": "I want to apply for a new PAN card"
    },
    "apply-huf-pan": {
        "name": "Rajesh Singh",
        "email": "rajesh.singh@example.com",
        "phone": "9876543214",
        "message": "Need to apply for HUF PAN for my family"
    },
    "withdraw-pf": {
        "name": "Deepak Verma",
        "email": "deepak.verma@example.com",
        "phone": "9876543215",
        "message": "Want to withdraw my PF amount"
    },
    "update-aadhaar-pan": {
        "name": "Anjali Gupta",
        "email": "anjali.gupta@example.com",
        "phone": "9876543216",
        "message": "Need to update my address in Aadhaar"
    },
    "online-trading-demat": {
        "name": "Vikram Mehta",
        "email": "vikram.mehta@example.com",
        "phone": "9876543217",
        "message": "Interested in opening a Demat account"
    },
    "bank-account": {
        "name": "Pooja Desai",
        "email": "pooja.desai@example.com",
        "phone": "9876543218",
        "message": "Want to open a savings account"
    },
    "financial-planning": {
        "name": "Suresh Nair",
        "email": "suresh.nair@example.com",
        "phone": "9876543219",
        "age": "35",
        "currentIncome": "800000",
        "investmentGoal": "retirement"
    }
}

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)

def print_result(success, message):
    """Print test result"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status}: {message}")

def test_inquiry_endpoint(service_type, data):
    """Test a single inquiry endpoint"""
    endpoint = f"{BASE_URL}/{service_type}"
    
    try:
        print(f"\n📤 Testing: POST {endpoint}")
        print(f"📋 Data: {json.dumps(data, indent=2)}")
        
        response = requests.post(endpoint, json=data, timeout=10)
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ Response: {json.dumps(result, indent=2)}")
            
            # Validate response structure
            if result.get("success") and result.get("inquiryId"):
                print_result(True, f"Inquiry submitted successfully - ID: {result.get('inquiryId')}")
                return True, result.get('inquiryId')
            else:
                print_result(False, "Response missing required fields")
                return False, None
        else:
            print(f"❌ Error Response: {response.text}")
            print_result(False, f"HTTP {response.status_code}")
            return False, None
            
    except requests.exceptions.ConnectionError:
        print_result(False, "Cannot connect to server. Is the backend running?")
        return False, None
    except Exception as e:
        print_result(False, f"Exception: {str(e)}")
        return False, None

def test_admin_endpoints(inquiry_ids):
    """Test admin endpoints"""
    print_header("TESTING ADMIN ENDPOINTS")
    
    # Test get all inquiries
    print("\n📤 Testing: GET All Inquiries")
    try:
        response = requests.get(f"{BASE_URL}/admin/inquiries")
        if response.status_code == 200:
            inquiries = response.json()
            print_result(True, f"Retrieved {len(inquiries)} inquiries")
            print(f"📋 Sample: {json.dumps(inquiries[:2], indent=2) if inquiries else 'No inquiries'}")
        else:
            print_result(False, f"HTTP {response.status_code}")
    except Exception as e:
        print_result(False, f"Exception: {str(e)}")
    
    # Test get inquiry by ID
    if inquiry_ids:
        test_id = inquiry_ids[0]
        print(f"\n📤 Testing: GET Inquiry by ID - {test_id}")
        try:
            response = requests.get(f"{BASE_URL}/admin/inquiries/{test_id}")
            if response.status_code == 200:
                inquiry = response.json()
                print_result(True, f"Retrieved inquiry: {inquiry.get('name')}")
                print(f"📋 Data: {json.dumps(inquiry, indent=2)}")
            else:
                print_result(False, f"HTTP {response.status_code}")
        except Exception as e:
            print_result(False, f"Exception: {str(e)}")
    
    # Test statistics
    print("\n📤 Testing: GET Statistics")
    try:
        response = requests.get(f"{BASE_URL}/admin/inquiries/statistics")
        if response.status_code == 200:
            stats = response.json()
            print_result(True, "Retrieved statistics")
            print(f"📊 Stats: {json.dumps(stats, indent=2)}")
        else:
            print_result(False, f"HTTP {response.status_code}")
    except Exception as e:
        print_result(False, f"Exception: {str(e)}")
    
    # Test update status
    if inquiry_ids:
        test_id = inquiry_ids[0]
        print(f"\n📤 Testing: PUT Update Status - {test_id}")
        try:
            response = requests.put(
                f"{BASE_URL}/admin/inquiries/{test_id}/status",
                json={"status": "contacted"}
            )
            if response.status_code == 200:
                result = response.json()
                print_result(True, f"Status updated to: {result.get('status')}")
            else:
                print_result(False, f"HTTP {response.status_code}")
        except Exception as e:
            print_result(False, f"Exception: {str(e)}")

def main():
    """Run all tests"""
    print_header("RETAIL INQUIRY API TESTING")
    print(f"🕐 Test Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Base URL: {BASE_URL}")
    
    # Test health check
    print("\n🏥 Testing Server Health...")
    try:
        response = requests.get("http://127.0.0.1:8000/health", timeout=5)
        if response.status_code == 200:
            print_result(True, "Server is running")
        else:
            print_result(False, "Server health check failed")
            print("⚠️  Please start the backend server first!")
            return
    except:
        print_result(False, "Cannot connect to server")
        print("⚠️  Please start the backend server first!")
        print("💡 Run: cd cashper_backend && python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000")
        return
    
    # Test all inquiry endpoints
    print_header("TESTING INQUIRY SUBMISSION ENDPOINTS")
    
    inquiry_ids = []
    passed = 0
    failed = 0
    
    for service_type, data in TEST_INQUIRIES.items():
        success, inquiry_id = test_inquiry_endpoint(service_type, data)
        if success:
            passed += 1
            if inquiry_id:
                inquiry_ids.append(inquiry_id)
        else:
            failed += 1
    
    # Test admin endpoints
    test_admin_endpoints(inquiry_ids)
    
    # Summary
    print_header("TEST SUMMARY")
    print(f"✅ Passed: {passed}/{len(TEST_INQUIRIES)} inquiry endpoints")
    print(f"❌ Failed: {failed}/{len(TEST_INQUIRIES)} inquiry endpoints")
    print(f"📝 Created Inquiries: {len(inquiry_ids)}")
    print(f"🕐 Test Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if failed == 0:
        print("\n🎉 All tests passed successfully!")
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()
