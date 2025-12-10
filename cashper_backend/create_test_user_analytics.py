"""
Script to create a test user with sample data for testing dashboard analytics APIs
"""

import sys
import os
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson import ObjectId

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.utils.security import hash_password
from app.config import mongo_url, mongo_db

def create_test_user_with_data():
    """Create test user with sample loans, investments, and insurance data"""
    
    # Test user credentials
    TEST_EMAIL = "testuser@cashper.com"
    TEST_PASSWORD = "Test@123"
    TEST_NAME = "Test User"
    TEST_PHONE = "9876543210"
    
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_url)
        db = client[mongo_db]
        
        print("\n" + "="*60)
        print("CREATING TEST USER WITH SAMPLE DATA")
        print("="*60)
        
        # Check if test user exists
        existing_user = db.users.find_one({"email": TEST_EMAIL.lower()})
        
        if existing_user:
            user_id = str(existing_user['_id'])
            print(f"✅ Test user already exists: {TEST_EMAIL}")
            print(f"   User ID: {user_id}")
        else:
            # Create test user
            hashed_password = hash_password(TEST_PASSWORD)
            
            new_user = {
                "fullName": TEST_NAME,
                "name": TEST_NAME,
                "email": TEST_EMAIL.lower(),
                "phone": TEST_PHONE,
                "password": hashed_password,
                "hashedPassword": hashed_password,
                "role": "user",
                "isActive": True,
                "isVerified": True,
                "isEmailVerified": True,
                "isPhoneVerified": True,
                "createdAt": datetime.utcnow(),
                "updatedAt": datetime.utcnow(),
                "lastLogin": datetime.utcnow()
            }
            
            result = db.users.insert_one(new_user)
            user_id = str(result.inserted_id)
            print(f"✅ Created test user: {TEST_EMAIL}")
            print(f"   User ID: {user_id}")
            print(f"   Password: {TEST_PASSWORD}")
        
        # Create sample data for last 6 months
        print("\n📊 Creating sample financial data...")
        
        # Generate dates for last 6 months
        months_data = []
        current = datetime.utcnow()
        for i in range(6):
            month_date = current - timedelta(days=30 * i)
            months_data.insert(0, month_date)
        
        # Clear existing test data for this user
        db.personal_loans.delete_many({"userId": user_id})
        db.home_loans.delete_many({"userId": user_id})
        db.business_loans.delete_many({"userId": user_id})
        db.short_term_loans.delete_many({"userId": user_id})
        db.mutual_fund_inquiries.delete_many({"userId": user_id})
        db.sip_inquiries.delete_many({"userId": user_id})
        db.health_insurance_inquiries.delete_many({"userId": user_id})
        db.motor_insurance_inquiries.delete_many({"userId": user_id})
        db.term_insurance_inquiries.delete_many({"userId": user_id})
        
        statuses = ["Approved", "Pending", "Under Review", "Rejected"]
        
        # Create personal loans
        print("   Creating personal loans...")
        loan_count = 0
        for i, month_date in enumerate(months_data):
            if i % 2 == 0:  # Create loan every other month
                loan = {
                    "userId": user_id,
                    "applicantName": TEST_NAME,
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "loanAmount": 50000 + (i * 10000),
                    "loanPurpose": "Personal expenses",
                    "employmentType": "Salaried",
                    "monthlyIncome": 60000,
                    "status": statuses[i % len(statuses)],
                    "createdAt": month_date,
                    "updatedAt": month_date
                }
                db.personal_loans.insert_one(loan)
                loan_count += 1
        print(f"   ✅ Created {loan_count} personal loans")
        
        # Create home loans
        print("   Creating home loans...")
        home_loan_count = 0
        if len(months_data) >= 3:
            home_loan = {
                "userId": user_id,
                "applicantName": TEST_NAME,
                "email": TEST_EMAIL,
                "phone": TEST_PHONE,
                "loanAmount": 2500000,
                "propertyValue": 3500000,
                "loanPurpose": "Purchase",
                "status": "Approved",
                "createdAt": months_data[2],
                "updatedAt": months_data[2]
            }
            db.home_loans.insert_one(home_loan)
            home_loan_count += 1
        print(f"   ✅ Created {home_loan_count} home loans")
        
        # Create business loans
        print("   Creating business loans...")
        business_loan_count = 0
        if len(months_data) >= 4:
            business_loan = {
                "userId": user_id,
                "applicantName": TEST_NAME,
                "email": TEST_EMAIL,
                "phone": TEST_PHONE,
                "loanAmount": 500000,
                "businessType": "Retail",
                "annualRevenue": 1200000,
                "status": "Under Review",
                "createdAt": months_data[3],
                "updatedAt": months_data[3]
            }
            db.business_loans.insert_one(business_loan)
            business_loan_count += 1
        print(f"   ✅ Created {business_loan_count} business loans")
        
        # Create mutual fund investments
        print("   Creating mutual fund investments...")
        mf_count = 0
        for i, month_date in enumerate(months_data):
            if i % 3 == 0:  # Create MF every third month
                mf = {
                    "userId": user_id,
                    "applicantName": TEST_NAME,
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "investmentAmount": 25000 + (i * 5000),
                    "investmentType": "Lump Sum",
                    "riskProfile": "Moderate",
                    "status": statuses[i % len(statuses)],
                    "createdAt": month_date,
                    "updatedAt": month_date
                }
                db.mutual_fund_inquiries.insert_one(mf)
                mf_count += 1
        print(f"   ✅ Created {mf_count} mutual fund investments")
        
        # Create SIP investments
        print("   Creating SIP investments...")
        sip_count = 0
        for i, month_date in enumerate(months_data):
            if i % 2 == 1:  # Create SIP alternating months
                sip = {
                    "userId": user_id,
                    "applicantName": TEST_NAME,
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "monthlyInvestment": 5000 + (i * 1000),
                    "sipDuration": 60,
                    "riskProfile": "Moderate",
                    "status": statuses[i % len(statuses)],
                    "createdAt": month_date,
                    "updatedAt": month_date
                }
                db.sip_inquiries.insert_one(sip)
                sip_count += 1
        print(f"   ✅ Created {sip_count} SIP investments")
        
        # Create health insurance
        print("   Creating health insurance policies...")
        health_count = 0
        for i, month_date in enumerate(months_data):
            if i % 3 == 1:
                health = {
                    "userId": user_id,
                    "applicantName": TEST_NAME,
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "coverageAmount": 500000 + (i * 100000),
                    "policyType": "Individual",
                    "status": statuses[i % len(statuses)],
                    "createdAt": month_date,
                    "updatedAt": month_date
                }
                db.health_insurance_inquiries.insert_one(health)
                health_count += 1
        print(f"   ✅ Created {health_count} health insurance policies")
        
        # Create motor insurance
        print("   Creating motor insurance policies...")
        motor_count = 0
        if len(months_data) >= 2:
            motor = {
                "userId": user_id,
                "applicantName": TEST_NAME,
                "email": TEST_EMAIL,
                "phone": TEST_PHONE,
                "vehicleValue": 800000,
                "vehicleType": "Four Wheeler",
                "status": "Approved",
                "createdAt": months_data[1],
                "updatedAt": months_data[1]
            }
            db.motor_insurance_inquiries.insert_one(motor)
            motor_count += 1
        print(f"   ✅ Created {motor_count} motor insurance policies")
        
        # Create term insurance
        print("   Creating term insurance policies...")
        term_count = 0
        if len(months_data) >= 1:
            term = {
                "userId": user_id,
                "applicantName": TEST_NAME,
                "email": TEST_EMAIL,
                "phone": TEST_PHONE,
                "coverageAmount": 10000000,
                "policyTerm": 20,
                "status": "Pending",
                "createdAt": months_data[0],
                "updatedAt": months_data[0]
            }
            db.term_insurance_inquiries.insert_one(term)
            term_count += 1
        print(f"   ✅ Created {term_count} term insurance policies")
        
        # Summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Test User: {TEST_EMAIL}")
        print(f"Password: {TEST_PASSWORD}")
        print(f"User ID: {user_id}")
        print(f"\nData Created:")
        print(f"   Loans: {loan_count + home_loan_count + business_loan_count}")
        print(f"   Investments: {mf_count + sip_count}")
        print(f"   Insurance: {health_count + motor_count + term_count}")
        print(f"\nYou can now use these credentials to test the dashboard APIs!")
        print("="*60 + "\n")
        
        return TEST_EMAIL, TEST_PASSWORD
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None, None


if __name__ == "__main__":
    create_test_user_with_data()
