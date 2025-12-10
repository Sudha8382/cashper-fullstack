#!/usr/bin/env python3
"""
Debug script to check actual data in MongoDB and what dashboard should display
"""
import sys
sys.path.insert(0, r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend')

from app.database.db import get_database
from datetime import datetime, timedelta

db = get_database()

print("=" * 60)
print("🔍 ACTUAL DATA IN MONGODB")
print("=" * 60)

# 1. Total Users
total_users = db["users"].count_documents({})
print(f"\n1️⃣  TOTAL USERS: {total_users}")

# 2. Active Loans
personal_loans_approved = list(db["personal_loan_applications"].find({"status": "approved"}))
home_loans_approved = list(db["home_loan_applications"].find({"status": "approved"})) if "home_loan_applications" in db.list_collection_names() else []
business_loans_approved = list(db["business_loan_applications"].find({"status": "approved"})) if "business_loan_applications" in db.list_collection_names() else []
short_term_loans_approved = list(db["short_term_loans"].find({"status": "approved"})) if "short_term_loans" in db.list_collection_names() else []

print(f"\n2️⃣  ACTIVE LOANS:")
print(f"   - Personal Loans (Approved): {len(personal_loans_approved)}")
print(f"   - Home Loans (Approved): {len(home_loans_approved)}")
print(f"   - Business Loans (Approved): {len(business_loans_approved)}")
print(f"   - Short Term Loans (Approved): {len(short_term_loans_approved)}")

personal_total = sum(float(l.get("loanAmount", 0)) for l in personal_loans_approved)
home_total = sum(float(l.get("loanAmount", 0)) for l in home_loans_approved)
business_total = sum(float(l.get("loanAmount", 0)) for l in business_loans_approved)
short_term_total = sum(float(l.get("loanAmount", 0)) for l in short_term_loans_approved)

total_loan_amount = personal_total + home_total + business_total + short_term_total
print(f"   - Personal Loans Total: ₹{personal_total:,.0f}")
print(f"   - Home Loans Total: ₹{home_total:,.0f}")
print(f"   - Business Loans Total: ₹{business_total:,.0f}")
print(f"   - Short Term Loans Total: ₹{short_term_total:,.0f}")
print(f"   - TOTAL ACTIVE LOAN AMOUNT: ₹{total_loan_amount:,.0f}")
print(f"   - Display as: ₹{total_loan_amount/10000000:.1f}Cr")

# 3. Insurance Policies
health_insurance = db["health_insurance_inquiries"].count_documents({})
motor_insurance = db["motor_insurance_inquiries"].count_documents({})
term_insurance = db["term_insurance_inquiries"].count_documents({})
insurance_policies_count = 0
if "insurance_policies" in db.list_collection_names():
    insurance_policies_count = db["insurance_policies"].count_documents({})

total_insurance = health_insurance + motor_insurance + term_insurance + insurance_policies_count

print(f"\n3️⃣  INSURANCE POLICIES:")
print(f"   - Health Insurance Inquiries: {health_insurance}")
print(f"   - Motor Insurance Inquiries: {motor_insurance}")
print(f"   - Term Insurance Inquiries: {term_insurance}")
print(f"   - Insurance Policies: {insurance_policies_count}")
print(f"   - TOTAL INSURANCE: {total_insurance}")

# 4. Total Revenue
loan_revenue = total_loan_amount * 0.12 / 12  # 12% annual interest, monthly
insurance_revenue = (health_insurance * 15000 + motor_insurance * 12000 + term_insurance * 25000) / 12
total_revenue = loan_revenue + insurance_revenue

print(f"\n4️⃣  TOTAL REVENUE (Monthly):")
print(f"   - Loan Revenue (12% interest): ₹{loan_revenue:,.0f}")
print(f"   - Insurance Revenue: ₹{insurance_revenue:,.0f}")
print(f"   - TOTAL REVENUE: ₹{total_revenue:,.0f}")
print(f"   - Display as: ₹{total_revenue/10000000:.1f}Cr")

print("\n" + "=" * 60)
print("📊 DASHBOARD SHOULD SHOW:")
print("=" * 60)
print(f"Total Users: {total_users}")
print(f"Active Loans: ₹{total_loan_amount/10000000:.1f}Cr")
print(f"Insurance Policies: {total_insurance}")
print(f"Total Revenue: ₹{total_revenue/10000000:.1f}Cr")
print("=" * 60)

if total_users == 10 and total_insurance == 98:
    print("\n⚠️  PROBLEM DETECTED:")
    print("   - Total Users showing as 10 (likely wrong)")
    print("   - Insurance Policies showing as 98 (likely wrong)")
    print("   - This suggests OLD/CACHED DATA, not real database data!")
    print("\n🔧 SOLUTION:")
    print("   1. Clear browser cache or do hard refresh (Ctrl+Shift+Del)")
    print("   2. Make sure backend is running latest code")
    print("   3. Check if API response has cache headers")
    print("   4. Restart backend server")
