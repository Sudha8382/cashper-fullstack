from pymongo import MongoClient
from bson import ObjectId
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['cashper_db']

# Try different collections
collections = ['personal_loan_applications', 'personal_loans', 'personal_loan_inquiries']

loan_id = '69471e2f713f6c8069813303'

print(f"Searching for loan ID: {loan_id}")
print("-" * 50)

for coll_name in collections:
    if coll_name in db.list_collection_names():
        try:
            loan = db[coll_name].find_one({'_id': ObjectId(loan_id)})
            if loan:
                print(f"\n✅ Found in collection: {coll_name}")
                loan['_id'] = str(loan['_id'])
                print(json.dumps(loan, indent=2, default=str))
                break
        except:
            pass
else:
    # Try finding by other fields
    print(f"\n❌ Not found by _id in standard collections")
    print("\nSearching by applicationId...")
    
    for coll_name in db.list_collection_names():
        if 'loan' in coll_name.lower():
            loan = db[coll_name].find_one({'applicationId': f'PL20251221748563'})
            if loan:
                print(f"\n✅ Found by applicationId in: {coll_name}")
                loan['_id'] = str(loan['_id'])
                print(json.dumps(loan, indent=2, default=str))
                break
