"""
Seed Sample Insurance Policy Data
Creates sample insurance policies matching the frontend structure
"""
import requests
import json
from datetime import datetime, timedelta

API_BASE_URL = "http://localhost:8000"

# Sample policies matching frontend data structure
sample_policies = [
    {
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
    },
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

def seed_insurance_policies():
    """Seed all insurance policies"""
    print("\n" + "="*50)
    print("SEEDING INSURANCE POLICY DATA")
    print("="*50)
    
    url = f"{API_BASE_URL}/api/admin/insurance-management/policies"
    
    success_count = 0
    failed_count = 0
    
    for idx, policy in enumerate(sample_policies, 1):
        try:
            print(f"\n[{idx}/{len(sample_policies)}] Creating policy for {policy['customer']}...")
            
            response = requests.post(url, json=policy)
            
            if response.status_code == 201:
                result = response.json()
                print(f"✅ SUCCESS - Policy ID: {result['id']}")
                print(f"   Type: {result['type']}")
                print(f"   Status: {result['status']}")
                print(f"   Coverage: {result['coverage']}")
                success_count += 1
            else:
                print(f"❌ FAILED - Status: {response.status_code}")
                print(f"   Error: {response.text}")
                failed_count += 1
        
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
            failed_count += 1
    
    print("\n" + "="*50)
    print("SEEDING SUMMARY")
    print("="*50)
    print(f"✅ Success: {success_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"📊 Total: {len(sample_policies)}")
    
    if success_count > 0:
        print("\n🎉 Insurance policies seeded successfully!")
        print(f"📌 You can now view them in the admin panel")
    
    return success_count > 0

if __name__ == "__main__":
    print("\n🚀 Starting Insurance Policy Data Seeding...")
    print(f"🌐 API Base URL: {API_BASE_URL}")
    
    try:
        # Test API connection
        response = requests.get(f"{API_BASE_URL}/health")
        if response.status_code == 200:
            print("✅ API is reachable")
        else:
            print("⚠️  API returned unexpected status")
    except Exception as e:
        print(f"❌ Cannot reach API: {str(e)}")
        print("Make sure the backend server is running!")
        exit(1)
    
    # Seed policies
    seed_insurance_policies()
