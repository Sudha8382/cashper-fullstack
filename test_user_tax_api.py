#!/usr/bin/env python3
"""
Test script to verify user-specific GET endpoints for Personal and Business Tax Planning
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_personal_tax_user_api(email):
    """Test getting personal tax applications by user email"""
    print(f"\n{'='*60}")
    print(f"Testing Personal Tax API - GET by Email: {email}")
    print('='*60)
    
    url = f"{BASE_URL}/personal-tax/application/user/{email}"
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        
        if response.ok:
            data = response.json()
            print(f"Found {len(data)} applications")
            if data:
                print(f"\nApplications for {email}:")
                for app in data:
                    print(f"\n  ID: {app.get('id')}")
                    print(f"  Name: {app.get('fullName')}")
                    print(f"  Email: {app.get('emailAddress')}")
                    print(f"  Phone: {app.get('phoneNumber')}")
                    print(f"  PAN: {app.get('panNumber')}")
                    print(f"  Status: {app.get('status')}")
                    print(f"  Employment Type: {app.get('employmentType')}")
                    print(f"  Annual Income: {app.get('annualIncome')}")
                    print(f"  Created: {app.get('createdAt')}")
        else:
            print(f"Error: {response.text}")
    
    except Exception as e:
        print(f"Request failed: {e}")


def test_business_tax_user_api(email):
    """Test getting business tax applications by user email"""
    print(f"\n{'='*60}")
    print(f"Testing Business Tax API - GET by Email: {email}")
    print('='*60)
    
    url = f"{BASE_URL}/business-tax/application/user/{email}"
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        
        if response.ok:
            data = response.json()
            print(f"Found {len(data)} applications")
            if data:
                print(f"\nApplications for {email}:")
                for app in data:
                    print(f"\n  ID: {app.get('id')}")
                    print(f"  Business Name: {app.get('businessName')}")
                    print(f"  Email: {app.get('businessEmail')}")
                    print(f"  Contact: {app.get('contactNumber')}")
                    print(f"  Business PAN: {app.get('businessPAN')}")
                    print(f"  Structure: {app.get('businessStructure')}")
                    print(f"  Industry: {app.get('industryType')}")
                    print(f"  Status: {app.get('status')}")
                    print(f"  Created: {app.get('createdAt')}")
        else:
            print(f"Error: {response.text}")
    
    except Exception as e:
        print(f"Request failed: {e}")


def test_submit_personal_tax_application(data):
    """Test submitting a personal tax application"""
    print(f"\n{'='*60}")
    print(f"Testing Personal Tax Submit API")
    print('='*60)
    
    url = f"{BASE_URL}/personal-tax/application/submit"
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        result = response.json()
        
        if response.ok:
            print(f"Application submitted successfully!")
            print(f"Application ID: {result.get('id')}")
            return result.get('id')
        else:
            print(f"Error: {result}")
    
    except Exception as e:
        print(f"Request failed: {e}")
    
    return None


def test_submit_business_tax_application(data):
    """Test submitting a business tax application"""
    print(f"\n{'='*60}")
    print(f"Testing Business Tax Submit API")
    print('='*60)
    
    url = f"{BASE_URL}/business-tax/application/submit"
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        result = response.json()
        
        if response.ok:
            print(f"Application submitted successfully!")
            print(f"Application ID: {result.get('id')}")
            return result.get('id')
        else:
            print(f"Error: {result}")
    
    except Exception as e:
        print(f"Request failed: {e}")
    
    return None


if __name__ == "__main__":
    # Test email
    test_email = "testuser@example.com"
    
    print("\n" + "="*60)
    print("USER-SPECIFIC TAX API TEST SUITE")
    print("="*60)
    
    # Step 1: Submit Personal Tax Application
    print("\n[STEP 1] Submitting Personal Tax Application...")
    personal_app_data = {
        "fullName": "Test User",
        "emailAddress": test_email,
        "phoneNumber": "9876543210",
        "panNumber": "ABCDE1234F",
        "annualIncome": "10-20",
        "employmentType": "salaried",
        "preferredTaxRegime": "new",
        "additionalInfo": "Test application"
    }
    
    personal_app_id = test_submit_personal_tax_application(personal_app_data)
    
    # Step 2: Submit Business Tax Application
    print("\n[STEP 2] Submitting Business Tax Application...")
    business_app_data = {
        "businessName": "Test Business Inc",
        "businessEmail": test_email,
        "contactNumber": "9876543210",
        "businessPAN": "ABCDE1234F",
        "businessStructure": "private",
        "industryType": "IT",
        "turnoverRange": "10-20"
    }
    
    business_app_id = test_submit_business_tax_application(business_app_data)
    
    # Step 3: Get Personal Tax Applications by Email
    print("\n[STEP 3] Retrieving Personal Tax Applications by Email...")
    test_personal_tax_user_api(test_email)
    
    # Step 4: Get Business Tax Applications by Email
    print("\n[STEP 4] Retrieving Business Tax Applications by Email...")
    test_business_tax_user_api(test_email)
    
    print("\n" + "="*60)
    print("TEST SUITE COMPLETE")
    print("="*60)
