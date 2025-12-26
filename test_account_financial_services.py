"""
Quick Test Script for Account Opening Services APIs
Tests: Trading/Demat Account, Bank Account, Financial Planning
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/retail-services"

print("=" * 80)
print("Testing Account Opening & Financial Services APIs".center(80))
print("=" * 80)

# Test 1: Trading & Demat Account
print("\n1. Testing Trading & Demat Account Application...")
trading_demat_data = {
    "fullName": "Test Trading User",
    "email": "test.trading@example.com",
    "phone": "7777777777",
    "panNumber": "RSTUV1234M",
    "aadhaarNumber": "456789012345",
    "dateOfBirth": "1992-03-10",
    "accountType": "individual",
    "tradingSegments": ["equity", "derivatives"],
    "annualIncome": "800000",
    "occupationType": "salaried",
    "experienceLevel": "beginner",
    "address": "Test Trading Address, Financial District",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400051",
    "bankName": "HDFC Bank",
    "accountNumber": "12345678901234",
    "ifscCode": "HDFC0001234"
}

try:
    response = requests.post(f"{BASE_URL}/trading-demat", json=trading_demat_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Trading & Demat Account Application Submitted!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  Applicant: {trading_demat_data['fullName']}")
        print(f"  Segments: {', '.join(trading_demat_data['tradingSegments'])}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 2: Bank Account Application
print("\n2. Testing Bank Account Application...")
bank_account_data = {
    "fullName": "Test Bank Account User",
    "email": "test.bank@example.com",
    "phone": "7777777776",
    "panNumber": "WXYZB5678N",
    "aadhaarNumber": "567890123456",
    "dateOfBirth": "1994-11-25",
    "accountType": "savings",
    "bankPreference": "ICICI Bank",
    "accountVariant": "regular",
    "monthlyIncome": "50000",
    "occupationType": "salaried",
    "nomineeRequired": True,
    "nomineeName": "Test Nominee",
    "nomineeRelation": "spouse",
    "address": "Test Bank Address, Main Street",
    "city": "Hyderabad",
    "state": "Telangana",
    "pincode": "500001",
    "residenceType": "rented"
}

try:
    response = requests.post(f"{BASE_URL}/bank-account", json=bank_account_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Bank Account Application Submitted!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  Applicant: {bank_account_data['fullName']}")
        print(f"  Bank: {bank_account_data['bankPreference']}")
        print(f"  Nominee: {bank_account_data['nomineeName']} ({bank_account_data['nomineeRelation']})")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test 3: Financial Planning Service
print("\n3. Testing Financial Planning Service...")
financial_planning_data = {
    "name": "Test Financial Planning User",
    "email": "test.financial@example.com",
    "phone": "7777777775",
    "age": 35,
    "occupation": "business owner",
    "annualIncome": "1500000",
    "existingInvestments": "PPF: 3L, Mutual Funds: 5L",
    "riskProfile": "moderate",
    "investmentGoal": "retirement planning",
    "timeHorizon": "15-20 years",
    "address": "Test Financial Planning Address",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560001",
    "panNumber": "CDEFG9012O"
}

try:
    response = requests.post(f"{BASE_URL}/financial-planning", json=financial_planning_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Financial Planning Application Submitted!")
        print(f"  Application ID: {result['applicationId']}")
        print(f"  Client: {financial_planning_data['name']}")
        print(f"  Goal: {financial_planning_data['investmentGoal']}")
        print(f"  Risk Profile: {financial_planning_data['riskProfile']}")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Error: {str(e)}")

# Test: Get Applications by Service Type
print("\n4. Testing Get Applications by Service Type...")
try:
    for service_type in ["trading-demat", "bank-account", "financial-planning"]:
        response = requests.get(f"{BASE_URL}/applications?service_type={service_type}")
        if response.status_code == 200:
            result = response.json()
            print(f"✓ {service_type}: {result['total']} applications")
except Exception as e:
    print(f"✗ Error: {str(e)}")

print("\n" + "=" * 80)
print("Account & Financial Services API Testing Complete!".center(80))
print("=" * 80)
