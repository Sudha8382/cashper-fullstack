"""
Comprehensive test script for Retail Services APIs
Tests all 10 retail service endpoints with realistic data
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

# ANSI color codes for better output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def print_test_header(service_name):
    """Print test section header"""
    print(f"\n{'='*80}")
    print(f"{BLUE}TESTING: {service_name}{RESET}")
    print(f"{'='*80}\n")


def print_result(success, message):
    """Print test result with color"""
    if success:
        print(f"{GREEN}✓ {message}{RESET}")
    else:
        print(f"{RED}✗ {message}{RESET}")


def test_itr_filing_service():
    """Test ITR Filing Service API"""
    print_test_header("ITR Filing Service")
    
    test_data = {
        "fullName": "Rajesh Kumar Singh",
        "email": "rajesh.kumar@example.com",
        "phone": "9876543210",
        "panNumber": "ABCDE1234F",
        "aadhaarNumber": "123456789012",
        "dateOfBirth": "1985-05-15",
        "employmentType": "salaried",
        "annualIncome": "800000",
        "itrType": "ITR-1",
        "hasBusinessIncome": False,
        "hasCapitalGains": False,
        "hasHouseProperty": True,
        "address": "A-101, Green Valley Apartments, MG Road",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400001"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/itr-filing", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_itr_revision_service():
    """Test ITR Revision Service API"""
    print_test_header("ITR Revision Service")
    
    test_data = {
        "fullName": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "phone": "9876543211",
        "panNumber": "BCDEF2345G",
        "aadhaarNumber": "123456789013",
        "acknowledgementNumber": "ACK123456789012345",
        "originalFilingDate": "2023-07-20",
        "reasonForRevision": "Incorrect income from house property reported. Need to add rental income details.",
        "address": "B-202, Sunshine Towers, Linking Road",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400050"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/itr-revision", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_itr_notice_reply_service():
    """Test ITR Notice Reply Service API"""
    print_test_header("ITR Notice Reply Service")
    
    test_data = {
        "fullName": "Amit Patel",
        "email": "amit.patel@example.com",
        "phone": "9876543212",
        "panNumber": "CDEFG3456H",
        "noticeNumber": "NOTICE/2024/123456",
        "noticeDate": "2024-01-15",
        "noticeSubject": "Mismatch in Form 26AS and ITR",
        "noticeDescription": "The Income Tax Department has identified a mismatch between Form 26AS and the Income Tax Return filed. Please provide clarification regarding unreported TDS deductions.",
        "address": "C-303, Royal Heights, SV Road",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560001"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/itr-notice-reply", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_individual_pan_service():
    """Test Individual PAN Application API"""
    print_test_header("Individual PAN Application")
    
    test_data = {
        "fullName": "Sneha Reddy",
        "fatherName": "Ramesh Reddy",
        "dateOfBirth": "1995-03-20",
        "email": "sneha.reddy@example.com",
        "phone": "9876543213",
        "aadhaarNumber": "123456789014",
        "gender": "female",
        "category": "individual",
        "applicationType": "new",
        "address": "D-404, Lakeside Residency, Tank Road",
        "city": "Hyderabad",
        "state": "Telangana",
        "pincode": "500001"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/individual-pan", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_huf_pan_service():
    """Test HUF PAN Application API"""
    print_test_header("HUF PAN Application")
    
    test_data = {
        "hufName": "Kumar Family HUF",
        "kartaName": "Vikram Kumar",
        "kartaPAN": "DEFGH4567I",
        "email": "vikram.kumar@example.com",
        "phone": "9876543214",
        "dateOfFormation": "2020-04-01",
        "hufMembers": 5,
        "address": "E-505, Heritage Mansion, Park Street",
        "city": "Kolkata",
        "state": "West Bengal",
        "pincode": "700001"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/huf-pan", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_pf_withdrawal_service():
    """Test PF Withdrawal Application API"""
    print_test_header("PF Withdrawal Application")
    
    test_data = {
        "fullName": "Arjun Verma",
        "email": "arjun.verma@example.com",
        "phone": "9876543215",
        "panNumber": "EFGHI5678J",
        "uanNumber": "100123456789",
        "employerName": "Tech Solutions Pvt Ltd",
        "withdrawalType": "partial",
        "withdrawalAmount": 150000.00,
        "withdrawalReason": "Medical emergency - hospitalization expenses for family member requiring urgent treatment",
        "lastWorkingDate": "2024-01-31",
        "address": "F-606, Skyline Towers, Brigade Road",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560025"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/pf-withdrawal", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_document_update_service():
    """Test Document Update Application API"""
    print_test_header("Document Update Application (Aadhaar/PAN)")
    
    test_data = {
        "fullName": "Neha Gupta",
        "email": "neha.gupta@example.com",
        "phone": "9876543216",
        "updateType": "both",
        "currentAadhaarNumber": "123456789015",
        "currentPANNumber": "FGHIJ6789K",
        "updateReason": "Change of address after relocation to new city",
        "newDetails": "New address: G-707, Ocean View Apartments, Marine Drive, Mumbai 400020",
        "address": "G-707, Ocean View Apartments, Marine Drive",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400020"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/document-update", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_trading_demat_service():
    """Test Trading & Demat Account Application API"""
    print_test_header("Trading & Demat Account Application")
    
    test_data = {
        "fullName": "Karan Malhotra",
        "email": "karan.malhotra@example.com",
        "phone": "9876543217",
        "panNumber": "GHIJK7890L",
        "aadhaarNumber": "123456789016",
        "dateOfBirth": "1990-08-12",
        "accountType": "individual",
        "tradingSegments": ["equity", "derivatives", "commodity"],
        "annualIncome": "1200000",
        "occupationType": "business",
        "experienceLevel": "intermediate",
        "address": "H-808, Trade Center, Nariman Point",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400021",
        "bankName": "HDFC Bank",
        "accountNumber": "12345678901234",
        "ifscCode": "HDFC0001234"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/trading-demat", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_bank_account_service():
    """Test Bank Account Application API"""
    print_test_header("Bank Account Application")
    
    test_data = {
        "fullName": "Divya Krishnan",
        "email": "divya.krishnan@example.com",
        "phone": "9876543218",
        "panNumber": "HIJKL8901M",
        "aadhaarNumber": "123456789017",
        "dateOfBirth": "1992-11-25",
        "accountType": "savings",
        "bankPreference": "HDFC Bank",
        "accountVariant": "regular-savings",
        "monthlyIncome": "75000",
        "occupationType": "salaried",
        "nomineeRequired": True,
        "nomineeName": "Arvind Krishnan",
        "nomineeRelation": "Father",
        "address": "I-909, Palm Grove Apartments, Anna Nagar",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "pincode": "600040",
        "residenceType": "owned"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/bank-account", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_financial_planning_service():
    """Test Financial Planning Service API"""
    print_test_header("Financial Planning Service")
    
    test_data = {
        "name": "Rohan Desai",
        "email": "rohan.desai@example.com",
        "phone": "9876543219",
        "age": 32,
        "occupation": "Software Engineer",
        "annualIncome": "1500000",
        "existingInvestments": "Mutual Funds: ₹5L, PPF: ₹3L, Fixed Deposits: ₹2L",
        "riskProfile": "moderate",
        "investmentGoal": "Retirement planning and children's education",
        "timeHorizon": "15-20 years",
        "address": "J-1010, Tech Park Residency, Whitefield",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560066",
        "panNumber": "IJKLM9012N"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/retail-services/financial-planning", json=test_data)
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Application submitted successfully - ID: {result.get('applicationId')}")
        return result.get('applicationId')
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return None


def test_get_applications(application_ids):
    """Test GET all applications endpoint"""
    print_test_header("GET All Applications")
    
    try:
        response = requests.get(f"{BASE_URL}/api/retail-services/applications")
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Retrieved {result.get('total')} applications")
        print(f"\n{YELLOW}Application Summary:{RESET}")
        for app in result.get('applications', [])[:5]:
            print(f"  - {app['applicantName']} ({app['serviceType']}) - Status: {app['status']}")
        return True
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return False


def test_get_specific_application(application_id):
    """Test GET specific application by service type"""
    print_test_header("GET Specific Application")
    
    if not application_id:
        print_result(False, "No application ID provided")
        return False
    
    try:
        response = requests.get(f"{BASE_URL}/api/retail-services/itr-filing/{application_id}")
        response.raise_for_status()
        result = response.json()
        print_result(True, f"Retrieved application for {result['applicantName']}")
        return True
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return False


def test_update_application_status(application_id):
    """Test PATCH update application status"""
    print_test_header("UPDATE Application Status")
    
    if not application_id:
        print_result(False, "No application ID provided")
        return False
    
    try:
        response = requests.patch(
            f"{BASE_URL}/api/retail-services/applications/{application_id}/status",
            params={"status": "under-review", "admin_notes": "Application received and being reviewed by team"}
        )
        response.raise_for_status()
        result = response.json()
        print_result(True, "Application status updated successfully")
        return True
    except Exception as e:
        print_result(False, f"Failed: {str(e)}")
        return False


def main():
    """Run all tests"""
    print(f"\n{BLUE}{'='*80}{RESET}")
    print(f"{BLUE}RETAIL SERVICES API COMPREHENSIVE TEST SUITE{RESET}")
    print(f"{BLUE}{'='*80}{RESET}\n")
    print(f"{YELLOW}Testing Base URL: {BASE_URL}{RESET}\n")
    
    # Store application IDs for later tests
    application_ids = {}
    
    # Test all service submission endpoints
    application_ids['itr_filing'] = test_itr_filing_service()
    application_ids['itr_revision'] = test_itr_revision_service()
    application_ids['itr_notice_reply'] = test_itr_notice_reply_service()
    application_ids['individual_pan'] = test_individual_pan_service()
    application_ids['huf_pan'] = test_huf_pan_service()
    application_ids['pf_withdrawal'] = test_pf_withdrawal_service()
    application_ids['document_update'] = test_document_update_service()
    application_ids['trading_demat'] = test_trading_demat_service()
    application_ids['bank_account'] = test_bank_account_service()
    application_ids['financial_planning'] = test_financial_planning_service()
    
    # Test retrieval and management endpoints
    test_get_applications(application_ids)
    test_get_specific_application(application_ids.get('itr_filing'))
    test_update_application_status(application_ids.get('itr_filing'))
    
    # Print summary
    print(f"\n{BLUE}{'='*80}{RESET}")
    print(f"{BLUE}TEST SUMMARY{RESET}")
    print(f"{BLUE}{'='*80}{RESET}\n")
    
    successful_apps = [k for k, v in application_ids.items() if v is not None]
    print(f"{GREEN}✓ Successfully created {len(successful_apps)} applications{RESET}")
    print(f"{YELLOW}Application IDs:{RESET}")
    for service, app_id in application_ids.items():
        if app_id:
            print(f"  - {service}: {app_id}")
    
    print(f"\n{GREEN}All tests completed!{RESET}\n")


if __name__ == "__main__":
    main()
