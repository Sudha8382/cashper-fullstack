"""
Test Recent Activities API
"""

import requests
import json
from datetime import datetime

# Configuration
BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = f"{BASE_URL}/api/auth/login"

# Test user credentials
TEST_USER = {
    "email": "testuser@cashper.com",
    "password": "Test@123"
}

def get_auth_token():
    """Login and get JWT token"""
    try:
        print("\n" + "="*60)
        print("LOGGING IN...")
        print("="*60)
        
        response = requests.post(LOGIN_URL, json=TEST_USER)
        
        if response.status_code == 200:
            data = response.json()
            token = data.get("access_token")
            print(f"✅ Login successful!")
            print(f"Token: {token[:50]}...")
            return token
        else:
            print(f"❌ Login failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Login error: {str(e)}")
        return None


def test_recent_activities(token, limit=10):
    """Test Recent Activities API"""
    try:
        print("\n" + "="*60)
        print(f"TESTING RECENT ACTIVITIES API (Limit: {limit})")
        print("="*60)
        
        headers = {"Authorization": f"Bearer {token}"}
        url = f"{BASE_URL}/api/dashboard/recent-activities?limit={limit}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API call successful!")
            print(f"\n📊 TOTAL ACTIVITIES: {data.get('total', 0)}")
            
            print(f"\n📋 ACTIVITIES LIST:")
            for i, activity in enumerate(data.get('activities', []), 1):
                print(f"\n   {i}. {activity.get('title')}")
                print(f"      Category: {activity.get('category')}")
                print(f"      Amount: {activity.get('amount')}")
                print(f"      Date: {activity.get('date')}")
                print(f"      Status: {activity.get('statusLabel')} ({activity.get('status')})")
                if activity.get('description'):
                    print(f"      Description: {activity.get('description')}")
            
            # Group by type
            by_type = {}
            for activity in data.get('activities', []):
                act_type = activity.get('type', 'unknown')
                by_type[act_type] = by_type.get(act_type, 0) + 1
            
            print(f"\n📈 BREAKDOWN BY TYPE:")
            for act_type, count in by_type.items():
                print(f"   {act_type.capitalize()}: {count}")
            
            # Group by status
            by_status = {}
            for activity in data.get('activities', []):
                status = activity.get('status', 'unknown')
                by_status[status] = by_status.get(status, 0) + 1
            
            print(f"\n📊 BREAKDOWN BY STATUS:")
            for status, count in by_status.items():
                print(f"   {status.replace('_', ' ').capitalize()}: {count}")
            
            return data
        else:
            print(f"❌ API call failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        return None


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("RECENT ACTIVITIES API TEST SUITE")
    print("="*60)
    print(f"Base URL: {BASE_URL}")
    print(f"Test User: {TEST_USER['email']}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get authentication token
    token = get_auth_token()
    
    if not token:
        print("\n❌ Cannot proceed without authentication token")
        return
    
    # Test Recent Activities with different limits
    print("\n" + "="*60)
    print("TEST 1: Recent Activities (10 items)")
    print("="*60)
    result1 = test_recent_activities(token, 10)
    
    print("\n" + "="*60)
    print("TEST 2: Recent Activities (5 items)")
    print("="*60)
    result2 = test_recent_activities(token, 5)
    
    print("\n" + "="*60)
    print("TEST 3: Recent Activities (20 items)")
    print("="*60)
    result3 = test_recent_activities(token, 20)
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    tests_passed = 0
    tests_failed = 0
    
    if result1:
        tests_passed += 1
        print("✅ Test 1 (10 items): PASSED")
    else:
        tests_failed += 1
        print("❌ Test 1 (10 items): FAILED")
    
    if result2:
        tests_passed += 1
        print("✅ Test 2 (5 items): PASSED")
    else:
        tests_failed += 1
        print("❌ Test 2 (5 items): FAILED")
    
    if result3:
        tests_passed += 1
        print("✅ Test 3 (20 items): PASSED")
    else:
        tests_failed += 1
        print("❌ Test 3 (20 items): FAILED")
    
    print(f"\n📊 Results: {tests_passed} passed, {tests_failed} failed")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
