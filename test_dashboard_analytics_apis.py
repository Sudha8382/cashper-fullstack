"""
Test script for Dashboard Analytics APIs
Tests Financial Growth Trend and Application Status Overview endpoints
"""

import requests
import json
from datetime import datetime

# Configuration
BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = f"{BASE_URL}/api/auth/login"

# Test user credentials (update with actual test user)
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


def test_financial_growth_trend(token, period="6months"):
    """Test Financial Growth Trend API"""
    try:
        print("\n" + "="*60)
        print(f"TESTING FINANCIAL GROWTH TREND API (Period: {period})")
        print("="*60)
        
        headers = {"Authorization": f"Bearer {token}"}
        url = f"{BASE_URL}/api/dashboard/financial-growth-trend?period={period}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API call successful!")
            print(f"\n📊 SUMMARY:")
            print(f"   Period: {data.get('period', 'N/A')}")
            print(f"   Total Loans: ₹{data['summary']['totalLoans']:,}")
            print(f"   Total Investments: ₹{data['summary']['totalInvestments']:,}")
            print(f"   Total Insurance: ₹{data['summary']['totalInsurance']:,}")
            print(f"   Grand Total: ₹{data['summary']['grandTotal']:,}")
            print(f"   Growth %: {data['summary']['growthPercentage']}%")
            
            print(f"\n📈 MONTHLY DATA:")
            for month_data in data['chartData']:
                print(f"   {month_data['month']}: Loans=₹{month_data['loans']:,}, "
                      f"Investments=₹{month_data['investments']:,}, "
                      f"Insurance=₹{month_data['insurance']:,}")
            
            return data
        else:
            print(f"❌ API call failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        return None


def test_application_status_overview(token):
    """Test Application Status Overview API"""
    try:
        print("\n" + "="*60)
        print("TESTING APPLICATION STATUS OVERVIEW API")
        print("="*60)
        
        headers = {"Authorization": f"Bearer {token}"}
        url = f"{BASE_URL}/api/dashboard/application-status-overview"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API call successful!")
            print(f"\n📊 STATUS COUNTS:")
            for status, count in data['statusCounts'].items():
                percentage = data['percentages'][status]
                print(f"   {status}: {count} ({percentage}%)")
            
            print(f"\n📈 TOTAL APPLICATIONS: {data['totalApplications']}")
            
            print(f"\n🔍 SERVICE BREAKDOWN:")
            for service, statuses in data['serviceBreakdown'].items():
                service_total = sum(statuses.values())
                print(f"   {service.upper()}: {service_total} total")
                for status, count in statuses.items():
                    if count > 0:
                        print(f"      - {status}: {count}")
            
            print(f"\n📊 CHART DATA:")
            for item in data['chartData']:
                print(f"   {item['status']}: {item['count']} (Color: {item['fill']})")
            
            return data
        else:
            print(f"❌ API call failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        return None


def test_all_periods(token):
    """Test Financial Growth Trend with all period options"""
    print("\n" + "="*60)
    print("TESTING ALL TIME PERIODS")
    print("="*60)
    
    periods = ["3months", "6months", "12months", "all"]
    
    for period in periods:
        result = test_financial_growth_trend(token, period)
        if result:
            print(f"✅ {period} test passed")
        else:
            print(f"❌ {period} test failed")


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("DASHBOARD ANALYTICS API TEST SUITE")
    print("="*60)
    print(f"Base URL: {BASE_URL}")
    print(f"Test User: {TEST_USER['email']}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get authentication token
    token = get_auth_token()
    
    if not token:
        print("\n❌ Cannot proceed without authentication token")
        print("Please ensure:")
        print("1. Backend server is running (python run_server.py)")
        print("2. Test user credentials are correct")
        print("3. MongoDB is connected")
        return
    
    # Test Financial Growth Trend (default period)
    print("\n" + "="*60)
    print("TEST 1: Financial Growth Trend (6 months)")
    print("="*60)
    growth_result = test_financial_growth_trend(token, "6months")
    
    # Test Application Status Overview
    print("\n" + "="*60)
    print("TEST 2: Application Status Overview")
    print("="*60)
    status_result = test_application_status_overview(token)
    
    # Test all periods
    print("\n" + "="*60)
    print("TEST 3: All Time Periods")
    print("="*60)
    test_all_periods(token)
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    tests_passed = 0
    tests_failed = 0
    
    if growth_result:
        tests_passed += 1
        print("✅ Financial Growth Trend API: PASSED")
    else:
        tests_failed += 1
        print("❌ Financial Growth Trend API: FAILED")
    
    if status_result:
        tests_passed += 1
        print("✅ Application Status Overview API: PASSED")
    else:
        tests_failed += 1
        print("❌ Application Status Overview API: FAILED")
    
    print(f"\n📊 Results: {tests_passed} passed, {tests_failed} failed")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
