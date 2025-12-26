"""
Test Script for JSON Format APIs:
- Tax Audit Application
- Legal Advice Application  
- ITR Filing Service Application

All endpoints now accept pure JSON with base64 encoded documents.
"""

import requests
import json
import base64
import os
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000/api"

# Helper function to create base64 encoded PDF
def create_test_pdf_base64(content_text):
    """Create a simple PDF and return base64 encoded string"""
    # Simple PDF content
    pdf_content = f"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj
2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj
3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
>>
endobj
4 0 obj
<<
/Length 44
>>
stream
BT
/F1 12 Tf
100 700 Td
({content_text}) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000214 00000 n 
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
308
%%EOF"""
    
    return base64.b64encode(pdf_content.encode()).decode('utf-8')

def test_tax_audit():
    """Test Tax Audit Application API with JSON format"""
    print("\n" + "="*60)
    print("🧪 Testing: Tax Audit Application (JSON Format)")
    print("="*60)
    
    url = f"{BASE_URL}/business-services/tax-audit"
    
    # Create test documents
    pan_card_base64 = create_test_pdf_base64("PAN Card - Test Document")
    gst_returns_base64 = create_test_pdf_base64("GST Returns - Test Document")
    balance_sheet_base64 = create_test_pdf_base64("Balance Sheet - Test Document")
    
    payload = {
        "full_name": "Rajesh Kumar",
        "business_name": "Kumar Industries Pvt Ltd",  # Changed from company_name
        "email": "rajesh.kumar@kumarindustries.com",
        "phone": "9876543210",
        "pan_number": "AAACU9603R",
        "turnover": 5000000.0,  # Changed from annual_turnover (string to float)
        "financial_year": "2023-24",
        "audit_type": "GST Audit",
        "address": "123 Industrial Area, Sector 8",
        "city": "Pune",
        "state": "Maharashtra",
        "pincode": "411028",
        
        # Base64 encoded documents
        "pan_card": pan_card_base64,
        "gst_returns": gst_returns_base64,
        "balance_sheet": balance_sheet_base64
    }
    
    try:
        print(f"\n📤 Sending POST request to: {url}")
        print(f"📋 Payload keys: {list(payload.keys())}")
        print(f"📄 Documents included: pan_card ({len(pan_card_base64)} chars), gst_returns ({len(gst_returns_base64)} chars), balance_sheet ({len(balance_sheet_base64)} chars)")
        
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        
        print(f"\n📥 Response Status: {response.status_code}")
        
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ SUCCESS! Application submitted")
            print(f"📝 Application ID: {result.get('application_id')}")
            print(f"📂 Documents saved:")
            for doc_name, doc_path in result.get('data', {}).get('documents', {}).items():
                print(f"   - {doc_name}: {doc_path}")
        else:
            print(f"❌ FAILED! Status: {response.status_code}")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception occurred: {str(e)}")


def test_legal_advice():
    """Test Legal Advice Application API with JSON format"""
    print("\n" + "="*60)
    print("🧪 Testing: Legal Advice Application (JSON Format)")
    print("="*60)
    
    url = f"{BASE_URL}/business-services/legal-advice"
    
    # Create test documents
    legal_docs_base64 = create_test_pdf_base64("Legal Documents - Test")
    supporting_docs_base64 = create_test_pdf_base64("Supporting Documents - Test")
    company_reg_base64 = create_test_pdf_base64("Company Registration - Test")
    
    payload = {
        "name": "Priya Sharma",  # Changed from full_name
        "company_name": "Sharma Legal Consultancy",
        "email": "priya.sharma@sharmaconsult.com",
        "phone": "9123456789",
        "legal_issue_type": "Contract Dispute",
        "case_description": "Need legal advice regarding breach of contract with vendor. Payment dispute of Rs. 2,50,000. Looking for resolution options and potential litigation strategy.",
        "urgency": "High",  # Changed from urgency_level
        "company_pan": "ABCDE1234F",  # Added required field
        "address": "45 MG Road, Commercial Complex",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560001",
        
        # Base64 encoded documents
        "legal_documents": legal_docs_base64,
        "supporting_documents": supporting_docs_base64,
        "company_registration": company_reg_base64
    }
    
    try:
        print(f"\n📤 Sending POST request to: {url}")
        print(f"📋 Payload keys: {list(payload.keys())}")
        print(f"📄 Documents included: legal_documents, supporting_documents, company_registration")
        
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        
        print(f"\n📥 Response Status: {response.status_code}")
        
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ SUCCESS! Application submitted")
            print(f"📝 Application ID: {result.get('application_id')}")
            print(f"📂 Documents saved:")
            for doc_name, doc_path in result.get('data', {}).get('documents', {}).items():
                print(f"   - {doc_name}: {doc_path}")
        else:
            print(f"❌ FAILED! Status: {response.status_code}")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception occurred: {str(e)}")


def test_itr_filing():
    """Test ITR Filing Service API with JSON format"""
    print("\n" + "="*60)
    print("🧪 Testing: ITR Filing Service (JSON Format)")
    print("="*60)
    
    url = f"{BASE_URL}/retail-services/itr-filing"
    
    # Create test documents
    pan_card_base64 = create_test_pdf_base64("PAN Card - Individual")
    aadhaar_card_base64 = create_test_pdf_base64("Aadhaar Card - Individual")
    form16_base64 = create_test_pdf_base64("Form 16 - Salary Certificate")
    bank_statement_base64 = create_test_pdf_base64("Bank Statement - 6 Months")
    
    payload = {
        "fullName": "Amit Verma",
        "email": "amit.verma@gmail.com",
        "phone": "9988776655",
        "panNumber": "ABCPV1234D",
        "aadhaarNumber": "123456789012",  # Fixed: removed spaces, exactly 12 digits
        "dateOfBirth": "1990-05-15",
        "employmentType": "Salaried",
        "annualIncome": "850000",
        "itrType": "ITR-1",
        "hasBusinessIncome": False,
        "hasCapitalGains": False,
        "hasHouseProperty": True,
        "address": "Flat 302, Green Valley Apartments",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400001",
        
        # Base64 encoded documents
        "pan_card": pan_card_base64,
        "aadhaar_card": aadhaar_card_base64,
        "form16": form16_base64,
        "bank_statement": bank_statement_base64
    }
    
    try:
        print(f"\n📤 Sending POST request to: {url}")
        print(f"📋 Payload keys: {list(payload.keys())}")
        print(f"📄 Documents included: pan_card, aadhaar_card, form16, bank_statement")
        
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        
        print(f"\n📥 Response Status: {response.status_code}")
        
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ SUCCESS! Application submitted")
            print(f"📝 Application ID: {result.get('applicationId')}")
            print(f"📂 Documents saved:")
            for doc_name, doc_path in result.get('documents', {}).items():
                print(f"   - {doc_name}: {doc_path}")
        else:
            print(f"❌ FAILED! Status: {response.status_code}")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception occurred: {str(e)}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 JSON Format API Testing Suite")
    print("Testing: Tax Audit, Legal Advice, ITR Filing")
    print("="*60)
    print(f"📡 Base URL: {BASE_URL}")
    print(f"⏰ Test started at: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run all tests
    test_tax_audit()
    test_legal_advice()
    test_itr_filing()
    
    print("\n" + "="*60)
    print("✅ All tests completed!")
    print("="*60 + "\n")
