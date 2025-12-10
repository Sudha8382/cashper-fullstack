import requests
import json

# Login
response = requests.post(
    'http://127.0.0.1:8000/api/admin/login',
    json={'email': 'sudha@gmail.com', 'password': 'Sudha@123'}
)
token = response.json()['access_token']

# Get performance metrics
metrics_response = requests.get(
    'http://127.0.0.1:8000/api/admin/dashboard/performance-metrics',
    headers={'Authorization': f'Bearer {token}'}
)
metrics = metrics_response.json()

print("\n" + "="*60)
print("🔄 CURRENT API DATA FROM BACKEND")
print("="*60)
print(f"  Total Logins: {metrics['total_logins']:,}")
print(f"  Hours Active: {metrics['hours_active']:,}")
print(f"  Tasks Completed: {metrics['tasks_completed']:,}")
print(f"  Rating: {metrics['rating']}/5")
print("="*60 + "\n")
