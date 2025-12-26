"""
Test to verify insurance application GET endpoint returns data
"""
import requests
import json

BASE_URL = "http://localhost:8000/api"

# You need to provide a valid JWT token from a successful login
# This is the userId from the user's last submission
TEST_USER_ID = "6915d49d212b60b1cd978073"
VALID_TOKEN = None  # You need to fill this from a login response

def test_with_token(token):
    """Test the GET endpoint with a valid token"""
    if not token:
        print("❌ No token provided. Cannot test.")
        return False
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print("=" * 80)
    print("Testing Health Insurance GET endpoint")
    print("=" * 80)
    print(f"\nToken: {token[:50]}...")
    print(f"Headers: {headers}")
    
    try:
        response = requests.get(
            f"{BASE_URL}/health-insurance/application/all",
            headers=headers
        )
        
        print(f"\n✓ Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Got {len(data)} applications")
            
            if data:
                print(f"\nFirst application:")
                for key, value in list(data[0].items())[:5]:
                    print(f"  {key}: {value}")
            else:
                print("\n⚠️ Response is empty array - no applications returned")
                print("\nThis could mean:")
                print("1. User has no applications in database")
                print("2. userId filter is not matching")
                print("3. User token is not being extracted correctly")
            
            return len(data) > 0
        else:
            print(f"✗ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ Exception: {e}")
        return False

def check_database_directly():
    """Check database directly for applications"""
    print("\n" + "=" * 80)
    print("Checking Database Directly")
    print("=" * 80)
    
    try:
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))
        
        # This will only work if MongoDB is running and configured
        from pymongo import MongoClient
        
        # Try to connect
        try:
            client = MongoClient('mongodb+srv://sudhayadav1103:2K6qL8pN9@payloan.ylvfqb6.mongodb.net/?retryWrites=true&w=majority')
            db = client['cashper_db']
            
            collection = db['health_insurance_applications']
            
            # Count documents
            total_count = collection.count_documents({})
            print(f"\n✓ Total applications in database: {total_count}")
            
            # Find applications for specific user
            user_apps = list(collection.find({"userId": TEST_USER_ID}).limit(1))
            print(f"✓ Applications for user {TEST_USER_ID}: {len(user_apps)}")
            
            if user_apps:
                app = user_apps[0]
                print(f"\nSample application:")
                print(f"  _id: {app.get('_id')}")
                print(f"  userId: {app.get('userId')}")
                print(f"  name: {app.get('name')}")
                print(f"  email: {app.get('email')}")
                print(f"  status: {app.get('status')}")
            
            # Show some applications with userId field
            print(f"\nSample of all applications with userId:")
            for app in collection.find({"userId": {"$exists": True}}).limit(3):
                print(f"  userId: {app.get('userId')}, name: {app.get('name')}")
                
        except Exception as e:
            print(f"Could not connect to MongoDB: {e}")
            
    except Exception as e:
        print(f"Error checking database: {e}")

if __name__ == "__main__":
    print("\nTo test the GET endpoint, you need to:")
    print("1. Login to get a valid JWT token")
    print("2. Replace VALID_TOKEN variable with the actual token")
    print("3. Run this script\n")
    
    # Try to check database
    check_database_directly()
    
    # Try to test with token if provided
    if VALID_TOKEN:
        test_with_token(VALID_TOKEN)
    else:
        print("\n⚠️ Skipping API test - no token provided")
