"""Check admin user in database"""
import sys
sys.path.append('cashper_backend')

from app.database.db import get_database

db = get_database()
admin = db['users'].find_one({'role': 'admin'})

if admin:
    print(f"Admin Email: {admin.get('email')}")
    print(f"Admin Name: {admin.get('fullName')}")
    print(f"Admin Role: {admin.get('role')}")
else:
    print("No admin user found!")
    print("\nLet's check all users:")
    users = db['users'].find().limit(5)
    for user in users:
        print(f"  - {user.get('email')} ({user.get('role', 'user')})")
