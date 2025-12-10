"""
Seed sample loan applications for admin panel testing
Creates realistic loan application data with different statuses
"""

import requests
import random
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8000/api/admin/loan-management"

# Sample data
CUSTOMERS = [
    {"name": "Rajesh Kumar", "email": "rajesh.kumar@gmail.com", "phone": "9876543210"},
    {"name": "Priya Sharma", "email": "priya.sharma@gmail.com", "phone": "9876543211"},
    {"name": "Amit Patel", "email": "amit.patel@gmail.com", "phone": "9876543212"},
    {"name": "Sneha Reddy", "email": "sneha.reddy@gmail.com", "phone": "9876543213"},
    {"name": "Vikram Singh", "email": "vikram.Singh@gmail.com", "phone": "9876543214"},
    {"name": "Anita Desai", "email": "anita.desai@gmail.com", "phone": "9876543215"},
    {"name": "Rahul Mehta", "email": "rahul.mehta@gmail.com", "phone": "9876543216"},
    {"name": "Pooja Iyer", "email": "pooja.iyer@gmail.com", "phone": "9876543217"},
    {"name": "Sanjay Gupta", "email": "sanjay.gupta@gmail.com", "phone": "9876543218"},
    {"name": "Kavita Nair", "email": "kavita.nair@gmail.com", "phone": "9876543219"},
    {"name": "Arjun Kapoor", "email": "arjun.kapoor@gmail.com", "phone": "9876543220"},
    {"name": "Deepika Rao", "email": "deepika.rao@gmail.com", "phone": "9876543221"},
    {"name": "Karan Malhotra", "email": "karan.malhotra@gmail.com", "phone": "9876543222"},
    {"name": "Ritu Joshi", "email": "ritu.joshi@gmail.com", "phone": "9876543223"},
    {"name": "Aditya Saxena", "email": "aditya.saxena@gmail.com", "phone": "9876543224"}
]

LOAN_TYPES = [
    {
        "type": "Personal Loan",
        "purposes": [
            "Wedding expenses",
            "Medical emergency",
            "Home renovation",
            "Debt consolidation",
            "Travel expenses"
        ],
        "amount_range": (50000, 500000),
        "tenure_range": (12, 60)
    },
    {
        "type": "Home Loan",
        "purposes": [
            "Purchase new apartment",
            "Purchase independent house",
            "Home construction",
            "Plot purchase",
            "Home renovation"
        ],
        "amount_range": (1000000, 5000000),
        "tenure_range": (120, 240)
    },
    {
        "type": "Business Loan",
        "purposes": [
            "Business expansion",
            "Working capital",
            "Equipment purchase",
            "Inventory financing",
            "New business setup"
        ],
        "amount_range": (200000, 2000000),
        "tenure_range": (24, 84)
    },
    {
        "type": "Education Loan",
        "purposes": [
            "MBA abroad",
            "Engineering course",
            "Medical education",
            "Professional certification",
            "Study abroad"
        ],
        "amount_range": (300000, 3000000),
        "tenure_range": (60, 120)
    },
    {
        "type": "Vehicle Loan",
        "purposes": [
            "Purchase new car",
            "Purchase used car",
            "Purchase two-wheeler",
            "Commercial vehicle purchase",
            "Refinance existing vehicle loan"
        ],
        "amount_range": (100000, 1500000),
        "tenure_range": (24, 84)
    }
]

STATUSES = ["Pending", "Under Review", "Approved", "Rejected", "Disbursed"]

DOCUMENTS = [
    "aadhaar_card.pdf",
    "pan_card.pdf",
    "salary_slips.pdf",
    "bank_statements.pdf",
    "form_16.pdf",
    "property_documents.pdf",
    "business_registration.pdf",
    "income_tax_returns.pdf",
    "address_proof.pdf",
    "passport.pdf"
]


def generate_loan_application():
    """Generate a random loan application"""
    customer = random.choice(CUSTOMERS)
    loan_type_data = random.choice(LOAN_TYPES)
    
    amount = random.randint(loan_type_data["amount_range"][0], loan_type_data["amount_range"][1])
    amount = (amount // 1000) * 1000  # Round to nearest thousand
    
    tenure = random.choice(range(
        loan_type_data["tenure_range"][0],
        loan_type_data["tenure_range"][1] + 1,
        6  # Multiples of 6 months
    ))
    
    # Interest rates based on loan type
    interest_rates = {
        "Personal Loan": (10.5, 18.0),
        "Home Loan": (8.0, 10.5),
        "Business Loan": (12.0, 20.0),
        "Education Loan": (9.0, 15.0),
        "Vehicle Loan": (9.5, 14.0)
    }
    
    interest_rate = round(random.uniform(*interest_rates[loan_type_data["type"]]), 2)
    
    # Income should be at least 3x of monthly EMI
    monthly_emi = (amount * interest_rate / 100 / 12) / (1 - (1 + interest_rate / 100 / 12) ** -tenure)
    min_income = int(monthly_emi * 3)
    income = random.randint(min_income, min_income * 2)
    income = (income // 1000) * 1000  # Round to nearest thousand
    
    # CIBIL score distribution
    cibil_weights = [(300, 550, 5), (551, 650, 10), (651, 750, 30), (751, 850, 40), (851, 900, 15)]
    cibil_range = random.choices(
        [(r[0], r[1]) for r in cibil_weights],
        weights=[r[2] for r in cibil_weights]
    )[0]
    cibil_score = random.randint(cibil_range[0], cibil_range[1])
    
    # Select 4-6 random documents
    num_documents = random.randint(4, 6)
    selected_documents = random.sample(DOCUMENTS, num_documents)
    
    return {
        "customer": customer["name"],
        "email": customer["email"],
        "phone": customer["phone"],
        "type": loan_type_data["type"],
        "amount": amount,
        "tenure": tenure,
        "interestRate": interest_rate,
        "purpose": random.choice(loan_type_data["purposes"]),
        "income": f"₹{income:,}/month",
        "cibilScore": cibil_score,
        "documents": selected_documents
    }


def seed_loan_applications(count=15):
    """Create sample loan applications"""
    print("=" * 80)
    print(f"SEEDING {count} LOAN APPLICATIONS")
    print("=" * 80)
    
    created_applications = []
    
    for i in range(count):
        application = generate_loan_application()
        
        try:
            print(f"\n[{i+1}/{count}] Creating application for {application['customer']}...")
            print(f"  Type: {application['type']}")
            print(f"  Amount: ₹{application['amount']:,}")
            print(f"  Tenure: {application['tenure']} months")
            print(f"  Interest Rate: {application['interestRate']}%")
            print(f"  Income: ₹{application['income']:,}")
            print(f"  CIBIL Score: {application['cibilScore']}")
            print(f"  Documents: {len(application['documents'])} files")
            
            response = requests.post(
                f"{BASE_URL}/applications",
                json=application,
                timeout=10
            )
            
            if response.status_code == 201:
                data = response.json()
                application_id = data.get("id")
                created_applications.append(application_id)
                print(f"  ✅ Created successfully (ID: {application_id})")
                
            else:
                print(f"  ❌ Failed: {response.status_code}")
                print(f"     {response.text}")
                
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
    
    print("\n" + "=" * 80)
    print(f"CREATED {len(created_applications)} APPLICATIONS")
    print("=" * 80)
    
    # Now update some applications with different statuses
    if created_applications:
        print("\n" + "=" * 80)
        print("UPDATING APPLICATION STATUSES")
        print("=" * 80)
        
        status_distribution = {
            "Under Review": 3,
            "Approved": 3,
            "Rejected": 2,
            "Disbursed": 2
        }
        
        applications_to_update = created_applications[:]
        random.shuffle(applications_to_update)
        
        for status, count in status_distribution.items():
            for i in range(min(count, len(applications_to_update))):
                app_id = applications_to_update.pop(0)
                
                try:
                    print(f"\nUpdating {app_id} to {status}...")
                    
                    update_data = {
                        "status": status
                    }
                    
                    if status == "Rejected":
                        rejection_reasons = [
                            "Low CIBIL score",
                            "Insufficient income",
                            "Incomplete documentation",
                            "High existing debt",
                            "Unable to verify employment"
                        ]
                        update_data["rejectionReason"] = random.choice(rejection_reasons)
                        print(f"  Reason: {update_data['rejectionReason']}")
                    
                    response = requests.patch(
                        f"{BASE_URL}/applications/{app_id}/status",
                        json=update_data,
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        print(f"  ✅ Updated to {status}")
                    else:
                        print(f"  ❌ Failed: {response.status_code}")
                        
                except Exception as e:
                    print(f"  ❌ Error: {str(e)}")
    
    print("\n" + "=" * 80)
    print("SEEDING COMPLETE!")
    print("=" * 80)
    
    # Get and display statistics
    try:
        print("\n" + "=" * 80)
        print("LOAN APPLICATION STATISTICS")
        print("=" * 80)
        
        response = requests.get(f"{BASE_URL}/statistics")
        
        if response.status_code == 200:
            stats = response.json()
            
            print(f"\n📊 Total Applications: {stats.get('totalApplications', 0)}")
            print(f"💰 Total Amount: {stats.get('totalAmount', '₹0')}")
            print(f"📈 Average Amount: {stats.get('averageAmount', '₹0')}")
            print(f"⭐ Average CIBIL: {stats.get('averageCibilScore', 0)}")
            
            print("\n📋 Status Breakdown:")
            status_counts = stats.get('statusCounts', {})
            for status, count in status_counts.items():
                if count > 0:
                    print(f"  • {status}: {count}")
                    
        else:
            print(f"Failed to fetch statistics: {response.status_code}")
            
    except Exception as e:
        print(f"Error fetching statistics: {str(e)}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("LOAN APPLICATION SEEDER")
    print("=" * 80)
    print("\nThis script will create sample loan applications for testing.")
    print("Make sure the backend server is running at http://localhost:8000")
    print("\n" + "=" * 80)
    
    # Auto-start seeding (removed input prompt for automation)
    print("\nStarting seeding process...")
    
    seed_loan_applications(15)
    
    print("\n✅ All done! Check the admin panel to see the applications.")
    print("🌐 Visit: http://localhost:5173 (if frontend is running)\n")
