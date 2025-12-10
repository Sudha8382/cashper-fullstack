"""
Test Dashboard Stats API to verify all counts are working
"""

import requests
import json
from datetime import datetime

# Configuration
BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = f"{BASE_URL}/api/auth/login"
STATS_URL = f"{BASE_URL}/api/dashboard/stats"

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


def test_dashboard_stats(token):
    """Test Dashboard Stats API"""
    try:
        print("\n" + "="*60)
        print("TESTING DASHBOARD STATS API")
        print("="*60)
        
        headers = {"Authorization": f"Bearer {token}"}
        
        response = requests.get(STATS_URL, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API call successful!")
            
            # Print formatted stats
            print(f"\n📊 DASHBOARD STATISTICS:")
            print(f"\n💰 LOANS:")
            print(f"   Total: {data['loans']['total']}")
            print(f"   Active: {data['loans']['active']}")
            print(f"   Completed: {data['loans']['completed']}")
            
            print(f"\n🛡️ INSURANCE:")
            print(f"   Total: {data['insurance']['total']}")
            print(f"   Health: {data['insurance']['health']}")
            print(f"   Motor: {data['insurance']['motor']}")
            print(f"   Term: {data['insurance']['term']}")
            
            print(f"\n📈 INVESTMENTS:")
            print(f"   Total: {data['investments']['total']}")
            print(f"   SIP: {data['investments']['sip']}")
            print(f"   Mutual Funds: {data['investments']['mutualFunds']}")
            
            print(f"\n📄 DOCUMENTS: {data['documents']}")
            
            print(f"\n🎫 SUPPORT:")
            print(f"   Total: {data['support']['total']}")
            print(f"   Pending: {data['support']['pending']}")
            print(f"   Resolved: {data['support']['resolved']}")
            
            print(f"\n🔔 NOTIFICATIONS:")
            print(f"   Unread: {data['notifications']['unread']}")
            
            print(f"\n🛠️ SERVICES:")
            print(f"   Tax Planning: {data['services']['taxPlanning']['used']} used / {data['services']['taxPlanning']['available']} available")
            print(f"   Retail Services: {data['services']['retailServices']['used']} used / {data['services']['retailServices']['available']} available")
            print(f"   Corporate Services: {data['services']['corporateServices']['used']} used / {data['services']['corporateServices']['available']} available")
            print(f"   Calculators: {data['services']['calculators']['used']} used / {data['services']['calculators']['available']} available")
            
            # Check if all values are zero
            all_zero = (
                data['loans']['total'] == 0 and
                data['insurance']['total'] == 0 and
                data['investments']['total'] == 0
            )
            
            if all_zero:
                print(f"\n⚠️ WARNING: All counts are ZERO!")
                print(f"   This might mean:")
                print(f"   1. Test user has no data in database")
                print(f"   2. userId field mismatch in collections")
                print(f"   3. Need to run seed script to add test data")
            else:
                print(f"\n✅ SUCCESS: Data found in database!")
            
            return data
        else:
            print(f"❌ API call failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """Run test"""
    print("\n" + "="*60)
    print("DASHBOARD STATS API TEST")
    print("="*60)
    print(f"Base URL: {BASE_URL}")
    print(f"Test User: {TEST_USER['email']}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get authentication token
    token = get_auth_token()
    
    if not token:
        print("\n❌ Cannot proceed without authentication token")
        return
    
    # Test Dashboard Stats
    result = test_dashboard_stats(token)
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    if result:
        print("✅ Dashboard Stats API: PASSED")
    else:
        print("❌ Dashboard Stats API: FAILED")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
