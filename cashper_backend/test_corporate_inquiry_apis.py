"""
Complete Test for ALL 9 Corporate Inquiry APIs
Tests every single business service endpoint
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

# Test data for all 9 corporate services
tests = [
    {
        "name": "Register New Company",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/register-company",
        "data": {
            "name": "Rajesh Kumar",
            "email": "rajesh.kumar@business.com",
            "phone": "9876543210",
            "companyName": "Tech Solutions Pvt Ltd",
            "message": "Want to register a Private Limited Company"
        }
    },
    {
        "name": "Compliance for New Company",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/compliance-new-company",
        "data": {
            "name": "Priya Sharma",
            "email": "priya.sharma@startup.com",
            "phone": "9876543211",
            "companyName": "StartUp Innovations LLP",
            "message": "Need compliance services for newly registered company"
        }
    },
    {
        "name": "Tax Audit",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/tax-audit",
        "data": {
            "name": "Amit Patel",
            "email": "amit.patel@enterprise.com",
            "phone": "9876543212",
            "companyName": "Enterprise Solutions Ltd",
            "message": "Require tax audit services for FY 2024-25"
        }
    },
    {
        "name": "Legal Advice",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/legal-advice",
        "data": {
            "name": "Sneha Reddy",
            "email": "sneha.reddy@corporate.com",
            "phone": "9876543213",
            "companyName": "Corporate Services Inc",
            "message": "Need legal advice on corporate restructuring"
        }
    },
    {
        "name": "Provident Fund Services",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/provident-fund",
        "data": {
            "name": "Ramesh Singh",
            "email": "ramesh.singh@manufacturing.com",
            "phone": "9876543214",
            "companyName": "Manufacturing Co Ltd",
            "message": "Need help with EPF registration and compliance"
        }
    },
    {
        "name": "TDS-Related Services",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/tds-services",
        "data": {
            "name": "Deepak Verma",
            "email": "deepak.verma@finance.com",
            "phone": "9876543215",
            "companyName": "Finance Solutions Pvt Ltd",
            "message": "Require TDS filing and compliance services"
        }
    },
    {
        "name": "GST-Related Services",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/gst-services",
        "data": {
            "name": "Anjali Gupta",
            "email": "anjali.gupta@trading.com",
            "phone": "9876543216",
            "companyName": "Trading Company Ltd",
            "message": "Need GST registration and monthly filing services"
        }
    },
    {
        "name": "Payroll Services",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/payroll-services",
        "data": {
            "name": "Vikram Mehta",
            "email": "vikram.mehta@hrservices.com",
            "phone": "9876543217",
            "companyName": "HR Services Pvt Ltd",
            "message": "Looking for complete payroll processing services"
        }
    },
    {
        "name": "Accounting & Bookkeeping",
        "endpoint": f"{BASE_URL}/api/corporate-inquiry/accounting-bookkeeping",
        "data": {
            "name": "Pooja Desai",
            "email": "pooja.desai@retail.com",
            "phone": "9876543218",
            "companyName": "Retail Ventures Ltd",
            "message": "Need accounting and bookkeeping services"
        }
    }
]

print("="*70)
print("COMPREHENSIVE TEST - ALL 9 CORPORATE INQUIRY APIs")
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
print("\n📋 Getting All Corporate Inquiries...")
try:
    response = requests.get(f"{BASE_URL}/api/corporate-inquiry/admin/inquiries")
    if response.status_code == 200:
        inquiries = response.json()
        print(f"✅ Retrieved {len(inquiries)} total corporate inquiries")
        print(f"Recent inquiries created in this test: {len(inquiry_ids)}")
        if inquiries:
            print(f"\nSample inquiry:")
            sample = inquiries[0]
            print(f"  - Name: {sample.get('name')}")
            print(f"  - Company: {sample.get('companyName')}")
            print(f"  - Service: {sample.get('serviceType')}")
    else:
        print(f"❌ Failed - Status: {response.status_code}")
except Exception as e:
    print(f"❌ Error: {e}")

# Get statistics
print("\n📊 Getting Corporate Statistics...")
try:
    response = requests.get(f"{BASE_URL}/api/corporate-inquiry/admin/statistics")
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

# Test update status if we have inquiries
if inquiry_ids:
    print(f"\n🔄 Testing Update Status for first inquiry...")
    try:
        test_id = inquiry_ids[0]
        response = requests.put(
            f"{BASE_URL}/api/corporate-inquiry/admin/inquiries/{test_id}/status",
            json={"status": "contacted"}
        )
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status updated successfully to: {result.get('status')}")
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
print(f"📝 Corporate Inquiries Created: {len(inquiry_ids)}")

if failed == 0:
    print("\n🎉 ALL TESTS PASSED! All 9 corporate inquiry APIs are working perfectly!")
    print("\n📋 Created Inquiry IDs:")
    for idx, inq_id in enumerate(inquiry_ids, 1):
        print(f"   {idx}. {inq_id}")
else:
    print("\n⚠️  Some tests failed. Please check the errors above.")

print("\n📚 API Documentation: http://127.0.0.1:8000/docs")
print(f"{'='*70}")
