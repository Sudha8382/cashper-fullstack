from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(uri)
db = client['cashper_db']
policies = db['insurance_policies']

# Get one policy with documents
policy = policies.find_one({'documents': {'$exists': True, '$ne': []}})
if policy:
    print('Policy found:')
    print('ID:', policy.get('_id'))
    print('Policy ID:', policy.get('policyId'))
    print('Documents:', policy.get('documents'))
    print('\nDocument names:', [doc if isinstance(doc, str) else doc.get('name') if isinstance(doc, dict) else doc for doc in policy.get('documents', [])])
else:
    print('No policies with documents found')
    print('Total policies:', policies.count_documents({}))
    
    # Show sample documents array structure
    sample = policies.find_one({})
    if sample:
        print('Sample policy:')
        print('- policyId:', sample.get('policyId'))
        print('- documents field:', sample.get('documents'))
