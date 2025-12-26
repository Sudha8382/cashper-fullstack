#!/usr/bin/env python3
"""
Simple test to check if GET /api/personal-tax/application/all is working
"""

import requests
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2OTRlZmE1MWFiZGY1NmYyZDMwNWI0ZmUiLCJlbWFpbCI6InRlc3RfdXNlcmlkXzIwMjUxMjI3XzAyNDI0NUB0ZXN0LmNvbSIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNzY3Mzg4MzcyfQ.ltgTplNdKCGCCLChzMopTgESqeFyCj1rqpAhI_ELJ_s"

response = requests.get(
    "http://localhost:8000/api/personal-tax/application/all",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
)

print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
