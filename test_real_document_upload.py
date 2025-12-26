import requests
import os

# Create test PDF files with actual content
test_files_dir = "test_documents"
os.makedirs(test_files_dir, exist_ok=True)

# Create a simple PDF with actual content
pan_card_content = b"""%PDF-1.4
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
/Resources <<
/Font <<
/F1 <<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
>>
>>
/MediaBox [0 0 612 792]
/Contents 4 0 R
>>
endobj
4 0 obj
<<
/Length 55
>>
stream
BT
/F1 24 Tf
100 700 Td
(PAN CARD - TEST) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000317 00000 n 
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
422
%%EOF
"""

# Save test files
with open(os.path.join(test_files_dir, "pan_card.pdf"), "wb") as f:
    f.write(pan_card_content)

with open(os.path.join(test_files_dir, "aadhaar_card.pdf"), "wb") as f:
    f.write(pan_card_content.replace(b"PAN CARD", b"AADHAAR CARD"))

with open(os.path.join(test_files_dir, "form16.pdf"), "wb") as f:
    f.write(pan_card_content.replace(b"PAN CARD", b"FORM 16"))

print("✅ Test documents created successfully!")
print(f"📁 Location: {os.path.abspath(test_files_dir)}")

# Now submit the application
url = "http://127.0.0.1:8000/api/retail-services/itr-filing"

# Prepare form data
form_data = {
    "fullName": "Test User - Real Documents",
    "email": "test.real@example.com",
    "phone": "9876543210",
    "panNumber": "ABCDE1234F",
    "aadhaarNumber": "123456789012",
    "dateOfBirth": "1990-01-01",
    "employmentType": "Salaried",
    "annualIncome": "500000",
    "itrType": "ITR-1",
    "hasBusinessIncome": "false",
    "hasCapitalGains": "false",
    "hasHouseProperty": "false",
    "address": "Test Address",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001"
}

# Prepare files
files = {
    "panCard": ("pan_card.pdf", open(os.path.join(test_files_dir, "pan_card.pdf"), "rb"), "application/pdf"),
    "aadhaarCard": ("aadhaar_card.pdf", open(os.path.join(test_files_dir, "aadhaar_card.pdf"), "rb"), "application/pdf"),
    "form16": ("form16.pdf", open(os.path.join(test_files_dir, "form16.pdf"), "rb"), "application/pdf")
}

print("\n🚀 Submitting ITR Filing application with real documents...")

try:
    response = requests.post(url, data=form_data, files=files)
    
    if response.status_code == 201:
        result = response.json()
        print("\n✅ Application submitted successfully!")
        print(f"📋 Application ID: {result.get('applicationId')}")
        print(f"📄 Documents uploaded: {list(result.get('application', {}).get('documents', {}).keys())}")
    else:
        print(f"\n❌ Failed to submit application")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"\n❌ Error: {str(e)}")

finally:
    # Close file handles
    for file_obj in files.values():
        file_obj[1].close()

print("\n✅ Test complete!")
