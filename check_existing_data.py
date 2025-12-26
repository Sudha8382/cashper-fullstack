#!/usr/bin/env python3
import requests

resp = requests.get('http://localhost:8000/api/personal-tax/application/all')
print('All Personal Tax Applications:')
data = resp.json()
print(f'Total: {len(data)}')
if data:
    for app in data[:3]:
        print(f'  - {app.get("fullName")}: {app.get("emailAddress")}')
else:
    print('  No applications found')

resp = requests.get('http://localhost:8000/api/business-tax/application/all')
print('\nAll Business Tax Applications:')
data = resp.json()
print(f'Total: {len(data)}')
if data:
    for app in data[:3]:
        print(f'  - {app.get("businessName")}: {app.get("businessEmail")}')
else:
    print('  No applications found')
