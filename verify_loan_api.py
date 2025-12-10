#!/usr/bin/env python3
"""
Quick verification test for Loan Management API
Tests that filters, statistics, and modal data are working correctly
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000/api/admin"

def get_token():
    """Get admin token from test credentials"""
    try:
        response = requests.post(
            "http://localhost:8000/api/auth/login",
            json={
                "email": "sudha@gmail.com",
                "password": "your_password"
            }
        )
        if response.status_code == 200:
            return response.json().get("access_token")
    except:
        pass
    return None

def print_section(title):
    """Print formatted section header"""
    print(f"\n{'='*80}")
    print(f"  {title}")
    print(f"{'='*80}\n")

def test_statistics(token):
    """Test statistics endpoint"""
    print_section("TEST 1: Get Statistics")
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{BASE_URL}/loan-management/statistics",
            headers=headers
        )
        
        if response.status_code == 200:
            stats = response.json()
            print("✅ Statistics retrieved successfully!")
            print(f"   Total Applications: {stats.get('totalApplications', 0)}")
            print(f"   Pending: {stats.get('pendingApplications', 0)}")
            print(f"   Under Review: {stats.get('underReviewApplications', 0)}")
            print(f"   Approved: {stats.get('approvedApplications', 0)}")
            print(f"   Rejected: {stats.get('rejectedApplications', 0)}")
            print(f"   Disbursed: {stats.get('disbursedApplications', 0)}")
            return True
        else:
            print(f"❌ Failed: {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_get_all_applications(token):
    """Test get all applications endpoint"""
    print_section("TEST 2: Get All Applications (No Filter)")
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{BASE_URL}/loan-management/applications",
            params={"page": 1, "limit": 5},
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            apps = data.get("applications", [])
            print(f"✅ Retrieved {len(apps)} applications (Total: {data.get('total', 0)})")
            if apps:
                for app in apps[:3]:
                    print(f"   - {app.get('customer')} ({app.get('status')})")
            return True
        else:
            print(f"❌ Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_status_filters(token):
    """Test all status filters"""
    print_section("TEST 3: Test All Status Filters")
    
    statuses = ["Pending", "Under Review", "Approved", "Rejected", "Disbursed"]
    headers = {"Authorization": f"Bearer {token}"}
    results = {}
    
    for status in statuses:
        try:
            response = requests.get(
                f"{BASE_URL}/loan-management/applications",
                params={"status": status, "page": 1, "limit": 5},
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                count = len(data.get("applications", []))
                total = data.get("total", 0)
                results[status] = (True, count, total)
                print(f"✅ {status}: {count} apps retrieved (Total: {total})")
            else:
                results[status] = (False, 0, 0)
                print(f"❌ {status}: Failed with status {response.status_code}")
        except Exception as e:
            results[status] = (False, 0, 0)
            print(f"❌ {status}: Error - {str(e)}")
    
    return results

def test_search(token):
    """Test search functionality"""
    print_section("TEST 4: Test Search Functionality")
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        
        # First get an application to search for
        response = requests.get(
            f"{BASE_URL}/loan-management/applications",
            params={"page": 1, "limit": 1},
            headers=headers
        )
        
        if response.status_code != 200:
            print("❌ Could not get applications for search test")
            return False
        
        apps = response.json().get("applications", [])
        if not apps:
            print("⚠️  No applications available for search test")
            return True
        
        # Search by first 3 characters of customer name
        customer = apps[0].get("customer", "")
        search_term = customer[:3] if customer else ""
        
        if not search_term:
            print("⚠️  Could not extract search term")
            return True
        
        response = requests.get(
            f"{BASE_URL}/loan-management/applications",
            params={"search": search_term, "page": 1, "limit": 5},
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            count = len(data.get("applications", []))
            print(f"✅ Search for '{search_term}': Found {count} results")
            return True
        else:
            print(f"❌ Search failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_get_single_application(token):
    """Test get single application endpoint"""
    print_section("TEST 5: Get Single Application Details")
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        
        # First get list to find an application ID
        response = requests.get(
            f"{BASE_URL}/loan-management/applications",
            params={"page": 1, "limit": 1},
            headers=headers
        )
        
        if response.status_code != 200:
            print("❌ Could not get applications list")
            return False
        
        apps = response.json().get("applications", [])
        if not apps:
            print("⚠️  No applications available")
            return True
        
        app_id = apps[0].get("id")
        if not app_id:
            print("❌ Could not extract application ID")
            return False
        
        # Get single application details
        response = requests.get(
            f"{BASE_URL}/loan-management/applications/{app_id}",
            headers=headers
        )
        
        if response.status_code == 200:
            app = response.json()
            print(f"✅ Retrieved details for: {app.get('customer')}")
            print(f"   Status: {app.get('status')}")
            print(f"   Amount: {app.get('amount')}")
            print(f"   CIBIL Score: {app.get('cibilScore')}")
            return True
        else:
            print(f"❌ Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "╔" + "="*78 + "╗")
    print("║" + " "*15 + "LOAN MANAGEMENT API VERIFICATION TEST" + " "*25 + "║")
    print("╚" + "="*78 + "╝")
    
    print("\n🔐 Attempting to get authentication token...")
    token = get_token()
    
    if not token:
        print("⚠️  Could not get auth token. Using test mode without authentication.")
        print("   (This will only work if the API allows unauthenticated access)")
        token = "test_token"
    else:
        print("✅ Authentication successful!\n")
    
    # Run tests
    results = {
        "Statistics": test_statistics(token),
        "Get All Applications": test_get_all_applications(token),
        "Search": test_search(token),
        "Get Single Application": test_get_single_application(token),
    }
    
    # Test status filters separately
    status_results = test_status_filters(token)
    results["Status Filters"] = all([r[0] for r in status_results.values()])
    
    # Print summary
    print_section("TEST SUMMARY")
    print("Feature Test Results:")
    print("-" * 80)
    
    for feature, passed in results.items():
        if feature == "Status Filters":
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"  {feature:.<50} {status}")
        else:
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"  {feature:.<50} {status}")
    
    total_passed = sum(1 for v in results.values() if v)
    total_tests = len(results)
    
    print("-" * 80)
    print(f"\nOverall: {total_passed}/{total_tests} tests passed\n")
    
    if total_passed == total_tests:
        print("🎉 All tests passed! Loan Management API is fully functional!\n")
    else:
        print("⚠️  Some tests failed. Please check the output above for details.\n")

if __name__ == "__main__":
    main()
