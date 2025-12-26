import sys
sys.path.insert(0, 'cashper_backend')

from pymongo import MongoClient
from app.config import mongo_url, mongo_db
from datetime import datetime
import random

try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['RetailServiceApplications']
    
    # User email - change this to match your logged in email
    print("=" * 70)
    print("ADDING TEST DATA FOR BANK ACCOUNT, TRADING, AND DOCUMENT UPDATE")
    print("=" * 70)
    
    user_email = input("\nEnter your logged-in email (or press Enter for 'test@test.com'): ").strip()
    if not user_email:
        user_email = "test@test.com"
    
    print(f"\nChecking existing data for: {user_email}")
    
    # Check current applications for this user
    existing_apps = list(col.find({"email": user_email}))
    print(f"Found {len(existing_apps)} existing applications")
    
    # Service types to add
    services_to_add = [
        {"type": "bank-account", "name": "Bank Account Services"},
        {"type": "trading-demat", "name": "Online Trading & Demat"},
        {"type": "document-update", "name": "Update Aadhaar or PAN Details"}
    ]
    
    added_count = 0
    
    for service in services_to_add:
        # Check if user already has this service
        existing = col.find_one({"email": user_email, "serviceType": service["type"]})
        
        if existing:
            print(f"✓ Already exists: {service['name']}")
        else:
            # Add new application
            app_id = f"{service['type'].upper()[:4]}{random.randint(10000, 99999)}"
            
            new_app = {
                "email": user_email,
                "applicantName": "Test User",
                "phone": "9876543210",
                "serviceType": service["type"],
                "status": "pending",
                "createdAt": datetime.now(),
                "applicationId": app_id,
                "documents": {}
            }
            
            col.insert_one(new_app)
            print(f"✅ Added: {service['name']} (ID: {app_id})")
            added_count += 1
    
    print("\n" + "=" * 70)
    print(f"SUMMARY: Added {added_count} new applications")
    print("=" * 70)
    
    # Show all applications for this user
    all_user_apps = list(col.find({"email": user_email}))
    print(f"\nTotal applications for {user_email}: {len(all_user_apps)}")
    
    service_counts = {}
    for app in all_user_apps:
        service = app.get("serviceType", "unknown")
        service_counts[service] = service_counts.get(service, 0) + 1
    
    print("\nBreakdown by service:")
    for service, count in service_counts.items():
        print(f"  {service}: {count}")
    
    print("\n✅ Done! Refresh your browser to see the applications.")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
