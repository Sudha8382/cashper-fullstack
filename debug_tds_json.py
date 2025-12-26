import json
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['cashper_db']

# Try to fetch and serialize TDS data
tds_collection = db['tds_services_applications']
apps = list(tds_collection.find().limit(1))

print(f"Found {len(apps)} applications")

if apps:
    app = apps[0]
    print(f"\nApplication keys: {list(app.keys())}")
    print(f"created_at type: {type(app.get('created_at'))}")
    print(f"created_at value: {app.get('created_at')}")
    print(f"updated_at type: {type(app.get('updated_at'))}")
    print(f"updated_at value: {app.get('updated_at')}")
    
    # Try to convert to JSON
    try:
        # Convert datetime
        if 'created_at' in app and hasattr(app['created_at'], 'isoformat'):
            app['created_at'] = app['created_at'].isoformat()
        if 'updated_at' in app and hasattr(app['updated_at'], 'isoformat'):
            app['updated_at'] = app['updated_at'].isoformat()
        
        app['_id'] = str(app['_id'])
        
        json_str = json.dumps(app)
        print(f"\n✅ Successfully serialized to JSON")
        print(f"JSON length: {len(json_str)} chars")
    except Exception as e:
        print(f"\n❌ Error serializing to JSON: {e}")
        print(f"Problem field analysis:")
        for key, value in app.items():
            try:
                json.dumps({key: value})
            except Exception as field_error:
                print(f"  - {key} ({type(value).__name__}): {field_error}")
