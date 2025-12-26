from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client['cashper_db']

# Get user
user = db.users.find_one({"email": "sudha@gmail.com"})
user_id = str(user.get("_id"))

print('=== DATABASE CHECK ===')
print(f'User ID: {user_id}')
print(f'User Email: {user.get("email")}')

print('\n=== ALL SHORT TERM LOANS (with userId info) ===')
all_loans = list(db.short_term_loans.find())
print(f'Total Short Term Loans in database: {len(all_loans)}')

for idx, loan in enumerate(all_loans, 1):
    print(f'\nLoan {idx}:')
    print(f'  _id: {loan.get("_id")}')
    print(f'  fullName: {loan.get("fullName")}')
    print(f'  email: {loan.get("email")}')
    print(f'  loanAmount: {loan.get("loanAmount")}')
    print(f'  userId: {loan.get("userId")}')
    print(f'  userId matches? {loan.get("userId") == user_id}')
    print(f'  status: {loan.get("status")}')
    print(f'  application_id: {loan.get("application_id")}')

print(f'\n=== FILTER TEST ===')
user_loans = list(db.short_term_loans.find({"userId": user_id}))
print(f'Loans with userId={user_id}: {len(user_loans)}')

if len(user_loans) == 0:
    print('\n❌ NO LOANS FOUND FOR THIS USER!')
    print('This is why dashboard is empty.')
    
    # Check if there are loans with this email
    email_loans = list(db.short_term_loans.find({"email": user.get("email")}))
    print(f'\nLoans with email={user.get("email")}: {len(email_loans)}')
    
    if len(email_loans) > 0:
        print('\n⚠️ Found loans with matching email but wrong/null userId')
        print('Fixing them now...')
        
        for loan in email_loans:
            result = db.short_term_loans.update_one(
                {"_id": loan.get("_id")},
                {"$set": {"userId": user_id}}
            )
            print(f'  ✅ Fixed loan {loan.get("_id")}')
        
        print('\n✅ All loans fixed! Dashboard should now show the data.')
else:
    print(f'\n✅ Found {len(user_loans)} loans for this user')
    for loan in user_loans:
        print(f'  - {loan.get("fullName")} | ₹{loan.get("loanAmount")}')
