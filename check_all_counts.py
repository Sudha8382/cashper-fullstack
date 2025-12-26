#!/usr/bin/env python
"""
Check all collection counts in database to match with dashboard
"""
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent / "cashper_backend"
sys.path.insert(0, str(backend_dir))

from app.database.db import get_database

def check_all_counts():
    """Check all collection counts"""
    print("\n[+] Connecting to MongoDB...")
    db = get_database()
    
    if db is None:
        print("❌ Failed to connect to database")
        return
    
    print("[+] Connected successfully!")
    
    print("\n" + "="*60)
    print("DATABASE COLLECTION COUNTS")
    print("="*60)
    
    # 1. USERS
    print("\n1. USERS:")
    users_count = db["users"].count_documents({})
    print(f"   Total Users: {users_count}")
    
    # 2. LOANS
    print("\n2. LOANS:")
    loan_collections = {
        "admin_loan_applications": 0,
        "personal_loan_applications": 0,
        "home_loan_applications": 0,
        "business_loan_applications": 0,
        "short_term_loan_applications": 0,
        "short_term_loans": 0
    }
    
    total_loans = 0
    for col_name in loan_collections.keys():
        if col_name in db.list_collection_names():
            count = db[col_name].count_documents({})
            loan_collections[col_name] = count
            total_loans += count
            print(f"   {col_name}: {count}")
    
    print(f"   TOTAL LOANS: {total_loans}")
    
    # 3. INSURANCE
    print("\n3. INSURANCE:")
    if "insurance_policies" in db.list_collection_names():
        insurance_count = db["insurance_policies"].count_documents({})
        print(f"   insurance_policies: {insurance_count}")
    else:
        print("   insurance_policies: NOT FOUND")
        print("   Counting from inquiries:")
        health = db["health_insurance_inquiries"].count_documents({})
        motor = db["motor_insurance_inquiries"].count_documents({})
        term = db["term_insurance_inquiries"].count_documents({})
        print(f"   health_insurance_inquiries: {health}")
        print(f"   motor_insurance_inquiries: {motor}")
        print(f"   term_insurance_inquiries: {term}")
        print(f"   TOTAL: {health + motor + term}")
    
    # 4. INQUIRIES
    print("\n4. INQUIRIES:")
    inquiry_collections = [
        "short_term_loan_get_in_touch",
        "personal_loan_get_in_touch",
        "business_loan_get_in_touch",
        "home_loan_get_in_touch",
        "term_insurance_inquiries",
        "motor_insurance_inquiries",
        "health_insurance_inquiries",
        "sip_inquiries",
        "consultations",
        "contact_submissions",
        "RetailServiceApplications"
    ]
    
    total_inquiries = 0
    for col_name in inquiry_collections:
        if col_name in db.list_collection_names():
            count = db[col_name].count_documents({})
            total_inquiries += count
            print(f"   {col_name}: {count}")
        else:
            print(f"   {col_name}: NOT FOUND")
    
    print(f"   TOTAL INQUIRIES: {total_inquiries}")
    
    # 5. INVESTMENTS
    print("\n5. INVESTMENTS:")
    investment_collections = ["sip_applications", "mutual_fund_applications", "investment_inquiries"]
    total_investments = 0
    for col_name in investment_collections:
        if col_name in db.list_collection_names():
            count = db[col_name].count_documents({})
            total_investments += count
            print(f"   {col_name}: {count}")
        else:
            print(f"   {col_name}: NOT FOUND")
    print(f"   TOTAL INVESTMENTS: {total_investments}")
    
    # 6. TAX PLANNING
    print("\n6. TAX PLANNING:")
    tax_collections = [
        "personal_tax_consultations",
        "business_tax_consultations",
        "itr_applications",
        "tax_inquiries",
        "tax_consultations"
    ]
    total_tax = 0
    for col_name in tax_collections:
        if col_name in db.list_collection_names():
            count = db[col_name].count_documents({})
            total_tax += count
            print(f"   {col_name}: {count}")
        else:
            print(f"   {col_name}: NOT FOUND")
    print(f"   TOTAL TAX PLANNING: {total_tax}")
    
    # 7. RETAIL SERVICES
    print("\n7. RETAIL SERVICES:")
    retail_collections = ["RetailServiceApplications", "retail_service_applications"]
    total_retail = 0
    for col_name in retail_collections:
        if col_name in db.list_collection_names():
            count = db[col_name].count_documents({})
            total_retail += count
            print(f"   {col_name}: {count}")
        else:
            print(f"   {col_name}: NOT FOUND")
    print(f"   TOTAL RETAIL SERVICES: {total_retail}")
    
    # 8. CORPORATE SERVICES
    print("\n8. CORPORATE SERVICES:")
    corporate_collections = [
        "CorporateServiceInquiries",
        "corporate_service_inquiries",
        "corporate_consultations"
    ]
    total_corporate = 0
    for col_name in corporate_collections:
        if col_name in db.list_collection_names():
            count = db[col_name].count_documents({})
            total_corporate += count
            print(f"   {col_name}: {count}")
        else:
            print(f"   {col_name}: NOT FOUND")
    print(f"   TOTAL CORPORATE SERVICES: {total_corporate}")
    
    print("\n" + "="*60)
    print("EXPECTED DASHBOARD VALUES:")
    print("="*60)
    print(f"Total Users: {users_count}")
    print(f"Total Loans: {total_loans}")
    print(f"Insurance Policies: {insurance_count if 'insurance_policies' in db.list_collection_names() else health + motor + term}")
    print(f"Total Inquiries: {total_inquiries}")
    print(f"Investments: {total_investments}")
    print(f"Tax Planning: {total_tax}")
    print(f"Retail Services: {total_retail}")
    print(f"Corporate Services: {total_corporate}")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        check_all_counts()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
