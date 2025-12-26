"""
Test Business Services Stats API
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_stats_api():
    """Test the business services stats endpoint"""
    print("\n" + "="*60)
    print("Testing Business Services Stats API")
    print("="*60)
    
    try:
        # Test stats endpoint
        print("\n1. Fetching Business Services Statistics...")
        response = requests.get(f"{BASE_URL}/api/business-services/stats")
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n✓ Stats fetched successfully!")
            print("\nStatistics:")
            print(f"  Total Applications: {data['stats']['total']}")
            print(f"  Pending: {data['stats']['pending']}")
            print(f"  In Progress: {data['stats']['in_progress']}")
            print(f"  Completed: {data['stats']['completed']}")
            print(f"  Rejected: {data['stats']['rejected']}")
            
            # Pretty print JSON
            print("\nFull Response:")
            print(json.dumps(data, indent=2))
            
        else:
            print(f"\n✗ Failed to fetch stats")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("\n✗ Connection Error: Make sure the backend server is running on port 8000")
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")

if __name__ == "__main__":
    test_stats_api()
