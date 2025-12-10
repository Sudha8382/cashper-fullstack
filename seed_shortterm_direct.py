"""
Direct MongoDB seeding for short-term loans
This script directly inserts loan data into MongoDB with type "Short-term Loan"
"""

from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["payloan"]
    collection = db["admin_loan_applications"]
    
    print("Connected to MongoDB successfully!")
    print(f"Database: payloan")
    print(f"Collection: admin_loan_applications")
    
    # Short-term loans data
    short_term_loans = [
        {
            "customer": "Rajesh Kumar",
            "email": "rajesh.kumar@gmail.com",
            "phone": "9876543210",
            "type": "Short-term Loan",
            "amount": 50000,
            "tenure": 6,
            "interestRate": 18.0,
            "purpose": "Emergency cash",
            "income": "₹40,000/month",
            "cibilScore": 680,
            "status": "Pending",
            "documents": ["aadhaar_card.pdf", "pan_card.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "Priya Sharma",
            "email": "priya.sharma@gmail.com",
            "phone": "9876543211",
            "type": "Short-term Loan",
            "amount": 75000,
            "tenure": 9,
            "interestRate": 17.5,
            "purpose": "Quick business need",
            "income": "₹60,000/month",
            "cibilScore": 700,
            "status": "Pending",
            "documents": ["aadhaar_card.pdf", "pan_card.pdf", "salary_slips.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
    ]
    
    print("\nInserting 2 Short-term Loans...")
    result = collection.insert_many(short_term_loans)
    
    print(f"✅ Successfully inserted {len(result.inserted_ids)} short-term loans")
    print(f"IDs: {result.inserted_ids}")
    
    # Show summary
    print("\n" + "="*80)
    print("CURRENT LOAN COUNTS BY TYPE:")
    print("="*80)
    
    loan_types = ["Home Loan", "Personal Loan", "Business Loan", "Short-term Loan", "Education Loan", "Vehicle Loan"]
    
    for loan_type in loan_types:
        count = collection.count_documents({"type": loan_type})
        print(f"{loan_type}: {count}")
    
    total = collection.count_documents({})
    print(f"\nTOTAL LOANS: {total}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("\nMake sure MongoDB is running on localhost:27017")
