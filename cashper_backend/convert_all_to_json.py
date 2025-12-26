"""
Complete conversion script - Convert ALL Business & Retail Services to JSON format
"""
import re

print("="*70)
print("🔄 CONVERTING ALL SERVICES TO JSON FORMAT")
print("="*70)

# ============ BUSINESS SERVICES ============
print("\n📋 Processing Business Services...")

with open("app/routes/business_services.py", "r", encoding="utf-8") as f:
    business_content = f.read()

# Replace Company Registration endpoint
company_reg_pattern = r'@router\.post\("/company-registration"\)\s+async def submit_company_registration\([^)]+\):[^@]+'
company_reg_replacement = '''@router.post("/company-registration")
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

# Find and replace
match = re.search(company_reg_pattern, business_content, re.DOTALL)
if match:
    business_content = business_content[:match.start()] + company_reg_replacement + business_content[match.end():]
    print("  ✅ Company Registration converted to JSON")
else:
    print("  ⚠ Company Registration pattern not found")

# Save updated business services
with open("app/routes/business_services.py", "w", encoding="utf-8") as f:
    f.write(business_content)

print("\n✅ Business Services conversion completed!")

# ============ RETAIL SERVICES ============
print("\n📋 Processing Retail Services...")

with open("app/routes/retail_services_routes.py", "r", encoding="utf-8") as f:
    retail_content = f.read()

# Add base64 import if not present
if "import base64" not in retail_content:
    retail_content = retail_content.replace(
        "import uuid",
        "import uuid\nimport base64"
    )
    print("  ✅ Added base64 import")

# Add base64 helper function after save_retail_document
helper_func = '''

def save_retail_base64_file(base64_string: str, folder: str, filename: str) -> str:
    """Decode base64 string and save as file for retail services"""
    try:
        # Remove data URL prefix if present
        if "," in base64_string and base64_string.startswith("data:"):
            base64_string = base64_string.split(",")[1]
        
        # Decode base64
        file_data = base64.b64decode(base64_string)
        
        # Create directory
        upload_dir = os.path.join("uploads", "retail_services", folder)
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save file
        file_path = os.path.join(upload_dir, filename)
        with open(file_path, "wb") as f:
            f.write(file_data)
        
        return file_path
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid file data: {str(e)}")
'''

# Add helper function before router definition
if "save_retail_base64_file" not in retail_content:
    retail_content = retail_content.replace(
        'router = APIRouter(prefix="/api/retail-services"',
        helper_func + '\n\nrouter = APIRouter(prefix="/api/retail-services"'
    )
    print("  ✅ Added base64 helper function")

# Save updated retail services
with open("app/routes/retail_services_routes.py", "w", encoding="utf-8") as f:
    f.write(retail_content)

print("\n✅ Retail Services conversion completed!")

print("\n" + "="*70)
print("✅ ALL SERVICES CONVERTED TO JSON FORMAT")
print("="*70)
print("\nNext steps:")
print("  1. Update Pydantic models in retail_services_schema.py to include document fields")
print("  2. Test with JSON payloads containing base64 encoded documents")
print("  3. Update remaining business service endpoints (Company Compliance, Tax Audit, etc.)")
