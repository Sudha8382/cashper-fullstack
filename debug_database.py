"""
Check and migrate TDS/GST data if needed
"""
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# List all databases
print("Available databases:")
for db_name in client.list_database_names():
    print(f"  - {db_name}")

# Check cashper_db
db = client['cashper_db']
print(f"\nCollections in 'cashper_db':")
for col_name in db.list_collection_names():
    count = db[col_name].count_documents({})
    if count > 0 or 'tds' in col_name or 'gst' in col_name:
        print(f"  - {col_name}: {count} documents")

# Specifically check TDS and GST
print("\n" + "="*60)
print("DETAILED CHECK:")
print("="*60)

tds_col = db['tds_services_applications']
gst_col = db['gst_services_applications']

tds_count = tds_col.count_documents({})
gst_count = gst_col.count_documents({})

print(f"TDS applications: {tds_count}")
if tds_count > 0:
    sample = tds_col.find_one()
    print(f"  Sample ID: {sample.get('application_id')}")
    print(f"  Sample Status: {sample.get('status')}")

print(f"GST applications: {gst_count}")
if gst_count > 0:
    sample = gst_col.find_one()
    print(f"  Sample ID: {sample.get('application_id')}")
    print(f"  Sample Status: {sample.get('status')}")

# Now try via the app's get_database function
import sys
sys.path.insert(0, 'C:\\Users\\ASUS\\Desktop\\payloan\\full_proj\\cashper_backend')

from app.database.db import get_database, connect_to_mongo

print("\n" + "="*60)
print("USING APP'S get_database():")
print("="*60)

# Connect first
connect_to_mongo()

# Now get database
app_db = get_database()
print(f"Database from app: {app_db}")
print(f"Database name: {app_db.name if app_db else 'None'}")

if app_db:
    tds_from_app = app_db['tds_services_applications']
    print(f"TDS count via app: {tds_from_app.count_documents({})}")
    
    gst_from_app = app_db['gst_services_applications']
    print(f"GST count via app: {gst_from_app.count_documents({})}")
