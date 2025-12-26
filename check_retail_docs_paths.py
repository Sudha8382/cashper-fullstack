import sys
sys.path.insert(0, 'cashper_backend')

from pymongo import MongoClient
from app.config import mongo_url, mongo_db

try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['RetailServiceApplications']
    
    print('CHECKING DOCUMENT PATHS IN RETAIL APPLICATIONS')
    print('=' * 70)
    
    # Check applications with documents
    apps_with_docs = list(col.find({"documents": {"$exists": True, "$ne": {}}}))
    
    if not apps_with_docs:
        print('\nNo applications with documents found')
        print('\nSample applications:')
        sample_apps = list(col.find().limit(3))
        for app in sample_apps:
            app_id = app.get('applicationId', 'N/A')
            docs = app.get('documents', 'NONE')
            print(f'AppID: {app_id}')
            print(f'Docs: {docs}')
            print('-' * 50)
    else:
        print(f'\nFound {len(apps_with_docs)} applications with documents\n')
        for app in apps_with_docs[:5]:
            app_id = app.get('applicationId', 'N/A')
            service_type = app.get('serviceType', 'N/A')
            email = app.get('email', 'N/A')
            print(f'AppID: {app_id}')
            print(f'Service: {service_type}')
            print(f'Email: {email}')
            print('Documents:')
            
            docs = app.get('documents', {})
            if isinstance(docs, dict):
                for key, path in docs.items():
                    print(f'  {key}: {path}')
            else:
                print(f'  Not a dict: {docs}')
            print('-' * 50)
            
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
