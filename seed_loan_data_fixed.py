"""
Seed loan applications with proper loan types for admin panel
This script creates sample data with exact counts:
- 2 Home Loans
- 7 Personal Loans
- 5 Business Loans
- 2 Short-term Loans
"""

import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8000/api/admin/loan-management"

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

# Define loan configurations
LOAN_CONFIGS = {
    "Home Loan": [
        {"customer_idx": 0, "amount": 2500000, "tenure": 240, "rate": 8.5, "purpose": "Purchase new apartment", "income": "₹100,000/month", "cibil": 750},
        {"customer_idx": 1, "amount": 3500000, "tenure": 180, "rate": 8.75, "purpose": "Home construction", "income": "₹120,000/month", "cibil": 780},
    ],
    "Personal Loan": [
        {"customer_idx": 2, "amount": 200000, "tenure": 36, "rate": 12.5, "purpose": "Wedding expenses", "income": "₹50,000/month", "cibil": 720},
        {"customer_idx": 3, "amount": 150000, "tenure": 24, "rate": 13.0, "purpose": "Medical emergency", "income": "₹45,000/month", "cibil": 700},
        {"customer_idx": 4, "amount": 300000, "tenure": 48, "rate": 12.0, "purpose": "Home renovation", "income": "₹60,000/month", "cibil": 760},
        {"customer_idx": 5, "amount": 100000, "tenure": 12, "rate": 14.0, "purpose": "Debt consolidation", "income": "₹35,000/month", "cibil": 680},
        {"customer_idx": 6, "amount": 250000, "tenure": 36, "rate": 11.5, "purpose": "Travel expenses", "income": "₹55,000/month", "cibil": 740},
        {"customer_idx": 0, "amount": 180000, "tenure": 30, "rate": 12.75, "purpose": "Education fees", "income": "₹48,000/month", "cibil": 710},
        {"customer_idx": 1, "amount": 220000, "tenure": 42, "rate": 12.25, "purpose": "Business investment", "income": "₹58,000/month", "cibil": 730},
    ],
    "Business Loan": [
        {"customer_idx": 2, "amount": 1000000, "tenure": 60, "rate": 15.0, "purpose": "Business expansion", "income": "₹80,000/month", "cibil": 750},
        {"customer_idx": 3, "amount": 800000, "tenure": 48, "rate": 15.5, "purpose": "Working capital", "income": "₹70,000/month", "cibil": 720},
        {"customer_idx": 4, "amount": 1500000, "tenure": 72, "rate": 14.5, "purpose": "Equipment purchase", "income": "₹100,000/month", "cibil": 770},
        {"customer_idx": 5, "amount": 600000, "tenure": 36, "rate": 16.0, "purpose": "Inventory financing", "income": "₹55,000/month", "cibil": 700},
        {"customer_idx": 6, "amount": 1200000, "tenure": 60, "rate": 15.25, "purpose": "New business setup", "income": "₹85,000/month", "cibil": 740},
    ],
    "Short-term Loan": [
        {"customer_idx": 0, "amount": 50000, "tenure": 6, "rate": 18.0, "purpose": "Emergency cash", "income": "₹40,000/month", "cibil": 680},
        {"customer_idx": 1, "amount": 75000, "tenure": 9, "rate": 17.5, "purpose": "Quick business need", "income": "₹60,000/month", "cibil": 700},
    ]
}

def create_loan_application(loan_type, config):
    """Create a loan application with given configuration"""
    customer = CUSTOMERS[config["customer_idx"]]
    
    application = {
        "customer": customer["name"],
        "email": customer["email"],
        "phone": customer["phone"],
        "type": loan_type,
        "amount": config["amount"],
        "tenure": config["tenure"],
        "interestRate": config["rate"],
        "purpose": config["purpose"],
        "income": config["income"],
        "cibilScore": config["cibil"],
        "documents": [
            "aadhaar_card.pdf",
            "pan_card.pdf",
            "salary_slips.pdf",
            "bank_statements.pdf"
        ]
    }
    
    return application


def seed_loans():
    """Seed all loan applications"""
    total_created = 0
    
    print("\n" + "=" * 80)
    print("SEEDING LOAN APPLICATIONS")
    print("=" * 80)
    
    for loan_type, configs in LOAN_CONFIGS.items():
        print(f"\n--- Creating {len(configs)} {loan_type}(s) ---")
        
        for i, config in enumerate(configs, 1):
            try:
                application = create_loan_application(loan_type, config)
                
                print(f"\n[{i}/{len(configs)}] {application['customer']}")
                print(f"  Type: {loan_type}")
                print(f"  Amount: ₹{application['amount']:,}")
                print(f"  Tenure: {application['tenure']} months")
                print(f"  Rate: {application['interestRate']}%")
                print(f"  CIBIL: {application['cibilScore']}")
                
                response = requests.post(
                    f"{BASE_URL}/applications",
                    json=application,
                    timeout=10
                )
                
                if response.status_code == 201:
                    data = response.json()
                    print(f"  [OK] Created successfully")
                    total_created += 1
                else:
                    print(f"  [FAIL] Status {response.status_code}")
                    try:
                        print(f"     Error: {response.json()}")
                    except:
                        print(f"     {response.text}")
                    
            except Exception as e:
                print(f"  [FAIL] Error: {str(e)}")
    
    print("\n" + "=" * 80)
    print(f"SUCCESSFULLY CREATED {total_created} LOAN APPLICATIONS")
    print("=" * 80)
    print(f"\nSummary:")
    print(f"  - Home Loans: 2")
    print(f"  - Personal Loans: 7")
    print(f"  - Business Loans: 5")
    print(f"  - Short-term Loans: 2")
    print(f"  - TOTAL: 16 applications")
    print("\n")


if __name__ == "__main__":
    try:
        seed_loans()
    except KeyboardInterrupt:
        print("\n\nSeeding interrupted by user")
    except Exception as e:
        print(f"\n\nError during seeding: {str(e)}")
