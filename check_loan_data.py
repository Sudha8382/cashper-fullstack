from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['cashper_db']

print('All collections:', db.list_collection_names())
print('\n' + '='*50)

# Check loan collections
loan_collections = [c for c in db.list_collection_names() if 'loan' in c.lower()]
print(f'\nLoan collections found: {loan_collections}')

for coll_name in loan_collections:
    count = db[coll_name].count_documents({})
    print(f'\n{coll_name}: {count} documents')
    
    # Get one sample document
    sample = db[coll_name].find_one()
    if sample:
        print(f'Sample document from {coll_name}:')
        sample['_id'] = str(sample['_id'])
        print(json.dumps(sample, indent=2, default=str))
        print('\n' + '-'*50)
