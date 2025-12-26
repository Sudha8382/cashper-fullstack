#!/usr/bin/env python3
"""
Check the last tax planning application in the database to see if userId is set
"""

from pymongo import MongoClient
import os
from datetime import datetime

# MongoDB connection
MONGO_URI = os.getenv("MONGODB_URI", "mongodb+srv://payloan:payloan123@cluster0.5vfgs.mongodb.net/?retryWrites=true&w=majority")

try:
    client = MongoClient(MONGO_URI)
    db = client["cashper_db"]
    collection = db["tax_planning_applications"]
    
    # Get the last application
    last_app = collection.find_one(sort=[("createdAt", -1)])
    
    if last_app:
        print("=" * 80)
        print("LAST TAX PLANNING APPLICATION IN DATABASE:")
        print("=" * 80)
        print(f"ID: {last_app.get('_id')}")
        print(f"Full Name: {last_app.get('fullName')}")
        print(f"Email: {last_app.get('emailAddress')}")
        print(f"Pan: {last_app.get('panNumber')}")
        print(f"userId: {last_app.get('userId')}")
        print(f"Created: {last_app.get('createdAt')}")
        print(f"\nFull Document:")
        import json
        print(json.dumps({k: str(v) if isinstance(v, datetime) else v for k, v in last_app.items()}, indent=2))
    else:
        print("No applications found in database")
    
    client.close()
except Exception as e:
    print(f"Error: {e}")
