#!/usr/bin/env python3
import requests

email = 'sudha@gmail.com'
resp = requests.get(f'http://localhost:8000/api/business-tax/application/user/{email}')
print(f'Status: {resp.status_code}')
print(f'Response: {resp.text}')
