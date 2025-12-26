import requests
import json

print("=" * 100)
print("TESTING ADMIN DASHBOARD API - REAL-TIME DATABASE COUNTS")
print("=" * 100)

# Login
print("\n1. Logging in as admin...")
login_response = requests.post(
    "http://127.0.0.1:8000/api/admin/login",
    json={"email": "sudha@gmail.com", "password": "Sudha@123"}
)

if login_response.status_code != 200:
    print(f"   ❌ Login failed: {login_response.status_code}")
    print("   Make sure backend server is running!")
    exit(1)

token = login_response.json()["access_token"]
print("   ✅ Login successful!")

headers = {"Authorization": f"Bearer {token}"}

# Test dashboard stats
print("\n2. Testing /api/admin/dashboard/stats...")
stats_response = requests.get("http://127.0.0.1:8000/api/admin/dashboard/stats", headers=headers)

if stats_response.status_code == 200:
    data = stats_response.json()
    print("   ✅ Dashboard stats retrieved!")
    print(f"\n   📊 Main Dashboard Cards:")
    print(f"      - Total Users: {data.get('totalUsers', 0)}")
    print(f"      - Active Loans: {data.get('activeLoansCount', 0)}")
    print(f"      - Insurance Policies: {data.get('insurancePolicies', 0)}")
    print(f"      - Total Inquiries: {data.get('totalInquiries', 0)} ⭐ (Expected: ~9 from DB)")
else:
    print(f"   ❌ Failed: {stats_response.status_code}")

# Test service stats
print("\n3. Testing /api/admin/dashboard/service-stats...")
service_response = requests.get("http://127.0.0.1:8000/api/admin/dashboard/service-stats", headers=headers)

if service_response.status_code == 200:
    data = service_response.json()
    print("   ✅ Service stats retrieved!")
    print(f"\n   📊 Service Cards:")
    print(f"      - Investments: {data.get('investments', 0)} ⭐ (Expected: 0)")
    print(f"      - Tax Planning: {data.get('taxPlanning', 0)} ⭐ (Expected: 0)")
    print(f"      - Retail Services: {data.get('retailServices', 0)} ⭐ (Expected: 0)")
    print(f"      - Corporate Services: {data.get('corporateServices', 0)} ⭐ (Expected: 60)")
else:
    print(f"   ❌ Failed: {service_response.status_code}")

print("\n" + "=" * 100)
print("✅ API TESTS COMPLETED")
print("\n💡 Expected vs Actual:")
print("   - Total Inquiries should be ~9 (not 234)")
print("   - Corporate Services should be 60 (not 147)")
print("   - Tax Planning should be 0 (not 1)")
print("   - Investments should be 0 (not 44)")
print("=" * 100)
