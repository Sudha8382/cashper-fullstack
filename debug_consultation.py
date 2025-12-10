#!/usr/bin/env python
"""
Debug script to check database documents directly
"""
import requests
import json

# Test with status filter - which works
print("Testing with status_filter=pending (WORKS):")
response = requests.get(
    "http://localhost:8000/api/personal-tax/consultation/all?status_filter=pending&limit=1",
    timeout=10
)

if response.status_code == 200:
    data = response.json()
    if data:
        print("Document structure:")
        print(json.dumps(data[0], indent=2, default=str))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
