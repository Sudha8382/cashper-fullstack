import requests
import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Direct database insert instead of API to avoid crashing
uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(uri)
db = client['cashper_db']
policies_collection = db['insurance_policies']

# Sample policies
sample_policies = [
    {
        "customer": "Deepak Sharma",
        "email": "deepak@gmail.com",
        "phone": "+91 98765 43220",
        "type": "Health Insurance",
        "premium": "₹22,000/year",
        "coverage": "₹20 Lakhs",
        "status": "Active",
        "startDate": "2024-01-05",
        "endDate": "2025-01-05",
        "nominee": "Family",
        "documents": ["pan_card.pdf", "health_certificate.pdf", "aadhaar.pdf"]
    },
    {
        "customer": "Pooja Kapoor",
        "email": "pooja@gmail.com",
        "phone": "+91 98765 43221",
        "type": "Motor Insurance",
        "premium": "₹11,000/year",
        "coverage": "₹10 Lakhs",
        "status": "Expired",
        "startDate": "2023-01-01",
        "endDate": "2024-01-01",
        "nominee": "Self",
        "documents": ["driving_license.pdf", "rc_book.pdf"]
    },
    {
        "customer": "Arjun Malhotra",
        "email": "arjun@gmail.com",
        "phone": "+91 98765 43222",
        "type": "Term Insurance",
        "premium": "₹30,000/year",
        "coverage": "₹3 Crore",
        "status": "Active",
        "startDate": "2024-05-01",
        "endDate": "2044-05-01",
        "nominee": "Spouse",
        "documents": ["pan_card.pdf", "medical_report.pdf", "income_proof.pdf"]
    },
    {
        "customer": "Sunita Rao",
        "email": "sunita@gmail.com",
        "phone": "+91 98765 43223",
        "type": "Health Insurance",
        "premium": "₹19,000/year",
        "coverage": "₹18 Lakhs",
        "status": "Active",
        "startDate": "2023-12-01",
        "endDate": "2024-12-01",
        "nominee": "Husband",
        "documents": ["pan_card.pdf", "health_certificate.pdf"]
    },
    {
        "customer": "Mohit Desai",
        "email": "mohit@gmail.com",
        "phone": "+91 98765 43224",
        "type": "Motor Insurance",
        "premium": "₹10,500/year",
        "coverage": "₹7 Lakhs",
        "status": "Active",
        "startDate": "2024-03-10",
        "endDate": "2025-03-10",
        "nominee": "Father",
        "documents": ["driving_license.pdf", "rc_book.pdf", "insurance_form.pdf"]
    }
]

print("\n" + "="*50)
print("INSERTING REMAINING POLICIES DIRECTLY TO DATABASE")
print("="*50)

success = 0
for idx, policy in enumerate(sample_policies, 11):
    try:
        # Generate policy ID
        existing_count = policies_collection.count_documents({})
        policy_id = f"INS{str(existing_count + 1).zfill(3)}"
        
        # Add policyId to policy data
        policy['policyId'] = policy_id
        policy['createdAt'] = __import__('datetime').datetime.utcnow()
        
        # Insert directly
        result = policies_collection.insert_one(policy)
        print(f"\n[{idx}/15] ✅ {policy['customer']}")
        print(f"   Policy ID: {policy_id}")
        print(f"   Documents: {', '.join(policy['documents'])}")
        success += 1
    except Exception as e:
        print(f"\n[{idx}/15] ❌ Error: {str(e)}")

print("\n" + "="*50)
print(f"✅ Successfully inserted {success} more policies")
print(f"📊 Total policies now: {policies_collection.count_documents({})}")
print("="*50)

# Verify
print("\n📋 Policy Summary:")
policies = list(policies_collection.find({}, {'policyId': 1, 'customer': 1, 'documents': 1}))
for p in policies:
    docs = p.get('documents', [])
    print(f"  {p['policyId']}: {p['customer']} ({len(docs)} documents)")
