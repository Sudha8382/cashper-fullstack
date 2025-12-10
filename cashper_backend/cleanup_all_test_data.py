"""
Script to remove all test data from MongoDB
"""
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(MONGODB_URI)
db = client["cashper_db"]

print("🧹 Cleaning up test data from MongoDB...\n")

# Collections to clean
collections_to_clean = {
    "users": ["testauth@example.com", "sudha@123gmail.com"],
    "loan_applications": [],
    "mutual_fund_applications": [],
    "insurance_inquiries": [],
    "contact_inquiries": [],
    "admin_users": ["sudha@123gmail.com"],
}

try:
    # 1. Remove test users
    print("1️⃣ Removing test users...")
    users_collection = db["users"]
    test_user_emails = ["testauth@example.com", "sudha@123gmail.com"]
    
    for email in test_user_emails:
        result = users_collection.delete_many({"email": email})
        if result.deleted_count > 0:
            print(f"   ✓ Deleted {result.deleted_count} user(s) with email: {email}")
    
    # 2. Remove test admin users
    print("\n2️⃣ Removing test admin users...")
    admin_collection = db["admin_users"]
    admin_emails = ["sudha@123gmail.com"]
    
    for email in admin_emails:
        result = admin_collection.delete_many({"email": email})
        if result.deleted_count > 0:
            print(f"   ✓ Deleted {result.deleted_count} admin(s) with email: {email}")
    
    # 3. Optional: Clear collections created by test scripts
    print("\n3️⃣ Checking for empty or test collections...")
    
    # Get all collection names
    all_collections = db.list_collection_names()
    
    for collection_name in all_collections:
        collection = db[collection_name]
        count = collection.count_documents({})
        
        # Show collection sizes
        if count == 0:
            print(f"   - {collection_name}: Empty (0 documents)")
        else:
            print(f"   - {collection_name}: {count} documents")
    
    print("\n✅ Cleanup completed successfully!")
    print("\n📊 Final Database Status:")
    
    for collection_name in all_collections:
        collection = db[collection_name]
        count = collection.count_documents({})
        if count > 0:
            print(f"   {collection_name}: {count} documents")

except Exception as e:
    print(f"❌ Error during cleanup: {str(e)}")
finally:
    client.close()
    print("\n🔌 Database connection closed.")
