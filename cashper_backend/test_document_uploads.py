"""
Test document upload for both Business and Retail Services
"""

import requests
import io
from pathlib import Path

BASE_URL = "http://localhost:8000"

def create_test_file(filename="test_document.pdf"):
    """Create a test PDF file"""
    content = b"%PDF-1.4\n%Test Document\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n%%EOF"
    return ("test.pdf", io.BytesIO(content), "application/pdf")

def test_company_registration_with_documents():
    """Test Company Registration with document upload"""
    print("\n" + "="*70)
    print("🧪 Testing Company Registration with Documents")
    print("="*70)
    
    # Prepare form data
    data = {
        "full_name": "Test User with Docs",
        "email": "testdocs@example.com",
        "phone": "9876543210",
        "pan_number": "ABCDE1234F",
        "proposed_company_name": "Test Company with Docs Pvt Ltd",
        "company_type": "Private Limited",
        "number_of_directors": "2",
        "registration_state": "Maharashtra",
        "address": "Test Address, Mumbai",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400001"
    }
    
    # Prepare files
    files = {
        "director_pan": create_test_file("director_pan.pdf"),
        "director_aadhaar": create_test_file("director_aadhaar.pdf"),
        "director_photo": ("photo.jpg", io.BytesIO(b"fake image data"), "image/jpeg")
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/business-services/company-registration",
            data=data,
            files=files,
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ SUCCESS!")
            print(f"Application ID: {result.get('application_id')}")
            print(f"\nDocuments in Response:")
            if 'data' in result and 'documents' in result['data']:
                docs = result['data']['documents']
                for doc_name, doc_path in docs.items():
                    print(f"  ✓ {doc_name}: {doc_path}")
                print(f"\nTotal Documents Uploaded: {len(docs)}")
            else:
                print("  ❌ No documents found in response")
        else:
            print(f"❌ FAILED: {response.text[:200]}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_itr_filing_with_documents():
    """Test ITR Filing with document upload"""
    print("\n" + "="*70)
    print("🧪 Testing ITR Filing with Documents")
    print("="*70)
    
    # Prepare form data (using snake_case field names)
    data = {
        "full_name": "ITR Test User",
        "email": "itrtest@example.com",
        "phone": "9876543211",
        "pan_number": "FGHIJ5678K",
        "aadhaar_number": "123456789012",
        "date_of_birth": "1990-01-01",
        "employment_type": "Salaried",
        "annual_income": "500000",
        "itr_type": "ITR-1",
        "has_business_income": "false",
        "has_capital_gains": "false",
        "has_house_property": "false",
        "address": "Test Address, Delhi",
        "city": "Delhi",
        "state": "Delhi",
        "pincode": "110001"
    }
    
    # Prepare files
    files = {
        "pan_card": create_test_file("pan.pdf"),
        "aadhaar_card": create_test_file("aadhaar.pdf"),
        "form16": create_test_file("form16.pdf")
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/retail-services/itr-filing",
            data=data,
            files=files,
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ SUCCESS!")
            print(f"Application ID: {result.get('applicationId')}")
            print(f"\nDocuments in Response:")
            if 'documents' in result:
                docs = result['documents']
                for doc_name, doc_path in docs.items():
                    print(f"  ✓ {doc_name}: {doc_path}")
                print(f"\nTotal Documents Uploaded: {len(docs)}")
            else:
                print("  ❌ No documents found in response")
        else:
            print(f"❌ FAILED: {response.text}")
            try:
                error_detail = response.json()
                print(f"Error Detail: {error_detail}")
            except:
                pass
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_get_with_documents():
    """Test GET endpoint to verify documents are returned"""
    print("\n" + "="*70)
    print("🧪 Testing GET Endpoint - Documents in Response")
    print("="*70)
    
    try:
        # Get company registrations
        response = requests.get(
            f"{BASE_URL}/api/business-services/company-registration",
            timeout=5
        )
        
        if response.status_code == 200:
            result = response.json()
            apps = result.get('applications', [])
            print(f"✅ Found {len(apps)} applications")
            
            if apps:
                print("\nChecking first application for documents:")
                first_app = apps[0]
                if 'documents' in first_app and first_app['documents']:
                    print(f"  ✓ Documents found: {list(first_app['documents'].keys())}")
                else:
                    print(f"  ℹ No documents in this application")
        else:
            print(f"❌ GET Failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def run_all_tests():
    print("\n" + "="*70)
    print("🚀 DOCUMENT UPLOAD TESTING")
    print("="*70)
    
    test_company_registration_with_documents()
    test_itr_filing_with_documents()
    test_get_with_documents()
    
    print("\n" + "="*70)
    print("✅ ALL DOCUMENT TESTS COMPLETED")
    print("="*70)

if __name__ == "__main__":
    run_all_tests()
