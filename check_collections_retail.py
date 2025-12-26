"""
Check all collections and find retail services data
"""

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

print("=" * 80)
print("MONGODB COLLECTIONS CHECK".center(80))
print("=" * 80)

# Check Cashper database
db = client.Cashper

print("\n📚 Collections in Cashper Database:")
print("-" * 80)
collections = db.list_collection_names()
for idx, coll in enumerate(sorted(collections), 1):
    count = db[coll].count_documents({})
    print(f"{idx:2}. {coll:<40} : {count:>6} documents")

print(f"\n🔍 Looking for retail service related collections...")
retail_collections = [c for c in collections if 'retail' in c.lower() or 'service' in c.lower()]

if retail_collections:
    print(f"Found {len(retail_collections)} related collections:")
    for coll in retail_collections:
        count = db[coll].count_documents({})
        print(f"  - {coll}: {count} documents")
        
        # Show sample document
        if count > 0:
            sample = db[coll].find_one({})
            if sample:
                print(f"    Sample fields: {list(sample.keys())[:5]}")
else:
    print("No retail service collections found yet.")
    print("\n💡 Retail service applications will be stored in: RetailServiceApplications")

print("\n" + "=" * 80)
