#!/usr/bin/env python3
"""
Check and verify admin user password in database
"""

from app.database.repository.user_repository import user_repository
from app.utils.security import verify_password, hash_password
from datetime import datetime

def check_admin_users():
    """Check all admin users in database"""
    collection = user_repository.get_collection()
    
    # Find all admin users
    admin_users = list(collection.find({"isAdmin": True}))
    
    print(f"\n{'='*60}")
    print(f"Found {len(admin_users)} admin user(s)")
    print(f"{'='*60}\n")
    
    for i, admin in enumerate(admin_users, 1):
        print(f"Admin User #{i}:")
        print(f"  ID: {admin.get('_id')}")
        print(f"  Email: {admin.get('email')}")
        print(f"  Full Name: {admin.get('fullName')}")
        print(f"  Has Password Hash: {'hashedPassword' in admin}")
        print(f"  Created At: {admin.get('createdAt')}")
        print(f"  Updated At: {admin.get('updatedAt')}")
        print()

def test_password_verification(email, password):
    """Test password verification for a user"""
    collection = user_repository.get_collection()
    user = collection.find_one({"email": email.lower()})
    
    if not user:
        print(f"❌ User with email '{email}' not found")
        return False
    
    print(f"\n{'='*60}")
    print(f"Testing password for: {email}")
    print(f"{'='*60}")
    print(f"User ID: {user.get('_id')}")
    print(f"Has hashedPassword: {'hashedPassword' in user}")
    
    if 'hashedPassword' not in user:
        print("❌ User has no hashedPassword field")
        return False
    
    try:
        is_valid = verify_password(password, user["hashedPassword"])
        if is_valid:
            print(f"✅ Password is CORRECT")
        else:
            print(f"❌ Password is INCORRECT")
        return is_valid
    except Exception as e:
        print(f"❌ Error verifying password: {str(e)}")
        return False

def update_admin_password(email, new_password):
    """Update admin password"""
    from app.utils.security import hash_password
    
    collection = user_repository.get_collection()
    user = collection.find_one({"email": email.lower()})
    
    if not user:
        print(f"❌ User with email '{email}' not found")
        return False
    
    print(f"\n{'='*60}")
    print(f"Updating password for: {email}")
    print(f"{'='*60}")
    
    hashed_password = hash_password(new_password)
    result = collection.update_one(
        {"_id": user["_id"]},
        {
            "$set": {
                "hashedPassword": hashed_password,
                "updatedAt": datetime.utcnow()
            }
        }
    )
    
    if result.modified_count > 0:
        print(f"✅ Password updated successfully")
        
        # Verify the update
        updated_user = collection.find_one({"_id": user["_id"]})
        is_valid = verify_password(new_password, updated_user["hashedPassword"])
        if is_valid:
            print(f"✅ Verification successful - new password works")
            return True
        else:
            print(f"❌ Verification failed - new password doesn't work")
            return False
    else:
        print(f"❌ Failed to update password")
        return False

def merge_admin_users():
    """Merge duplicate admin users, keeping the most recent one"""
    collection = user_repository.get_collection()
    
    # Find all admin users
    admin_users = list(collection.find({"isAdmin": True}).sort("updatedAt", -1))
    
    if len(admin_users) <= 1:
        print(f"✅ Only {len(admin_users)} admin user(s) found - no merge needed")
        return
    
    print(f"\n{'='*60}")
    print(f"Found {len(admin_users)} admin user(s) - merging to keep most recent")
    print(f"{'='*60}\n")
    
    # Keep the most recent one (first in descending order)
    keeper = admin_users[0]
    print(f"Keeping: {keeper.get('email')} (Updated: {keeper.get('updatedAt')})")
    
    # Delete the rest
    for i, admin in enumerate(admin_users[1:], 1):
        print(f"Deleting duplicate #{i}: {admin.get('email')} (Updated: {admin.get('updatedAt')})")
        result = collection.delete_one({"_id": admin["_id"]})
        if result.deleted_count > 0:
            print(f"  ✅ Deleted successfully")
        else:
            print(f"  ❌ Failed to delete")

if __name__ == "__main__":
    import sys
    
    print("\n" + "="*60)
    print("ADMIN USER PASSWORD CHECKER & FIXER")
    print("="*60)
    
    # Check all admin users
    check_admin_users()
    
    # Merge duplicate admin users
    merge_admin_users()
    
    # Example usage
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "test":
            email = sys.argv[2] if len(sys.argv) > 2 else "admin@cashper.com"
            password = sys.argv[3] if len(sys.argv) > 3 else "admin123"
            test_password_verification(email, password)
        
        elif command == "update":
            email = sys.argv[2] if len(sys.argv) > 2 else "admin@cashper.com"
            password = sys.argv[3] if len(sys.argv) > 3 else "NewAdmin123!"
            update_admin_password(email, password)
    
    print("\n" + "="*60)
    print("Usage:")
    print("  python check_admin_password.py test <email> <password>")
    print("  python check_admin_password.py update <email> <new_password>")
    print("="*60 + "\n")
