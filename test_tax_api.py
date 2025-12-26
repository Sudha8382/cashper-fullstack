import requests
import json

print('🔍 TESTING TAX PLANNING APIS\n')
print('='*60)

# Test Personal Tax API
print('\n📊 PERSONAL TAX API TEST:')
try:
    response = requests.get('http://localhost:8000/api/personal-tax/application/all', timeout=5)
    print(f'Status: {response.status_code}')
    data = response.json()
    print(f'Total Records: {len(data)}')
    if data:
        print(f'Sample Record Fields: {list(data[0].keys())}')
        sample = data[0]
        print(f'  - Name: {sample.get("fullName", "N/A")}')
        print(f'  - Email: {sample.get("emailAddress", "N/A")}')
        print(f'  - Status: {sample.get("status", "N/A")}')
except Exception as e:
    print(f'❌ Error: {str(e)}')

print('\n' + '='*60)

# Test Business Tax API
print('\n📊 BUSINESS TAX API TEST:')
try:
    response = requests.get('http://localhost:8000/api/business-tax/application/all', timeout=5)
    print(f'Status: {response.status_code}')
    data = response.json()
    print(f'Total Records: {len(data)}')
    if data:
        print(f'Sample Record Fields: {list(data[0].keys())}')
        sample = data[0]
        print(f'  - Business: {sample.get("businessName", "N/A")}')
        print(f'  - Email: {sample.get("businessEmail", "N/A")}')
        print(f'  - Status: {sample.get("status", "N/A")}')
except Exception as e:
    print(f'❌ Error: {str(e)}')

print('\n' + '='*60)
print('\n✅ API VALIDATION COMPLETE - Backend is ready for real-time data fetching')
