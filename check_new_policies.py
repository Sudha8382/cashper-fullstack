import requests
import json

r = requests.get('http://localhost:8000/api/admin/insurance-management/policies', params={'limit': 3, 'status': 'Pending'})
data = r.json()
print('Recent Pending Policies:')
for policy in data['policies']:
    print(f"\nPolicy ID: {policy.get('policyId')}")
    print(f"Customer: {policy.get('customer')}")
    print(f"Type: {policy.get('type')}")
    print(f"Status: {policy.get('status')}")
    print(f"Email: {policy.get('email')}")
    print(f"All keys: {list(policy.keys())}")
