"""
Complete database scan - All applications for current user
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("\n" + "="*70)
print("COMPLETE DATABASE SCAN - ALL APPLICATIONS")
print("="*70)

# Get current logged in user (sudha@gmail.com)
user = db["users"].find_one({"email": "sudha@gmail.com"})
if not user:
    print("\n❌ User not found!")
    client.close()
    exit()

user_id = str(user["_id"])
print(f"\n👤 User: {user.get('fullName', 'N/A')} ({user['email']})")
print(f"🆔 User ID: {user_id}")

# All collections to check
all_collections = {
    "Loans": [
        ("personal_loans", "Personal Loan"),
        ("home_loans", "Home Loan"),
        ("business_loans", "Business Loan"),
        ("short_term_loans", "Short Term Loan"),
    ],
    "Tax Planning": [
        ("tax_planning_applications", "Personal Tax Planning"),
        ("business_tax_applications", "Business Tax Planning"),
    ],
    "Insurance": [
        ("term_insurance_applications", "Term Insurance"),
        ("health_insurance_applications", "Health Insurance"),
        ("motor_insurance_applications", "Motor Insurance"),
    ],
    "Investments": [
        ("mutual_fund_applications", "Mutual Funds"),
        ("sip_applications", "SIP"),
        ("trading_demat_applications", "Trading & Demat"),
    ],
    "Retail Services": [
        ("itr_filing_applications", "ITR Filing"),
        ("pan_applications", "PAN Application"),
        ("pf_withdrawal_applications", "PF Withdrawal"),
        ("bank_account_applications", "Bank Account"),
    ]
}

grand_total = 0

for category, collections in all_collections.items():
    print(f"\n{'='*70}")
    print(f"{category.upper()}")
    print(f"{'='*70}")
    
    category_total = 0
    
    for collection_name, service_name in collections:
        if collection_name not in db.list_collection_names():
            continue
            
        # Count by userId
        count = db[collection_name].count_documents({"userId": user_id})
        
        if count > 0:
            print(f"\n✅ {service_name}: {count} application(s)")
            category_total += count
            
            # Show details
            apps = list(db[collection_name].find({"userId": user_id}).limit(5))
            for i, app in enumerate(apps, 1):
                print(f"   {i}. ID: {str(app['_id'])[:8]}...")
                
                # Display relevant fields
                if 'fullName' in app:
                    print(f"      Name: {app['fullName']}")
                if 'businessName' in app:
                    print(f"      Business: {app['businessName']}")
                if 'loanAmount' in app:
                    amount = app['loanAmount']
                    if isinstance(amount, (int, float)):
                        print(f"      Amount: ₹{amount:,}")
                    else:
                        print(f"      Amount: ₹{amount}")
                if 'emailAddress' in app:
                    print(f"      Email: {app['emailAddress']}")
                if 'businessEmail' in app:
                    print(f"      Email: {app['businessEmail']}")
                    
                status = app.get('status', 'N/A')
                print(f"      Status: {status}")
                print(f"      Created: {app.get('createdAt', 'N/A')}")
    
    if category_total > 0:
        print(f"\n📊 {category} Total: {category_total}")
        grand_total += category_total
    else:
        print(f"\n⚠️  No applications found in {category}")

print(f"\n{'='*70}")
print(f"🎯 GRAND TOTAL: {grand_total} applications")
print(f"{'='*70}")

# Also check applications without userId but with matching email
print(f"\n{'='*70}")
print("CHECKING APPLICATIONS WITHOUT userId (BY EMAIL)")
print(f"{'='*70}")

orphan_count = 0
for category, collections in all_collections.items():
    for collection_name, service_name in collections:
        if collection_name not in db.list_collection_names():
            continue
            
        query = {
            "userId": None,
            "$or": [
                {"emailAddress": "sudha@gmail.com"},
                {"businessEmail": "sudha@gmail.com"},
                {"email": "sudha@gmail.com"}
            ]
        }
        
        count = db[collection_name].count_documents(query)
        if count > 0:
            print(f"\n⚠️  {service_name}: {count} orphan application(s)")
            orphan_count += count

if orphan_count > 0:
    print(f"\n⚠️  Total orphan applications: {orphan_count}")
    print("These applications need userId to be added!")
else:
    print("\n✅ No orphan applications found")

print(f"\n{'='*70}")

client.close()
