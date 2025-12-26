import sys
sys.path.insert(0, 'C:\\Users\\ASUS\\Desktop\\payloan\\full_proj\\cashper_backend')

from pymongo import MongoClient
from fastapi.responses import JSONResponse

def get_database():
    client = MongoClient('mongodb://localhost:27017/')
    return client["cashper_db"]

async def test_gst():
    try:
        db = get_database()
        collection = db["gst_services_applications"]
        
        query = {}
        
        applications = list(collection.find(query).sort("created_at", -1))
        
        print(f"Found {len(applications)} GST applications")
        
        for app in applications:
            app["_id"] = str(app["_id"])
            if "created_at" in app and hasattr(app["created_at"], "isoformat"):
                app["created_at"] = app["created_at"].isoformat()
            if "updated_at" in app and hasattr(app["updated_at"], "isoformat"):
                app["updated_at"] = app["updated_at"].isoformat()
        
        result = {
            "success": True,
            "count": len(applications),
            "applications": applications
        }
        
        print(f"Result prepared successfully")
        return result
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None

# Run async function
import asyncio
result = asyncio.run(test_gst())
if result:
    print(f"✅ Success! Got {result['count']} applications")
else:
    print(f"❌ Failed to fetch data")
