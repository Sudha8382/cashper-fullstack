"""
Test Service Stats API - Quick test to verify the endpoint works
"""

import requests
import json

# Admin login credentials
ADMIN_EMAIL = "sudha@gmail.com"
ADMIN_PASSWORD = "Sudha@123"
BASE_URL = "http://localhost:8000"

def get_admin_token():
    """Login and get admin token"""
    response = requests.post(
        f"{BASE_URL}/api/admin/login",
        json={"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD}
    )
    
    if response.status_code == 200:
        token = response.json()["access_token"]
        print("✅ Admin login successful")
        return token
    else:
        print(f"❌ Login failed: {response.status_code}")
        print(response.text)
        return None

def test_service_stats_api(token):
    """Test the service stats API"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print("\n📊 Testing Service Stats API...")
    response = requests.get(
        f"{BASE_URL}/api/admin/dashboard/service-stats",
        headers=headers
    )
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Service Stats API Response:")
        print(json.dumps(data, indent=2))
        print(f"\n📈 Summary:")
        print(f"   - Investments: {data.get('investments', 0)}")
        print(f"   - Tax Planning: {data.get('taxPlanning', 0)}")
        print(f"   - Retail Services: {data.get('retailServices', 0)}")
        print(f"   - Corporate Services: {data.get('corporateServices', 0)}")
    else:
        print(f"❌ API failed: {response.status_code}")
        print(response.text)

def test_dashboard_stats_api(token):
    """Test the main dashboard stats API"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print("\n📊 Testing Dashboard Stats API...")
    response = requests.get(
        f"{BASE_URL}/api/admin/dashboard/stats",
        headers=headers
    )
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Dashboard Stats API Response:")
        print(f"   - Total Users: {data.get('totalUsers', 0)}")
        print(f"   - Active Loans: {data.get('activeLoans', '₹0Cr')}")
        print(f"   - Insurance Policies: {data.get('insurancePolicies', 0)}")
        print(f"   - Total Revenue: {data.get('totalRevenue', '₹0Cr')}")
    else:
        print(f"❌ API failed: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    print("🚀 Testing Admin Dashboard APIs\n")
    
    # Get admin token
    token = get_admin_token()
    
    if token:
        # Test both APIs
        test_dashboard_stats_api(token)
        test_service_stats_api(token)
        print("\n✅ All API tests completed!")
    else:
        print("\n❌ Cannot proceed without admin token")
