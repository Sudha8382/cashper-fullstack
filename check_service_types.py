import sys
sys.path.insert(0, 'cashper_backend')

from app.database.db import get_database

db = get_database()
col = db['RetailServiceApplications']
apps = list(col.find().limit(20))

print("ServiceType values in database:")
print("-" * 50)
for app in apps:
    service_type = app.get("serviceType", "N/A")
    print(f"ServiceType: {service_type}")
