"""
Check all collections in MongoDB and show loan data
"""

from pymongo import MongoClient
from datetime import datetime

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["payloan"]
    
    print("Connected to MongoDB!")
    print(f"Database: {db.name}")
    print(f"\nCollections in database:")
    
    collections = db.list_collection_names()
    for coll in collections:
        print(f"  - {coll}")
    
    # Check all collections for loan data
    print("\n" + "="*80)
    print("SEARCHING FOR LOAN DATA IN ALL COLLECTIONS")
    print("="*80)
    
    for coll_name in collections:
        collection = db[coll_name]
        count = collection.count_documents({})
        
        if "loan" in coll_name.lower() or count > 0:
            print(f"\n{coll_name}: {count} documents")
            
            # Try to find loan-like data
            if "loan" in coll_name.lower():
                try:
                    sample = collection.find_one({"type": {"$exists": True}})
                    if sample:
                        print(f"  Sample: {sample.get('type', 'N/A')}")
                except:
                    pass
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
