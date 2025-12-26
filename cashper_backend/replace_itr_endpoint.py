"""
Replace ITR Filing endpoint with working pattern from Company Registration
"""

# New ITR Filing endpoint based on working Company Registration pattern
new_endpoint = '''
@router.post("/itr-filing")
async def submit_itr_filing_application(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    pan_number: str = Form(...),
    aadhaar_number: str = Form(...),
    date_of_birth: str = Form(...),
    employment_type: str = Form(...),
    annual_income: str = Form(...),
    itr_type: str = Form(...),
    has_business_income: str = Form("false"),
    has_capital_gains: str = Form("false"),
    has_house_property: str = Form("false"),
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
        collection = db["RetailServiceApplications"]
        
        application_id = f"ITR{int(datetime.now().timestamp())}{uuid.uuid4().hex[:6].upper()}"
        
        application_data = {
            "applicationId": application_id,
            "serviceType": "itr-filing",
            "applicantName": full_name,
            "email": email,
            "phone": phone,
            "applicationData": {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "pan_number": pan_number,
                "aadhaar_number": aadhaar_number,
                "date_of_birth": date_of_birth,
                "employment_type": employment_type,
                "annual_income": annual_income,
                "itr_type": itr_type,
                "has_business_income": has_business_income.lower() == "true",
                "has_capital_gains": has_capital_gains.lower() == "true",
                "has_house_property": has_house_property.lower() == "true",
                "address": address,
                "city": city,
                "state": state,
                "pincode": pincode
            },
            "status": "pending",
            "documents": {},
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
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
        
        result = collection.insert_one(application_data)
        
        return JSONResponse(content={
            "success": True,
            "message": "ITR Filing application submitted successfully",
            "applicationId": application_id,
            "status": "pending",
            "documents": application_data["documents"],
            "data": {k: v.isoformat() if isinstance(v, datetime) else v for k, v in application_data.items() if k != "_id"}
        }, status_code=200)
        
    except Exception as e:
        import traceback
        print(f"❌ ITR Filing Error: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")
'''

# Read current file
with open("app/routes/retail_services_routes.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find ITR Filing endpoint (starts around line 43, ends around line 150)
start_line = None
end_line = None

for i, line in enumerate(lines):
    if '@router.post("/itr-filing"' in line:
        start_line = i
    if start_line is not None and end_line is None:
        if line.strip().startswith('@router.') and i > start_line:
            end_line = i
            break
        if 'def get_itr_filing_application' in line:
            # Find the previous function's end
            end_line = i
            break

if start_line is not None and end_line is not None:
    # Replace the endpoint
    new_lines = lines[:start_line] + [new_endpoint + "\n\n"] + lines[end_line:]
    
    with open("app/routes/retail_services_routes.py", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    
    print(f"✅ Replaced ITR Filing endpoint (lines {start_line+1} to {end_line})")
    print(f"✅ New endpoint uses working pattern from Company Registration")
else:
    print(f"❌ Could not find ITR Filing endpoint boundaries")
    print(f"Start: {start_line}, End: {end_line}")
