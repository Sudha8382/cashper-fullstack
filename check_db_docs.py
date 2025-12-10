#!/usr/bin/env python3
import sys
sys.path.insert(0, 'cashper_backend')
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv('cashper_backend/.env')
uri = os.getenv('MONGODB_URI')
client = MongoClient(uri)
db = client['cashper']

total = db['mutual_fund_applications'].count_documents({})
print(f"Total MF applications: {total}")

apps = list(db['mutual_fund_applications'].find({}))
print(f"Total found: {len(apps)}")

if apps:
    for i, app in enumerate(apps[-3:]):  # Last 3
        print(f"\n[{i}] {app.get('name', 'N/A')}")
        print(f"    Documents: {app.get('documents')}")
        print(f"    Status: {app.get('status')}")
