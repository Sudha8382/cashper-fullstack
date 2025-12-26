from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client['cashper_db']

print('=== Current User ===')
user = db.users.find_one({"email": "sudha@gmail.com"})
if user:
    user_id = str(user.get("_id"))
    print(f'User ID: {user_id}')
    print(f'Email: {user.get("email")}')
    print(f'Is Admin: {user.get("isAdmin")}')
    
    print(f'\n=== User Loans Count ===')
    personal = db.personal_loans.count_documents({"userId": user_id})
    home = db.home_loans.count_documents({"userId": user_id})
    business = db.business_loans.count_documents({"userId": user_id})
    short_term = db.short_term_loans.count_documents({"userId": user_id})
    
    print(f'Personal Loans: {personal}')
    print(f'Home Loans: {home}')
    print(f'Business Loans: {business}')
    print(f'Short Term Loans: {short_term}')
    
    if short_term > 0:
        print(f'\n=== Short Term Loan Details ===')
        for loan in db.short_term_loans.find({"userId": user_id}):
            print(f'ID: {loan.get("_id")}')
            print(f'Name: {loan.get("fullName")}')
            print(f'Email: {loan.get("email")}')
            print(f'Amount: {loan.get("loanAmount")}')
            print(f'Status: {loan.get("status")}')
            print(f'Created: {loan.get("createdAt")}')
    else:
        print('\n❌ No Short Term Loans found for this user')
        print('\nCreating a test loan...')
        from datetime import datetime
        
        test_loan = {
            "fullName": "Sudha Yadav",
            "email": "sudha@gmail.com",
            "phone": "9876543210",
            "relativeName": "Test Relative",
            "relativeRelation": "brother",
            "relativePhone": "9876543211",
            "loanAmount": "75000",
            "purpose": "emergency",
            "employment": "salaried",
            "monthlyIncome": "45000",
            "companyName": "Test Company",
            "workExperience": "5",
            "creditScore": "750",
            "panNumber": "ABCDE1234F",
            "aadharNumber": "123456789012",
            "address": "Test Address",
            "city": "Test City",
            "state": "Test State",
            "pincode": "123456",
            "aadhar": "/uploads/test_aadhar.png",
            "pan": "/uploads/test_pan.png",
            "bankStatement": "/uploads/test_bank.pdf",
            "salarySlip": "/uploads/test_salary.pdf",
            "photo": "/uploads/test_photo.png",
            "userId": user_id,
            "application_id": f"STL-TEST-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "status": "pending",
            "createdAt": datetime.now()
        }
        
        result = db.short_term_loans.insert_one(test_loan)
        print(f'✅ Test loan created with ID: {result.inserted_id}')
