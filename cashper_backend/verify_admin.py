"""
Script to verify and update admin user password
"""

import sys
import os
from datetime import datetime
from pymongo import MongoClient

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.utils.security import hash_password, verify_password
from app.config import mongo_url, mongo_db

def verify_and_update_admin():
    """Verify admin user exists and update password"""
    
    ADMIN_EMAIL = "sudha@123gmail.com"
    ADMIN_PASSWORD = "Sudha@123"
    
    try:
        client = MongoClient(mongo_url)
        db = client[mongo_db]
        users_collection = db["users"]
        
        # Get admin user
        admin_user = users_collection.find_one({"email": ADMIN_EMAIL.lower()})
        
        if not admin_user:
            print(f"❌ Admin user not found: {ADMIN_EMAIL}")
            return
        
        print(f"✅ Found admin user: {ADMIN_EMAIL}")
        print(f"   User ID: {admin_user['_id']}")
        print(f"   Full Name: {admin_user.get('fullName', 'N/A')}")
        print(f"   Role: {admin_user.get('role', 'N/A')}")
        print(f"   Active: {admin_user.get('isActive', False)}")
        
        # Check if password matches
        if admin_user.get('hashedPassword'):
            password_valid = verify_password(ADMIN_PASSWORD, admin_user['hashedPassword'])
            print(f"   Password Valid: {password_valid}")
            
            if not password_valid:
                print("\n⚠️  Password doesn't match. Updating password...")
                new_hashed_password = hash_password(ADMIN_PASSWORD)
                users_collection.update_one(
                    {"_id": admin_user["_id"]},
                    {"$set": {
                        "hashedPassword": new_hashed_password,
                        "role": "admin",
                        "isActive": True,
                        "updatedAt": datetime.utcnow()
                    }}
                )
                print(f"✅ Password updated successfully!")
        else:
            print("\n⚠️  No password set. Setting password...")
            new_hashed_password = hash_password(ADMIN_PASSWORD)
            users_collection.update_one(
                {"_id": admin_user["_id"]},
                {"$set": {
                    "hashedPassword": new_hashed_password,
                    "role": "admin",
                    "isActive": True,
                    "updatedAt": datetime.utcnow()
                }}
            )
            print(f"✅ Password set successfully!")
        
        # Ensure role is admin
        if admin_user.get('role') != 'admin':
            users_collection.update_one(
                {"_id": admin_user["_id"]},
                {"$set": {"role": "admin", "updatedAt": datetime.utcnow()}}
            )
            print(f"✅ Role updated to 'admin'")
        
        # Ensure account is active
        if not admin_user.get('isActive', False):
            users_collection.update_one(
                {"_id": admin_user["_id"]},
                {"$set": {"isActive": True, "updatedAt": datetime.utcnow()}}
            )
            print(f"✅ Account activated")
        
        print("\n" + "="*60)
        print("✅ Admin user is ready!")
        print(f"   Email: {ADMIN_EMAIL}")
        print(f"   Password: {ADMIN_PASSWORD}")
        print(f"   Role: admin")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    print("="*60)
    print("Verifying Admin User")
    print("="*60)
    verify_and_update_admin()
