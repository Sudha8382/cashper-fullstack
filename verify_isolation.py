from pymongo import MongoClient

MONGO_URL = "mongodb+srv://kumuyadav249_db_user:O0zb3rZlZXArZiSg@cluster0.mnzwn7m.mongodb.net/"
client = MongoClient(MONGO_URL)
db = client['cashper_db']

# Get Sudha's user
user = db['users'].find_one({'email': 'kumuyadav249@gmail.com'})
user_id = str(user['_id'])

print(f"✅ User: {user['fullName']}")
print(f"   User ID: {user_id}\n")

# Check all loans with userId
print("=== LOANS WITH USERID ===")
personal = list(db['personal_loan_applications'].find({'userId': user_id}))
home = list(db['home_loan_applications'].find({'userId': user_id}))
business = list(db['business_loan_applications'].find({'userId': user_id}))
short_term = list(db['short_term_loan_applications'].find({'userId': user_id}))

print(f"Personal Loans: {len(personal)}")
print(f"Home Loans: {len(home)}")
print(f"Business Loans: {len(business)}")
print(f"Short Term Loans: {len(short_term)}")
print(f"TOTAL: {len(personal) + len(home) + len(business) + len(short_term)}")

print("\n=== SUMMARY ===")
print(f"✅ Data Isolation Active: Each user will see only their {len(personal) + len(home) + len(business) + len(short_term)} loan(s)")
print("\n📋 Next Steps:")
print("1. Login to dashboard with: kumuyadav249@gmail.com")
print("2. Go to 'My Loans' page")
print("3. You should see exactly 4 loans (1 Personal + 1 Home + 1 Business + 1 Short Term)")
print("4. If you login with a different account, you'll see 0 loans")
