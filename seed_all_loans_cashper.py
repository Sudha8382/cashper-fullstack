"""
Seed loan applications with proper loan types to cashper_db database
This script creates sample data with exact counts:
- 2 Home Loans
- 7 Personal Loans
- 5 Business Loans
- 2 Short-term Loans
"""

from pymongo import MongoClient
from datetime import datetime

# MongoDB connection to correct database
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["cashper_db"]  # Correct database name
    collection = db["admin_loan_applications"]
    
    # First clear existing data
    print("Clearing existing loan data...")
    result = collection.delete_many({})
    print(f"Deleted: {result.deleted_count} documents")
    
    # Sample customers
    CUSTOMERS = [
        {"name": "Rajesh Kumar", "email": "rajesh.kumar@gmail.com", "phone": "9876543210"},
        {"name": "Priya Sharma", "email": "priya.sharma@gmail.com", "phone": "9876543211"},
        {"name": "Amit Patel", "email": "amit.patel@gmail.com", "phone": "9876543212"},
        {"name": "Sneha Reddy", "email": "sneha.reddy@gmail.com", "phone": "9876543213"},
        {"name": "Vikram Singh", "email": "vikram.singh@gmail.com", "phone": "9876543214"},
        {"name": "Anita Desai", "email": "anita.desai@gmail.com", "phone": "9876543215"},
        {"name": "Rahul Mehta", "email": "rahul.mehta@gmail.com", "phone": "9876543216"},
    ]
    
    # Define all loans
    all_loans = []
    
    # Home Loans (2)
    all_loans.extend([
        {
            "customer": "Rajesh Kumar",
            "email": "rajesh.kumar@gmail.com",
            "phone": "9876543210",
            "type": "Home Loan",
            "amount": 2500000,
            "tenure": 240,
            "interestRate": 8.5,
            "purpose": "Purchase new apartment",
            "income": "Rs 100,000/month",
            "cibilScore": 750,
            "status": "Pending",
            "documents": ["aadhaar_card.pdf", "pan_card.pdf", "salary_slips.pdf", "bank_statements.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "customer": "Priya Sharma",
            "email": "priya.sharma@gmail.com",
            "phone": "9876543211",
            "type": "Home Loan",
            "amount": 3500000,
            "tenure": 180,
            "interestRate": 8.75,
            "purpose": "Home construction",
            "income": "Rs 120,000/month",
            "cibilScore": 780,
            "status": "Pending",
            "documents": ["aadhaar_card.pdf", "pan_card.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
    ])
    
    # Personal Loans (7)
    personal_data = [
        ("Amit Patel", "amit.patel@gmail.com", "9876543212", 200000, 36, 12.5, "Wedding expenses", "Rs 50,000/month", 720),
        ("Sneha Reddy", "sneha.reddy@gmail.com", "9876543213", 150000, 24, 13.0, "Medical emergency", "Rs 45,000/month", 700),
        ("Vikram Singh", "vikram.singh@gmail.com", "9876543214", 300000, 48, 12.0, "Home renovation", "Rs 60,000/month", 760),
        ("Anita Desai", "anita.desai@gmail.com", "9876543215", 100000, 12, 14.0, "Debt consolidation", "Rs 35,000/month", 680),
        ("Rahul Mehta", "rahul.mehta@gmail.com", "9876543216", 250000, 36, 11.5, "Travel expenses", "Rs 55,000/month", 740),
        ("Rajesh Kumar", "rajesh.kumar@gmail.com", "9876543210", 180000, 30, 12.75, "Education fees", "Rs 48,000/month", 710),
        ("Priya Sharma", "priya.sharma@gmail.com", "9876543211", 220000, 42, 12.25, "Business investment", "Rs 58,000/month", 730),
    ]
    
    for name, email, phone, amount, tenure, rate, purpose, income, cibil in personal_data:
        all_loans.append({
            "customer": name,
            "email": email,
            "phone": phone,
            "type": "Personal Loan",
            "amount": amount,
            "tenure": tenure,
            "interestRate": rate,
            "purpose": purpose,
            "income": income,
            "cibilScore": cibil,
            "status": "Pending",
            "documents": ["aadhaar_card.pdf", "pan_card.pdf", "salary_slips.pdf", "bank_statements.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        })
    
    # Business Loans (5)
    business_data = [
        ("Amit Patel", "amit.patel@gmail.com", "9876543212", 1000000, 60, 15.0, "Business expansion", "Rs 80,000/month", 750),
        ("Sneha Reddy", "sneha.reddy@gmail.com", "9876543213", 800000, 48, 15.5, "Working capital", "Rs 70,000/month", 720),
        ("Vikram Singh", "vikram.singh@gmail.com", "9876543214", 1500000, 72, 14.5, "Equipment purchase", "Rs 100,000/month", 770),
        ("Anita Desai", "anita.desai@gmail.com", "9876543215", 600000, 36, 16.0, "Inventory financing", "Rs 55,000/month", 700),
        ("Rahul Mehta", "rahul.mehta@gmail.com", "9876543216", 1200000, 60, 15.25, "New business setup", "Rs 85,000/month", 740),
    ]
    
    for name, email, phone, amount, tenure, rate, purpose, income, cibil in business_data:
        all_loans.append({
            "customer": name,
            "email": email,
            "phone": phone,
            "type": "Business Loan",
            "amount": amount,
            "tenure": tenure,
            "interestRate": rate,
            "purpose": purpose,
            "income": income,
            "cibilScore": cibil,
            "status": "Pending",
            "documents": ["aadhaar_card.pdf", "pan_card.pdf", "salary_slips.pdf", "bank_statements.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        })
    
    # Short-term Loans (2)
    all_loans.extend([
        {
            "customer": "Rajesh Kumar",
            "email": "rajesh.kumar@gmail.com",
            "phone": "9876543210",
            "type": "Short-term Loan",
            "amount": 50000,
            "tenure": 6,
            "interestRate": 18.0,
            "purpose": "Emergency cash",
            "income": "Rs 40,000/month",
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
            "income": "Rs 60,000/month",
            "cibilScore": 700,
            "status": "Pending",
            "documents": ["aadhaar_card.pdf", "pan_card.pdf", "salary_slips.pdf"],
            "appliedDate": datetime.now(),
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
    ])
    
    print(f"\nInserting {len(all_loans)} loans into cashper_db...")
    result = collection.insert_many(all_loans)
    print(f"[OK] Successfully inserted {len(result.inserted_ids)} loans")
    
    # Show summary
    print("\n" + "="*80)
    print("CURRENT LOAN COUNTS BY TYPE (in cashper_db):")
    print("="*80)
    
    loan_types = ["Home Loan", "Personal Loan", "Business Loan", "Short-term Loan"]
    
    total_loans = 0
    for loan_type in loan_types:
        count = collection.count_documents({"type": loan_type})
        total_loans += count
        print(f"{loan_type}: {count}")
    
    grand_total = collection.count_documents({})
    print(f"\nTOTAL LOANS: {grand_total}")
    
except Exception as e:
    import traceback
    print(f"Error: {str(e)}")
    traceback.print_exc()
    print("\nMake sure MongoDB is running on localhost:27017")
