"""
Debug MongoDB - show all documents
"""

from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["payloan"]
    collection = db["admin_loan_applications"]
    
    # Clear the collection and start fresh
    count_before = collection.count_documents({})
    print(f"Documents before clear: {count_before}")
    
    # Delete all and start fresh
    result = collection.delete_many({})
    print(f"Deleted: {result.deleted_count} documents")
    
    print(f"Documents after clear: {collection.count_documents({})}")
    
except Exception as e:
    print(f"Error: {str(e)}")
