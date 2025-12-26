import sys
sys.path.insert(0, 'cashper_backend')

from pymongo import MongoClient
from app.config import mongo_url, mongo_db

try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['RetailServiceApplications']
    
    # Get all unique service types
    service_types = col.distinct("serviceType")
    
    print("All unique serviceType values in database:")
    print("=" * 60)
    for st in service_types:
        count = col.count_documents({"serviceType": st})
        print(f"  '{st}' - {count} applications")
    
    print("\n" + "=" * 60)
    print(f"Total unique service types: {len(service_types)}")
    
except Exception as e:
    print(f"Error: {e}")
