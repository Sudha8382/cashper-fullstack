#!/usr/bin/env python3
"""Check short-term loans in admin collection"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend\.env')
MONGO_URL = os.getenv('MONGO_URL')
MONGO_DB = os.getenv('MONGO_DB', 'cashper_db')

client = MongoClient(MONGO_URL)
db = client[MONGO_DB]
col = db['admin_loan_applications']

# Get all short-term loans
short_term = list(col.find({'type': {'$regex': 'short-term', '$options': 'i'}}))
print(f'Short-term loans in admin collection: {len(short_term)}')
for loan in short_term:
    print(f'  - {loan.get("customer")}: {loan.get("type")}')

# Get all loan types
all_loans = list(col.find())
print(f'\nAll loans by type:')
types = {}
for loan in all_loans:
    t = loan.get('type', 'Unknown')
    types[t] = types.get(t, 0) + 1
for t, count in sorted(types.items()):
    print(f'  {t}: {count}')

client.close()
