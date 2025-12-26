"""
Seed sample data for all 6 remaining corporate services
- Legal Advice
- Provident Fund Services
- TDS-Related Services
- GST-Related Services
- Payroll Services
- Accounting & Bookkeeping
"""

import sys
from datetime import datetime, timedelta
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# MongoDB connection
MONGO_URI = "mongodb+srv://kumuyadav249_db_user:O0zb3rZlZXArZiSg@cluster0.mnzwn7m.mongodb.net/"
# Or use local MongoDB
# MONGO_URI = "mongodb://localhost:27017/cashper_db"

def connect_db():
    """Connect to MongoDB"""
    client = MongoClient(MONGO_URI)
    db = client["cashper_db"]
    return db

def seed_legal_advice_applications(db):
    """Seed legal advice applications"""
    collection = db["legal_advice_applications"]
    
    applications = [
        {
            "application_id": "LEG202401001",
            "name": "Rajesh Kumar Singh",
            "email": "rajesh.singh@company.com",
            "phone": "9876543210",
            "company_name": "TechCorp Industries",
            "legal_issue_type": "Contract Review",
            "case_description": "Need legal review of vendor contracts and terms. Looking for expert advice on contract negotiation and compliance issues. This is urgent as we need to finalize contracts within next 2 weeks.",
            "urgency": "High",
            "address": "Plot 123, Tech Park Road",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560076",
            "company_pan": "AAACT1234J",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=2),
            "updated_at": datetime.now() - timedelta(days=2)
        },
        {
            "application_id": "LEG202401002",
            "name": "Priya Sharma",
            "email": "priya.sharma@business.com",
            "phone": "8765432109",
            "company_name": "Business Solutions Ltd",
            "legal_issue_type": "Employment Dispute",
            "case_description": "Help required for employment termination case. Need legal guidance on termination procedures and possible liabilities. Employee has filed a dispute claiming wrongful termination.",
            "urgency": "Medium",
            "address": "456 Business Avenue",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "400001",
            "company_pan": "AAACB5678K",
            "status": "Under Review",
            "created_at": datetime.now() - timedelta(days=5),
            "updated_at": datetime.now() - timedelta(days=3)
        },
        {
            "application_id": "LEG202401003",
            "name": "Amit Patel",
            "email": "amit.patel@enterprise.com",
            "phone": "7654321098",
            "company_name": "Enterprise Solutions",
            "legal_issue_type": "Intellectual Property",
            "case_description": "Patent infringement concern. Our company believes another firm is using our patented technology without permission. Need legal advice on IP protection and possible actions.",
            "urgency": "High",
            "address": "789 Enterprise Plaza",
            "city": "Delhi",
            "state": "Delhi",
            "pincode": "110001",
            "company_pan": "AAACE9876L",
            "status": "Approved",
            "created_at": datetime.now() - timedelta(days=10),
            "updated_at": datetime.now() - timedelta(days=8)
        },
        {
            "application_id": "LEG202401004",
            "name": "Neha Gupta",
            "email": "neha.gupta@startup.com",
            "phone": "6543210987",
            "company_name": "StartUp Innovations",
            "legal_issue_type": "Regulatory Compliance",
            "case_description": "Need guidance on regulatory compliance for our new product launch. Product involves data privacy concerns and we need to ensure all legal requirements are met.",
            "urgency": "Medium",
            "address": "321 Innovation Hub",
            "city": "Hyderabad",
            "state": "Telangana",
            "pincode": "500001",
            "company_pan": "AAACF2345M",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=1),
            "updated_at": datetime.now() - timedelta(days=1)
        },
        {
            "application_id": "LEG202401005",
            "name": "Vikram Reddy",
            "email": "vikram.reddy@corp.com",
            "phone": "5432109876",
            "company_name": "Corporate Ventures",
            "legal_issue_type": "Merger & Acquisition",
            "case_description": "Legal support for merger negotiations with another company. Need guidance on due diligence, contract terms, and regulatory approvals for the M&A transaction.",
            "urgency": "High",
            "address": "654 Corporate Avenue",
            "city": "Pune",
            "state": "Maharashtra",
            "pincode": "411001",
            "company_pan": "AAACG6789N",
            "status": "In Progress",
            "created_at": datetime.now() - timedelta(days=7),
            "updated_at": datetime.now() - timedelta(days=4)
        }
    ]
    
    try:
        collection.insert_many(applications, ordered=False)
        print(f"✅ Seeded {len(applications)} Legal Advice applications")
    except DuplicateKeyError:
        print("⚠️  Some Legal Advice applications already exist")

def seed_provident_fund_applications(db):
    """Seed provident fund service applications"""
    collection = db["provident_fund_services_applications"]
    
    applications = [
        {
            "application_id": "PF202401001",
            "name": "Suresh Kumar",
            "email": "suresh@company.com",
            "phone": "9876543210",
            "company_name": "Manufacturing Corp",
            "number_of_employees": 150,
            "existing_pf_number": None,
            "existing_esi_number": None,
            "service_required": "New PF Account Registration",
            "address": "Industrial Park, Plot 45",
            "city": "Chennai",
            "state": "Tamil Nadu",
            "pincode": "600001",
            "company_pan": "AAADM1234P",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=3),
            "updated_at": datetime.now() - timedelta(days=3)
        },
        {
            "application_id": "PF202401002",
            "name": "Mohan Verma",
            "email": "mohan@industry.com",
            "phone": "8765432109",
            "company_name": "Manufacturing Industries",
            "number_of_employees": 250,
            "existing_pf_number": "KA/ABM1234/001",
            "existing_esi_number": "KA102034567800101",
            "service_required": "PF Account Modification",
            "address": "Industrial Zone, Sector 5",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560076",
            "company_pan": "AAADP5678Q",
            "status": "Under Review",
            "created_at": datetime.now() - timedelta(days=6),
            "updated_at": datetime.now() - timedelta(days=4)
        },
        {
            "application_id": "PF202401003",
            "name": "Deepak Singh",
            "email": "deepak@services.com",
            "phone": "7654321098",
            "company_name": "Business Services Pvt Ltd",
            "number_of_employees": 85,
            "existing_pf_number": "MH/ABD9876/001",
            "existing_esi_number": "MH101234567890101",
            "service_required": "Annual Compliance Filing",
            "address": "Financial District, Mumbai",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "400001",
            "company_pan": "AAADQ9876R",
            "status": "Approved",
            "created_at": datetime.now() - timedelta(days=12),
            "updated_at": datetime.now() - timedelta(days=10)
        },
        {
            "application_id": "PF202401004",
            "name": "Anitha Reddy",
            "email": "anitha@enterprise.com",
            "phone": "6543210987",
            "company_name": "IT Enterprise Solutions",
            "number_of_employees": 320,
            "existing_pf_number": "TG/ABE5432/002",
            "existing_esi_number": "TG103456789012101",
            "service_required": "PF Withdrawal Processing",
            "address": "Tech Park Building C",
            "city": "Hyderabad",
            "state": "Telangana",
            "pincode": "500001",
            "company_pan": "AAADS2345S",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=2),
            "updated_at": datetime.now() - timedelta(days=2)
        },
        {
            "application_id": "PF202401005",
            "name": "Rajesh Nair",
            "email": "rajesh@tech.com",
            "phone": "5432109876",
            "company_name": "Technology Solutions",
            "number_of_employees": 200,
            "existing_pf_number": "KL/ABF8765/001",
            "existing_esi_number": "KL104567890123101",
            "service_required": "Annual Audit & Compliance",
            "address": "Tech Campus, Kochi",
            "city": "Kochi",
            "state": "Kerala",
            "pincode": "682001",
            "company_pan": "AAADT6789T",
            "status": "In Progress",
            "created_at": datetime.now() - timedelta(days=8),
            "updated_at": datetime.now() - timedelta(days=5)
        }
    ]
    
    try:
        collection.insert_many(applications, ordered=False)
        print(f"✅ Seeded {len(applications)} Provident Fund Service applications")
    except DuplicateKeyError:
        print("⚠️  Some Provident Fund applications already exist")

def seed_tds_services_applications(db):
    """Seed TDS services applications"""
    collection = db["tds_services_applications"]
    
    applications = [
        {
            "application_id": "TDS202401001",
            "full_name": "Sanjay Kumar",
            "email": "sanjay@company.com",
            "phone": "9876543210",
            "pan_number": "AABCT1234A",
            "company_name": "Trade Services Ltd",
            "tan_number": "MUMA12345A",
            "service_type": "TDS Return Filing",
            "quarter_year": "Q3 2024",
            "address": "Business Tower, Floor 5",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "400001",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=4),
            "updated_at": datetime.now() - timedelta(days=4)
        },
        {
            "application_id": "TDS202401002",
            "full_name": "Priya Malhotra",
            "email": "priya@exports.com",
            "phone": "8765432109",
            "pan_number": "AABDU5678B",
            "company_name": "Export Trading Company",
            "tan_number": "DELX98765B",
            "service_type": "TDS Reconciliation",
            "quarter_year": "Q2 2024",
            "address": "Export Complex, Delhi",
            "city": "Delhi",
            "state": "Delhi",
            "pincode": "110001",
            "status": "Under Review",
            "created_at": datetime.now() - timedelta(days=7),
            "updated_at": datetime.now() - timedelta(days=5)
        },
        {
            "application_id": "TDS202401003",
            "full_name": "Rahul Sharma",
            "email": "rahul@finance.com",
            "phone": "7654321098",
            "pan_number": "AABEV9876C",
            "company_name": "Financial Services Inc",
            "tan_number": "BANA54321C",
            "service_type": "TDS Compliance Audit",
            "quarter_year": "Q1 2024",
            "address": "Finance Plaza, Bangalore",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560001",
            "status": "Approved",
            "created_at": datetime.now() - timedelta(days=14),
            "updated_at": datetime.now() - timedelta(days=12)
        },
        {
            "application_id": "TDS202401004",
            "full_name": "Neha Kapoor",
            "email": "neha@consulting.com",
            "phone": "6543210987",
            "pan_number": "AABFW2345D",
            "company_name": "Consulting Group Ltd",
            "tan_number": "CHNA12345D",
            "service_type": "TDS Certificate Generation",
            "quarter_year": "Q4 2023",
            "address": "Consulting Center, Chennai",
            "city": "Chennai",
            "state": "Tamil Nadu",
            "pincode": "600001",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=1),
            "updated_at": datetime.now() - timedelta(days=1)
        },
        {
            "application_id": "TDS202401005",
            "full_name": "Vikram Patel",
            "email": "vikram@trading.com",
            "phone": "5432109876",
            "pan_number": "AABGX6789E",
            "company_name": "Trading Enterprises",
            "tan_number": "JAIA98765E",
            "service_type": "TDS Amendment Filing",
            "quarter_year": "Q3 2023",
            "address": "Trade Center, Ahmedabad",
            "city": "Ahmedabad",
            "state": "Gujarat",
            "pincode": "380001",
            "status": "In Progress",
            "created_at": datetime.now() - timedelta(days=9),
            "updated_at": datetime.now() - timedelta(days=6)
        }
    ]
    
    try:
        collection.insert_many(applications, ordered=False)
        print(f"✅ Seeded {len(applications)} TDS Services applications")
    except DuplicateKeyError:
        print("⚠️  Some TDS Services applications already exist")

def seed_gst_services_applications(db):
    """Seed GST services applications"""
    collection = db["gst_services_applications"]
    
    applications = [
        {
            "application_id": "GST202401001",
            "full_name": "Arjun Reddy",
            "email": "arjun@retail.com",
            "phone": "9876543210",
            "pan_number": "AABHA1234F",
            "business_name": "Retail Trading Co",
            "gstin": "27AAJHA1234H2Z5",
            "service_type": "GST Registration",
            "turnover": 50000000,
            "address": "Retail Mall, Sector 10",
            "city": "Hyderabad",
            "state": "Telangana",
            "pincode": "500001",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=5),
            "updated_at": datetime.now() - timedelta(days=5)
        },
        {
            "application_id": "GST202401002",
            "full_name": "Sneha Desai",
            "email": "sneha@ecommerce.com",
            "phone": "8765432109",
            "pan_number": "AABHB5678G",
            "business_name": "E-Commerce Solutions",
            "gstin": "29AABHE5678G1ZM",
            "service_type": "GST Return Filing",
            "turnover": 75000000,
            "address": "E-Commerce Hub, Pune",
            "city": "Pune",
            "state": "Maharashtra",
            "pincode": "411001",
            "status": "Under Review",
            "created_at": datetime.now() - timedelta(days=8),
            "updated_at": datetime.now() - timedelta(days=6)
        },
        {
            "application_id": "GST202401003",
            "full_name": "Rohan Verma",
            "email": "rohan@manufacturing.com",
            "phone": "7654321098",
            "pan_number": "AABHC9876H",
            "business_name": "Manufacturing Units",
            "gstin": "23AABHE9876H2Z0",
            "service_type": "GST Compliance Audit",
            "turnover": 100000000,
            "address": "Industrial Area, Surat",
            "city": "Surat",
            "state": "Gujarat",
            "pincode": "395001",
            "status": "Approved",
            "created_at": datetime.now() - timedelta(days=16),
            "updated_at": datetime.now() - timedelta(days=14)
        },
        {
            "application_id": "GST202401004",
            "full_name": "Kavya Singh",
            "email": "kavya@services.com",
            "phone": "6543210987",
            "pan_number": "AABHD2345I",
            "business_name": "Service Industry Ltd",
            "gstin": "25AABHD2345I1Z9",
            "service_type": "GST Refund Processing",
            "turnover": 45000000,
            "address": "Service Park, Jaipur",
            "city": "Jaipur",
            "state": "Rajasthan",
            "pincode": "302001",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=2),
            "updated_at": datetime.now() - timedelta(days=2)
        },
        {
            "application_id": "GST202401005",
            "full_name": "Ashok Kumar",
            "email": "ashok@logistics.com",
            "phone": "5432109876",
            "pan_number": "AABHE6789J",
            "business_name": "Logistics Company",
            "gstin": "20AABHE6789J2ZX",
            "service_type": "GST Amendment Filing",
            "turnover": 60000000,
            "address": "Logistics Park, Bangalore",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560001",
            "status": "In Progress",
            "created_at": datetime.now() - timedelta(days=10),
            "updated_at": datetime.now() - timedelta(days=7)
        }
    ]
    
    try:
        collection.insert_many(applications, ordered=False)
        print(f"✅ Seeded {len(applications)} GST Services applications")
    except DuplicateKeyError:
        print("⚠️  Some GST Services applications already exist")

def seed_payroll_services_applications(db):
    """Seed payroll services applications"""
    collection = db["payroll_services_applications"]
    
    applications = [
        {
            "application_id": "PAY202401001",
            "name": "Mahesh Kumar",
            "email": "mahesh@hrms.com",
            "phone": "9876543210",
            "company_name": "HRMS Solutions",
            "number_of_employees": 120,
            "industry_type": "IT Services",
            "address": "Tech Park, Building A",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560001",
            "company_pan": "AABPI1234K",
            "gst_number": "29AABPI1234H2Z5",
            "pf_number": "KA/ABP1234/001",
            "esi_number": "KA102034567800101",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=3),
            "updated_at": datetime.now() - timedelta(days=3)
        },
        {
            "application_id": "PAY202401002",
            "name": "Divya Nair",
            "email": "divya@payroll.com",
            "phone": "8765432109",
            "company_name": "Payroll Systems Ltd",
            "number_of_employees": 200,
            "industry_type": "Staffing Solutions",
            "address": "Office Complex, Mumbai",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "400001",
            "company_pan": "AABPJ5678L",
            "gst_number": "27AABPJ5678G1ZM",
            "pf_number": "MH/ABP5678/001",
            "esi_number": "MH101234567890101",
            "status": "Under Review",
            "created_at": datetime.now() - timedelta(days=6),
            "updated_at": datetime.now() - timedelta(days=4)
        },
        {
            "application_id": "PAY202401003",
            "name": "Sumit Jain",
            "email": "sumit@manufacturing.com",
            "phone": "7654321098",
            "company_name": "Manufacturing Plant",
            "number_of_employees": 350,
            "industry_type": "Manufacturing",
            "address": "Industrial Estate, Pune",
            "city": "Pune",
            "state": "Maharashtra",
            "pincode": "411001",
            "company_pan": "AABPK9876M",
            "gst_number": "27AABPK9876H2Z0",
            "pf_number": "MH/ABP9876/002",
            "esi_number": "MH102345678901102",
            "status": "Approved",
            "created_at": datetime.now() - timedelta(days=13),
            "updated_at": datetime.now() - timedelta(days=11)
        },
        {
            "application_id": "PAY202401004",
            "name": "Anjali Gupta",
            "email": "anjali@retail.com",
            "phone": "6543210987",
            "company_name": "Retail Group India",
            "number_of_employees": 450,
            "industry_type": "Retail",
            "address": "Retail Complex, Delhi",
            "city": "Delhi",
            "state": "Delhi",
            "pincode": "110001",
            "company_pan": "AABPL2345N",
            "gst_number": "07AABPL2345G1ZX",
            "pf_number": "DL/ABP2345/001",
            "esi_number": "DL103456789012103",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=1),
            "updated_at": datetime.now() - timedelta(days=1)
        },
        {
            "application_id": "PAY202401005",
            "name": "Ravi Teja",
            "email": "ravi@hospitality.com",
            "phone": "5432109876",
            "company_name": "Hospitality Services",
            "number_of_employees": 280,
            "industry_type": "Hospitality",
            "address": "Hotel Complex, Goa",
            "city": "Goa",
            "state": "Goa",
            "pincode": "403001",
            "company_pan": "AABPM6789O",
            "gst_number": "30AABPM6789G1ZW",
            "pf_number": "GA/ABP6789/001",
            "esi_number": "GA104567890123104",
            "status": "In Progress",
            "created_at": datetime.now() - timedelta(days=7),
            "updated_at": datetime.now() - timedelta(days=5)
        }
    ]
    
    try:
        collection.insert_many(applications, ordered=False)
        print(f"✅ Seeded {len(applications)} Payroll Services applications")
    except DuplicateKeyError:
        print("⚠️  Some Payroll Services applications already exist")

def seed_accounting_bookkeeping_applications(db):
    """Seed accounting & bookkeeping service applications"""
    collection = db["accounting_bookkeeping_applications"]
    
    applications = [
        {
            "application_id": "ACC202401001",
            "full_name": "Rajesh Kapoor",
            "email": "rajesh@accounting.com",
            "phone": "9876543210",
            "pan_number": "AABQA1234P",
            "business_name": "Accounting Services LLC",
            "business_type": "Sole Proprietor",
            "service_required": "Monthly Bookkeeping",
            "number_of_transactions": "200-500",
            "address": "Accounting Building, Floor 3",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "400001",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=4),
            "updated_at": datetime.now() - timedelta(days=4)
        },
        {
            "application_id": "ACC202401002",
            "full_name": "Pooja Mehta",
            "email": "pooja@business.com",
            "phone": "8765432109",
            "pan_number": "AABQB5678Q",
            "business_name": "Traders & Co",
            "business_type": "Partnership Firm",
            "service_required": "Annual Audit & Accounting",
            "number_of_transactions": "1000+",
            "address": "Business Center, Bangalore",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560001",
            "status": "Under Review",
            "created_at": datetime.now() - timedelta(days=7),
            "updated_at": datetime.now() - timedelta(days=5)
        },
        {
            "application_id": "ACC202401003",
            "full_name": "Vikram Saxena",
            "email": "vikram@services.com",
            "phone": "7654321098",
            "pan_number": "AABQC9876R",
            "business_name": "Services Private Limited",
            "business_type": "Private Limited",
            "service_required": "Quarterly Compliance & Tax Planning",
            "number_of_transactions": "500-1000",
            "address": "Service Tower, Delhi",
            "city": "Delhi",
            "state": "Delhi",
            "pincode": "110001",
            "status": "Approved",
            "created_at": datetime.now() - timedelta(days=15),
            "updated_at": datetime.now() - timedelta(days=13)
        },
        {
            "application_id": "ACC202401004",
            "full_name": "Nisha Menon",
            "email": "nisha@enterprise.com",
            "phone": "6543210987",
            "pan_number": "AABQD2345S",
            "business_name": "Enterprise Solutions Pvt Ltd",
            "business_type": "Private Limited",
            "service_required": "Payroll Processing & HR Accounting",
            "number_of_transactions": "200-500",
            "address": "Enterprise Park, Pune",
            "city": "Pune",
            "state": "Maharashtra",
            "pincode": "411001",
            "status": "Pending",
            "created_at": datetime.now() - timedelta(days=2),
            "updated_at": datetime.now() - timedelta(days=2)
        },
        {
            "application_id": "ACC202401005",
            "full_name": "Arun Pillai",
            "email": "arun@import.com",
            "phone": "5432109876",
            "pan_number": "AABQE6789T",
            "business_name": "Import-Export Traders",
            "business_type": "Partnership",
            "service_required": "GST & Income Tax Compliance",
            "number_of_transactions": "1000+",
            "address": "Trade Complex, Chennai",
            "city": "Chennai",
            "state": "Tamil Nadu",
            "pincode": "600001",
            "status": "In Progress",
            "created_at": datetime.now() - timedelta(days=8),
            "updated_at": datetime.now() - timedelta(days=6)
        }
    ]
    
    try:
        collection.insert_many(applications, ordered=False)
        print(f"✅ Seeded {len(applications)} Accounting & Bookkeeping applications")
    except DuplicateKeyError:
        print("⚠️  Some Accounting & Bookkeeping applications already exist")

def main():
    """Main function to seed all data"""
    try:
        print("🚀 Starting to seed all 6 corporate services data...\n")
        
        db = connect_db()
        
        # Seed all 6 services
        seed_legal_advice_applications(db)
        seed_provident_fund_applications(db)
        seed_tds_services_applications(db)
        seed_gst_services_applications(db)
        seed_payroll_services_applications(db)
        seed_accounting_bookkeeping_applications(db)
        
        print("\n✅ All services seeded successfully!")
        print("📊 Total: 30 sample applications created (5 per service)")
        print("\n🎯 Now you can:")
        print("   1. Search for applications by name, email, phone, service, or ID")
        print("   2. Filter by any of the 9 services (all will now have data)")
        print("   3. View complete application details in the modal")
        print("   4. Export filtered results to CSV")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
