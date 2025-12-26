import sys
sys.path.insert(0, 'cashper_backend')

from pymongo import MongoClient
from app.config import mongo_url, mongo_db

try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    col = db['RetailServiceApplications']
    
    print("=" * 70)
    print("CHECKING BANK ACCOUNT SERVICES DATA")
    print("=" * 70)
    
    # Check all bank-account applications
    bank_apps = list(col.find({"serviceType": "bank-account"}))
    print(f"\nTotal bank-account applications: {len(bank_apps)}")
    
    if bank_apps:
        print("\nBank Account Applications Details:")
        print("-" * 70)
        for app in bank_apps:
            email = app.get("email", "N/A")
            name = app.get("applicantName", "N/A")
            status = app.get("status", "N/A")
            app_id = app.get("applicationId", "N/A")
            print(f"Email: {email}")
            print(f"Name: {name}")
            print(f"Status: {status}")
            print(f"Application ID: {app_id}")
            print("-" * 70)
    
    # Check what user emails exist
    print("\n" + "=" * 70)
    print("ALL USER EMAILS IN DATABASE:")
    print("=" * 70)
    all_emails = col.distinct("email")
    for email in all_emails:
        count = col.count_documents({"email": email})
        print(f"  {email} - {count} applications")
    
    print("\n" + "=" * 70)
    print("CHECK YOUR LOGGED IN EMAIL IN BROWSER")
    print("=" * 70)
    print("Open browser console and type: localStorage.getItem('access_token')")
    print("Then decode the JWT token to see which email you're logged in with")
    
except Exception as e:
    print(f"Error: {e}")
