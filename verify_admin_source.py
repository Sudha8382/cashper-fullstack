#!/usr/bin/env python3
"""Verify admin applications endpoint is only returning admin collection data"""

import requests
import json

print("="*80)
print("VERIFY ADMIN ENDPOINT DATA SOURCE")
print("="*80)

# Get first few applications with detailed info
r = requests.get('http://127.0.0.1:8000/api/admin/loan-management/applications?page=1&limit=10')
data = r.json()

print("\nApplications returned from /api/admin/loan-management/applications:")
print("Total Count: {}".format(data.get('total')))
print("Current Page: {}".format(data.get('page')))
print("\nApplications:")

for i, app in enumerate(data.get('applications', []), 1):
    app_id = app.get('id', 'N/A')
    customer = app.get('customer', 'Unknown')
    email = app.get('email', 'N/A')
    app_type = app.get('type', 'N/A')
    amount = app.get('amount', 'N/A')
    
    print("\n[{}] {}".format(i, customer))
    print("    ID: {}".format(app_id))
    print("    Type: {}".format(app_type))
    print("    Amount: {}".format(amount))
    print("    Email: {}".format(email))
    
    # Check if this is Sudha Yadav
    if 'Sudha' in customer:
        print("    WARNING: Found Sudha Yadav in admin endpoint!")

print("\n" + "="*80)
print("CHECK: Is Sudha Yadav in the results? {}".format(
    any('Sudha' in app.get('customer', '') for app in data.get('applications', []))
))
print("="*80)
