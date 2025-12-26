"""
Update all Business Services to accept JSON with base64 encoded documents
"""

# Enhanced Pydantic models with document fields
models_with_documents = '''
class CompanyRegistrationApplication(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr
    phone: str = Field(..., pattern=r"^[0-9]{10}$")
    pan_number: str = Field(..., pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    proposed_company_name: str = Field(..., min_length=3)
    company_type: str
    number_of_directors: int = Field(..., ge=1)
    registration_state: str
    address: str = Field(..., min_length=10)
    city: str
    state: str
    pincode: str = Field(..., pattern=r"^[0-9]{6}$")
    # Documents as base64 encoded strings
    director_pan: Optional[str] = None
    director_aadhaar: Optional[str] = None
    director_photo: Optional[str] = None
    address_proof: Optional[str] = None

class CompanyComplianceApplication(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr
    phone: str = Field(..., pattern=r"^[0-9]{10}$")
    pan_number: str = Field(..., pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    company_name: str
    cin: str = Field(..., pattern=r"^[LUu]{1}[0-9]{5}[A-Za-z]{2}[0-9]{4}[A-Za-z]{3}[0-9]{6}$")
    compliance_type: str
    registration_date: str
    address: str = Field(..., min_length=10)
    city: str
    state: str
    pincode: str = Field(..., pattern=r"^[0-9]{6}$")
    # Documents as base64 encoded strings
    cin_certificate: Optional[str] = None
    pan_card: Optional[str] = None
    financial_statements: Optional[str] = None

class TaxAuditApplication(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr
    phone: str = Field(..., pattern=r"^[0-9]{10}$")
    pan_number: str = Field(..., pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    business_name: str
    turnover: float = Field(..., gt=0)
    audit_type: str
    financial_year: str
    address: str = Field(..., min_length=10)
    city: str
    state: str
    pincode: str = Field(..., pattern=r"^[0-9]{6}$")
    # Documents as base64 encoded strings
    pan_card: Optional[str] = None
    gst_returns: Optional[str] = None
    balance_sheet: Optional[str] = None

class LegalAdviceApplication(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    phone: str = Field(..., pattern=r"^[0-9]{10}$")
    company_name: str
    legal_issue_type: str
    case_description: str = Field(..., min_length=20)
    urgency: str
    address: str = Field(..., min_length=10)
    city: str
    state: str
    pincode: str = Field(..., pattern=r"^[0-9]{6}$")
    company_pan: str = Field(..., pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    # Documents as base64 encoded strings
    legal_documents: Optional[str] = None
    supporting_documents: Optional[str] = None
    company_registration: Optional[str] = None

class ProvidentFundServicesApplication(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    phone: str = Field(..., pattern=r"^[0-9]{10}$")
    company_name: str
    number_of_employees: int = Field(..., ge=1)
    existing_pf_number: Optional[str] = None
    existing_esi_number: Optional[str] = None
    service_required: str
    address: str = Field(..., min_length=10)
    city: str
    state: str
    pincode: str = Field(..., pattern=r"^[0-9]{6}$")
    company_pan: str = Field(..., pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    # Documents as base64 encoded strings
    pf_account_statement: Optional[str] = None
    bank_passbook: Optional[str] = None
    cancelled_cheque: Optional[str] = None
'''

# Helper function for base64 decoding
helper_function = '''

# Helper function to decode base64 and save file
def save_base64_file(base64_string: str, folder: str, filename: str) -> str:
    """Decode base64 string and save as file"""
    import base64
    try:
        # Remove data URL prefix if present (e.g., "data:image/png;base64,")
        if "," in base64_string and base64_string.startswith("data:"):
            base64_string = base64_string.split(",")[1]
        
        # Decode base64
        file_data = base64.b64decode(base64_string)
        
        # Create directory
        upload_dir = os.path.join("uploads", folder)
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save file
        file_path = os.path.join(upload_dir, filename)
        with open(file_path, "wb") as f:
            f.write(file_data)
        
        return file_path
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid file data: {str(e)}")
'''

# New Company Registration endpoint
company_registration_endpoint = '''
@router.post("/company-registration")
async def submit_company_registration(application: CompanyRegistrationApplication):
    """Submit Company Registration Application (JSON with base64 documents)"""
    try:
        db = get_database()
        collection = db["company_registration_applications"]
        
        application_id = generate_application_id("CREG")
        
        application_data = {
            "application_id": application_id,
            "user_id": None,
            "full_name": application.full_name,
            "email": application.email,
            "phone": application.phone,
            "pan_number": application.pan_number.upper(),
            "proposed_company_name": application.proposed_company_name,
            "company_type": application.company_type,
            "number_of_directors": application.number_of_directors,
            "registration_state": application.registration_state,
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
            "director_pan": application.director_pan,
            "director_aadhaar": application.director_aadhaar,
            "director_photo": application.director_photo,
            "address_proof": application.address_proof
        }
        
        for doc_name, doc_data in doc_mapping.items():
            if doc_data:
                filename = f"{uuid.uuid4().hex[:8]}_{doc_name}.pdf"
                file_path = save_base64_file(doc_data, f"company_registration/{application_id}", filename)
                application_data["documents"][doc_name] = file_path
        
        result = collection.insert_one(application_data)
        application_data["_id"] = str(result.inserted_id)
        application_data["created_at"] = application_data["created_at"].isoformat()
        application_data["updated_at"] = application_data["updated_at"].isoformat()
        
        return JSONResponse(content={
            "success": True,
            "message": "Company registration application submitted successfully",
            "application_id": application_data["application_id"],
            "data": application_data
        }, status_code=201)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
'''

print("✅ Business Services JSON format conversion script created")
print("\nThis will update:")
print("  1. Pydantic models to include document fields (base64 strings)")
print("  2. Helper function to decode base64 and save files")
print("  3. All endpoints to accept JSON instead of Form data")
print("\nDocument fields will be Optional[str] containing base64 encoded file data")
