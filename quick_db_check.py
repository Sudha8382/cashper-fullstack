import pymongo
from pymongo import MongoClient
import os
from pathlib import Path

# Load environment variables
env_path = Path(__file__).parent / "cashper_backend" / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

# Get MongoDB URL from environment
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
MONGO_DB = os.getenv("MONGO_DB", "cashper_db")

print(f"\nConnecting to: {MONGO_URL[:50]}...")
print(f"Database: {MONGO_DB}\n")

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=10000)
    db = client[MONGO_DB]
    
    print("\n" + "="*70)
    print("DATABASE COLLECTION COUNTS - REAL-TIME")
    print("="*70)
    
    # 1. USERS
    users_count = db["users"].count_documents({})
    print(f"\n1. Total Users: {users_count}")
    
    # 2. LOANS
    print(f"\n2. LOANS:")
    loan_collections = [
        "admin_loan_applications",
        "personal_loan_applications",
        "home_loan_applications",
        "business_loan_applications",
        "short_term_loan_applications",
        "short_term_loans"
    ]
    
    total_loans = 0
    all_collections = db.list_collection_names()
    for col_name in loan_collections:
        if col_name in all_collections:
            count = db[col_name].count_documents({})
            total_loans += count
            if count > 0:
                print(f"   {col_name}: {count}")
    
    print(f"   ✅ TOTAL LOANS: {total_loans}")
    
    # 3. INSURANCE
    print(f"\n3. INSURANCE POLICIES:")
    if "insurance_policies" in all_collections:
        insurance_count = db["insurance_policies"].count_documents({})
        print(f"   insurance_policies: {insurance_count}")
        print(f"   ✅ TOTAL: {insurance_count}")
    else:
        health = db["health_insurance_inquiries"].count_documents({}) if "health_insurance_inquiries" in all_collections else 0
        motor = db["motor_insurance_inquiries"].count_documents({}) if "motor_insurance_inquiries" in all_collections else 0
        term = db["term_insurance_inquiries"].count_documents({}) if "term_insurance_inquiries" in all_collections else 0
        print(f"   health_insurance_inquiries: {health}")
        print(f"   motor_insurance_inquiries: {motor}")
        print(f"   term_insurance_inquiries: {term}")
        insurance_count = health + motor + term
        print(f"   ✅ TOTAL: {insurance_count}")
    
    # 4. INQUIRIES
    print(f"\n4. INQUIRIES:")
    inquiry_collections = {
        "short_term_loan_get_in_touch": 0,
        "personal_loan_get_in_touch": 0,
        "business_loan_get_in_touch": 0,
        "home_loan_get_in_touch": 0,
        "term_insurance_inquiries": 0,
        "motor_insurance_inquiries": 0,
        "health_insurance_inquiries": 0,
        "sip_inquiries": 0,
        "consultations": 0,
        "contact_submissions": 0,
        "RetailServiceApplications": 0
    }
    
    total_inquiries = 0
    for col_name in inquiry_collections.keys():
        if col_name in all_collections:
            count = db[col_name].count_documents({})
            inquiry_collections[col_name] = count
            total_inquiries += count
            if count > 0:
                print(f"   {col_name}: {count}")
    
    print(f"   ✅ TOTAL INQUIRIES: {total_inquiries}")
    
    # 5. INVESTMENTS
    print(f"\n5. INVESTMENTS:")
    investment_collections = ["sip_applications", "mutual_fund_applications", "investment_inquiries"]
    total_investments = 0
    for col_name in investment_collections:
        if col_name in all_collections:
            count = db[col_name].count_documents({})
            total_investments += count
            if count > 0:
                print(f"   {col_name}: {count}")
    print(f"   ✅ TOTAL: {total_investments}")
    
    # 6. TAX PLANNING
    print(f"\n6. TAX PLANNING:")
    tax_collections = [
        "personal_tax_consultations",
        "business_tax_consultations",
        "itr_applications",
        "tax_inquiries",
        "tax_consultations"
    ]
    total_tax = 0
    for col_name in tax_collections:
        if col_name in all_collections:
            count = db[col_name].count_documents({})
            total_tax += count
            if count > 0:
                print(f"   {col_name}: {count}")
    print(f"   ✅ TOTAL: {total_tax}")
    
    # 7. RETAIL SERVICES
    print(f"\n7. RETAIL SERVICES:")
    total_retail = 0
    if "RetailServiceApplications" in all_collections:
        count = db["RetailServiceApplications"].count_documents({})
        total_retail += count
        print(f"   RetailServiceApplications: {count}")
    if "retail_service_applications" in all_collections:
        count = db["retail_service_applications"].count_documents({})
        total_retail += count
        print(f"   retail_service_applications: {count}")
    print(f"   ✅ TOTAL: {total_retail}")
    
    # 8. CORPORATE SERVICES
    print(f"\n8. CORPORATE SERVICES:")
    total_corporate = 0
    if "CorporateServiceInquiries" in all_collections:
        count = db["CorporateServiceInquiries"].count_documents({})
        total_corporate += count
        print(f"   CorporateServiceInquiries: {count}")
    if "corporate_service_inquiries" in all_collections:
        count = db["corporate_service_inquiries"].count_documents({})
        total_corporate += count
        print(f"   corporate_service_inquiries: {count}")
    if "corporate_consultations" in all_collections:
        count = db["corporate_consultations"].count_documents({})
        total_corporate += count
        print(f"   corporate_consultations: {count}")
    print(f"   ✅ TOTAL: {total_corporate}")
    
    print("\n" + "="*70)
    print("EXPECTED DASHBOARD VALUES:")
    print("="*70)
    print(f"✅ Total Users: {users_count}")
    print(f"✅ Total Loans: {total_loans}")
    print(f"✅ Insurance Policies: {insurance_count}")
    print(f"✅ Total Inquiries: {total_inquiries}")
    print(f"✅ Investments: {total_investments}")
    print(f"✅ Tax Planning: {total_tax}")
    print(f"✅ Retail Services: {total_retail}")
    print(f"✅ Corporate Services: {total_corporate}")
    print("="*70 + "\n")
    
    client.close()
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
