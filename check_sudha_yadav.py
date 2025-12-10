#!/usr/bin/env python3
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend\.env')
MONGO_URL = os.getenv('MONGO_URL')
client = MongoClient(MONGO_URL)
db = client['cashper_db']

# Check short-term collection
col = db['short_term_loan_applications']
doc = col.find_one({'fullName': 'Sudha Yadav'})
print('Found Sudha Yadav in short_term_loan_applications:')
if doc:
    print(f'  Name: {doc.get("fullName")}')
    print(f'  Status: {doc.get("status")}')
    print(f'  Amount: {doc.get("loanAmount")}')
    print(f'  Email: {doc.get("email")}')
    print(f'  Application ID: {doc.get("applicationId")}')
else:
    print('  NOT FOUND')

# Check all short-term count
count = col.count_documents({})
print(f'\nTotal short-term applications: {count}')

client.close()
