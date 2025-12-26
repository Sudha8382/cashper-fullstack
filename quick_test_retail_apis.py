"""Quick test for retail services APIs"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("\n" + "="*80)
print("TESTING RETAIL SERVICES APIs")
print("="*80 + "\n")

# Test 1: ITR Filing
print("1. Testing ITR Filing Service...")
data = {
    "fullName": "Rajesh Kumar",
    "email": "rajesh@test.com",
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
    "address": "A-101, Green Valley, MG Road",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001"
}

try:
    r = requests.post(f"{BASE_URL}/api/retail-services/itr-filing", json=data, timeout=5)
    if r.status_code == 200:
        result = r.json()
        print(f"   ✓ Success - Application ID: {result.get('applicationId')}")
        itr_id = result.get('applicationId')
    else:
        print(f"   ✗ Failed - Status: {r.status_code}")
        itr_id = None
except Exception as e:
    print(f"   ✗ Error: {str(e)}")
    itr_id = None

# Test 2: Individual PAN
print("\n2. Testing Individual PAN Application...")
data = {
    "fullName": "Priya Sharma",
    "fatherName": "Ramesh Sharma",
    "dateOfBirth": "1992-03-20",
    "email": "priya@test.com",
    "phone": "9876543211",
    "aadhaarNumber": "123456789013",
    "gender": "female",
    "category": "individual",
    "applicationType": "new",
    "address": "B-202, Sunshine Towers",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400050"
}

try:
    r = requests.post(f"{BASE_URL}/api/retail-services/individual-pan", json=data, timeout=5)
    if r.status_code == 200:
        result = r.json()
        print(f"   ✓ Success - Application ID: {result.get('applicationId')}")
    else:
        print(f"   ✗ Failed - Status: {r.status_code}")
except Exception as e:
    print(f"   ✗ Error: {str(e)}")

# Test 3: PF Withdrawal
print("\n3. Testing PF Withdrawal Application...")
data = {
    "fullName": "Amit Patel",
    "email": "amit@test.com",
    "phone": "9876543212",
    "panNumber": "BCDEF2345G",
    "uanNumber": "100123456789",
    "employerName": "Tech Solutions Ltd",
    "withdrawalType": "partial",
    "withdrawalAmount": 150000,
    "withdrawalReason": "Medical emergency requiring immediate funds for treatment",
    "lastWorkingDate": "2024-01-31",
    "address": "C-303, Royal Heights",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560001"
}

try:
    r = requests.post(f"{BASE_URL}/api/retail-services/pf-withdrawal", json=data, timeout=5)
    if r.status_code == 200:
        result = r.json()
        print(f"   ✓ Success - Application ID: {result.get('applicationId')}")
    else:
        print(f"   ✗ Failed - Status: {r.status_code}")
except Exception as e:
    print(f"   ✗ Error: {str(e)}")

# Test 4: Bank Account
print("\n4. Testing Bank Account Application...")
data = {
    "fullName": "Divya Krishnan",
    "email": "divya@test.com",
    "phone": "9876543213",
    "panNumber": "CDEFG3456H",
    "aadhaarNumber": "123456789014",
    "dateOfBirth": "1990-11-25",
    "accountType": "savings",
    "bankPreference": "HDFC Bank",
    "accountVariant": "regular-savings",
    "monthlyIncome": "75000",
    "occupationType": "salaried",
    "nomineeRequired": True,
    "nomineeName": "Arvind Krishnan",
    "nomineeRelation": "Father",
    "address": "D-404, Palm Grove",
    "city": "Chennai",
    "state": "Tamil Nadu",
    "pincode": "600040",
    "residenceType": "owned"
}

try:
    r = requests.post(f"{BASE_URL}/api/retail-services/bank-account", json=data, timeout=5)
    if r.status_code == 200:
        result = r.json()
        print(f"   ✓ Success - Application ID: {result.get('applicationId')}")
    else:
        print(f"   ✗ Failed - Status: {r.status_code}")
except Exception as e:
    print(f"   ✗ Error: {str(e)}")

# Test 5: Trading & Demat
print("\n5. Testing Trading & Demat Account...")
data = {
    "fullName": "Karan Malhotra",
    "email": "karan@test.com",
    "phone": "9876543214",
    "panNumber": "DEFGH4567I",
    "aadhaarNumber": "123456789015",
    "dateOfBirth": "1988-08-12",
    "accountType": "individual",
    "tradingSegments": ["equity", "derivatives"],
    "annualIncome": "1200000",
    "occupationType": "business",
    "experienceLevel": "intermediate",
    "address": "E-505, Trade Center",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400021",
    "bankName": "HDFC Bank",
    "accountNumber": "12345678901234",
    "ifscCode": "HDFC0001234"
}

try:
    r = requests.post(f"{BASE_URL}/api/retail-services/trading-demat", json=data, timeout=5)
    if r.status_code == 200:
        result = r.json()
        print(f"   ✓ Success - Application ID: {result.get('applicationId')}")
    else:
        print(f"   ✗ Failed - Status: {r.status_code}")
except Exception as e:
    print(f"   ✗ Error: {str(e)}")

# Test 6: Financial Planning
print("\n6. Testing Financial Planning Service...")
data = {
    "name": "Rohan Desai",
    "email": "rohan@test.com",
    "phone": "9876543215",
    "age": 32,
    "occupation": "Software Engineer",
    "annualIncome": "1500000",
    "existingInvestments": "Mutual Funds: ₹5L",
    "riskProfile": "moderate",
    "investmentGoal": "Retirement planning",
    "timeHorizon": "15-20 years",
    "address": "F-606, Tech Park",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560066",
    "panNumber": "EFGHI5678J"
}

try:
    r = requests.post(f"{BASE_URL}/api/retail-services/financial-planning", json=data, timeout=5)
    if r.status_code == 200:
        result = r.json()
        print(f"   ✓ Success - Application ID: {result.get('applicationId')}")
    else:
        print(f"   ✗ Failed - Status: {r.status_code}")
except Exception as e:
    print(f"   ✗ Error: {str(e)}")

# Test GET all applications
print("\n7. Testing GET All Applications...")
try:
    r = requests.get(f"{BASE_URL}/api/retail-services/applications", timeout=5)
    if r.status_code == 200:
        result = r.json()
        print(f"   ✓ Success - Total Applications: {result.get('total')}")
    else:
        print(f"   ✗ Failed - Status: {r.status_code}")
except Exception as e:
    print(f"   ✗ Error: {str(e)}")

# Test GET specific application
if itr_id:
    print(f"\n8. Testing GET Specific Application (ID: {itr_id})...")
    try:
        r = requests.get(f"{BASE_URL}/api/retail-services/itr-filing/{itr_id}", timeout=5)
        if r.status_code == 200:
            result = r.json()
            print(f"   ✓ Success - Retrieved: {result.get('applicantName')}")
        else:
            print(f"   ✗ Failed - Status: {r.status_code}")
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")

print("\n" + "="*80)
print("TESTING COMPLETE")
print("="*80 + "\n")
