import requests

print("Testing all 9 services APIs...")
print("=" * 60)

services = [
    'company-registration',
    'company-compliance',
    'tax-audit',
    'legal-advice',
    'provident-fund-services',
    'tds-services',
    'gst-services',
    'payroll-services',
    'accounting-bookkeeping'
]

for service in services:
    try:
        res = requests.get(f'http://127.0.0.1:8000/api/business-services/{service}')
        count = res.json().get('count', 0)
        status = "✅" if count > 0 else "⚠️"
        print(f"{status} {service:35} Status: {res.status_code}, Count: {count}")
    except Exception as e:
        print(f"❌ {service:35} Error: {str(e)}")

print("=" * 60)
