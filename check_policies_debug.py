import requests
import json

r = requests.get('http://localhost:8000/api/admin/insurance-management/policies', params={'limit': 5})
data = r.json()
print('Response:')
print(json.dumps(data, indent=2))
