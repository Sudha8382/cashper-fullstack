import requests

r = requests.get('http://localhost:8000/api/admin/insurance-management/policies', params={'limit': 20})
policies = r.json()['policies']
print('Recent policies:')
for p in policies[:10]:
    print(f"{p['policyNumber']} - {p['customerName']} - {p['insuranceType']}")
