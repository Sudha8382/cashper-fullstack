"""
Seed loan applications for testing
This script adds sample loan applications to the database
"""

import sys
import os
from datetime import datetime, timedelta
from pymongo import MongoClient
import random

# Add the parent directory to the path to import app modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.config import mongo_url, mongo_db

def seed_loan_applications():
    """Seed loan applications into the database"""
    
    sample_applications = [
        {
            "customer": "Rajesh Kumar",
            "email": "rajesh.kumar@example.com",
            "phone": "+91 98765 43210",
            "type": "Personal Loan",
            "amount": 500000,
            "status": "Pending",
            "appliedDate": (datetime.utcnow() - timedelta(days=5)).isoformat(),
            "tenure": 36,
            "interestRate": 12.5,
            "purpose": "Medical Emergency",
            "income": "60000",
            "cibilScore": 750,
            "documents": ["aadhar.pdf", "pancard.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Priya Singh",
            "email": "priya.Singh@example.com",
            "phone": "+91 97654 32109",
            "type": "Home Loan",
            "amount": 3000000,
            "status": "Under Review",
            "appliedDate": (datetime.utcnow() - timedelta(days=10)).isoformat(),
            "tenure": 180,
            "interestRate": 7.5,
            "purpose": "Home Purchase",
            "income": "150000",
            "cibilScore": 800,
            "documents": ["aadhar.pdf", "pancard.pdf", "salary_slip.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Amit Patel",
            "email": "amit.patel@example.com",
            "phone": "+91 96543 21098",
            "type": "Business Loan",
            "amount": 1000000,
            "status": "Approved",
            "appliedDate": (datetime.utcnow() - timedelta(days=15)).isoformat(),
            "tenure": 60,
            "interestRate": 11.0,
            "purpose": "Business Expansion",
            "income": "200000",
            "cibilScore": 780,
            "documents": ["aadhar.pdf", "pancard.pdf", "business_proof.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Divya Sharma",
            "email": "divya.sharma@example.com",
            "phone": "+91 95432 10987",
            "type": "Education Loan",
            "amount": 800000,
            "status": "Rejected",
            "appliedDate": (datetime.utcnow() - timedelta(days=20)).isoformat(),
            "tenure": 84,
            "interestRate": 8.5,
            "purpose": "Higher Education",
            "income": "0",
            "cibilScore": 650,
            "documents": ["aadhar.pdf", "pancard.pdf"],
            "rejectionReason": "CIBIL score below minimum threshold",
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Vikram Mehta",
            "email": "vikram.mehta@example.com",
            "phone": "+91 94321 09876",
            "type": "Vehicle Loan",
            "amount": 600000,
            "status": "Disbursed",
            "appliedDate": (datetime.utcnow() - timedelta(days=25)).isoformat(),
            "tenure": 60,
            "interestRate": 10.5,
            "purpose": "Car Purchase",
            "income": "80000",
            "cibilScore": 770,
            "documents": ["aadhar.pdf", "pancard.pdf", "driving_license.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Neha Gupta",
            "email": "neha.gupta@example.com",
            "phone": "+91 93210 98765",
            "type": "Personal Loan",
            "amount": 250000,
            "status": "Pending",
            "appliedDate": (datetime.utcnow() - timedelta(days=2)).isoformat(),
            "tenure": 24,
            "interestRate": 13.0,
            "purpose": "Debt Consolidation",
            "income": "45000",
            "cibilScore": 700,
            "documents": ["aadhar.pdf", "pancard.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Arjun Reddy",
            "email": "arjun.reddy@example.com",
            "phone": "+91 92109 87654",
            "type": "Personal Loan",
            "amount": 350000,
            "status": "Under Review",
            "appliedDate": (datetime.utcnow() - timedelta(days=7)).isoformat(),
            "tenure": 36,
            "interestRate": 12.0,
            "purpose": "Wedding Expenses",
            "income": "55000",
            "cibilScore": 740,
            "documents": ["aadhar.pdf", "pancard.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Pooja Verma",
            "email": "pooja.verma@example.com",
            "phone": "+91 91098 76543",
            "type": "Home Loan",
            "amount": 2500000,
            "status": "Approved",
            "appliedDate": (datetime.utcnow() - timedelta(days=12)).isoformat(),
            "tenure": 180,
            "interestRate": 7.8,
            "purpose": "Home Purchase",
            "income": "120000",
            "cibilScore": 820,
            "documents": ["aadhar.pdf", "pancard.pdf", "salary_slip.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Sanjay Das",
            "email": "sanjay.das@example.com",
            "phone": "+91 90987 65432",
            "type": "Business Loan",
            "amount": 1500000,
            "status": "Disbursed",
            "appliedDate": (datetime.utcnow() - timedelta(days=30)).isoformat(),
            "tenure": 60,
            "interestRate": 10.5,
            "purpose": "Shop Renovation",
            "income": "180000",
            "cibilScore": 790,
            "documents": ["aadhar.pdf", "pancard.pdf", "business_proof.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
        {
            "customer": "Meera Nair",
            "email": "meera.nair@example.com",
            "phone": "+91 89876 54321",
            "type": "Personal Loan",
            "amount": 400000,
            "status": "Pending",
            "appliedDate": (datetime.utcnow() - timedelta(days=3)).isoformat(),
            "tenure": 36,
            "interestRate": 12.5,
            "purpose": "Medical Treatment",
            "income": "65000",
            "cibilScore": 760,
            "documents": ["aadhar.pdf", "pancard.pdf"],
            "rejectionReason": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        },
    ]
    
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_url)
        db = client[mongo_db]
        applications_collection = db["admin_loan_applications"]  # Correct collection name
        
        # Clear existing data
        result = applications_collection.delete_many({})
        print(f"[INFO] Deleted {result.deleted_count} existing applications\n")
        
        # Insert sample applications
        result = applications_collection.insert_many(sample_applications)
        
        print(f"[PASS] Successfully seeded {len(result.inserted_ids)} loan applications")
        print(f"\nStatistics:")
        print(f"  Total: {len(sample_applications)}")
        
        # Count by status
        statuses = {}
        for app in sample_applications:
            status = app['status']
            statuses[status] = statuses.get(status, 0) + 1
        
        for status, count in statuses.items():
            print(f"  {status}: {count}")
        
        print(f"\n[PASS] Seeding completed successfully!")
        
    except Exception as e:
        print(f"[ERROR] Error seeding applications: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    print("="*60)
    print("Seeding Loan Applications")
    print("="*60 + "\n")
    seed_loan_applications()
    print("="*60)
