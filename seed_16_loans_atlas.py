"""Delete all loans from MongoDB Atlas and seed only our 16 loans"""
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env
env_path = Path('cashper_backend/app/.env')
load_dotenv(env_path)

mongo_url = os.getenv('MONGO_URL', 'mongodb+srv://kumuyadav249_db_user:O0zb3rZlZXArZiSg@cluster0.mnzwn7m.mongodb.net/')
mongo_db = os.getenv('MONGO_DB', 'cashper_db')

try:
    print("Connecting to MongoDB Atlas...")
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['admin_loan_applications']
    
    print("\n" + "="*70)
    print("DELETING ALL EXISTING LOANS")
    print("="*70)
    
    before_count = col.count_documents({})
    print(f"Loans before cleanup: {before_count}")
    
    # Delete all documents
    result = col.delete_many({})
    print(f"Deleted: {result.deleted_count}")
    
    after_count = col.count_documents({})
    print(f"Loans after cleanup: {after_count}")
    
    print("\n" + "="*70)
    print("SEEDING 16 EXACT LOANS")
    print("="*70)
    
    # Define our 16 loans exactly
    loans = [
        # 2 Home Loans
        {
            "customer": "राज कुमार",
            "email": "raj.kumar@email.com",
            "phone": "9876543210",
            "type": "Home Loan",
            "amount": 2500000,
            "tenure": 180,
            "interestRate": 6.5,
            "purpose": "Home Purchase",
            "income": 75000,
            "cibilScore": 750,
            "status": "Pending",
            "documents": ["aadhar.pdf", "income_proof.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "प्रिया शर्मा",
            "email": "priya.sharma@email.com",
            "phone": "9876543211",
            "type": "Home Loan",
            "amount": 3500000,
            "tenure": 240,
            "interestRate": 6.8,
            "purpose": "Home Extension",
            "income": 95000,
            "cibilScore": 760,
            "status": "Pending",
            "documents": ["pan.pdf", "bank_statement.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        # 7 Personal Loans
        {
            "customer": "अमित पटेल",
            "email": "amit.patel@email.com",
            "phone": "9876543212",
            "type": "Personal Loan",
            "amount": 100000,
            "tenure": 12,
            "interestRate": 12.5,
            "purpose": "Medical Emergency",
            "income": 35000,
            "cibilScore": 700,
            "status": "Pending",
            "documents": ["id_proof.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "विजय सिंह",
            "email": "vijay.singh@email.com",
            "phone": "9876543213",
            "type": "Personal Loan",
            "amount": 150000,
            "tenure": 24,
            "interestRate": 11.8,
            "purpose": "Wedding Expenses",
            "income": 45000,
            "cibilScore": 720,
            "status": "Pending",
            "documents": ["salary_slip.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "नीता देसाई",
            "email": "neeta.desai@email.com",
            "phone": "9876543214",
            "type": "Personal Loan",
            "amount": 200000,
            "tenure": 36,
            "interestRate": 11.2,
            "purpose": "Education Loan",
            "income": 55000,
            "cibilScore": 740,
            "status": "Pending",
            "documents": ["aadhaar.pdf", "bank_statement.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "रोहित वर्मा",
            "email": "rohit.verma@email.com",
            "phone": "9876543215",
            "type": "Personal Loan",
            "amount": 175000,
            "tenure": 24,
            "interestRate": 12.0,
            "purpose": "Car Purchase",
            "income": 50000,
            "cibilScore": 710,
            "status": "Pending",
            "documents": ["pancard.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "सुनीता भारद्वाज",
            "email": "sunita.bharadwaj@email.com",
            "phone": "9876543216",
            "type": "Personal Loan",
            "amount": 250000,
            "tenure": 48,
            "interestRate": 10.8,
            "purpose": "Business Expansion",
            "income": 65000,
            "cibilScore": 750,
            "status": "Pending",
            "documents": ["business_license.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "राकेश कुलकर्णी",
            "email": "rakesh.kulkarni@email.com",
            "phone": "9876543217",
            "type": "Personal Loan",
            "amount": 120000,
            "tenure": 18,
            "interestRate": 12.3,
            "purpose": "Debt Consolidation",
            "income": 42000,
            "cibilScore": 690,
            "status": "Pending",
            "documents": ["electricity_bill.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        # 5 Business Loans
        {
            "customer": "संजय त्रिपाठी",
            "email": "sanjay.tripathi@email.com",
            "phone": "9876543218",
            "type": "Business Loan",
            "amount": 600000,
            "tenure": 60,
            "interestRate": 10.5,
            "purpose": "Retail Shop Setup",
            "income": 150000,
            "cibilScore": 760,
            "status": "Pending",
            "documents": ["gst_certificate.pdf", "business_plan.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "मीरा अग्रवाल",
            "email": "mira.agarwal@email.com",
            "phone": "9876543219",
            "type": "Business Loan",
            "amount": 900000,
            "tenure": 84,
            "interestRate": 10.2,
            "purpose": "Manufacturing Unit",
            "income": 200000,
            "cibilScore": 770,
            "status": "Pending",
            "documents": ["factory_license.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "हरिश महाजन",
            "email": "harish.mahajan@email.com",
            "phone": "9876543220",
            "type": "Business Loan",
            "amount": 1200000,
            "tenure": 72,
            "interestRate": 9.8,
            "purpose": "Export Business",
            "income": 250000,
            "cibilScore": 780,
            "status": "Pending",
            "documents": ["export_license.pdf", "bank_reference.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "दीप्ति चौधरी",
            "email": "deepti.chaudhary@email.com",
            "phone": "9876543221",
            "type": "Business Loan",
            "amount": 800000,
            "tenure": 48,
            "interestRate": 10.0,
            "purpose": "IT Services Startup",
            "income": 180000,
            "cibilScore": 750,
            "status": "Pending",
            "documents": ["incorporation_cert.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "विक्रम गुप्ता",
            "email": "vikram.gupta@email.com",
            "phone": "9876543222",
            "type": "Business Loan",
            "amount": 1500000,
            "tenure": 96,
            "interestRate": 9.5,
            "purpose": "Hotel & Restaurant",
            "income": 300000,
            "cibilScore": 790,
            "status": "Pending",
            "documents": ["food_license.pdf", "financial_statements.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        # 2 Short-term Loans
        {
            "customer": "निशा खन्ना",
            "email": "nisha.khanna@email.com",
            "phone": "9876543223",
            "type": "Short-term Loan",
            "amount": 50000,
            "tenure": 6,
            "interestRate": 15.0,
            "purpose": "Emergency Funds",
            "income": 40000,
            "cibilScore": 680,
            "status": "Pending",
            "documents": ["recent_payslip.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "अनिल मिश्रा",
            "email": "anil.mishra@email.com",
            "phone": "9876543224",
            "type": "Short-term Loan",
            "amount": 75000,
            "tenure": 3,
            "interestRate": 16.5,
            "purpose": "Quick Cash Need",
            "income": 48000,
            "cibilScore": 700,
            "status": "Pending",
            "documents": ["identity_proof.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
    ]
    
    # Insert loans
    result = col.insert_many(loans)
    print(f"\nInserted {len(result.inserted_ids)} loans")
    
    # Verify counts
    print("\n" + "="*70)
    print("VERIFICATION")
    print("="*70)
    total = col.count_documents({})
    home = col.count_documents({"type": "Home Loan"})
    personal = col.count_documents({"type": "Personal Loan"})
    business = col.count_documents({"type": "Business Loan"})
    short_term = col.count_documents({"type": "Short-term Loan"})
    
    print(f"Total loans: {total}")
    print(f"  ✓ Home Loan: {home}")
    print(f"  ✓ Personal Loan: {personal}")
    print(f"  ✓ Business Loan: {business}")
    print(f"  ✓ Short-term Loan: {short_term}")
    
    if total == 16 and home == 2 and personal == 7 and business == 5 and short_term == 2:
        print("\n✅ SUCCESS! Database has exactly 16 loans with correct distribution")
    else:
        print("\n❌ ERROR: Loan counts don't match expected values")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
