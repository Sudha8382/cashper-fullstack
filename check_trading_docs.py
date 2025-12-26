import sys
sys.path.insert(0, 'cashper_backend')

from pymongo import MongoClient
from app.config import mongo_url, mongo_db
import os
from pathlib import Path

try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['RetailServiceApplications']
    
    print("=" * 70)
    print("CHECKING TRADING-DEMAT DOCUMENTS")
    print("=" * 70)
    
    # Find trading-demat applications
    trading_apps = list(col.find({"serviceType": "trading-demat"}))
    
    print(f"\nFound {len(trading_apps)} trading-demat applications\n")
    
    backend_dir = Path(__file__).parent / 'cashper_backend'
    
    for app in trading_apps:
        app_id = app.get('applicationId', 'N/A')
        email = app.get('email', 'N/A')
        docs = app.get('documents', {})
        
        print(f"Application ID: {app_id}")
        print(f"Email: {email}")
        print(f"Documents in DB:")
        
        if isinstance(docs, dict) and docs:
            for key, path in docs.items():
                print(f"  {key}: {path}")
                
                # Check if file exists
                full_path = backend_dir / path.replace('/', '\\')
                exists = full_path.exists()
                print(f"    File exists: {exists}")
                if not exists:
                    print(f"    Looking for: {full_path}")
        else:
            print("  No documents found")
        
        print("-" * 70)
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
