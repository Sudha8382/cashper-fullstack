"""
Test Corporate Services Status Update API
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/business-services"

def print_separator(title=""):
    print("\n" + "=" * 60)
    if title:
        print(title)
    print("=" * 60)

# First, get a sample application ID
print_separator("FETCHING SAMPLE APPLICATION")
response = requests.get(f"{BASE_URL}/all-applications")
if response.status_code == 200:
    data = response.json()
    if data.get("applications") and len(data["applications"]) > 0:
        sample_app = data["applications"][0]
        app_id = sample_app.get("_id")
        current_status = sample_app.get("status", "Unknown")
        service_type = sample_app.get("service_type", "Unknown")
        
        print(f"✓ Found Application:")
        print(f"  - ID: {app_id}")
        print(f"  - Service: {service_type}")
        print(f"  - Current Status: {current_status}")
        print(f"  - Company: {sample_app.get('company_name', sample_app.get('full_name', 'N/A'))}")
        
        # Test status updates
        test_statuses = ["In Progress", "Completed", "Pending", "Rejected"]
        
        for new_status in test_statuses:
            print_separator(f"TESTING STATUS UPDATE: {new_status}")
            
            update_url = f"{BASE_URL}/{app_id}/status"
            payload = {"status": new_status}
            
            print(f"URL: {update_url}")
            print(f"Payload: {json.dumps(payload, indent=2)}")
            
            response = requests.put(update_url, json=payload)
            print(f"✓ Status Code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"✓ Success: {result.get('success')}")
                print(f"✓ Message: {result.get('message')}")
                print(f"✓ New Status: {result.get('new_status')}")
                
                # Verify the update
                verify_response = requests.get(f"{BASE_URL}/all-applications")
                if verify_response.status_code == 200:
                    verify_data = verify_response.json()
                    updated_app = next(
                        (app for app in verify_data.get("applications", []) if app.get("_id") == app_id),
                        None
                    )
                    if updated_app:
                        actual_status = updated_app.get("status")
                        print(f"✓ Verified Status in Database: {actual_status}")
                        if actual_status == new_status:
                            print("✓ STATUS UPDATE VERIFIED SUCCESSFULLY!")
                        else:
                            print(f"✗ MISMATCH: Expected '{new_status}', Got '{actual_status}'")
            else:
                print(f"✗ Failed: {response.text}")
        
        print_separator("✓ ALL STATUS UPDATE TESTS COMPLETED!")
        
    else:
        print("✗ No applications found to test")
else:
    print(f"✗ Failed to fetch applications: {response.status_code}")
