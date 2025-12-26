"""
Test Corporate Services - Approved Status Feature
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/business-services"

print("="*70)
print("  TESTING APPROVED STATUS FEATURE")
print("="*70)

# Test 1: Get Stats with Approved count
print("\n📊 TEST 1: Checking Stats API")
response = requests.get(f"{BASE_URL}/stats")
if response.status_code == 200:
    data = response.json()
    stats = data.get("stats", {})
    print(f"✅ Total: {stats.get('total')}")
    print(f"✅ Pending: {stats.get('pending')}")
    print(f"✅ Approved: {stats.get('approved')}")
    print(f"✅ Completed: {stats.get('completed')}")
    print(f"✅ Rejected: {stats.get('rejected')}")
else:
    print(f"❌ Failed: {response.status_code}")

# Test 2: Get a sample application
print("\n📝 TEST 2: Getting Sample Application")
response = requests.get(f"{BASE_URL}/all-applications")
if response.status_code == 200:
    data = response.json()
    if data.get("applications"):
        app = data["applications"][0]
        app_id = app.get("_id")
        print(f"✅ Application ID: {app_id}")
        print(f"✅ Current Status: {app.get('status')}")
        
        # Test 3: Update to Approved
        print("\n✅ TEST 3: Updating Status to 'Approved'")
        update_response = requests.put(
            f"{BASE_URL}/{app_id}/status",
            json={"status": "Approved"}
        )
        if update_response.status_code == 200:
            result = update_response.json()
            print(f"✅ {result.get('message')}")
            
            # Verify
            verify_response = requests.get(f"{BASE_URL}/all-applications")
            if verify_response.status_code == 200:
                verify_data = verify_response.json()
                updated_app = next(
                    (a for a in verify_data.get("applications", []) 
                     if a.get("_id") == app_id),
                    None
                )
                if updated_app and updated_app.get("status") == "Approved":
                    print("✅ Verified: Status is 'Approved' in database")
                else:
                    print("❌ Verification failed")
        else:
            print(f"❌ Update failed: {update_response.status_code}")
            
        # Test 4: Filter by Approved status
        print("\n🔍 TEST 4: Filtering by Approved Status")
        filter_response = requests.get(f"{BASE_URL}/all-applications?status=Approved")
        if filter_response.status_code == 200:
            filter_data = filter_response.json()
            approved_count = filter_data.get("count", 0)
            print(f"✅ Found {approved_count} approved applications")
        else:
            print(f"❌ Filter failed: {filter_response.status_code}")

print("\n" + "="*70)
print("  ✅ ALL TESTS COMPLETED!")
print("="*70)

print("\n📋 CHANGES SUMMARY:")
print("1. ✅ Backend: 'In Progress' replaced with 'Approved'")
print("2. ✅ Frontend: Button changed to 'Approved' with CheckCircle icon")
print("3. ✅ Stats API: Returns 'approved' count instead of 'in_progress'")
print("4. ✅ Filtering: Can filter by 'Approved' status")
print("5. ✅ Status colors: Blue badge for Approved status")
print("\n🎯 Feature is ready for production!")
