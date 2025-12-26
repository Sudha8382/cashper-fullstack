"""
Check Retail Services Applications in Database
Shows statistics and sample applications
"""

from pymongo import MongoClient
from datetime import datetime
from collections import Counter

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.Cashper

print("=" * 80)
print("RETAIL SERVICES APPLICATIONS DATABASE CHECK".center(80))
print("=" * 80)

# Get collection
collection = db.RetailServiceApplications

# Total count
total_count = collection.count_documents({})
print(f"\n📊 Total Applications in Database: {total_count}")

if total_count > 0:
    # Get all applications
    applications = list(collection.find({}))
    
    # Count by service type
    service_types = [app.get('serviceType') for app in applications]
    service_counts = Counter(service_types)
    
    print(f"\n📋 Applications by Service Type:")
    print("-" * 80)
    for service, count in sorted(service_counts.items()):
        print(f"  {service:<30}: {count:>3} applications")
    
    # Count by status
    statuses = [app.get('status') for app in applications]
    status_counts = Counter(statuses)
    
    print(f"\n📈 Applications by Status:")
    print("-" * 80)
    for status, count in sorted(status_counts.items()):
        print(f"  {status:<30}: {count:>3} applications")
    
    # Show recent applications
    print(f"\n📝 Recent Applications (Last 5):")
    print("-" * 80)
    recent_apps = sorted(applications, key=lambda x: x.get('createdAt', datetime.min), reverse=True)[:5]
    
    for idx, app in enumerate(recent_apps, 1):
        print(f"\n{idx}. Application ID: {app.get('_id')}")
        print(f"   Service Type: {app.get('serviceType')}")
        print(f"   Applicant: {app.get('applicantName')}")
        print(f"   Email: {app.get('email')}")
        print(f"   Status: {app.get('status')}")
        print(f"   Created: {app.get('createdAt')}")
    
    # Show service type examples
    print(f"\n🔍 Sample Application Data by Service Type:")
    print("-" * 80)
    
    unique_services = set(service_types)
    for service in sorted(unique_services)[:3]:  # Show first 3 types
        app = collection.find_one({"serviceType": service})
        if app:
            print(f"\n📌 {service.upper()}")
            print(f"   Applicant: {app.get('applicantName')}")
            print(f"   Phone: {app.get('phone')}")
            print(f"   Status: {app.get('status')}")
            
            # Show key fields from applicationData
            app_data = app.get('applicationData', {})
            if 'panNumber' in app_data:
                print(f"   PAN: {app_data.get('panNumber')}")
            if 'city' in app_data:
                print(f"   City: {app_data.get('city')}")
            if 'state' in app_data:
                print(f"   State: {app_data.get('state')}")

else:
    print("\n⚠️  No applications found in database.")
    print("   Run test scripts to create sample applications.")

print("\n" + "=" * 80)
print("DATABASE CHECK COMPLETE".center(80))
print("=" * 80)
