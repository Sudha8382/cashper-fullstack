import requests
import json

# Test Dashboard Stats API
API_URL = "http://127.0.0.1:8000"

# You need to replace this with an actual valid token from your browser's localStorage
# Open browser console and type: localStorage.getItem('access_token')
TOKEN = "your_token_here"

def test_dashboard_stats():
    """Test the dashboard stats endpoint"""
    print("=" * 60)
    print("Testing Dashboard Stats API")
    print("=" * 60)
    
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(f"{API_URL}/api/dashboard/stats", headers=headers)
        print(f"\n📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n✅ Response Data:")
            print(json.dumps(data, indent=2))
            
            print("\n📈 Summary:")
            print(f"  Total Loans: {data.get('loans', {}).get('total', 0)}")
            print(f"  Active Loans: {data.get('loans', {}).get('active', 0)}")
            print(f"  Total Insurance: {data.get('insurance', {}).get('total', 0)}")
            print(f"  Total Investments: {data.get('investments', {}).get('total', 0)}")
            print(f"  Documents: {data.get('documents', 0)}")
            
        else:
            print(f"\n❌ Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"\n❌ Exception: {e}")

if __name__ == "__main__":
    if TOKEN == "your_token_here":
        print("⚠️  Please update TOKEN variable with actual token from browser localStorage")
        print("\nTo get token:")
        print("1. Open browser and login to dashboard")
        print("2. Open browser console (F12)")
        print("3. Type: localStorage.getItem('access_token')")
        print("4. Copy the token and paste it in this script")
    else:
        test_dashboard_stats()
