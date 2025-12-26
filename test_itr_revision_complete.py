#!/usr/bin/env python3
"""
Complete ITR Revision API Testing Script
Tests the form submission endpoint with proper authentication flow
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8000"
API_URL = f"{BASE_URL}/api/retail-services/itr-revision"
LOGIN_URL = f"{BASE_URL}/api/users/login"

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_section(title):
    print(f"\n{BLUE}{'='*60}")
    print(f"{title}")
    print(f"{'='*60}{RESET}\n")

def print_success(msg):
    print(f"{GREEN}✓ {msg}{RESET}")

def print_error(msg):
    print(f"{RED}✗ {msg}{RESET}")

def print_info(msg):
    print(f"{YELLOW}ℹ {msg}{RESET}")

print_section("ITR REVISION API - COMPLETE TESTING SUITE")

# Step 1: Check if server is running
print_info("Step 1: Checking if backend server is running...")
try:
    response = requests.get(f"{BASE_URL}/docs", timeout=2)
    print_success("Backend server is accessible")
except Exception as e:
    print_error(f"Backend server not accessible: {e}")
    print_info("Please start the server with: python run_server.py")
    exit(1)

# Step 2: Test login
print_info("Step 2: Logging in to get authentication token...")
try:
    login_response = requests.post(
        LOGIN_URL,
        json={
            "email": "admin@cashper.ai",
            "password": "admin@123"
        },
        timeout=5
    )
    
    if login_response.status_code != 200:
        print_error(f"Login failed with status {login_response.status_code}")
        print_error(f"Response: {login_response.text}")
        exit(1)
    
    login_data = login_response.json()
    token = login_data.get("access_token")
    
    if not token:
        print_error("No access token received from login")
        exit(1)
    
    print_success(f"Login successful! Token: {token[:30]}...")
    
except Exception as e:
    print_error(f"Login request failed: {e}")
    exit(1)

# Step 3: Prepare test data
print_info("Step 3: Preparing test form data...")

test_data = {
    "fullName": "Raj Kumar Singh",
    "email": "raj.kumar@example.com",
    "phone": "9876543210",
    "panNumber": "ABCDE1234F",
    "assessmentYear": "2023-24",
    "itrType": "ITR-2",
    "acknowledgmentNumber": "123456789012345",
    "originalFilingDate": "2024-01-15",
    "revisionReason": "Correction of income details from salary slip and deduction claims for medical insurance premiums",
    "address": "123 Main Street, Building A, Apartment 5",
    "city": "Delhi",
    "state": "Delhi",
    "pincode": "110001"
}

print_success(f"Test data prepared with {len(test_data)} fields")
for key, value in test_data.items():
    print(f"  • {key}: {value[:50] if len(str(value)) > 50 else value}")

# Step 4: Test without authentication (should fail)
print_section("TEST 1: Submission without authentication (should fail)")
try:
    response = requests.post(API_URL, data=test_data, timeout=5)
    print_info(f"Status Code: {response.status_code}")
    print_info(f"Response: {response.text[:200]}...")
    if response.status_code in [401, 403]:
        print_success("Correctly rejected request without authentication")
    else:
        print_error(f"Unexpected status code: {response.status_code}")
except Exception as e:
    print_error(f"Request failed: {e}")

# Step 5: Test with authentication but without files
print_section("TEST 2: Submission with auth but without required files")
try:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(API_URL, data=test_data, headers=headers, timeout=5)
    print_info(f"Status Code: {response.status_code}")
    
    if response.status_code == 400:
        error_detail = response.json().get("detail", "Unknown error")
        if "required" in str(error_detail).lower() or "document" in str(error_detail).lower():
            print_success(f"Correctly rejected: {error_detail}")
        else:
            print_error(f"Unexpected error: {error_detail}")
    else:
        print_error(f"Unexpected status code: {response.status_code}")
        print_info(f"Response: {response.text}")
except Exception as e:
    print_error(f"Request failed: {e}")

# Step 6: Test with files (mock files)
print_section("TEST 3: Submission with required documents")
try:
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create mock files in memory
    files = {
        "originalITR": ("sample_itr.txt", "Sample ITR Document Content", "text/plain"),
        "acknowledgmentReceipt": ("sample_receipt.txt", "Sample Acknowledgment Receipt", "text/plain")
    }
    
    print_info("Uploading with files...")
    response = requests.post(
        API_URL, 
        data=test_data, 
        files=files,
        headers=headers, 
        timeout=10
    )
    
    print_info(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print_success("Form submission successful!")
        print_success(f"Application ID: {result.get('applicationId')}")
        print_success(f"Message: {result.get('message')}")
        
        # Print response details
        print_info("\nResponse Details:")
        print(json.dumps(result, indent=2)[:500] + "...")
        
    elif response.status_code == 401:
        print_error("Authentication failed - invalid or expired token")
    elif response.status_code == 400:
        error_detail = response.json().get("detail", "Validation error")
        print_error(f"Validation error: {error_detail}")
    else:
        print_error(f"Request failed with status {response.status_code}")
        print_error(f"Response: {response.text[:300]}")
        
except Exception as e:
    print_error(f"Request failed: {e}")

# Summary
print_section("TEST SUMMARY")
print_info("All tests completed!")
print_info("Check the results above for any errors or issues")
print_info("\nKey things to verify:")
print("  1. Backend server is running on port 8000")
print("  2. Authentication token is properly set")
print("  3. Form data is complete and valid")
print("  4. Required documents are uploaded")
print("  5. Database connection is working")
print_info("\nFor detailed debugging:")
print("  • Check backend server logs for [ITR REVISION] messages")
print("  • Check browser DevTools Console for frontend errors")
print("  • Verify MongoDB connection and RetailServiceApplications collection")
