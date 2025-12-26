from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client['cashper_db']

print('=== Checking User: bhoomi.sudha83@gmail.com ===')
user = db.users.find_one({"email": "bhoomi.sudha83@gmail.com"})

if not user:
    print('❌ User NOT FOUND in database')
    print('\nChecking sudha@gmail.com instead...')
    user = db.users.find_one({"email": "sudha@gmail.com"})
    if user:
        print(f'✓ Found: sudha@gmail.com')
    else:
        print('❌ No user found')
        exit()

user_id = str(user.get("_id"))
print(f'\n✓ User Found:')
print(f'  Email: {user.get("email")}')
print(f'  Name: {user.get("name")}')
print(f'  User ID: {user_id}')
print(f'  Is Admin: {user.get("isAdmin")}')

print(f'\n=== Loans for this User ===')
personal = db.personal_loans.count_documents({"userId": user_id})
home = db.home_loans.count_documents({"userId": user_id})
business = db.business_loans.count_documents({"userId": user_id})
short_term = db.short_term_loans.count_documents({"userId": user_id})

print(f'Personal Loans: {personal}')
print(f'Home Loans: {home}')
print(f'Business Loans: {business}')
print(f'Short Term Loans: {short_term}')
print(f'TOTAL: {personal + home + business + short_term}')

if personal > 0:
    print(f'\n=== Personal Loans ===')
    for loan in db.personal_loans.find({"userId": user_id}):
        print(f'  - {loan.get("fullName")} | ₹{loan.get("loanAmount")} | {loan.get("status")}')

if home > 0:
    print(f'\n=== Home Loans ===')
    for loan in db.home_loans.find({"userId": user_id}):
        print(f'  - {loan.get("fullName")} | ₹{loan.get("loanAmount")} | {loan.get("status")}')

if business > 0:
    print(f'\n=== Business Loans ===')
    for loan in db.business_loans.find({"userId": user_id}):
        print(f'  - {loan.get("fullName")} | ₹{loan.get("loanAmount")} | {loan.get("status")}')

if short_term > 0:
    print(f'\n=== Short Term Loans ===')
    for loan in db.short_term_loans.find({"userId": user_id}):
        print(f'  - {loan.get("fullName")} | ₹{loan.get("loanAmount")} | {loan.get("status")}')

# Check all users
print(f'\n=== All Users in Database ===')
for u in db.users.find():
    print(f'  - {u.get("email")} (ID: {u.get("_id")})')
