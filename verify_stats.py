"""Verify backend API returns correct statistics"""
import requests
import json

try:
    response = requests.get("http://127.0.0.1:8000/api/admin/loan-management/statistics")
    
    if response.status_code == 200:
        data = response.json()
        
        print("Backend Statistics Response:")
        print("="*60)
        print(f"Total Applications: {data.get('totalApplications')}")
        print(f"Home Loan Count: {data.get('homeLoanCount')}")
        print(f"Personal Loan Count: {data.get('personalLoanCount')}")
        print(f"Business Loan Count: {data.get('businessLoanCount')}")
        print(f"Short-term Loan Count: {data.get('shortTermLoanCount')}")
        print("="*60)
        
        total_loans = (
            data.get('homeLoanCount', 0) +
            data.get('personalLoanCount', 0) +
            data.get('businessLoanCount', 0) +
            data.get('shortTermLoanCount', 0)
        )
        
        print(f"\n✓ Total loan type count: {total_loans}")
        
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"Connection error: {str(e)}")
    print("Make sure backend is running on port 8000")
