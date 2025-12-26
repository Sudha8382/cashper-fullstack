#!/usr/bin/env python3
"""
Diagnostic script to check short-term loans in the database
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

from app.database.db import get_database
from bson import ObjectId

def check_short_term_loans():
    """Check all short-term loans in the database"""
    db = get_database()
    collection = db["short_term_loans"]
    
    print("\n" + "="*80)
    print("SHORT-TERM LOANS DATABASE DIAGNOSTIC")
    print("="*80)
    
    # Count total documents
    total = collection.count_documents({})
    print(f"\n📊 Total short-term loans in database: {total}")
    
    if total == 0:
        print("⚠️  No short-term loans found in database")
        return
    
    # Get all documents
    all_loans = list(collection.find().limit(10))
    
    print(f"\n📋 Sample of {len(all_loans)} loans:")
    print("-" * 80)
    
    for idx, loan in enumerate(all_loans, 1):
        print(f"\n📌 Loan #{idx}:")
        print(f"  _id: {loan.get('_id')} (type: {type(loan.get('_id')).__name__})")
        print(f"  applicationId: {loan.get('application_id', loan.get('applicationId', 'N/A'))}")
        print(f"  fullName: {loan.get('fullName', 'N/A')}")
        print(f"  email: {loan.get('email', 'N/A')}")
        print(f"  userId: {loan.get('userId')} (type: {type(loan.get('userId')).__name__ if loan.get('userId') else 'None'})")
        print(f"  status: {loan.get('status', 'N/A')}")
        print(f"  createdAt: {loan.get('createdAt', loan.get('created_at', 'N/A'))}")
    
    # Group by userId
    print(f"\n📈 Loans grouped by userId:")
    print("-" * 80)
    
    pipeline = [
        {
            "$group": {
                "_id": "$userId",
                "count": {"$sum": 1},
                "emails": {"$push": "$email"}
            }
        }
    ]
    
    results = list(collection.aggregate(pipeline))
    for result in results:
        user_id = result.get("_id")
        count = result.get("count", 0)
        emails = result.get("emails", [])
        print(f"\n  userId: {user_id}")
        print(f"  Count: {count}")
        print(f"  Emails: {emails}")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    try:
        check_short_term_loans()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
