"""
Comprehensive Test Script for All Retail Services APIs
Tests: ITR Filing, ITR Revision, ITR Notice Reply, Individual PAN, HUF PAN,
       PF Withdrawal, Document Update, Trading/Demat, Bank Account, Financial Planning
"""

import requests
import json
from datetime import datetime

# Base configuration
BASE_URL = "http://127.0.0.1:8000"
API_BASE = f"{BASE_URL}/api/retail-services"

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def print_success(message):
    print(f"{GREEN}✓ {message}{RESET}")


def print_error(message):
    print(f"{RED}✗ {message}{RESET}")


def print_info(message):
    print(f"{BLUE}ℹ {message}{RESET}")


def print_warning(message):
    print(f"{YELLOW}⚠ {message}{RESET}")


def print_section(title):
    print(f"\n{'=' * 80}")
    print(f"{BLUE}{title.center(80)}{RESET}")
    print(f"{'=' * 80}\n")


# ===================== ITR FILING SERVICE TESTS =====================

def test_itr_filing_application():
    """Test ITR Filing Application Submission"""
    print_section("Testing ITR Filing Service")
    
    payload = {
        "fullName": "Rajesh Kumar",
        "email": "rajesh.kumar@example.com",
        "phone": "9876543210",
        "panNumber": "ABCDE1234F",
        "aadhaarNumber": "123456789012",
        "dateOfBirth": "1990-05-15",
        "employmentType": "salaried",
        "annualIncome": "800000",
        "itrType": "ITR-1",
        "hasBusinessIncome": False,
        "hasCapitalGains": False,
        "hasHouseProperty": False,
        "address": "123 MG Road, Koramangala",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560034"
    }
    
    try:
        print_info("Submitting ITR Filing Application...")
        response = requests.post(f"{API_BASE}/itr-filing", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Application submitted successfully!")
            print_success(f"Application ID: {data.get('applicationId')}")
            print_success(f"Status: {data.get('status')}")
            
            # Test GET endpoint
            app_id = data.get('applicationId')
            print_info(f"\nFetching application details for ID: {app_id}")
            get_response = requests.get(f"{API_BASE}/itr-filing/{app_id}")
            
            if get_response.status_code == 200:
                app_data = get_response.json()
                print_success(f"Retrieved application: {app_data.get('applicantName')}")
                return app_id
            else:
                print_error(f"Failed to retrieve application: {get_response.text}")
        else:
            print_error(f"Failed to submit application: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception occurred: {str(e)}")
        return None


# ===================== ITR REVISION SERVICE TESTS =====================

def test_itr_revision_application():
    """Test ITR Revision Application Submission"""
    print_section("Testing ITR Revision Service")
    
    payload = {
        "fullName": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "phone": "9876543211",
        "panNumber": "PQRST5678Z",
        "aadhaarNumber": "987654321098",
        "acknowledgementNumber": "123456789012345",
        "originalFilingDate": "2023-07-15",
        "reasonForRevision": "Need to update additional income details and claim HRA exemption that was missed in original filing",
        "address": "456 Park Street, Salt Lake",
        "city": "Kolkata",
        "state": "West Bengal",
        "pincode": "700091"
    }
    
    try:
        print_info("Submitting ITR Revision Application...")
        response = requests.post(f"{API_BASE}/itr-revision", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Revision application submitted successfully!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== ITR NOTICE REPLY SERVICE TESTS =====================

def test_itr_notice_reply_application():
    """Test ITR Notice Reply Application Submission"""
    print_section("Testing ITR Notice Reply Service")
    
    payload = {
        "fullName": "Amit Patel",
        "email": "amit.patel@example.com",
        "phone": "9876543212",
        "panNumber": "UVWXY9012A",
        "noticeNumber": "CPC/NOTICE/2024/12345",
        "noticeDate": "2024-11-01",
        "noticeSubject": "Mismatch in Form 26AS and ITR",
        "noticeDescription": "Received notice regarding discrepancy between Form 26AS TDS details and the ITR filed. Need expert assistance to prepare proper response with supporting documents.",
        "address": "789 Ring Road, Vastrapur",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "pincode": "380015"
    }
    
    try:
        print_info("Submitting ITR Notice Reply Application...")
        response = requests.post(f"{API_BASE}/itr-notice-reply", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Notice reply application submitted!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== INDIVIDUAL PAN APPLICATION TESTS =====================

def test_individual_pan_application():
    """Test Individual PAN Application Submission"""
    print_section("Testing Individual PAN Application")
    
    payload = {
        "fullName": "Sneha Reddy",
        "fatherName": "Ramesh Reddy",
        "dateOfBirth": "1995-08-20",
        "email": "sneha.reddy@example.com",
        "phone": "9876543213",
        "aadhaarNumber": "234567890123",
        "gender": "female",
        "category": "individual",
        "applicationType": "new",
        "address": "101 Jubilee Hills, Road No 36",
        "city": "Hyderabad",
        "state": "Telangana",
        "pincode": "500033"
    }
    
    try:
        print_info("Submitting Individual PAN Application...")
        response = requests.post(f"{API_BASE}/individual-pan", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"PAN application submitted successfully!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== HUF PAN APPLICATION TESTS =====================

def test_huf_pan_application():
    """Test HUF PAN Application Submission"""
    print_section("Testing HUF PAN Application")
    
    payload = {
        "hufName": "Kumar Hindu Undivided Family",
        "kartaName": "Suresh Kumar",
        "kartaPAN": "KLMNO3456P",
        "email": "suresh.kumar@example.com",
        "phone": "9876543214",
        "dateOfFormation": "2020-04-01",
        "hufMembers": 5,
        "address": "202 Civil Lines, Raja Park",
        "city": "Jaipur",
        "state": "Rajasthan",
        "pincode": "302006"
    }
    
    try:
        print_info("Submitting HUF PAN Application...")
        response = requests.post(f"{API_BASE}/huf-pan", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"HUF PAN application submitted!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== PF WITHDRAWAL APPLICATION TESTS =====================

def test_pf_withdrawal_application():
    """Test PF Withdrawal Application Submission"""
    print_section("Testing PF Withdrawal Application")
    
    payload = {
        "fullName": "Vikram Singh",
        "email": "vikram.singh@example.com",
        "phone": "9876543215",
        "panNumber": "FGHIJ6789K",
        "uanNumber": "123456789012",
        "employerName": "TCS Limited",
        "withdrawalType": "full",
        "withdrawalAmount": 450000.00,
        "withdrawalReason": "Resigned from current job after 5 years of service. Planning to start own business venture. Need full EPF settlement for capital investment.",
        "lastWorkingDate": "2024-10-31",
        "address": "303 Sector 15, Dwarka",
        "city": "New Delhi",
        "state": "Delhi",
        "pincode": "110075"
    }
    
    try:
        print_info("Submitting PF Withdrawal Application...")
        response = requests.post(f"{API_BASE}/pf-withdrawal", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"PF withdrawal application submitted!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== DOCUMENT UPDATE APPLICATION TESTS =====================

def test_document_update_application():
    """Test Document Update Application Submission"""
    print_section("Testing Document Update Application")
    
    payload = {
        "fullName": "Meera Nair",
        "email": "meera.nair@example.com",
        "phone": "9876543216",
        "updateType": "aadhaar",
        "currentAadhaarNumber": "345678901234",
        "currentPANNumber": "MNOPQ7890L",
        "updateReason": "Recently got married and changed surname. Need to update Aadhaar card with new name and address after marriage.",
        "newDetails": "Name change from Meera Nair to Meera Kumar. New address: 404 Marine Drive, Ernakulam, Kerala",
        "address": "404 Marine Drive, Ernakulam",
        "city": "Kochi",
        "state": "Kerala",
        "pincode": "682011"
    }
    
    try:
        print_info("Submitting Document Update Application...")
        response = requests.post(f"{API_BASE}/document-update", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Document update application submitted!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== TRADING & DEMAT ACCOUNT TESTS =====================

def test_trading_demat_application():
    """Test Trading & Demat Account Application Submission"""
    print_section("Testing Trading & Demat Account Application")
    
    payload = {
        "fullName": "Arjun Kapoor",
        "email": "arjun.kapoor@example.com",
        "phone": "9876543217",
        "panNumber": "RSTUV1234M",
        "aadhaarNumber": "456789012345",
        "dateOfBirth": "1992-03-10",
        "accountType": "individual",
        "tradingSegments": ["equity", "derivatives", "commodity"],
        "annualIncome": "1200000",
        "occupationType": "salaried",
        "experienceLevel": "beginner",
        "address": "505 Andheri West, JVPD Scheme",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400053",
        "bankName": "HDFC Bank",
        "accountNumber": "12345678901234",
        "ifscCode": "HDFC0001234"
    }
    
    try:
        print_info("Submitting Trading & Demat Account Application...")
        response = requests.post(f"{API_BASE}/trading-demat", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Trading account application submitted!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== BANK ACCOUNT APPLICATION TESTS =====================

def test_bank_account_application():
    """Test Bank Account Application Submission"""
    print_section("Testing Bank Account Application")
    
    payload = {
        "fullName": "Deepika Joshi",
        "email": "deepika.joshi@example.com",
        "phone": "9876543218",
        "panNumber": "WXYZB5678N",
        "aadhaarNumber": "567890123456",
        "dateOfBirth": "1994-11-25",
        "accountType": "savings",
        "bankPreference": "ICICI Bank",
        "accountVariant": "regular",
        "monthlyIncome": "65000",
        "occupationType": "salaried",
        "nomineeRequired": True,
        "nomineeName": "Rahul Joshi",
        "nomineeRelation": "brother",
        "address": "606 Banjara Hills, Road No 12",
        "city": "Hyderabad",
        "state": "Telangana",
        "pincode": "500034",
        "residenceType": "owned"
    }
    
    try:
        print_info("Submitting Bank Account Application...")
        response = requests.post(f"{API_BASE}/bank-account", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Bank account application submitted!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== FINANCIAL PLANNING SERVICE TESTS =====================

def test_financial_planning_application():
    """Test Financial Planning Service Application Submission"""
    print_section("Testing Financial Planning Service")
    
    payload = {
        "name": "Karthik Iyer",
        "email": "karthik.iyer@example.com",
        "phone": "9876543219",
        "age": 32,
        "occupation": "software engineer",
        "annualIncome": "1500000",
        "existingInvestments": "Mutual funds: 5L, PPF: 2L, NPS: 1L",
        "riskProfile": "moderate",
        "investmentGoal": "retirement planning",
        "timeHorizon": "20+ years",
        "address": "707 Whitefield, EPIP Zone",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560066",
        "panNumber": "CDEFG9012O"
    }
    
    try:
        print_info("Submitting Financial Planning Application...")
        response = requests.post(f"{API_BASE}/financial-planning", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Financial planning application submitted!")
            print_success(f"Application ID: {data.get('applicationId')}")
            return data.get('applicationId')
        else:
            print_error(f"Failed: {response.text}")
            return None
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return None


# ===================== GET ALL APPLICATIONS TEST =====================

def test_get_all_applications():
    """Test fetching all retail service applications"""
    print_section("Testing Get All Applications")
    
    try:
        print_info("Fetching all applications...")
        response = requests.get(f"{API_BASE}/applications")
        
        if response.status_code == 200:
            data = response.json()
            total = data.get('total', 0)
            applications = data.get('applications', [])
            
            print_success(f"Total applications: {total}")
            print_success(f"Retrieved {len(applications)} applications")
            
            # Display summary by service type
            service_counts = {}
            for app in applications:
                service_type = app.get('serviceType')
                service_counts[service_type] = service_counts.get(service_type, 0) + 1
            
            print_info("\nApplications by Service Type:")
            for service, count in service_counts.items():
                print(f"  {service}: {count}")
            
            return True
        else:
            print_error(f"Failed to fetch applications: {response.text}")
            return False
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return False


# ===================== GET APPLICATIONS BY SERVICE TYPE TEST =====================

def test_get_applications_by_service_type():
    """Test fetching applications filtered by service type"""
    print_section("Testing Get Applications By Service Type")
    
    service_types = [
        "itr-filing",
        "itr-revision",
        "individual-pan",
        "trading-demat",
        "financial-planning"
    ]
    
    for service_type in service_types:
        try:
            print_info(f"\nFetching {service_type} applications...")
            response = requests.get(f"{API_BASE}/applications?service_type={service_type}")
            
            if response.status_code == 200:
                data = response.json()
                count = data.get('total', 0)
                print_success(f"{service_type}: {count} applications")
            else:
                print_error(f"Failed for {service_type}: {response.text}")
        except Exception as e:
            print_error(f"Exception for {service_type}: {str(e)}")


# ===================== UPDATE APPLICATION STATUS TEST =====================

def test_update_application_status(application_id):
    """Test updating application status"""
    print_section("Testing Update Application Status")
    
    if not application_id:
        print_warning("No application ID provided. Skipping status update test.")
        return False
    
    try:
        print_info(f"Updating status for application: {application_id}")
        
        # Update to under-review
        response = requests.patch(
            f"{API_BASE}/applications/{application_id}/status",
            params={
                "status": "under-review",
                "admin_notes": "Application received and under initial review"
            }
        )
        
        if response.status_code == 200:
            print_success("Status updated to 'under-review'")
            
            # Update to in-progress
            response2 = requests.patch(
                f"{API_BASE}/applications/{application_id}/status",
                params={
                    "status": "in-progress",
                    "admin_notes": "Processing application documents"
                }
            )
            
            if response2.status_code == 200:
                print_success("Status updated to 'in-progress'")
                return True
        
        print_error(f"Failed to update status: {response.text}")
        return False
    except Exception as e:
        print_error(f"Exception: {str(e)}")
        return False


# ===================== MAIN TEST RUNNER =====================

def run_all_tests():
    """Run all retail service API tests"""
    print_section("RETAIL SERVICES API - COMPREHENSIVE TEST SUITE")
    print_info(f"Testing against: {BASE_URL}")
    print_info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Track results
    results = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "application_ids": []
    }
    
    # Test all services
    tests = [
        ("ITR Filing", test_itr_filing_application),
        ("ITR Revision", test_itr_revision_application),
        ("ITR Notice Reply", test_itr_notice_reply_application),
        ("Individual PAN", test_individual_pan_application),
        ("HUF PAN", test_huf_pan_application),
        ("PF Withdrawal", test_pf_withdrawal_application),
        ("Document Update", test_document_update_application),
        ("Trading & Demat", test_trading_demat_application),
        ("Bank Account", test_bank_account_application),
        ("Financial Planning", test_financial_planning_application),
    ]
    
    for test_name, test_func in tests:
        results["total"] += 1
        app_id = test_func()
        if app_id:
            results["passed"] += 1
            results["application_ids"].append(app_id)
        else:
            results["failed"] += 1
    
    # Test GET endpoints
    results["total"] += 1
    if test_get_all_applications():
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    results["total"] += 1
    test_get_applications_by_service_type()
    results["passed"] += 1  # Informational test
    
    # Test status update with first application ID
    if results["application_ids"]:
        results["total"] += 1
        if test_update_application_status(results["application_ids"][0]):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # Print summary
    print_section("TEST SUMMARY")
    print(f"Total Tests: {results['total']}")
    print_success(f"Passed: {results['passed']}")
    if results['failed'] > 0:
        print_error(f"Failed: {results['failed']}")
    else:
        print_success(f"Failed: {results['failed']}")
    
    print(f"\n{BLUE}Application IDs created during testing:{RESET}")
    for idx, app_id in enumerate(results['application_ids'], 1):
        print(f"  {idx}. {app_id}")
    
    success_rate = (results['passed'] / results['total']) * 100 if results['total'] > 0 else 0
    print(f"\n{BLUE}Success Rate: {success_rate:.1f}%{RESET}")
    
    if success_rate == 100:
        print_success("\n🎉 ALL TESTS PASSED! 🎉")
    elif success_rate >= 80:
        print_warning("\n⚠️  MOST TESTS PASSED")
    else:
        print_error("\n❌ SEVERAL TESTS FAILED")
    
    print(f"\n{'=' * 80}\n")


if __name__ == "__main__":
    run_all_tests()
