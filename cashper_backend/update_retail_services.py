"""
Update retail services to add file upload helper and return documents in response
"""

file_path = "app/routes/retail_services_routes.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add helper function after imports
helper_function = '''
import os
import uuid
import shutil

# Helper function for file upload
def save_retail_document(file: UploadFile, application_id: str, doc_type: str) -> str:
    """Save uploaded document and return file path"""
    try:
        upload_dir = os.path.join("uploads", "retail_services", application_id)
        os.makedirs(upload_dir, exist_ok=True)
        
        file_ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{doc_type}_{uuid.uuid4().hex[:8]}{file_ext}"
        file_path = os.path.join(upload_dir, unique_filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

'''

# Find the position after imports and before first route
import_end = content.find('router = APIRouter')
if import_end != -1:
    content = content[:import_end] + helper_function + "\n" + content[import_end:]

# Update ITR Filing to support files
itr_filing_old = '''@router.post("/itr-filing", response_model=dict)
async def submit_itr_filing_application(application: ITRFilingRequest):
    """Submit ITR Filing Service Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.ITR_FILING,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "ITR Filing application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")'''

itr_filing_new = '''@router.post("/itr-filing", response_model=dict)
async def submit_itr_filing_application(
    fullName: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    panNumber: str = Form(...),
    aadhaarNumber: str = Form(...),
    dateOfBirth: str = Form(...),
    employmentType: str = Form(...),
    annualIncome: str = Form(...),
    itrType: str = Form(...),
    hasBusinessIncome: bool = Form(False),
    hasCapitalGains: bool = Form(False),
    hasHouseProperty: bool = Form(False),
    address: str = Form(...),
    city: str = Form(...),
    state: str = Form(...),
    pincode: str = Form(...),
    pan_card: Optional[UploadFile] = File(None),
    aadhaar_card: Optional[UploadFile] = File(None),
    form16: Optional[UploadFile] = File(None),
    bank_statement: Optional[UploadFile] = File(None)
):
    """Submit ITR Filing Service Application"""
    try:
        db = get_database()
        
        application_id = f"ITR{int(datetime.utcnow().timestamp())}{uuid.uuid4().hex[:6].upper()}"
        
        application_data = {
            "applicationId": application_id,
            "serviceType": ServiceType.ITR_FILING,
            "applicantName": fullName,
            "email": email,
            "phone": phone,
            "applicationData": {
                "fullName": fullName,
                "email": email,
                "phone": phone,
                "panNumber": panNumber,
                "aadhaarNumber": aadhaarNumber,
                "dateOfBirth": dateOfBirth,
                "employmentType": employmentType,
                "annualIncome": annualIncome,
                "itrType": itrType,
                "hasBusinessIncome": hasBusinessIncome,
                "hasCapitalGains": hasCapitalGains,
                "hasHouseProperty": hasHouseProperty,
                "address": address,
                "city": city,
                "state": state,
                "pincode": pincode
            },
            "documents": {},
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
        
        # Handle file uploads
        if pan_card:
            file_path = save_retail_document(pan_card, application_id, "pan_card")
            application_data["documents"]["pan_card"] = file_path
        
        if aadhaar_card:
            file_path = save_retail_document(aadhaar_card, application_id, "aadhaar_card")
            application_data["documents"]["aadhaar_card"] = file_path
        
        if form16:
            file_path = save_retail_document(form16, application_id, "form16")
            application_data["documents"]["form16"] = file_path
        
        if bank_statement:
            file_path = save_retail_document(bank_statement, application_id, "bank_statement")
            application_data["documents"]["bank_statement"] = file_path
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "ITR Filing application submitted successfully",
            "applicationId": application_id,
            "status": ApplicationStatus.PENDING,
            "documents": application_data["documents"],
            "data": application_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")'''

content = content.replace(itr_filing_old, itr_filing_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Updated retail services with file upload support for ITR Filing")
print("✅ Added helper function save_retail_document()")
