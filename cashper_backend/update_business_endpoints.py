"""
Script to update all business services POST endpoints to support file uploads
"""

import re

file_path = "app/routes/business_services.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define replacements for each endpoint
replacements = [
    # Tax Audit
    {
        "old": '''@router.post("/tax-audit")
async def submit_tax_audit(
    application: TaxAuditApplication
):
    """Submit Tax Audit Application"""
    try:
        db = get_database()
        collection = db["tax_audit_applications"]
        
        application_data = {
            "application_id": generate_application_id("TAUD"),
            "user_id": None,  # No authentication
            "full_name": application.full_name,
            "email": application.email,
            "phone": application.phone,
            "pan_number": application.pan_number.upper(),
            "business_name": application.business_name,
            "turnover": application.turnover,
            "audit_type": application.audit_type,
            "financial_year": application.financial_year,
            "address": application.address,
            "city": application.city,
            "state": application.state,
            "pincode": application.pincode,
            "status": "Pending",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }''',
        "new": '''@router.post("/tax-audit")
async def submit_tax_audit(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    pan_number: str = Form(...),
    business_name: str = Form(...),
    turnover: float = Form(...),
    audit_type: str = Form(...),
    financial_year: str = Form(...),
    address: str = Form(...),
    city: str = Form(...),
    state: str = Form(...),
    pincode: str = Form(...),
    pan_card: Optional[UploadFile] = File(None),
    gst_returns: Optional[UploadFile] = File(None),
    balance_sheet: Optional[UploadFile] = File(None)
):
    """Submit Tax Audit Application"""
    try:
        db = get_database()
        collection = db["tax_audit_applications"]
        
        application_id = generate_application_id("TAUD")
        
        application_data = {
            "application_id": application_id,
            "user_id": None,
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "pan_number": pan_number.upper(),
            "business_name": business_name,
            "turnover": turnover,
            "audit_type": audit_type,
            "financial_year": financial_year,
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
        if pan_card:
            file_path = save_uploaded_file(pan_card, f"tax_audit/{application_id}")
            application_data["documents"]["pan_card"] = file_path
        
        if gst_returns:
            file_path = save_uploaded_file(gst_returns, f"tax_audit/{application_id}")
            application_data["documents"]["gst_returns"] = file_path
        
        if balance_sheet:
            file_path = save_uploaded_file(balance_sheet, f"tax_audit/{application_id}")
            application_data["documents"]["balance_sheet"] = file_path'''
    }
]

for replacement in replacements:
    content = content.replace(replacement["old"], replacement["new"])

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Updated Tax Audit endpoint with file upload support")
