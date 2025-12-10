#!/usr/bin/env python3
"""
Verify that the Loan Management admin panel is getting real-time data
Tests both statistics and applications endpoints
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")

def test_statistics():
    """Test the statistics endpoint"""
    print_section("TEST 1: Statistics Endpoint")
    
    try:
        url = f"{BASE_URL}/api/admin/loan-management/statistics"
        response = requests.get(url)
        
        print(f"URL: {url}")
        print(f"Status: {response.status_code} {'✓ OK' if response.status_code == 200 else '✗ FAILED'}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nStatistics Response:")
            print(f"  Total Applications: {data.get('totalApplications', 0)}")
            print(f"  Pending: {data.get('pendingApplications', 0)}")
            print(f"  Under Review: {data.get('underReviewApplications', 0)}")
            print(f"  Approved: {data.get('approvedApplications', 0)}")
            print(f"  Rejected: {data.get('rejectedApplications', 0)}")
            print(f"  Disbursed: {data.get('disbursedApplications', 0)}")
            print(f"\nLoan Type Breakdown:")
            print(f"  Home Loans: {data.get('homeLoanCount', 0)}")
            print(f"  Personal Loans: {data.get('personalLoanCount', 0)}")
            print(f"  Business Loans: {data.get('businessLoanCount', 0)}")
            print(f"  Short-term Loans: {data.get('shortTermLoanCount', 0)}")
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Exception: {str(e)}")
        return False

def test_applications():
    """Test the applications endpoint"""
    print_section("TEST 2: Applications Endpoint")
    
    try:
        url = f"{BASE_URL}/api/admin/loan-management/applications?page=1&limit=5"
        response = requests.get(url)
        
        print(f"URL: {url}")
        print(f"Status: {response.status_code} {'✓ OK' if response.status_code == 200 else '✗ FAILED'}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nPagination Info:")
            print(f"  Total Applications: {data.get('total', 0)}")
            print(f"  Current Page: {data.get('page', 1)}")
            print(f"  Limit: {data.get('limit', 10)}")
            print(f"  Total Pages: {data.get('totalPages', 1)}")
            
            applications = data.get('applications', [])
            print(f"\nApplications on this page: {len(applications)}")
            
            for i, app in enumerate(applications, 1):
                print(f"\n  [{i}] {app.get('customer', 'Unknown')}")
                print(f"      ID: {app.get('id', 'N/A')}")
                print(f"      Type: {app.get('type', 'N/A')}")
                print(f"      Amount: {app.get('amount', 'N/A')}")
                print(f"      Status: {app.get('status', 'N/A')}")
                print(f"      Applied Date: {app.get('appliedDate', 'N/A')}")
                print(f"      Documents: {len(app.get('documents', []))}")
            
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Exception: {str(e)}")
        return False

def test_status_filter():
    """Test filtering by status"""
    print_section("TEST 3: Filter by Status - Pending")
    
    try:
        url = f"{BASE_URL}/api/admin/loan-management/applications?status=Pending&page=1&limit=5"
        response = requests.get(url)
        
        print(f"URL: {url}")
        print(f"Status: {response.status_code} {'✓ OK' if response.status_code == 200 else '✗ FAILED'}")
        
        if response.status_code == 200:
            data = response.json()
            applications = data.get('applications', [])
            total = data.get('total', 0)
            
            print(f"Pending Applications: {total}")
            print(f"Showing first {len(applications)} applications:")
            
            for i, app in enumerate(applications[:3], 1):
                print(f"  [{i}] {app.get('customer')} - {app.get('status')}")
            
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Exception: {str(e)}")
        return False

def test_loan_type_filter():
    """Test filtering by loan type"""
    print_section("TEST 4: Filter by Loan Type - Home Loan")
    
    try:
        url = f"{BASE_URL}/api/admin/loan-management/applications?loan_type=Home Loan&page=1&limit=5"
        response = requests.get(url)
        
        print(f"URL: {url}")
        print(f"Status: {response.status_code} {'✓ OK' if response.status_code == 200 else '✗ FAILED'}")
        
        if response.status_code == 200:
            data = response.json()
            applications = data.get('applications', [])
            total = data.get('total', 0)
            
            print(f"Home Loan Applications: {total}")
            print(f"Showing first {len(applications)} applications:")
            
            for i, app in enumerate(applications[:3], 1):
                print(f"  [{i}] {app.get('customer')} - {app.get('type')}")
            
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Exception: {str(e)}")
        return False

def main():
    print(f"\n{'*'*70}")
    print(f"  LOAN MANAGEMENT ADMIN PANEL - REAL-TIME DATA VERIFICATION")
    print(f"  Testing at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'*'*70}")
    
    results = {
        "Statistics": test_statistics(),
        "Applications": test_applications(),
        "Status Filter": test_status_filter(),
        "Loan Type Filter": test_loan_type_filter()
    }
    
    print_section("TEST SUMMARY")
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    print(f"\nOverall Status: {'✓ ALL TESTS PASSED' if all_passed else '✗ SOME TESTS FAILED'}")
    print(f"{'*'*70}\n")

if __name__ == "__main__":
    main()
