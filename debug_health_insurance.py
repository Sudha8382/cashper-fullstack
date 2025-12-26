"""
Debug script to check what userId is being saved and retrieved
"""
import os
import sys
import requests
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

BASE_URL = "http://localhost:8000/api"

# First, let's check if user is already logged in
def get_user_token():
    """Get token from existing login"""
    # Try to login as sudha
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": "kumuyadav249@gmail.com",
            "password": "your_password_here"  # This might not work, but we'll try
        }
    )
    
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Login failed: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def check_health_insurance_data():
    """Check what's in the database directly"""
    print("=" * 80)
    print("DEBUG: Checking Health Insurance Database")
    print("=" * 80)
    
    try:
        from app.database.db import get_database
        db = get_database()
        collection = db["health_insurance_applications"]
        
        # Get all applications
        all_apps = list(collection.find().limit(5))
        
        print(f"\nTotal applications in collection: {collection.count_documents({})}")
        print("\nFirst few applications:")
        
        for app in all_apps:
            print(f"\n--- Application ---")
            print(f"ID: {app.get('_id')}")
            print(f"Name: {app.get('name')}")
            print(f"Email: {app.get('email')}")
            print(f"userId: {app.get('userId')}")
            print(f"userId type: {type(app.get('userId'))}")
            print(f"All keys: {list(app.keys())}")
        
        # Now test filtering
        print("\n\n" + "=" * 80)
        print("Testing Filter Logic")
        print("=" * 80)
        
        if all_apps:
            user_id = all_apps[0].get('userId')
            print(f"\nSearching for applications with userId: {user_id}")
            print(f"userId type: {type(user_id)}")
            
            # Try different query approaches
            print("\n1. Direct string match:")
            result1 = list(collection.find({"userId": user_id}))
            print(f"   Found: {len(result1)}")
            
            print("\n2. Check if userId field exists at all:")
            result2 = list(collection.find({"userId": {"$exists": True}}))
            print(f"   Found: {len(result2)}")
            
            print("\n3. Get ALL documents:")
            result3 = list(collection.find())
            print(f"   Found: {len(result3)}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

def check_api_response():
    """Check what the API is actually returning"""
    print("\n\n" + "=" * 80)
    print("DEBUG: Checking API Response")
    print("=" * 80)
    
    # First, get a valid token by checking if there's one in the request
    token = "your_token_here"  # You'll need to provide this
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        f"{BASE_URL}/health-insurance/application/all",
        headers=headers
    )
    
    print(f"\nAPI Status: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    # Check database directly
    check_health_insurance_data()
    
    # Optionally check API response
    # check_api_response()
