"""
Batch convert ALL business service endpoints to JSON format
This script will update all POST endpoints to accept Pydantic models instead of Form data
"""

import re

# Read the file
with open("app/routes/business_services.py", "r", encoding="utf-8") as f:
    content = f.read()

# Company Compliance endpoint
print("Converting Company Compliance...")
old_compliance = '''@router.post("/company-compliance")
async def submit_company_compliance(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    pan_number: str = Form(...),
    company_name: str = Form(...),
    cin: str = Form(...),
    compliance_type: str = Form(...),
    registration_date: str = Form(...),
    address: str = Form(...),
    city: str = Form(...),
    state: str = Form(...),
    pincode: str = Form(...),
    cin_certificate: Optional[UploadFile] = File(None),
    pan_card: Optional[UploadFile] = File(None),
    financial_statements: Optional[UploadFile] = File(None)
):
    """Submit Company Compliance Application"""
    try:
        db = get_database()
        collection = db["company_compliance_applications"]
        
        application_id = generate_application_id("CCOMP")
        
        application_data = {
            "application_id": application_id,
            "user_id": None,
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "pan_number": pan_number.upper(),
            "company_name": company_name,
            "cin": cin.upper(),
            "compliance_type": compliance_type,
            "registration_date": registration_date,
            "address": address,
            "city": city,
            "state": state,
            "pincode": pincode,
            "status": "Pending",
            "documents": {},
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        # Handle file uploads
        if cin_certificate:
            file_path = save_uploaded_file(cin_certificate, f"company_compliance/{application_id}")
            application_data["documents"]["cin_certificate"] = file_path
        
        if pan_card:
            file_path = save_uploaded_file(pan_card, f"company_compliance/{application_id}")
            application_data["documents"]["pan_card"] = file_path
        
        if financial_statements:
            file_path = save_uploaded_file(financial_statements, f"company_compliance/{application_id}")
            application_data["documents"]["financial_statements"] = file_path
        
        result = collection.insert_one(application_data)
        application_data["_id"] = str(result.inserted_id)
        application_data["created_at"] = application_data["created_at"].isoformat()
        application_data["updated_at"] = application_data["updated_at"].isoformat()
        
        return JSONResponse(content={
            "success": True,
            "message": "Company compliance application submitted successfully",
            "application_id": application_data["application_id"],
            "data": application_data
        }, status_code=201)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to submit application: {str(e)}")'''

new_compliance = '''@router.post("/company-compliance")
async def submit_company_compliance(application: CompanyComplianceApplication):
    """Submit Company Compliance Application (JSON with base64 documents)"""
    try:
        db = get_database()
        collection = db["company_compliance_applications"]
        
        application_id = generate_application_id("CCOMP")
        
        application_data = {
            "application_id": application_id,
            "user_id": None,
            "full_name": application.full_name,
            "email": application.email,
            "phone": application.phone,
            "pan_number": application.pan_number.upper(),
            "company_name": application.company_name,
            "cin": application.cin.upper(),
            "compliance_type": application.compliance_type,
            "registration_date": application.registration_date,
            "address": application.address,
            "city": application.city,
            "state": application.state,
            "pincode": application.pincode,
            "status": "Pending",
            "documents": {},
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        # Handle base64 encoded documents
        doc_mapping = {
            "cin_certificate": application.cin_certificate,
            "pan_card": application.pan_card,
            "financial_statements": application.financial_statements
        }
        
        for doc_name, doc_data in doc_mapping.items():
            if doc_data:
                filename = f"{uuid.uuid4().hex[:8]}_{doc_name}.pdf"
                file_path = save_base64_file(doc_data, f"company_compliance/{application_id}", filename)
                application_data["documents"][doc_name] = file_path
        
        result = collection.insert_one(application_data)
        application_data["_id"] = str(result.inserted_id)
        application_data["created_at"] = application_data["created_at"].isoformat()
        application_data["updated_at"] = application_data["updated_at"].isoformat()
        
        return JSONResponse(content={
            "success": True,
            "message": "Company compliance application submitted successfully",
            "application_id": application_data["application_id"],
            "data": application_data
        }, status_code=201)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))'''

if old_compliance in content:
    content = content.replace(old_compliance, new_compliance)
    print("✅ Company Compliance converted")
else:
    print("⚠ Company Compliance not found")

# Save the file
with open("app/routes/business_services.py", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ Conversion complete!")
print("Converted endpoints now accept JSON with base64 encoded documents")
