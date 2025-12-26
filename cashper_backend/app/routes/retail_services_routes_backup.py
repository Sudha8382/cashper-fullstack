from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from ..database.schema.retail_services_schema import (
    ITRFilingRequest, ITRRevisionRequest, ITRNoticeReplyRequest,
    IndividualPANRequest, HUFPANRequest, PFWithdrawalRequest,
    DocumentUpdateRequest, TradingDematRequest, BankAccountRequest,
    FinancialPlanningRequest, ServiceApplicationResponse,
    ServiceType, ApplicationStatus
)
from ..database.db import get_database


import os
import uuid
import base64
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


router = APIRouter(prefix="/api/retail-services", tags=["Retail Services"])


# ===================== ITR FILING SERVICE =====================


@router.post("/itr-filing")
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
    panCard: UploadFile = File(None),
    aadhaarCard: UploadFile = File(None),
    form16: UploadFile = File(None),
    bankStatement: UploadFile = File(None),
    investmentProofs: UploadFile = File(None)
):
    """Submit ITR Filing Service Application with file uploads"""
    try:
        db = get_database()
        collection = db["RetailServiceApplications"]
        
        application_id = f"ITR{int(datetime.now().timestamp())}{uuid.uuid4().hex[:6].upper()}"
        
        application_data = {
            "applicationId": application_id,
            "serviceType": "itr-filing",
            "applicantName": fullName,
            "email": email,
            "phone": phone,
            "applicationData": {
                "full_name": fullName,
                "email": email,
                "phone": phone,
                "pan_number": panNumber,
                "aadhaar_number": aadhaarNumber,
                "date_of_birth": dateOfBirth,
                "employment_type": employmentType,
                "annual_income": annualIncome,
                "itr_type": itrType,
                "has_business_income": hasBusinessIncome,
                "has_capital_gains": hasCapitalGains,
                "has_house_property": hasHouseProperty,
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
        doc_mapping = {
            "pan_card": panCard,
            "aadhaar_card": aadhaarCard,
            "form16": form16,
            "bank_statement": bankStatement,
            "investment_proofs": investmentProofs
        }
        
        for doc_name, file in doc_mapping.items():
            if file and file.filename:
                file_path = save_retail_document(file, application_id, doc_name)
                application_data["documents"][doc_name] = file_path
        
        result = collection.insert_one(application_data)
        
        return JSONResponse(content={
            "success": True,
            "message": "ITR Filing application submitted successfully",
            "applicationId": application_id,
            "status": "pending",
            "documents": application_data["documents"],
            "data": {k: v.isoformat() if isinstance(v, datetime) else v for k, v in application_data.items() if k != "_id"}
        }, status_code=201)
        
    except Exception as e:
        print(f"ITR Filing Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/itr-filing/{application_id}")
async def get_itr_filing_application(application_id: str):
    """Get ITR Filing Application by ID"""
    try:
        db = get_database()
        application = db.RetailServiceApplications.find_one({
            "_id": ObjectId(application_id),
            "serviceType": ServiceType.ITR_FILING
        })
        
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")
        
        application["id"] = str(application.pop("_id"))
        return application
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===================== ITR REVISION SERVICE =====================

@router.post("/itr-revision", response_model=dict)
async def submit_itr_revision_application(application: ITRRevisionRequest):
    """Submit ITR Revision Service Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.ITR_REVISION,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "ITR Revision application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== ITR NOTICE REPLY SERVICE =====================

@router.post("/itr-notice-reply", response_model=dict)
async def submit_itr_notice_reply_application(application: ITRNoticeReplyRequest):
    """Submit ITR Notice Reply Service Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.ITR_NOTICE_REPLY,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "ITR Notice Reply application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== INDIVIDUAL PAN APPLICATION =====================

@router.post("/individual-pan", response_model=dict)
async def submit_individual_pan_application(application: IndividualPANRequest):
    """Submit Individual PAN Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.INDIVIDUAL_PAN,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "Individual PAN application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== HUF PAN APPLICATION =====================

@router.post("/huf-pan", response_model=dict)
async def submit_huf_pan_application(application: HUFPANRequest):
    """Submit HUF PAN Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.HUF_PAN,
            "applicantName": application.hufName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "HUF PAN application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== PF WITHDRAWAL APPLICATION =====================

@router.post("/pf-withdrawal", response_model=dict)
async def submit_pf_withdrawal_application(application: PFWithdrawalRequest):
    """Submit PF Withdrawal Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.PF_WITHDRAWAL,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "PF Withdrawal application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== DOCUMENT UPDATE APPLICATION =====================

@router.post("/document-update", response_model=dict)
async def submit_document_update_application(application: DocumentUpdateRequest):
    """Submit Document Update Application (Aadhaar/PAN)"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.DOCUMENT_UPDATE,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "Document Update application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== TRADING & DEMAT ACCOUNT =====================

@router.post("/trading-demat", response_model=dict)
async def submit_trading_demat_application(application: TradingDematRequest):
    """Submit Trading & Demat Account Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.TRADING_DEMAT,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "Trading & Demat Account application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== BANK ACCOUNT APPLICATION =====================

@router.post("/bank-account", response_model=dict)
async def submit_bank_account_application(application: BankAccountRequest):
    """Submit Bank Account Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.BANK_ACCOUNT,
            "applicantName": application.fullName,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "Bank Account application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== FINANCIAL PLANNING SERVICE =====================

@router.post("/financial-planning", response_model=dict)
async def submit_financial_planning_application(application: FinancialPlanningRequest):
    """Submit Financial Planning Service Application"""
    try:
        db = get_database()
        
        application_data = {
            "serviceType": ServiceType.FINANCIAL_PLANNING,
            "applicantName": application.name,
            "email": application.email,
            "phone": application.phone,
            "applicationData": application.dict(),
            "status": ApplicationStatus.PENDING,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        
        result = db.RetailServiceApplications.insert_one(application_data)
        
        return {
            "success": True,
            "message": "Financial Planning application submitted successfully",
            "applicationId": str(result.inserted_id),
            "status": ApplicationStatus.PENDING
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Application submission failed: {str(e)}")


# ===================== COMMON ENDPOINTS =====================

@router.get("/applications")
async def get_all_applications(
    service_type: Optional[str] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 50
):
    """Get all retail service applications with filters"""
    try:
        db = get_database()
        query = {}
        
        if service_type:
            query["serviceType"] = service_type
        if status:
            query["status"] = status
        
        applications = list(db.RetailServiceApplications.find(query).skip(skip).limit(limit))
        
        for app in applications:
            app["id"] = str(app.pop("_id"))
        
        total = db.RetailServiceApplications.count_documents(query)
        
        return {
            "applications": applications,
            "total": total,
            "skip": skip,
            "limit": limit
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/applications/{application_id}/status")
async def update_application_status(
    application_id: str,
    status: ApplicationStatus,
    admin_notes: Optional[str] = None
):
    """Update application status (Admin only)"""
    try:
        db = get_database()
        
        update_data = {
            "status": status,
            "updatedAt": datetime.now()
        }
        
        if admin_notes:
            update_data["adminNotes"] = admin_notes
        
        result = db.RetailServiceApplications.update_one(
            {"_id": ObjectId(application_id)},
            {"$set": update_data}
        )
        
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Application not found")
        
        return {
            "success": True,
            "message": "Application status updated successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/applications/{application_id}")
async def delete_application(application_id: str):
    """Delete application (Admin only)"""
    try:
        db = get_database()
        
        result = db.RetailServiceApplications.delete_one({"_id": ObjectId(application_id)})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Application not found")
        
        return {
            "success": True,
            "message": "Application deleted successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
