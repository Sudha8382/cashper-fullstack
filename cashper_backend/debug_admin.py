"""
Debug admin login issue
"""
import sys
import os
from pymongo import MongoClient

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.utils.security import verify_password
from app.config import mongo_url, mongo_db

def debug_admin_login():
    """Debug admin login"""
    
    ADMIN_EMAIL = "sudha@123gmail.com"
    TEST_PASSWORD = "Sudha@123"
    
    try:
        client = MongoClient(mongo_url)
        db = client[mongo_db]
        users_collection = db["users"]
        
        # Get admin user
        admin_user = users_collection.find_one({"email": ADMIN_EMAIL.lower()})
        
        if not admin_user:
            print(f"❌ User not found: {ADMIN_EMAIL}")
            return
        
        print("="*60)
        print("Admin User Debug Info")
        print("="*60)
        print(f"Email in DB: {admin_user.get('email')}")
        print(f"Full Name: {admin_user.get('fullName')}")
        print(f"Role: {admin_user.get('role')}")
        print(f"Is Active: {admin_user.get('isActive')}")
        print(f"Has Password: {bool(admin_user.get('hashedPassword'))}")
        
        if admin_user.get('hashedPassword'):
            print(f"\nHashed Password (first 50 chars): {admin_user['hashedPassword'][:50]}...")
            
            # Test password verification
            is_valid = verify_password(TEST_PASSWORD, admin_user['hashedPassword'])
            print(f"\nPassword Test: '{TEST_PASSWORD}'")
            print(f"Password Valid: {is_valid}")
            
            if not is_valid:
                print("\n⚠️  PASSWORD MISMATCH!")
                print("Testing different password variations...")
                
                variations = [
                    "Sudha@123",
                    "sudha@123",
                    "Sudha@123 ",
                    " Sudha@123",
                ]
                
                for pwd in variations:
                    result = verify_password(pwd, admin_user['hashedPassword'])
                    print(f"  '{pwd}' -> {result}")
        else:
            print("\n❌ No password set in database!")
        
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    debug_admin_login()
