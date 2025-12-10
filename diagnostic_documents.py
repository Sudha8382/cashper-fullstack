#!/usr/bin/env python
"""
Diagnostic script to understand the document storage structure
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent / 'cashper_backend'))

from app.database.db import connect_to_mongo, get_db
from bson import ObjectId
import json

print("=" * 70)
print("DOCUMENT STORAGE DIAGNOSTIC")
print("=" * 70)

try:
    connect_to_mongo()
    db = get_db()
    
    # Check all collections that might have documents
    collections_to_check = [
        ('short_term_loan_applications', 'Short-term Loan'),
        ('home_loan_applications', 'Home Loan'),
        ('business_loan_applications', 'Business Loan'),
        ('personal_loan_applications', 'Personal Loan'),
        ('loan_applications', 'Admin Loan Applications')
    ]
    
    for collection_name, label in collections_to_check:
        try:
            collection = db[collection_name]
            count = collection.count_documents({})
            
            if count > 0:
                print(f"\n{label} ({collection_name}):")
                print(f"  Total documents: {count}")
                
                # Get a sample document with documents field
                sample = collection.find_one(
                    {f"$or": [
                        {"documents": {"$exists": True, "$ne": None, "$ne": []}},
                        {"pan": {"$exists": True, "$ne": None}},
                        {"aadhar": {"$exists": True, "$ne": None}},
                        {"bankStatement": {"$exists": True, "$ne": None}}
                    ]}
                )
                
                if sample:
                    print(f"  Sample document found:")
                    
                    # Show document fields
                    if 'documents' in sample and sample['documents']:
                        print(f"    - documents field: {sample['documents']}")
                    if 'pan' in sample and sample['pan']:
                        print(f"    - pan field: {sample['pan']}")
                    if 'aadhar' in sample and sample['aadhar']:
                        print(f"    - aadhar field: {sample['aadhar']}")
                    if 'bankStatement' in sample and sample['bankStatement']:
                        print(f"    - bankStatement field: {sample['bankStatement']}")
                    if 'salarySlip' in sample and sample['salarySlip']:
                        print(f"    - salarySlip field: {sample['salarySlip']}")
                    if 'photo' in sample and sample['photo']:
                        print(f"    - photo field: {sample['photo']}")
                else:
                    print(f"  No documents with document fields found")
        except Exception as e:
            print(f"  Error: {e}")
    
    # Check actual files in uploads directory
    print(f"\n{'=' * 70}")
    print("FILES IN UPLOADS DIRECTORY:")
    uploads_dir = Path("cashper_backend/uploads/documents")
    if uploads_dir.exists():
        files = list(uploads_dir.glob("*"))
        print(f"  Total files: {len(files)}")
        print(f"  Sample files:")
        for f in files[:5]:
            print(f"    - {f.name}")
        print(f"    ...")
    else:
        print(f"  Directory not found: {uploads_dir}")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

print(f"\n{'=' * 70}")
