import requests
import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Direct database insert
uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(uri)
db = client['cashper_db']
policies_collection = db['insurance_policies']

# Sample policies (first 10 that were created via API)
sample_policies = [
    {
        "policyId": "INS037",
        "customer": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "phone": "+91 98765 43210",
        "type": "Term Insurance",
        "premium": "₹12,000/year",
        "coverage": "₹1 Crore",
        "status": "Active",
        "startDate": "2024-01-01",
        "endDate": "2044-01-01",
        "nominee": "Mrs. Sharma",
        "documents": ["pan_card.pdf", "medical_report.pdf"]
    },
    {
        "policyId": "INS038",
        "customer": "Priya Patel",
        "email": "priya@gmail.com",
        "phone": "+91 98765 43211",
        "type": "Health Insurance",
        "premium": "₹18,000/year",
        "coverage": "₹10 Lakhs",
        "status": "Pending",
        "startDate": "2024-02-01",
        "endDate": "2025-02-01",
        "nominee": "Mr. Patel",
        "documents": ["pan_card.pdf", "health_certificate.pdf", "aadhaar.pdf"]
    },
    {
        "policyId": "INS039",
        "customer": "Amit Kumar",
        "email": "amit@gmail.com",
        "phone": "+91 98765 43212",
        "type": "Motor Insurance",
        "premium": "₹8,500/year",
        "coverage": "₹5 Lakhs",
        "status": "Active",
        "startDate": "2023-12-15",
        "endDate": "2024-12-15",
        "nominee": "Self",
        "documents": ["driving_license.pdf", "rc_book.pdf"]
    },
    {
        "policyId": "INS040",
        "customer": "Sneha Gupta",
        "email": "sneha@gmail.com",
        "phone": "+91 98765 43213",
        "type": "Term Insurance",
        "premium": "₹15,000/year",
        "coverage": "₹50 Lakhs",
        "status": "Expired",
        "startDate": "2020-03-01",
        "endDate": "2024-01-01",
        "nominee": "Parents",
        "documents": ["pan_card.pdf", "medical_report.pdf"]
    },
    {
        "policyId": "INS041",
        "customer": "Rajesh Verma",
        "email": "rajesh@gmail.com",
        "phone": "+91 98765 43214",
        "type": "Health Insurance",
        "premium": "₹20,000/year",
        "coverage": "₹15 Lakhs",
        "status": "Active",
        "startDate": "2024-03-01",
        "endDate": "2025-03-01",
        "nominee": "Wife",
        "documents": ["pan_card.pdf", "health_certificate.pdf"]
    },
    {
        "policyId": "INS042",
        "customer": "Anita Singh",
        "email": "anita@gmail.com",
        "phone": "+91 98765 43215",
        "type": "Motor Insurance",
        "premium": "₹9,500/year",
        "coverage": "₹8 Lakhs",
        "status": "Active",
        "startDate": "2024-01-20",
        "endDate": "2025-01-20",
        "nominee": "Husband",
        "documents": ["driving_license.pdf", "rc_book.pdf", "insurance_form.pdf"]
    },
    {
        "policyId": "INS043",
        "customer": "Vikram Reddy",
        "email": "vikram@gmail.com",
        "phone": "+91 98765 43216",
        "type": "Term Insurance",
        "premium": "₹25,000/year",
        "coverage": "₹2 Crore",
        "status": "Active",
        "startDate": "2023-11-01",
        "endDate": "2043-11-01",
        "nominee": "Spouse",
        "documents": ["pan_card.pdf", "medical_report.pdf", "income_proof.pdf"]
    },
    {
        "policyId": "INS044",
        "customer": "Meera Joshi",
        "email": "meera@gmail.com",
        "phone": "+91 98765 43217",
        "type": "Health Insurance",
        "premium": "₹16,000/year",
        "coverage": "₹12 Lakhs",
        "status": "Pending",
        "startDate": "2024-04-01",
        "endDate": "2025-04-01",
        "nominee": "Parents",
        "documents": ["pan_card.pdf", "health_certificate.pdf"]
    },
    {
        "policyId": "INS045",
        "customer": "Sanjay Mehta",
        "email": "sanjay@gmail.com",
        "phone": "+91 98765 43218",
        "type": "Motor Insurance",
        "premium": "₹7,500/year",
        "coverage": "₹4 Lakhs",
        "status": "Active",
        "startDate": "2024-02-15",
        "endDate": "2025-02-15",
        "nominee": "Self",
        "documents": ["driving_license.pdf", "rc_book.pdf"]
    },
    {
        "policyId": "INS046",
        "customer": "Kavita Agarwal",
        "email": "kavita@gmail.com",
        "phone": "+91 98765 43219",
        "type": "Term Insurance",
        "premium": "₹18,000/year",
        "coverage": "₹75 Lakhs",
        "status": "Active",
        "startDate": "2023-10-01",
        "endDate": "2043-10-01",
        "nominee": "Children",
        "documents": ["pan_card.pdf", "medical_report.pdf"]
    }
]

print("\n" + "="*50)
print("BULK INSERTING ALL POLICIES TO DATABASE")
print("="*50)

# Clear existing policies for clean data
policies_collection.delete_many({})
print("✅ Cleared existing policies")

success = 0
for idx, policy in enumerate(sample_policies, 1):
    try:
        policy['createdAt'] = datetime.utcnow()
        policies_collection.insert_one(policy)
        print(f"[{idx:2d}/10] ✅ {policy['customer']:20s} | {policy['policyId']} | {len(policy['documents'])} docs")
        success += 1
    except Exception as e:
        print(f"[{idx:2d}/10] ❌ Error: {str(e)}")

print("\n" + "="*50)
print(f"✅ Successfully inserted {success} policies")
print(f"📊 Total policies now: {policies_collection.count_documents({})}")
print("="*50)

# Verify
print("\n📋 All Policies in Database:")
policies = list(policies_collection.find({}, {'policyId': 1, 'customer': 1, 'documents': 1}).sort('policyId', 1))
for p in policies:
    docs = p.get('documents', [])
    print(f"  {p['policyId']}: {p['customer']:20s} ({len(docs)} documents)")
