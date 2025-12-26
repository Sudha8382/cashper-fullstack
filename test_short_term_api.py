import requests

print('=== Testing Short Term Loan API ===\n')

# You need to get token from browser localStorage
print('STEP 1: Get your access token')
print('  1. Open browser console (F12)')
print('  2. Run: localStorage.getItem("access_token")')
print('  3. Copy the token\n')

token = input('Enter your access_token: ').strip()

if not token:
    print('❌ No token provided. Exiting.')
    exit()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

print('\n=== Testing All Loan APIs ===')

endpoints = {
    'Personal Loan': 'http://127.0.0.1:8000/api/personal-loan/applications',
    'Home Loan': 'http://127.0.0.1:8000/api/home-loan/applications',
    'Business Loan': 'http://127.0.0.1:8000/api/business-loan/applications',
    'Short Term Loan': 'http://127.0.0.1:8000/api/short-term-loan/applications',
}

for name, url in endpoints.items():
    print(f'\n{name}:')
    print(f'  URL: {url}')
    
    try:
        response = requests.get(url, headers=headers)
        print(f'  Status: {response.status_code}')
        
        if response.status_code == 200:
            data = response.json()
            print(f'  ✅ Count: {len(data)} loans')
            if data and len(data) > 0:
                print(f'  First loan: {data[0].get("fullName", "N/A")} - ₹{data[0].get("loanAmount", "N/A")}')
        elif response.status_code == 403:
            print(f'  ❌ Forbidden: {response.json()}')
        elif response.status_code == 401:
            print(f'  ❌ Unauthorized: {response.json()}')
        else:
            print(f'  ❌ Error: {response.text[:200]}')
    except Exception as e:
        print(f'  ❌ Exception: {e}')

print('\n=== Test Complete ===')
