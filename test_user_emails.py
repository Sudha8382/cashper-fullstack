#!/usr/bin/env python3
import requests

emails = [
    'sudha@123gmail.com',
    'test@test.com',
    'sudha.yadav@gmail.com'
]

for email in emails:
    print(f'\n=== Testing with email: {email} ===')
    
    # Personal Tax
    resp = requests.get(f'http://localhost:8000/api/personal-tax/application/user/{email}')
    print(f'Personal Tax: {resp.status_code}')
    if resp.ok:
        data = resp.json()
        print(f'  Found {len(data)} applications')
        for app in data[:1]:
            print(f'    Name: {app.get("fullName")}, Email: {app.get("emailAddress")}')
    
    # Business Tax
    resp = requests.get(f'http://localhost:8000/api/business-tax/application/user/{email}')
    print(f'Business Tax: {resp.status_code}')
    if resp.ok:
        data = resp.json()
        print(f'  Found {len(data)} applications')
        for app in data[:1]:
            print(f'    Name: {app.get("businessName")}, Email: {app.get("businessEmail")}')
