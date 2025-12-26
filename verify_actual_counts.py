from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['cashper_db']

print("=" * 100)
print("CHECKING ACTUAL DATABASE COUNTS")
print("=" * 100)

# 1. TOTAL INQUIRIES (should be 303)
print("\n📋 TOTAL INQUIRIES:")
inquiry_collections = {
    "short_term_loan_get_in_touch": db["short_term_loan_get_in_touch"].count_documents({}) if "short_term_loan_get_in_touch" in db.list_collection_names() else 0,
    "personal_loan_get_in_touch": db["personal_loan_get_in_touch"].count_documents({}) if "personal_loan_get_in_touch" in db.list_collection_names() else 0,
    "business_loan_get_in_touch": db["business_loan_get_in_touch"].count_documents({}) if "business_loan_get_in_touch" in db.list_collection_names() else 0,
    "home_loan_get_in_touch": db["home_loan_get_in_touch"].count_documents({}) if "home_loan_get_in_touch" in db.list_collection_names() else 0,
    "term_insurance_inquiries": db["term_insurance_inquiries"].count_documents({}) if "term_insurance_inquiries" in db.list_collection_names() else 0,
    "motor_insurance_inquiries": db["motor_insurance_inquiries"].count_documents({}) if "motor_insurance_inquiries" in db.list_collection_names() else 0,
    "health_insurance_inquiries": db["health_insurance_inquiries"].count_documents({}) if "health_insurance_inquiries" in db.list_collection_names() else 0,
    "sip_inquiries": db["sip_inquiries"].count_documents({}) if "sip_inquiries" in db.list_collection_names() else 0,
    "mutual_fund_inquiries": db["mutual_fund_inquiries"].count_documents({}) if "mutual_fund_inquiries" in db.list_collection_names() else 0,
    "consultations": db["consultations"].count_documents({}) if "consultations" in db.list_collection_names() else 0,
    "contact_submissions": db["contact_submissions"].count_documents({}) if "contact_submissions" in db.list_collection_names() else 0,
    "RetailServiceApplications": db["RetailServiceApplications"].count_documents({}) if "RetailServiceApplications" in db.list_collection_names() else 0,
}
for name, count in inquiry_collections.items():
    if count > 0:
        print(f"  {name}: {count}")
total_inquiries = sum(inquiry_collections.values())
print(f"  🔢 TOTAL: {total_inquiries}")

# 2. CORPORATE SERVICES (should be 89)
print("\n🏢 CORPORATE SERVICES:")
corporate_collections = {
    "tds_services_applications": db["tds_services_applications"].count_documents({}) if "tds_services_applications" in db.list_collection_names() else 0,
    "gst_services_applications": db["gst_services_applications"].count_documents({}) if "gst_services_applications" in db.list_collection_names() else 0,
    "legal_advice_applications": db["legal_advice_applications"].count_documents({}) if "legal_advice_applications" in db.list_collection_names() else 0,
    "provident_fund_services_applications": db["provident_fund_services_applications"].count_documents({}) if "provident_fund_services_applications" in db.list_collection_names() else 0,
    "payroll_services_applications": db["payroll_services_applications"].count_documents({}) if "payroll_services_applications" in db.list_collection_names() else 0,
    "accounting_bookkeeping_applications": db["accounting_bookkeeping_applications"].count_documents({}) if "accounting_bookkeeping_applications" in db.list_collection_names() else 0,
    "company_registration_applications": db["company_registration_applications"].count_documents({}) if "company_registration_applications" in db.list_collection_names() else 0,
    "company_compliance_applications": db["company_compliance_applications"].count_documents({}) if "company_compliance_applications" in db.list_collection_names() else 0,
    "tax_audit_applications": db["tax_audit_applications"].count_documents({}) if "tax_audit_applications" in db.list_collection_names() else 0,
}
for name, count in corporate_collections.items():
    if count > 0:
        print(f"  {name}: {count}")
total_corporate = sum(corporate_collections.values())
print(f"  🔢 TOTAL: {total_corporate}")

# 3. TAX PLANNING (should be 4)
print("\n📊 TAX PLANNING:")
tax_collections = {
    "personal_tax_applications": db["personal_tax_applications"].count_documents({}) if "personal_tax_applications" in db.list_collection_names() else 0,
    "business_tax_applications": db["business_tax_applications"].count_documents({}) if "business_tax_applications" in db.list_collection_names() else 0,
    "itr_applications": db["itr_applications"].count_documents({}) if "itr_applications" in db.list_collection_names() else 0,
    "personal_tax_consultations": db["personal_tax_consultations"].count_documents({}) if "personal_tax_consultations" in db.list_collection_names() else 0,
    "business_tax_consultations": db["business_tax_consultations"].count_documents({}) if "business_tax_consultations" in db.list_collection_names() else 0,
}
for name, count in tax_collections.items():
    if count > 0:
        print(f"  {name}: {count}")
total_tax = sum(tax_collections.values())
print(f"  🔢 TOTAL: {total_tax}")

# 4. INVESTMENTS (should be 2)
print("\n💰 INVESTMENTS:")
investment_collections = {
    "sip_applications": db["sip_applications"].count_documents({}) if "sip_applications" in db.list_collection_names() else 0,
    "mutual_fund_applications": db["mutual_fund_applications"].count_documents({}) if "mutual_fund_applications" in db.list_collection_names() else 0,
    "investment_applications": db["investment_applications"].count_documents({}) if "investment_applications" in db.list_collection_names() else 0,
}
for name, count in investment_collections.items():
    if count > 0:
        print(f"  {name}: {count}")
total_investments = sum(investment_collections.values())
print(f"  🔢 TOTAL: {total_investments}")

print("\n" + "=" * 100)
print("SUMMARY:")
print(f"  Total Inquiries: {total_inquiries} (expected: 303)")
print(f"  Corporate Services: {total_corporate} (expected: 89)")
print(f"  Tax Planning: {total_tax} (expected: 4)")
print(f"  Investments: {total_investments} (expected: 2)")
print("=" * 100)
