"""
Simplified test for Carporate Services APIs (No Authentication Required)
Tests all 9 business service endpoints
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_company_registration():
    """Test Company Registration API"""
    print("\n" + "="*70)
    print("🏢 Testing Company Registration API")
    print("="*70)
    
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
    
    print("\n1. Creating Company Registration Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/company-registration", json=data)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Success! Application ID: {result.get('application_id')}")
        print(f"Status: {result.get('status')}")
        return result.get('application_id')
    else:
        print(f"❌ Error: {response.text}")
        return None

def test_company_compliance():
    """Test Company Compliance API"""
    print("\n" + "="*70)
    print("📋 Testing Company Compliance API")
    print("="*70)
    
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
    response = requests.post(f"{BASE_URL}/api/business-services/company-compliance", json=data)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Success! Application ID: {result.get('application_id')}")
        return result.get('application_id')
    else:
        print(f"❌ Error: {response.text}")
        return None

def test_tax_audit():
    """Test Tax Audit API"""
    print("\n" + "="*70)
    print("📊 Testing Tax Audit API")
    print("="*70)
    
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
    response = requests.post(f"{BASE_URL}/api/business-services/tax-audit", json=data)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Success! Application ID: {result.get('application_id')}")
        return result.get('application_id')
    else:
        print(f"❌ Error: {response.text}")
        return None

def test_legal_advice():
    """Test Legal Advice API"""
    print("\n" + "="*70)
    print("⚖️ Testing Legal Advice API")
    print("="*70)
    
    data = {
        "name": "Sanjay Verma",
        "email": "sanjay.verma@example.com",
        "phone": "9876543213",
        "company_name": "Verma Consultants Pvt Ltd",
        "legal_issue_type": "Contract Dispute",
        "case_description": "Contract dispute with vendor regarding payment terms",
        "urgency": "High",
        "address": "Office 301, Business Tower, Powai",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400076",
        "company_pan": "KLMNO3456P"
    }
    
    print("\n1. Creating Legal Advice Application...")
    response = requests.post(f"{BASE_URL}/api/business-services/legal-advice", json=data)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Success! Application ID: {result.get('application_id')}")
        return result.get('application_id')
    else:
        print(f"❌ Error: {response.text}")
        return None

def test_provident_fund_services():
    """Test PF Services API"""
    print("\n" + "="*70)
    print("💰 Testing Provident Fund Services API")
    print("="*70)
    
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
    response = requests.post(f"{BASE_URL}/api/business-services/provident-fund-services", json=data)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Success! Application ID: {result.get('application_id')}")
        return result.get('application_id')
    else:
        print(f"❌ Error: {response.text}")
        return None

def test_get_all_applications():
    """Test Get All Applications"""
    print("\n" + "="*70)
    print("📑 Testing Get All Applications API")
    print("="*70)
    
    response = requests.get(f"{BASE_URL}/api/business-services/all-applications")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Success! Total Applications: {result.get('count')}")
        
        if result.get('count') > 0:
            print("\nRecent Applications:")
            for app in result.get('applications', [])[:5]:
                print(f"  - {app.get('application_id')}: {app.get('service_type')} ({app.get('status')})")
        return True
    else:
        print(f"❌ Error: {response.text}")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*70)
    print("🚀 STARTING Carporate Services API TESTS (No Authentication)")
    print("="*70)
    
    results = {
        "total": 0,
        "success": 0,
        "failed": 0
    }
    
    tests = [
        ("Company Registration", test_company_registration),
        ("Company Compliance", test_company_compliance),
        ("Tax Audit", test_tax_audit),
        ("Legal Advice", test_legal_advice),
        ("Provident Fund Services", test_provident_fund_services),
        ("Get All Applications", test_get_all_applications)
    ]
    
    for test_name, test_func in tests:
        results["total"] += 1
        try:
            result = test_func()
            if result:
                results["success"] += 1
            else:
                results["failed"] += 1
        except Exception as e:
            print(f"\n❌ {test_name} test failed with exception: {str(e)}")
            results["failed"] += 1
    
    print("\n" + "="*70)
    print("📊 TEST SUMMARY")
    print("="*70)
    print(f"Total Tests: {results['total']}")
    print(f"✅ Success: {results['success']}")
    print(f"❌ Failed: {results['failed']}")
    print(f"Success Rate: {(results['success']/results['total']*100):.1f}%")
    print("="*70)

if __name__ == "__main__":
    run_all_tests()
