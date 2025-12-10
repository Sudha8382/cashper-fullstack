"""
Check MongoDB for all databases and collections
"""

from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    
    # List all databases
    print("Databases:")
    for db_name in client.list_database_names():
        print(f"  - {db_name}")
        db = client[db_name]
        collections = db.list_collection_names()
        if collections:
            for coll in collections:
                count = db[coll].count_documents({})
                if count > 0:
                    print(f"      {coll}: {count} docs")
    
except Exception as e:
    print(f"Error: {str(e)}")
