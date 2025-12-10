#!/usr/bin/env python3
"""Debug script to find where the sample data is coming from"""

import requests
import json

print("="*80)
print("DEBUGGING: Finding source of sample data")
print("="*80)

# Check admin endpoint
print("\n1. Checking Admin Endpoint:")
print("-"*80)
r = requests.get('http://127.0.0.1:8000/api/admin/loan-management/applications?page=1&limit=10')
admin_data = r.json()

print("Admin Endpoint - Applications:")
for app in admin_data.get('applications', [])[:3]:
    customer = app.get('customer', 'Unknown')
    print("  - Customer: {}".format(customer))
    print("    ID: {}".format(app.get('id')))
    print("    Type: {}".format(app.get('type')))
    print()

# Check short-term loan endpoint
print("\n2. Checking Short-Term Loan Endpoint:")
print("-"*80)
try:
    r = requests.get('http://127.0.0.1:8000/api/short-term-loan/applications')
    stl_data = r.json()
    
    if isinstance(stl_data, list):
        print("Short-Term Loans (Array format):")
        for app in stl_data[:3]:
            customer = app.get('fullName', 'Unknown')
            print("  - Customer: {}".format(customer))
            print("    ID: {}".format(app.get('_id', 'N/A')))
            print()
    elif isinstance(stl_data, dict):
        apps = stl_data.get('applications', [])
        print("Short-Term Loans (Object format):")
        for app in apps[:3]:
            customer = app.get('fullName', 'Unknown')
            print("  - Customer: {}".format(customer))
            print("    ID: {}".format(app.get('_id', 'N/A')))
            print()
except Exception as e:
    print("Error: {}".format(str(e)))

# Check personal loan endpoint
print("\n3. Checking Personal Loan Endpoint:")
print("-"*80)
try:
    r = requests.get('http://127.0.0.1:8000/api/personal-loan/applications')
    pl_data = r.json()
    
    if isinstance(pl_data, list):
        print("Personal Loans (Array format):")
        for app in pl_data[:3]:
            customer = app.get('fullName', app.get('customer', 'Unknown'))
            print("  - Customer: {}".format(customer))
            print()
except Exception as e:
    print("Error: {}".format(str(e)))

# Search for Sudha Yadav specifically
print("\n4. Searching for 'Sudha Yadav':")
print("-"*80)
try:
    r = requests.get('http://127.0.0.1:8000/api/short-term-loan/applications')
    stl_data = r.json()
    
    if isinstance(stl_data, list):
        for app in stl_data:
            if 'Sudha' in app.get('fullName', ''):
                print("FOUND in short-term endpoint:")
                print(json.dumps(app, indent=2, ensure_ascii=False)[:500])
except Exception as e:
    print("Not found in short-term: {}".format(str(e)))

print("\n" + "="*80)
