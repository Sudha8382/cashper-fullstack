"""
Script to create an admin user in the database
Run this script once to add the admin user: sudha@123gmail.com
"""

import sys
import os
from datetime import datetime
from pymongo import MongoClient

# Add the parent directory to the path to import app modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.utils.security import hash_password
from app.config import mongo_url, mongo_db

def create_admin_user():
    """Create admin user if it doesn't exist"""
    
    # Admin credentials
    ADMIN_EMAIL = "sudha@123gmail.com"
    ADMIN_PASSWORD = "Sudha@123"
    ADMIN_NAME = "Sudha Admin"
    ADMIN_PHONE = "9999999999"
    
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_url)
        db = client[mongo_db]
        users_collection = db["users"]
        
        # Check if admin user already exists
        existing_admin = users_collection.find_one({"email": ADMIN_EMAIL.lower()})
        
        if existing_admin:
            print(f"⚠️  Admin user already exists: {ADMIN_EMAIL}")
            print(f"   User ID: {existing_admin['_id']}")
            print(f"   Role: {existing_admin.get('role', 'N/A')}")
            
            # Update role if it's not set to admin
            if existing_admin.get('role') != 'admin':
                users_collection.update_one(
                    {"email": ADMIN_EMAIL.lower()},
                    {"$set": {"role": "admin", "updatedAt": datetime.utcnow()}}
                )
                print("✅ Updated role to 'admin'")
            return
        
        # Hash the password
        hashed_password = hash_password(ADMIN_PASSWORD)
        
        # Create admin user document
        admin_user = {
            "fullName": ADMIN_NAME,
            "email": ADMIN_EMAIL.lower(),
            "phone": ADMIN_PHONE,
            "hashedPassword": hashed_password,
            "role": "admin",  # Admin role
            "authProvider": "email",
            "isEmailVerified": True,
            "isPhoneVerified": True,
            "isActive": True,
            "agreeToTerms": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": None
        }
        
        # Insert admin user
        result = users_collection.insert_one(admin_user)
        
        print("✅ Admin user created successfully!")
        print(f"   Email: {ADMIN_EMAIL}")
        print(f"   Password: {ADMIN_PASSWORD}")
        print(f"   Role: admin")
        print(f"   User ID: {result.inserted_id}")
        print("\n🔐 Use these credentials to login to the Admin Panel")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {str(e)}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    print("=" * 60)
    print("Creating Admin User")
    print("=" * 60)
    create_admin_user()
    print("=" * 60)
