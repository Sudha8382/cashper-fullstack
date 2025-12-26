#!/usr/bin/env python3
"""
Test script for business services API endpoints
Tests company-registration, company-compliance, and tax-audit endpoints
"""

import requests
import json
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"

def test_company_registration():
    """Test company registration endpoint"""
    print("\n" + "="*60)
    print("Testing Company Registration Endpoint")
    print("="*60)
    
    url = f"{BASE_URL}/api/business-services/company-registration"
    
    # Prepare form data
    data = {
        'full_name': 'John Doe',
        'email': 'john@example.com',
        'phone': '9876543210',
        'pan_number': 'ABCDE1234F',
        'proposed_company_name': 'Tech Solutions Pvt Ltd',
        'company_type': 'Private Limited',
        'number_of_directors': '2',
        'registration_state': 'Maharashtra',
        'address': '123 Business Park, Tech Lane',
        'city': 'Mumbai',
        'state': 'Maharashtra',
        'pincode': '400001'
    }
    
    # Create dummy files
    files = {
        'director_pan': ('pan.pdf', b'PAN Document Content'),
        'director_aadhaar': ('aadhaar.pdf', b'Aadhaar Document Content'),
        'director_photo': ('photo.jpg', b'Photo Content'),
        'address_proof': ('address.pdf', b'Address Proof Content')
    }
    
    try:
        response = requests.post(url, data=data, files=files, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print("✅ Company Registration Test PASSED")
            return True
        else:
            print("❌ Company Registration Test FAILED")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def test_company_compliance():
    """Test company compliance endpoint"""
    print("\n" + "="*60)
    print("Testing Company Compliance Endpoint")
    print("="*60)
    
    url = f"{BASE_URL}/api/business-services/company-compliance"
    
    # Prepare form data
    data = {
        'full_name': 'Jane Smith',
        'email': 'jane@example.com',
        'phone': '9876543211',
        'pan_number': 'XYZZZ9876A',
        'company_name': 'Tech Solutions Pvt Ltd',
        'cin': 'U72100MH2020PTC350000',
        'compliance_type': 'Annual Filing',
        'registration_date': '2020-01-15',
        'address': '123 Business Park, Tech Lane',
        'city': 'Mumbai',
        'state': 'Maharashtra',
        'pincode': '400001'
    }
    
    # Create dummy files
    files = {
        'cin_certificate': ('cin.pdf', b'CIN Certificate Content'),
        'pan_card': ('pan.pdf', b'PAN Document Content'),
        'financial_statements': ('financials.pdf', b'Financial Statements Content')
    }
    
    try:
        response = requests.post(url, data=data, files=files, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print("✅ Company Compliance Test PASSED")
            return True
        else:
            print("❌ Company Compliance Test FAILED")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def test_tax_audit():
    """Test tax audit endpoint"""
    print("\n" + "="*60)
    print("Testing Tax Audit Endpoint")
    print("="*60)
    
    url = f"{BASE_URL}/api/business-services/tax-audit"
    
    # Prepare form data
    data = {
        'full_name': 'Raj Kumar',
        'email': 'raj@example.com',
        'phone': '9876543212',
        'pan_number': 'PQRST5678K',
        'business_name': 'Raj Trading Company',
        'turnover': '50000000',
        'audit_type': 'Statutory Audit',
        'financial_year': '2023-2024',
        'address': '456 Commerce Street',
        'city': 'Delhi',
        'state': 'Delhi',
        'pincode': '110001'
    }
    
    # Create dummy files
    files = {
        'pan_card': ('pan.pdf', b'PAN Document Content'),
        'gst_returns': ('gst.pdf', b'GST Returns Content'),
        'balance_sheet': ('balance_sheet.pdf', b'Balance Sheet Content'),
        'profit_loss': ('profit_loss.pdf', b'Profit & Loss Statement Content'),
        'bank_statements': ('bank_statement.pdf', b'Bank Statement Content')
    }
    
    try:
        response = requests.post(url, data=data, files=files, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print("✅ Tax Audit Test PASSED")
            return True
        else:
            print("❌ Tax Audit Test FAILED")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Business Services API Tests")
    print("="*60)
    
    results = {
        'Company Registration': test_company_registration(),
        'Company Compliance': test_company_compliance(),
        'Tax Audit': test_tax_audit()
    }
    
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    print("\n" + ("="*60))
    if all_passed:
        print("✅ All tests PASSED!")
    else:
        print("❌ Some tests FAILED")
    print("="*60)
