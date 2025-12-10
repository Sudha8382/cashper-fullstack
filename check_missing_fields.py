#!/usr/bin/env python
"""Check for documents with missing fields"""
from pymongo import MongoClient
import os

mongo_url = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
client = MongoClient(mongo_url)
db = client['payloan']

collection = db['personal_tax_consultations']
docs = list(collection.find({}, {'_id': 1, 'name': 1, 'status': 1}).limit(20))
print('Personal Tax Consultations:')
for doc in docs:
    has_name = 'name' in doc
    doc_id = str(doc['_id'])
    status = doc.get('status', 'N/A')
    print(f'  ID: {doc_id[:20]}..., Has name: {has_name}, Status: {status}')

# Find documents without name
print('\nDocuments missing name field:')
missing_name = list(collection.find({'name': {'$exists': False}}))
print(f'Count: {len(missing_name)}')
if missing_name:
    print(f'Example: {missing_name[0]}')
