"""
Assign sample data to current logged-in user for dashboard testing
"""
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('cashper_backend/.env')

# Get MongoDB connection string
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'cashper')

def assign_test_data_to_user(user_email):
    """Assign some test loan/insurance data to specified user"""
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        
        # Find user by email
        user = db.users.find_one({"email": user_email})
        
        if not user:
            print(f"❌ User with email '{user_email}' not found")
            return
        
        user_id = str(user["_id"])
        print(f"✅ Found user: {user.get('name', 'Unknown')} ({user_email})")
        print(f"   User ID: {user_id}")
        
        # Check if user already has data
        existing_loans = (
            db.personal_loan_get_in_touch.count_documents({"userId": user_id}) +
            db.home_loan_get_in_touch.count_documents({"userId": user_id}) +
            db.business_loan_get_in_touch.count_documents({"userId": user_id}) +
            db.short_term_loan_get_in_touch.count_documents({"userId": user_id})
        )
        
        existing_insurance = (
            db.health_insurance_inquiries.count_documents({"userId": user_id}) +
            db.motor_insurance_inquiries.count_documents({"userId": user_id}) +
            db.term_insurance_inquiries.count_documents({"userId": user_id})
        )
        
        existing_investments = (
            db.sip_inquiries.count_documents({"userId": user_id}) +
            db.mutual_fund_inquiries.count_documents({"userId": user_id})
        )
        
        print(f"\n📊 Current data for this user:")
        print(f"   Loans: {existing_loans}")
        print(f"   Insurance: {existing_insurance}")
        print(f"   Investments: {existing_investments}")
        
        if existing_loans > 0 or existing_insurance > 0 or existing_investments > 0:
            response = input("\n⚠️  User already has data. Do you want to add more? (y/n): ")
            if response.lower() != 'y':
                print("❌ Cancelled")
                return
        
        # Add sample data
        print("\n🔄 Adding sample data...")
        
        # Add 2 personal loans
        personal_loans_data = [
            {
                "userId": user_id,
                "fullName": user.get("name", "Test User"),
                "email": user_email,
                "phone": user.get("phone", "9876543210"),
                "loanAmount": "500000",
                "employmentType": "Salaried",
                "monthlyIncome": "50000",
                "purpose": "Personal expenses",
                "status": "pending",
                "createdAt": datetime.utcnow()
            },
            {
                "userId": user_id,
                "fullName": user.get("name", "Test User"),
                "email": user_email,
                "phone": user.get("phone", "9876543210"),
                "loanAmount": "300000",
                "employmentType": "Self-employed",
                "monthlyIncome": "60000",
                "purpose": "Business expansion",
                "status": "confirmed",
                "createdAt": datetime.utcnow()
            }
        ]
        db.personal_loan_get_in_touch.insert_many(personal_loans_data)
        print("   ✅ Added 2 personal loans")
        
        # Add 1 home loan
        home_loan_data = {
            "userId": user_id,
            "fullName": user.get("name", "Test User"),
            "email": user_email,
            "phone": user.get("phone", "9876543210"),
            "loanAmount": "5000000",
            "propertyValue": "7000000",
            "employmentType": "Salaried",
            "monthlyIncome": "100000",
            "status": "pending",
            "createdAt": datetime.utcnow()
        }
        db.home_loan_get_in_touch.insert_one(home_loan_data)
        print("   ✅ Added 1 home loan")
        
        # Add 2 health insurance
        health_insurance_data = [
            {
                "userId": user_id,
                "fullName": user.get("name", "Test User"),
                "email": user_email,
                "phone": user.get("phone", "9876543210"),
                "coverageAmount": "500000",
                "familyMembers": "4",
                "status": "pending",
                "createdAt": datetime.utcnow()
            },
            {
                "userId": user_id,
                "fullName": user.get("name", "Test User"),
                "email": user_email,
                "phone": user.get("phone", "9876543210"),
                "coverageAmount": "1000000",
                "familyMembers": "2",
                "status": "confirmed",
                "createdAt": datetime.utcnow()
            }
        ]
        db.health_insurance_inquiries.insert_many(health_insurance_data)
        print("   ✅ Added 2 health insurance inquiries")
        
        # Add 1 motor insurance
        motor_insurance_data = {
            "userId": user_id,
            "fullName": user.get("name", "Test User"),
            "email": user_email,
            "phone": user.get("phone", "9876543210"),
            "vehicleType": "Four Wheeler",
            "vehicleNumber": "MH12AB1234",
            "status": "pending",
            "createdAt": datetime.utcnow()
        }
        db.motor_insurance_inquiries.insert_one(motor_insurance_data)
        print("   ✅ Added 1 motor insurance inquiry")
        
        # Add 2 SIP investments
        sip_data = [
            {
                "userId": user_id,
                "fullName": user.get("name", "Test User"),
                "email": user_email,
                "phone": user.get("phone", "9876543210"),
                "monthlyInvestment": "5000",
                "investmentPeriod": "10 years",
                "status": "pending",
                "createdAt": datetime.utcnow()
            },
            {
                "userId": user_id,
                "fullName": user.get("name", "Test User"),
                "email": user_email,
                "phone": user.get("phone", "9876543210"),
                "monthlyInvestment": "10000",
                "investmentPeriod": "5 years",
                "status": "confirmed",
                "createdAt": datetime.utcnow()
            }
        ]
        db.sip_inquiries.insert_many(sip_data)
        print("   ✅ Added 2 SIP investments")
        
        # Add some documents
        doc_data = {
            "userId": user_id,
            "fileName": "aadhar_card.pdf",
            "fileType": "application/pdf",
            "fileSize": 1024000,
            "filePath": "/uploads/documents/aadhar_card.pdf",
            "uploadedAt": datetime.utcnow()
        }
        db.documents.insert_one(doc_data)
        
        doc_data2 = {
            "userId": user_id,
            "fileName": "pan_card.pdf",
            "fileType": "application/pdf",
            "fileSize": 512000,
            "filePath": "/uploads/documents/pan_card.pdf",
            "uploadedAt": datetime.utcnow()
        }
        db.documents.insert_one(doc_data2)
        print("   ✅ Added 2 documents")
        
        print("\n✅ Sample data added successfully!")
        print("\n📊 New totals for this user:")
        print(f"   Loans: {existing_loans + 3}")
        print(f"   Insurance: {existing_insurance + 3}")
        print(f"   Investments: {existing_investments + 2}")
        print(f"   Documents: 2")
        
        print("\n🔄 Please refresh your dashboard to see the updated data!")
        
        client.close()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("=" * 80)
    print("ASSIGN SAMPLE DASHBOARD DATA TO USER")
    print("=" * 80)
    
    email = input("\nEnter user email: ").strip()
    
    if not email:
        print("❌ Email cannot be empty")
    else:
        assign_test_data_to_user(email)
