import sys
sys.path.insert(0, 'cashper_backend')

from pymongo import MongoClient
from app.config import mongo_url, mongo_db

try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['RetailServiceApplications']
    
    print('CHECKING DOCUMENT PATHS')
    print('=' * 70)
    
    apps_with_docs = list(col.find({'documents': {'$exists': True, '$ne': {}}}))
    
    if not apps_with_docs:
        print('No applications with documents found')
        sample_apps = list(col.find().limit(3))
        for app in sample_apps:
            print(f\"AppID: {app.get('applicationId', 'N/A')}\")
            print(f\"Docs: {app.get('documents', 'NONE')}\")
            print('-' * 50)
    else:
        print(f'Found {len(apps_with_docs)} apps with documents')
        for app in apps_with_docs[:3]:
            print(f\"AppID: {app.get('applicationId', 'N/A')}\")
            docs = app.get('documents', {})
            for key, path in docs.items():
                print(f\"  {key}: {path}\")
            print('-' * 50)
            
except Exception as e:
    print(f'Error: {e}')
