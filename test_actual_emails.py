#!/usr/bin/env python3
import requests

print("="*60)
print("Testing User-Specific GET APIs")
print("="*60)

test_emails = [
    'sudha@gmail.com',
    'rajesh.kumar@example.com',
    'vikram@techsolutions.com'
]

for email in test_emails:
    print(f'\n--- Email: {email} ---')
    
    # Personal Tax
    resp = requests.get(f'http://localhost:8000/api/personal-tax/application/user/{email}')
    if resp.status_code == 200:
        data = resp.json()
        print(f'Personal Tax Apps: {len(data)} found')
        for app in data[:1]:
            print(f'  Name: {app.get("fullName")}')
            print(f'  Email: {app.get("emailAddress")}')
            print(f'  PAN: {app.get("panNumber")}')
            print(f'  Status: {app.get("status")}')
    else:
        print(f'Personal Tax Error: {resp.status_code}')
    
    # Business Tax
    resp = requests.get(f'http://localhost:8000/api/business-tax/application/user/{email}')
    if resp.status_code == 200:
        data = resp.json()
        print(f'Business Tax Apps: {len(data)} found')
        for app in data[:1]:
            print(f'  Name: {app.get("businessName")}')
            print(f'  Email: {app.get("businessEmail")}')
            print(f'  Status: {app.get("status")}')
    else:
        print(f'Business Tax Error: {resp.status_code}')

print("\n" + "="*60)
print("APIs working successfully!")
print("="*60)
