import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/api"
ADMIN_URL = "http://127.0.0.1:8000/api/admin"

print("\n" + "="*70)
print("🔧 SETTING UP TEST DATA FOR ADMIN METRICS - WITH PROPER PARAMETERS")
print("="*70)

# Step 1: Admin Login
print("\n📝 Step 1: Admin Login...")
login_response = requests.post(
    f"{ADMIN_URL}/login",
    json={"email": "sudha@gmail.com", "password": "Sudha@123"}
)

if login_response.status_code != 200:
    print(f"❌ Login failed: {login_response.text}")
    exit(1)

admin_token = login_response.json()['access_token']
headers = {'Authorization': f'Bearer {admin_token}'}
print(f"✅ Admin Login successful!")

# Step 2: Get pending loan applications
print("\n📋 Step 2: Fetching Pending Loan Applications...")
approvals_response = requests.get(
    f"{ADMIN_URL}/dashboard/pending-approvals",
    headers=headers
)

if approvals_response.status_code == 200:
    data = approvals_response.json()
    pending = data.get('pending_approvals', [])
    print(f"✅ Found {len(pending)} pending approvals")
    
    # Step 3: Approve first 5 loans with proper parameters
    if pending:
        print(f"\n✔️ Step 3: Approving First 5 Loans...")
        for i, approval in enumerate(pending[:5]):
            loan_id = approval.get('id') or approval.get('loan_id')
            loan_type = approval.get('type', 'personal').lower()
            
            # Map common loan type names
            type_map = {
                'personal': 'personal',
                'home': 'home',
                'business': 'business',
                'short term': 'short_term',
                'short_term': 'short_term'
            }
            mapped_type = type_map.get(loan_type, 'personal')
            
            approve_response = requests.put(
                f"{ADMIN_URL}/loans/{loan_id}/approve",
                headers=headers,
                json={
                    "loan_type": mapped_type,
                    "remarks": f"Approved by admin test script"
                }
            )
            
            if approve_response.status_code == 200:
                print(f"   ✅ Loan {i+1}: {approval.get('type', 'N/A')} - {approval.get('customer', 'N/A')} (₹{approval.get('amount', 'N/A')}) - APPROVED")
            else:
                print(f"   ⚠️  Loan {i+1}: Failed - {approve_response.status_code} - {approve_response.text[:100]}")
    else:
        print("⚠️  No pending approvals found")
else:
    print(f"❌ Failed to fetch approvals: {approvals_response.text}")

# Step 4: Check updated metrics
print("\n📊 Step 4: Checking Updated Performance Metrics...")
metrics_response = requests.get(
    f"{ADMIN_URL}/dashboard/performance-metrics",
    headers=headers
)

if metrics_response.status_code == 200:
    metrics = metrics_response.json()
    print(f"✅ Updated Metrics:")
    print(f"   📈 Total Logins: {metrics['total_logins']:,}")
    print(f"   ⏱️  Hours Active: {metrics['hours_active']:,}")
    print(f"   ✔️  Tasks Completed: {metrics['tasks_completed']:,}")
    print(f"   ⭐ Rating: {metrics['rating']}/5")
else:
    print(f"❌ Failed to fetch metrics: {metrics_response.text}")

print("\n" + "="*70)
print("✅ TEST DATA SETUP COMPLETED!")
print("="*70 + "\n")
