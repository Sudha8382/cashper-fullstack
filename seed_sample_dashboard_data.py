"""
Seed sample data for comprehensive testing
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

# Login credentials
TEST_USER = {
    "email": "insurance.test@example.com",
    "password": "Test@12345"
}

ACCESS_TOKEN = None

class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def get_auth_headers():
    """Get authorization headers"""
    return {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }


def login():
    """Login and get access token"""
    global ACCESS_TOKEN
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/auth/login",
            json=TEST_USER
        )
        
        if response.status_code == 200:
            data = response.json()
            ACCESS_TOKEN = data.get("access_token")
            print(f"{Colors.OKGREEN}✓ Logged in successfully{Colors.ENDC}")
            return True
        else:
            print(f"{Colors.FAIL}✗ Login failed: {response.text}{Colors.ENDC}")
            return False
            
    except Exception as e:
        print(f"{Colors.FAIL}✗ Login error: {str(e)}{Colors.ENDC}")
        return False


def create_sample_loans():
    """Create sample loans"""
    print(f"\n{Colors.BOLD}Creating sample loans...{Colors.ENDC}")
    
    loans = [
        {"loanType": "Personal Loan", "loanAmount": 500000, "interestRate": 12.5, "tenureMonths": 36},
        {"loanType": "Home Loan", "loanAmount": 2500000, "interestRate": 8.5, "tenureMonths": 240},
        {"loanType": "Business Loan", "loanAmount": 1000000, "interestRate": 11.0, "tenureMonths": 60}
    ]
    
    created = 0
    for loan in loans:
        try:
            response = requests.post(
                f"{BASE_URL}/api/loan-management/create-loan",
                headers=get_auth_headers(),
                json=loan
            )
            
            if response.status_code == 201:
                print(f"{Colors.OKGREEN}✓ Created {loan['loanType']}{Colors.ENDC}")
                created += 1
            else:
                print(f"{Colors.WARNING}⊘ {loan['loanType']}: {response.text}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}✗ Error creating {loan['loanType']}: {str(e)}{Colors.ENDC}")
    
    print(f"Created {created}/{len(loans)} loans")


def create_sample_insurance():
    """Create sample insurance applications"""
    print(f"\n{Colors.BOLD}Creating sample insurance applications...{Colors.ENDC}")
    
    # Health Insurance
    health_data = {
        "name": "Test User",
        "email": TEST_USER["email"],
        "phone": "9876543210",
        "age": 30,
        "familySize": 4,
        "coverageAmount": "10 Lakhs"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/health-insurance/contact/submit",
            json=health_data
        )
        
        if response.status_code == 201:
            print(f"{Colors.OKGREEN}✓ Created Health Insurance application{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}⊘ Health Insurance: {response.text}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}✗ Error creating Health Insurance: {str(e)}{Colors.ENDC}")
    
    # Motor Insurance
    motor_data = {
        "name": "Test User",
        "email": TEST_USER["email"],
        "phone": "9876543210",
        "age": 30,
        "vehicleType": "Car",
        "vehicleModel": "Honda City 2020",
        "registrationNumber": "DL01AB1234"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/motor-insurance/contact/submit",
            json=motor_data
        )
        
        if response.status_code == 201:
            print(f"{Colors.OKGREEN}✓ Created Motor Insurance application{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}⊘ Motor Insurance: {response.text}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}✗ Error creating Motor Insurance: {str(e)}{Colors.ENDC}")
    
    # Term Insurance
    term_data = {
        "name": "Test User",
        "email": TEST_USER["email"],
        "phone": "9876543210",
        "age": 30,
        "coverage": "50 Lakhs",
        "term": 20
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/term-insurance/contact/submit",
            json=term_data
        )
        
        if response.status_code == 201:
            print(f"{Colors.OKGREEN}✓ Created Term Insurance application{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}⊘ Term Insurance: {response.text}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}✗ Error creating Term Insurance: {str(e)}{Colors.ENDC}")


def create_sample_investments():
    """Create sample investment applications"""
    print(f"\n{Colors.BOLD}Creating sample investment applications...{Colors.ENDC}")
    
    # SIP Investment
    sip_data = {
        "name": "Test User",
        "email": TEST_USER["email"],
        "phone": "9876543210",
        "investmentAmount": 5000,
        "duration": "10 years"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/sip/contact/submit",
            json=sip_data
        )
        
        if response.status_code == 201:
            print(f"{Colors.OKGREEN}✓ Created SIP Investment application{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}⊘ SIP Investment: {response.text}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}✗ Error creating SIP Investment: {str(e)}{Colors.ENDC}")
    
    # Mutual Fund Investment
    mf_data = {
        "name": "Test User",
        "email": TEST_USER["email"],
        "phone": "9876543210",
        "investmentAmount": 100000,
        "investmentGoal": "Wealth Creation"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/api/mutual-funds/contact/submit",
            json=mf_data
        )
        
        if response.status_code == 201:
            print(f"{Colors.OKGREEN}✓ Created Mutual Fund Investment application{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}⊘ Mutual Fund Investment: {response.text}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}✗ Error creating Mutual Fund Investment: {str(e)}{Colors.ENDC}")


def main():
    """Main function"""
    print(f"\n{Colors.BOLD}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.BOLD}SEEDING SAMPLE DATA FOR TESTING{Colors.ENDC}")
    print(f"{Colors.BOLD}{'=' * 60}{Colors.ENDC}")
    
    # Login first
    if not login():
        print(f"\n{Colors.FAIL}Authentication failed. Cannot seed data.{Colors.ENDC}")
        return
    
    # Create sample data
    create_sample_loans()
    create_sample_insurance()
    create_sample_investments()
    
    print(f"\n{Colors.BOLD}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✓ Sample data seeding completed!{Colors.ENDC}")
    print(f"{Colors.BOLD}{'=' * 60}{Colors.ENDC}\n")


if __name__ == "__main__":
    main()
