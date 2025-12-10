"""
Keep only the 16 newly seeded loans and delete all others
"""

from pymongo import MongoClient
from datetime import datetime, timedelta

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["cashper_db"]
    collection = db["admin_loan_applications"]
    
    print("Cleaning database...")
    print("="*60)
    
    # Get all documents
    all_docs = list(collection.find({}))
    print(f"Total documents before: {len(all_docs)}")
    
    # Keep only documents with our 4 loan types
    valid_types = ["Home Loan", "Personal Loan", "Business Loan", "Short-term Loan"]
    
    # Count by type
    print("\nCurrent counts:")
    for loan_type in valid_types:
        count = collection.count_documents({"type": loan_type})
        print(f"  {loan_type}: {count}")
    
    # Delete all but the last 16 created (our seed data)
    # Delete documents that have other types or are old
    result = collection.delete_many({
        "$or": [
            {"type": {"$nin": valid_types}},  # Delete non-standard types
        ]
    })
    
    print(f"\nDeleted documents with invalid types: {result.deleted_count}")
    
    # Now delete old loans, keep only recent ones
    # Get the last 16 by date
    recent_loans = list(collection.find({}).sort("_id", -1).limit(16))
    recent_ids = [loan["_id"] for loan in recent_loans]
    
    result = collection.delete_many({
        "_id": {"$nin": recent_ids}
    })
    
    print(f"Deleted old loans: {result.deleted_count}")
    
    # Final count
    print("\n" + "="*60)
    print("After cleanup:")
    total = 0
    for loan_type in valid_types:
        count = collection.count_documents({"type": loan_type})
        total += count
        print(f"  {loan_type}: {count}")
    
    print(f"\nTotal loans: {total}")
    print("="*60)
    
    if total == 16:
        print("\n✓ Database cleaned successfully! Only 16 loans remain.")
    else:
        print(f"\n⚠ Warning: Expected 16 loans but found {total}")
    
except Exception as e:
    import traceback
    print(f"Error: {str(e)}")
    traceback.print_exc()
