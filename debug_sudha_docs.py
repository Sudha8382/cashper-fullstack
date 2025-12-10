#!/usr/bin/env python3
"""Debug - check what type documents are being returned"""

import os
import sys
sys.path.insert(0, r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend')

from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

load_dotenv(r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend\.env')
MONGO_URL = os.getenv('MONGO_URL')

client = MongoClient(MONGO_URL)
db = client['cashper_db']

# Get Sudha Yadav
col = db['short_term_loan_applications']
sudha = col.find_one({'fullName': 'Sudha Yadav'})

if sudha:
    print("Sudha Yadav document from MongoDB:")
    print(f"  _id: {sudha.get('_id')}")
    print(f"  fullName: {sudha.get('fullName')}")
    print(f"  status: {sudha.get('status')}")
    print(f"  loanAmount: {sudha.get('loanAmount')}")
    
    print(f"\n  documents field:")
    docs = sudha.get('documents')
    print(f"    Value: {docs}")
    print(f"    Type: {type(docs)}")
    
    print(f"\n  Individual document fields:")
    for field in ["aadhar", "pan", "bankStatement", "salarySlip", "photo"]:
        val = sudha.get(field)
        if val:
            print(f"    {field}: {val} (type: {type(val).__name__})")

client.close()
