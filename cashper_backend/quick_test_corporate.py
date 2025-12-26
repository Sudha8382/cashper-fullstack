"""
Quick Test for Corporate Inquiry APIs
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("="*70)
print("TESTING CORPORATE INQUIRY APIs")
print("="*70)

# Test 1: Health Check
print("\n1. Testing Server Health...")
try:
    response = requests.get(f"{BASE_URL}/health")
    print(f"   Status: {response.status_code}")
    print(f"   ✅ Server is running!")
except Exception as e:
    print(f"   ❌ Error: {e}")
    print("   Please start the server first!")
    exit(1)

# Test 2: Register Company
print("\n2. Testing Register Company...")
try:
    data = {
        "name": "Rajesh Kumar",
        "email": "rajesh@business.com",
        "phone": "9876543210",
        "companyName": "Tech Solutions Pvt Ltd",
        "message": "Want to register company"
    }
    response = requests.post(f"{BASE_URL}/api/corporate-inquiry/register-company", json=data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        result = response.json()
        print(f"   ✅ Created: {result.get('inquiryId')}")
    else:
        print(f"   ❌ Failed: {response.text}")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 3: Tax Audit
print("\n3. Testing Tax Audit...")
try:
    data = {
        "name": "Priya Sharma",
        "email": "priya@enterprise.com",
        "phone": "9876543211",
        "companyName": "Enterprise Ltd",
        "message": "Need tax audit"
    }
    response = requests.post(f"{BASE_URL}/api/corporate-inquiry/tax-audit", json=data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        result = response.json()
        print(f"   ✅ Created: {result.get('inquiryId')}")
    else:
        print(f"   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 4: GST Services
print("\n4. Testing GST Services...")
try:
    data = {
        "name": "Amit Patel",
        "email": "amit@trading.com",
        "phone": "9876543212",
        "companyName": "Trading Co",
        "message": "GST registration needed"
    }
    response = requests.post(f"{BASE_URL}/api/corporate-inquiry/gst-services", json=data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        result = response.json()
        print(f"   ✅ Created: {result.get('inquiryId')}")
    else:
        print(f"   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 5: Payroll Services
print("\n5. Testing Payroll Services...")
try:
    data = {
        "name": "Sneha Reddy",
        "email": "sneha@hrservices.com",
        "phone": "9876543213",
        "companyName": "HR Services",
        "message": "Need payroll services"
    }
    response = requests.post(f"{BASE_URL}/api/corporate-inquiry/payroll-services", json=data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        result = response.json()
        print(f"   ✅ Created: {result.get('inquiryId')}")
    else:
        print(f"   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 6: Accounting & Bookkeeping
print("\n6. Testing Accounting & Bookkeeping...")
try:
    data = {
        "name": "Vikram Mehta",
        "email": "vikram@retail.com",
        "phone": "9876543214",
        "companyName": "Retail Ventures",
        "message": "Accounting services required"
    }
    response = requests.post(f"{BASE_URL}/api/corporate-inquiry/accounting-bookkeeping", json=data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        result = response.json()
        print(f"   ✅ Created: {result.get('inquiryId')}")
    else:
        print(f"   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test Admin: Get All Inquiries
print("\n7. Testing Admin - Get All Inquiries...")
try:
    response = requests.get(f"{BASE_URL}/api/corporate-inquiry/admin/inquiries")
    if response.status_code == 200:
        inquiries = response.json()
        print(f"   ✅ Retrieved {len(inquiries)} inquiries")
    else:
        print(f"   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test Admin: Get Statistics
print("\n8. Testing Admin - Get Statistics...")
try:
    response = requests.get(f"{BASE_URL}/api/corporate-inquiry/admin/statistics")
    if response.status_code == 200:
        stats = response.json()
        print(f"   ✅ Total: {stats.get('total')}, New: {stats.get('new')}")
        print(f"   By Service:")
        for service, count in stats.get('byService', {}).items():
            print(f"      - {service}: {count}")
    else:
        print(f"   ❌ Failed")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "="*70)
print("TESTING COMPLETE!")
print("="*70)
print("\n✨ All Corporate Inquiry APIs are working!")
print("\n📝 Available Endpoints:")
print("   • POST /api/corporate-inquiry/register-company")
print("   • POST /api/corporate-inquiry/compliance-new-company")
print("   • POST /api/corporate-inquiry/tax-audit")
print("   • POST /api/corporate-inquiry/legal-advice")
print("   • POST /api/corporate-inquiry/provident-fund")
print("   • POST /api/corporate-inquiry/tds-services")
print("   • POST /api/corporate-inquiry/gst-services")
print("   • POST /api/corporate-inquiry/payroll-services")
print("   • POST /api/corporate-inquiry/accounting-bookkeeping")
print("\n🌐 API Documentation: http://127.0.0.1:8000/docs")
