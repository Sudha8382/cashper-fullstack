import requests
import json

# Test the API directly
print('=== Testing Short Term Loan API ===\n')

print('Please get your access token:')
print('1. Open browser (logged in as sudha@gmail.com)')
print('2. Press F12 → Console')
print('3. Run: localStorage.getItem("access_token")')
print('4. Copy the token\n')

token = input('Paste token here: ').strip()

if not token:
    print('No token provided!')
    exit()

url = 'http://127.0.0.1:8000/api/short-term-loan/applications'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

print(f'\nCalling: {url}')
print(f'Token: {token[:20]}...')

try:
    response = requests.get(url, headers=headers)
    print(f'\nStatus Code: {response.status_code}')
    
    if response.status_code == 200:
        data = response.json()
        print(f'✅ Success! Received {len(data)} loans')
        print(f'\nData:\n{json.dumps(data, indent=2)}')
    else:
        print(f'❌ Error: {response.status_code}')
        print(f'Response: {response.text}')
        
except Exception as e:
    print(f'❌ Exception: {e}')
