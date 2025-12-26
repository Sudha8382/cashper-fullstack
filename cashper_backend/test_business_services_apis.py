"""
Test file for Carporate Services APIs
Tests all 9 business service endpoints:
1. Company Registration
2. Company Compliance
3. Tax Audit
4. Legal Advice
5. Provident Fund Services
6. TDS Services
7. GST Services
8. Payroll Services
9. Accounting & Bookkeeping
"""

import requests
import json
from datetime import datetime

# Base URL
BASE_URL = "http://localhost:8000"

# Test credentials (you need to use a valid logged-in user token)
# First, login to get the token
def get_auth_token():
    """Login and get authentication token"""
    login_data = {
        "email": "test@example.com",  # Change to your test user
        "password": "Test@123"  # Change to your test password
    }
    
    response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    if response.status_code == 200:
        token = response.json().get("access_token")
        print(f"✅ Login successful! Token: {token[:20]}...")
        return token
    else:
        print(f"❌ Login failed: {response.json()}")
        return None

# Test data for each service
def test_company_registration(token):
    """Test Company Registration API"""
    print("\n" + "="*50)
    print("Testing Company Registration API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "full_name": "Rajesh Kumar Singh",
        "email": "rajesh.kumar@example.com",
        "phone": "9876543210",
        "pan_number": "ABCDE1234F",
        "proposed_company_name": "Tech Innovations Pvt Ltd",
        "company_type": "Private Limited",
        "number_of_directors": 2,
        "registration_state": "Maharashtra",
        "address": "Plot No 123, Sector 5, Vashi",
        "city": "Navi Mumbai",
        "state": "Maharashtra",
        "pincode": "400703"
    }
    
    # POST - Create application
    print("\n1. Creating Company Registration Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/company-registration", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        application_id = response.json()["application_id"]
        
        # GET - Fetch all applications
        print("\n2. Fetching all Company Registration Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/company-registration", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")
        
        # GET - Fetch specific application
        print(f"\n3. Fetching specific application: {application_id}")
        response = requests.get(f"{BASE_URL}/api/business-services/company-registration/{application_id}", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Application ID: {response.json()['application']['application_id']}")

def test_company_compliance(token):
    """Test Company Compliance API"""
    print("\n" + "="*50)
    print("Testing Company Compliance API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "full_name": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "phone": "9876543211",
        "pan_number": "CDEFG5678H",
        "company_name": "Sharma Enterprises Pvt Ltd",
        "cin": "U74999MH2020PTC123456",
        "compliance_type": "Annual ROC Filing",
        "registration_date": "2020-05-15",
        "address": "Office No 45, Trade Center, Bandra",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400050"
    }
    
    print("\n1. Creating Company Compliance Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/company-compliance", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all Company Compliance Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/company-compliance", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_tax_audit(token):
    """Test Tax Audit API"""
    print("\n" + "="*50)
    print("Testing Tax Audit API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "full_name": "Amit Patel",
        "email": "amit.patel@example.com",
        "phone": "9876543212",
        "pan_number": "FGHIJ9012K",
        "business_name": "Patel Trading Company",
        "turnover": 25000000.50,
        "audit_type": "Tax Audit u/s 44AB",
        "financial_year": "2023-2024",
        "address": "Shop No 12, Market Road, Andheri",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400058"
    }
    
    print("\n1. Creating Tax Audit Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/tax-audit", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all Tax Audit Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/tax-audit", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_legal_advice(token):
    """Test Legal Advice API"""
    print("\n" + "="*50)
    print("Testing Legal Advice API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": "Sanjay Verma",
        "email": "sanjay.verma@example.com",
        "phone": "9876543213",
        "company_name": "Verma Consultants Pvt Ltd",
        "legal_issue_type": "Contract Dispute",
        "case_description": "We have a contract dispute with our vendor regarding payment terms and delivery schedules. Need legal consultation.",
        "urgency": "High",
        "address": "Office 301, Business Tower, Powai",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400076",
        "company_pan": "KLMNO3456P"
    }
    
    print("\n1. Creating Legal Advice Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/legal-advice", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all Legal Advice Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/legal-advice", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_provident_fund_services(token):
    """Test Provident Fund Services API"""
    print("\n" + "="*50)
    print("Testing Provident Fund Services API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": "Neha Gupta",
        "email": "neha.gupta@example.com",
        "phone": "9876543214",
        "company_name": "Gupta Industries Ltd",
        "number_of_employees": 50,
        "existing_pf_number": "MH/MUM/12345/001",
        "existing_esi_number": "12-34-567890-000",
        "service_required": "PF Compliance & Filing",
        "address": "Industrial Estate, Plot 15, Mahape",
        "city": "Navi Mumbai",
        "state": "Maharashtra",
        "pincode": "400710",
        "company_pan": "PQRST7890U"
    }
    
    print("\n1. Creating PF Services Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/provident-fund-services", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all PF Services Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/provident-fund-services", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_tds_services(token):
    """Test TDS Services API"""
    print("\n" + "="*50)
    print("Testing TDS Services API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "full_name": "Vikram Singh",
        "email": "vikram.singh@example.com",
        "phone": "9876543215",
        "pan_number": "UVWXY1234Z",
        "company_name": "Singh Exports Pvt Ltd",
        "tan_number": "MUMB12345E",
        "service_type": "TDS Return Filing",
        "quarter_year": "Q1 2024-25",
        "address": "Export House, Freight Rd, SEEPZ",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400096"
    }
    
    print("\n1. Creating TDS Services Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/tds-services", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all TDS Services Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/tds-services", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_gst_services(token):
    """Test GST Services API"""
    print("\n" + "="*50)
    print("Testing GST Services API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "full_name": "Aarti Desai",
        "email": "aarti.desai@example.com",
        "phone": "9876543216",
        "pan_number": "ABCDE5678F",
        "business_name": "Desai Retail Stores",
        "gstin": "27ABCDE5678F1Z5",
        "service_type": "GST Return Filing",
        "turnover": 15000000.00,
        "address": "Shop Complex, Station Road, Dadar",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400014"
    }
    
    print("\n1. Creating GST Services Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/gst-services", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all GST Services Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/gst-services", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_payroll_services(token):
    """Test Payroll Services API"""
    print("\n" + "="*50)
    print("Testing Payroll Services API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": "Rahul Mehta",
        "email": "rahul.mehta@example.com",
        "phone": "9876543217",
        "company_name": "Mehta IT Solutions Pvt Ltd",
        "number_of_employees": 75,
        "industry_type": "Information Technology",
        "address": "IT Park, Tower B, Thane West",
        "city": "Thane",
        "state": "Maharashtra",
        "pincode": "400601",
        "company_pan": "FGHIJ9012K",
        "gst_number": "27FGHIJ9012K1Z5",
        "pf_number": "MH/THN/67890/001",
        "esi_number": "12-89-123456-000"
    }
    
    print("\n1. Creating Payroll Services Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/payroll-services", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all Payroll Services Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/payroll-services", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_accounting_bookkeeping(token):
    """Test Accounting & Bookkeeping API"""
    print("\n" + "="*50)
    print("Testing Accounting & Bookkeeping API")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "full_name": "Kavita Joshi",
        "email": "kavita.joshi@example.com",
        "phone": "9876543218",
        "pan_number": "KLMNO3456P",
        "business_name": "Joshi Enterprises",
        "business_type": "Partnership",
        "service_required": "Full Accounting Services",
        "number_of_transactions": "500-1000 per month",
        "address": "Office 12, Commercial Complex, Kandivali",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400101"
    }
    
    print("\n1. Creating Accounting & Bookkeeping Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/accounting-bookkeeping", 
                           json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print("\n2. Fetching all Accounting & Bookkeeping Applications...")
        response = requests.get(f"{BASE_URL}/api/business-services/accounting-bookkeeping", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Count: {response.json()['count']}")

def test_get_all_applications(token):
    """Test Get All Applications API"""
    print("\n" + "="*50)
    print("Testing Get All Business Service Applications")
    print("="*50)
    
    headers = {"Authorization": f"Bearer {token}"}
    
    print("\nFetching all business service applications...")
    response = requests.get(f"{BASE_URL}/api/business-services/all-applications", 
                          headers=headers)
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Total Applications: {result['count']}")
    
    if result['count'] > 0:
        print("\nApplication Summary:")
        for app in result['applications'][:5]:  # Show first 5
            print(f"- {app['application_id']}: {app['service_type']} ({app['status']})")

def run_all_tests():
    """Run all business service API tests"""
    print("\n" + "="*70)
    print("🚀 STARTING Carporate Services API TESTS")
    print("="*70)
    
    # Get authentication token
    token = get_auth_token()
    
    if not token:
        print("\n❌ Cannot proceed without authentication token")
        print("Please create a test user first or update credentials")
        return
    
    # Run all tests
    try:
        test_company_registration(token)
        test_company_compliance(token)
        test_tax_audit(token)
        test_legal_advice(token)
        test_provident_fund_services(token)
        test_tds_services(token)
        test_gst_services(token)
        test_payroll_services(token)
        test_accounting_bookkeeping(token)
        test_get_all_applications(token)
        
        print("\n" + "="*70)
        print("✅ ALL TESTS COMPLETED!")
        print("="*70)
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_all_tests()
