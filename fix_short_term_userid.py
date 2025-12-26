from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client['cashper_db']

# Get user
user = db.users.find_one({"email": "sudha@gmail.com"})
if not user:
    print('User not found!')
    exit()

user_id = str(user.get("_id"))
print(f'User ID: {user_id}')
print(f'Email: {user.get("email")}')

# Find Short Term Loans with null userId
print('\n=== Fixing Short Term Loans with null userId ===')
loans_to_fix = list(db.short_term_loans.find({"userId": None}))
print(f'Found {len(loans_to_fix)} loans with null userId')

if loans_to_fix:
    for loan in loans_to_fix:
        print(f'\nFixing loan: {loan.get("_id")}')
        print(f'  Email: {loan.get("email")}')
        
        # Update userId if email matches
        if loan.get("email") == user.get("email"):
            result = db.short_term_loans.update_one(
                {"_id": loan.get("_id")},
                {"$set": {"userId": user_id}}
            )
            print(f'  ✅ Updated userId to {user_id}')
        else:
            print(f'  ⚠️  Email does not match, skipping')

# Verify
print('\n=== Verification ===')
total_with_userid = db.short_term_loans.count_documents({"userId": user_id})
total_null = db.short_term_loans.count_documents({"userId": None})
print(f'Short Term Loans with userId: {total_with_userid}')
print(f'Short Term Loans with null userId: {total_null}')
