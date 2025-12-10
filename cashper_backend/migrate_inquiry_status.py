#!/usr/bin/env python3
"""
Migration script to add status field to all inquiry records
Ensures all inquiries have a status for proper filtering
"""
from pymongo import MongoClient
from app.database.db import get_database
from datetime import datetime

def migrate_inquiries():
    """Add status field to all inquiry collections"""
    
    db = get_database()
    
    collections_to_migrate = [
        "short_term_loan_get_in_touch",
        "personal_loan_get_in_touch",
        "business_loan_get_in_touch",
        "home_loan_get_in_touch",
        "term_insurance_inquiries",
        "motor_insurance_inquiries",
        "health_insurance_inquiries",
        "sip_inquiries",
        "mutual_funds_inquiries",
        "short_term_get_in_touch"
    ]
    
    for collection_name in collections_to_migrate:
        try:
            collection = db[collection_name]
            
            # Count documents without status
            no_status_count = collection.count_documents({"status": {"$exists": False}})
            
            if no_status_count > 0:
                print(f"\n{collection_name}:")
                print(f"  - Documents without status: {no_status_count}")
                
                # Update all documents without status to "pending"
                result = collection.update_many(
                    {"status": {"$exists": False}},
                    {"$set": {"status": "pending", "updated_at": datetime.utcnow()}}
                )
                
                print(f"  - Updated: {result.modified_count} documents")
                
                # Show status breakdown
                pending_count = collection.count_documents({"status": "pending"})
                confirmed_count = collection.count_documents({"status": "confirmed"})
                completed_count = collection.count_documents({"status": "completed"})
                cancelled_count = collection.count_documents({"status": "cancelled"})
                
                print(f"  - Status breakdown:")
                print(f"    - Pending: {pending_count}")
                print(f"    - Confirmed: {confirmed_count}")
                print(f"    - Completed: {completed_count}")
                print(f"    - Cancelled: {cancelled_count}")
            else:
                total_count = collection.count_documents({})
                if total_count > 0:
                    print(f"\n{collection_name}: Already has status field")
                    
                    pending_count = collection.count_documents({"status": "pending"})
                    confirmed_count = collection.count_documents({"status": "confirmed"})
                    completed_count = collection.count_documents({"status": "completed"})
                    cancelled_count = collection.count_documents({"status": "cancelled"})
                    
                    print(f"  - Pending: {pending_count}")
                    print(f"  - Confirmed: {confirmed_count}")
                    print(f"  - Completed: {completed_count}")
                    print(f"  - Cancelled: {cancelled_count}")
                    
        except Exception as e:
            print(f"\n{collection_name}: Skipped (collection may not exist)")

if __name__ == "__main__":
    print("Starting inquiry migration...")
    migrate_inquiries()
    print("\nMigration complete!")
