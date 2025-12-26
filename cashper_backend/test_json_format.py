"""
Test JSON format with base64 encoded documents
"""
import requests
import base64

BASE_URL = "http://localhost:8000"

# Create a simple test PDF as base64
def create_test_base64():
    """Create a simple PDF file as base64"""
    pdf_content = b"%PDF-1.4\n%Test Document\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n%%EOF"
    return base64.b64encode(pdf_content).decode('utf-8')

def test_company_registration_json():
    """Test Company Registration with JSON and base64 documents"""
    print("\n" + "="*70)
    print("🧪 Testing Company Registration (JSON Format)")
    print("="*70)
    
    test_doc = create_test_base64()
    
    payload = {
        "full_name": "JSON Test User",
        "email": "jsontest@example.com",
        "phone": "9876543210",
        "pan_number": "ABCDE1234F",
        "proposed_company_name": "JSON Test Company Pvt Ltd",
        "company_type": "Private Limited",
        "number_of_directors": 2,
        "registration_state": "Maharashtra",
        "address": "Test Address, Mumbai",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400001",
        # Base64 encoded documents
        "director_pan": test_doc,
        "director_aadhaar": test_doc,
        "director_photo": test_doc,
        "address_proof": test_doc
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/business-services/company-registration",
            json=payload,  # Sending as JSON
            headers={"Content-Type": "application/json"},
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
                print(f"\nTotal Documents Stored: {len(docs)}")
            else:
                print("  ❌ No documents found in response")
        else:
            print(f"❌ FAILED")
            print(f"Response: {response.text[:500]}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_company_compliance_json():
    """Test Company Compliance with JSON and base64 documents"""
    print("\n" + "="*70)
    print("🧪 Testing Company Compliance (JSON Format)")
    print("="*70)
    
    test_doc = create_test_base64()
    
    payload = {
        "full_name": "Compliance Test User",
        "email": "compliancetest@example.com",
        "phone": "9876543211",
        "pan_number": "FGHIJ5678K",
        "company_name": "Test Compliance Company Ltd",
        "cin": "U12345MH2020PTC123456",
        "compliance_type": "Annual Filing",
        "registration_date": "2020-01-01",
        "address": "Test Address, Mumbai",
        "city": "Mumbai",
        "state": "Maharashtra",
        "pincode": "400001",
        # Base64 encoded documents
        "cin_certificate": test_doc,
        "pan_card": test_doc,
        "financial_statements": test_doc
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/business-services/company-compliance",
            json=payload,
            headers={"Content-Type": "application/json"},
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
                print(f"\nTotal Documents Stored: {len(docs)}")
            else:
                print("  ❌ No documents found in response")
        else:
            print(f"❌ FAILED")
            print(f"Response: {response.text[:500]}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 JSON FORMAT TESTING WITH BASE64 DOCUMENTS")
    print("="*70)
    
    test_company_registration_json()
    test_company_compliance_json()
    
    print("\n" + "="*70)
    print("✅ JSON FORMAT TESTING COMPLETED")
    print("="*70)
