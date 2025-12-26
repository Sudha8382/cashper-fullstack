"""
Test script for Corporate Services filtering API
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/business-services"

def test_all_applications():
    """Test getting all applications"""
    print("\n" + "="*60)
    print("TEST 1: Getting all applications")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/all-applications")
    data = response.json()
    
    print(f"✓ Status Code: {response.status_code}")
    print(f"✓ Total Applications: {data['count']}")
    print(f"✓ Success: {data['success']}")
    
    if data['applications']:
        print(f"\n✓ Sample Application:")
        app = data['applications'][0]
        print(f"  - Service Type: {app.get('service_type')}")
        print(f"  - Status: {app.get('status')}")
        print(f"  - Company: {app.get('company_name', app.get('full_name'))}")

def test_filter_by_service():
    """Test filtering by service type"""
    print("\n" + "="*60)
    print("TEST 2: Filtering by Service Type")
    print("="*60)
    
    service_types = [
        "Accounting & Bookkeeping",
        "GST Services",
        "TDS Services",
        "Payroll Services"
    ]
    
    for service in service_types:
        response = requests.get(
            f"{BASE_URL}/all-applications",
            params={"service_type": service}
        )
        data = response.json()
        print(f"\n✓ {service}: {data['count']} applications")
        
        # Verify all returned apps have correct service type
        if data['applications']:
            all_match = all(app['service_type'] == service for app in data['applications'])
            print(f"  {'✓' if all_match else '✗'} All applications match filter")

def test_filter_by_status():
    """Test filtering by status"""
    print("\n" + "="*60)
    print("TEST 3: Filtering by Status")
    print("="*60)
    
    statuses = ["Pending", "In Progress", "Completed", "Rejected"]
    
    for status in statuses:
        response = requests.get(
            f"{BASE_URL}/all-applications",
            params={"status": status}
        )
        data = response.json()
        print(f"\n✓ {status}: {data['count']} applications")
        
        # Verify all returned apps have correct status
        if data['applications']:
            all_match = all(
                app['status'].lower() == status.lower() 
                for app in data['applications']
            )
            print(f"  {'✓' if all_match else '✗'} All applications match filter")

def test_combined_filters():
    """Test combining service type and status filters"""
    print("\n" + "="*60)
    print("TEST 4: Combined Filters (Service + Status)")
    print("="*60)
    
    test_cases = [
        ("Accounting & Bookkeeping", "Pending"),
        ("GST Services", "Completed"),
        ("Payroll Services", "In Progress")
    ]
    
    for service, status in test_cases:
        response = requests.get(
            f"{BASE_URL}/all-applications",
            params={
                "service_type": service,
                "status": status
            }
        )
        data = response.json()
        print(f"\n✓ {service} + {status}: {data['count']} applications")
        
        # Verify filters applied correctly
        if data['applications']:
            all_match = all(
                app['service_type'] == service and 
                app['status'].lower() == status.lower()
                for app in data['applications']
            )
            print(f"  {'✓' if all_match else '✗'} All applications match both filters")

def test_filter_response_format():
    """Test response format with filters"""
    print("\n" + "="*60)
    print("TEST 5: Response Format Validation")
    print("="*60)
    
    response = requests.get(
        f"{BASE_URL}/all-applications",
        params={
            "service_type": "GST Services",
            "status": "Pending"
        }
    )
    data = response.json()
    
    print(f"✓ Has 'success' field: {'success' in data}")
    print(f"✓ Has 'count' field: {'count' in data}")
    print(f"✓ Has 'applications' field: {'applications' in data}")
    print(f"✓ Has 'filters' field: {'filters' in data}")
    
    if 'filters' in data:
        print(f"\n✓ Applied Filters:")
        print(f"  - Service Type: {data['filters'].get('service_type')}")
        print(f"  - Status: {data['filters'].get('status')}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CORPORATE SERVICES FILTERING API TESTS")
    print("="*60)
    
    try:
        test_all_applications()
        test_filter_by_service()
        test_filter_by_status()
        test_combined_filters()
        test_filter_response_format()
        
        print("\n" + "="*60)
        print("✓ ALL TESTS COMPLETED SUCCESSFULLY!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}\n")
        import traceback
        traceback.print_exc()
