"""
Script to remove Car Loan collections from MongoDB database
This will drop all car loan related collections
"""

from pymongo import MongoClient
import sys

# MongoDB connection string
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "cashper_db"

def remove_car_loan_collections():
    """Remove all car loan related collections from database"""
    try:
        # Connect to MongoDB
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        
        # List of car loan collections to remove
        car_loan_collections = [
            "car_loan_get_in_touch",
            "car_loan_applications",
            "car_loan_eligibility_criteria"
        ]
        
        print("=" * 60)
        print("CAR LOAN COLLECTIONS REMOVAL")
        print("=" * 60)
        
        # Check and remove each collection
        existing_collections = db.list_collection_names()
        
        for collection_name in car_loan_collections:
            if collection_name in existing_collections:
                # Get count before deletion
                count = db[collection_name].count_documents({})
                print(f"\n📋 Collection: {collection_name}")
                print(f"   Documents: {count}")
                
                # Drop the collection
                db[collection_name].drop()
                print(f"   ✅ REMOVED")
            else:
                print(f"\n📋 Collection: {collection_name}")
                print(f"   ⚠️  NOT FOUND (already removed or never existed)")
        
        print("\n" + "=" * 60)
        print("✅ CAR LOAN REMOVAL COMPLETED SUCCESSFULLY")
        print("=" * 60)
        
        # Show remaining collections
        print("\n📊 Remaining Collections in Database:")
        remaining = db.list_collection_names()
        for col in sorted(remaining):
            count = db[col].count_documents({})
            print(f"   - {col}: {count} documents")
        
        # Close connection
        client.close()
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    print("\n🚨 WARNING: This will permanently delete all Car Loan data from database!")
    response = input("Are you sure you want to continue? (yes/no): ")
    
    if response.lower() == 'yes':
        remove_car_loan_collections()
    else:
        print("\n❌ Operation cancelled.")
