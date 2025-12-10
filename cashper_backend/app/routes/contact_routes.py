from fastapi import APIRouter, HTTPException, status, Depends, Query
from typing import List, Optional
from app.database.schema.contact_schema import (
    ContactSubmissionRequest,
    ContactSubmissionResponse,
    ContactSubmissionInDB,
    ContactUpdateStatusRequest,
    ContactStatus,
    FAQRequest,
    FAQResponse,
    FAQInDB,
    FAQCategory,
    ContactStatisticsResponse,
    PaginatedContactResponse
)
from app.database.repository.contact_repository import contact_repository
from app.utils.auth_middleware import get_current_user_optional
from datetime import datetime

router = APIRouter(prefix="/api/contact", tags=["Contact"])


# ===================== PUBLIC ENDPOINTS (No Authentication) =====================

@router.post("/submit", response_model=ContactSubmissionResponse, status_code=status.HTTP_201_CREATED)
def submit_contact_form(submission: ContactSubmissionRequest):
    """
    Submit a contact form (PUBLIC - No authentication required)
    
    This endpoint allows anyone to submit a contact form with their:
    - Name
    - Email
    - Phone number
    - Subject
    - Message
    
    All fields are validated before submission.
    """
    try:
        # Create submission in database
        submission_in_db = ContactSubmissionInDB(
            name=submission.name,
            email=submission.email.lower(),
            phone=submission.phone,
            subject=submission.subject,
            message=submission.message,
            status=ContactStatus.PENDING,
            isRead=False,
            createdAt=datetime.utcnow()
        )
        
        created_submission = contact_repository.create_submission(submission_in_db)
        
        return created_submission
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to submit contact form. Please try again. Error: {str(e)}"
        )


@router.get("/faqs", response_model=List[FAQResponse])
def get_faqs(
    category: Optional[str] = Query(None, description="Filter by category: all, loans, insurance, investments, tax")
):
    """
    Get all active FAQs (PUBLIC - No authentication required)
    
    Optional filter by category:
    - all: Get all FAQs
    - loans: Loan-related questions
    - insurance: Insurance-related questions
    - investments: Investment-related questions
    - tax: Tax planning questions
    """
    try:
        faqs = contact_repository.get_all_faqs(category=category, is_active=True)
        
        return [
            FAQResponse(
                id=str(faq["_id"]),
                category=faq["category"],
                question=faq["question"],
                answer=faq["answer"],
                highlight=faq.get("highlight"),
                isActive=faq.get("isActive", True),
                order=faq.get("order", 0),
                createdAt=faq["createdAt"],
                updatedAt=faq.get("updatedAt")
            )
            for faq in faqs
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch FAQs. Error: {str(e)}"
        )


# ===================== ADMIN ENDPOINTS (Authentication Required) =====================

@router.get("/submissions", response_model=PaginatedContactResponse)
def get_all_submissions(
    skip: int = Query(0, ge=0, description="Number of records to skip (Default: 0)"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of records to return (Default: 50, Max: 100)"),
    status: Optional[str] = Query(None, description="Filter by status (pending, in_progress, resolved, closed)"),
    is_read: Optional[bool] = Query(None, description="Filter by read status (true/false)"),
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Get all contact submissions with pagination (ADMIN ONLY - Requires authentication)
    
    **Query Parameters:**
    - **skip** (integer): Number of records to skip (for pagination) - Default: 0
    - **limit** (integer): Maximum number of records to return - Default: 50, Max: 100
    - **status** (string): Filter by status - Options: pending, in_progress, resolved, closed
    - **is_read** (boolean): Filter by read status - Options: true, false
    
    **Returns JSON:**
    ```json
    {
      "data": [...],
      "total": 150,
      "skip": 0,
      "limit": 50,
      "hasMore": true
    }
    ```
    """
    try:
        # Get total count
        total_count = contact_repository.count_submissions(status=status, is_read=is_read)
        
        # Get submissions
        submissions = contact_repository.get_all_submissions(
            skip=skip,
            limit=limit,
            status=status,
            is_read=is_read
        )
        
        # Convert to response model
        submissions_data = [
            ContactSubmissionResponse(
                id=str(sub["_id"]),
                name=sub["name"],
                email=sub["email"],
                phone=sub["phone"],
                subject=sub["subject"],
                message=sub["message"],
                status=sub["status"],
                isRead=sub.get("isRead", False),
                adminNotes=sub.get("adminNotes"),
                createdAt=sub["createdAt"],
                updatedAt=sub.get("updatedAt"),
                resolvedAt=sub.get("resolvedAt")
            )
            for sub in submissions
        ]
        
        # Return paginated response
        return PaginatedContactResponse(
            data=submissions_data,
            total=total_count,
            skip=skip,
            limit=limit,
            hasMore=(skip + len(submissions_data)) < total_count
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch submissions. Error: {str(e)}"
        )


@router.get("/submissions/{submission_id}", response_model=ContactSubmissionResponse)
def get_submission_by_id(
    submission_id: str,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Get a specific contact submission by ID (ADMIN ONLY)
    
    Automatically marks the submission as read when fetched.
    """
    submission = contact_repository.get_submission_by_id(submission_id)
    
    if not submission:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact submission not found"
        )
    
    # Mark as read when admin views it
    if not submission.get("isRead", False):
        contact_repository.mark_as_read(submission_id)
        submission["isRead"] = True
    
    return ContactSubmissionResponse(
        id=str(submission["_id"]),
        name=submission["name"],
        email=submission["email"],
        phone=submission["phone"],
        subject=submission["subject"],
        message=submission["message"],
        status=submission["status"],
        isRead=submission.get("isRead", False),
        adminNotes=submission.get("adminNotes"),
        createdAt=submission["createdAt"],
        updatedAt=submission.get("updatedAt"),
        resolvedAt=submission.get("resolvedAt")
    )


@router.patch("/submissions/{submission_id}/status", status_code=status.HTTP_200_OK)
def update_submission_status(
    submission_id: str,
    status_update: ContactUpdateStatusRequest,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Update the status of a contact submission (ADMIN ONLY)
    
    Allowed statuses:
    - pending: Initial status
    - in_progress: Being worked on
    - resolved: Issue resolved
    - closed: Submission closed
    
    Can also add admin notes for internal tracking.
    """
    submission = contact_repository.get_submission_by_id(submission_id)
    
    if not submission:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact submission not found"
        )
    
    success = contact_repository.update_submission_status(
        submission_id=submission_id,
        status=status_update.status,
        admin_notes=status_update.adminNotes
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update submission status"
        )
    
    return {
        "message": "Submission status updated successfully",
        "status": status_update.status.value
    }


@router.patch("/submissions/{submission_id}/read", status_code=status.HTTP_200_OK)
def mark_submission_as_read(
    submission_id: str,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Mark a contact submission as read (ADMIN ONLY)
    """
    submission = contact_repository.get_submission_by_id(submission_id)
    
    if not submission:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact submission not found"
        )
    
    success = contact_repository.mark_as_read(submission_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to mark submission as read"
        )
    
    return {"message": "Submission marked as read"}


@router.delete("/submissions/{submission_id}", status_code=status.HTTP_200_OK)
def delete_submission(
    submission_id: str,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Delete a contact submission (ADMIN ONLY)
    
    This is a permanent deletion and cannot be undone.
    """
    submission = contact_repository.get_submission_by_id(submission_id)
    
    if not submission:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact submission not found"
        )
    
    success = contact_repository.delete_submission(submission_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete submission"
        )
    
    return {"message": "Submission deleted successfully"}

@router.get("/statistics", response_model=ContactStatisticsResponse)
def get_contact_statistics(current_user: dict = Depends(get_current_user_optional)):
    """
    Get contact submission statistics (ADMIN ONLY)
    Returns:
    - Total submissions
    - Count by status (pending, in_progress, resolved, closed)
    - Unread count
    - Today's submissions
    - This week's submissions
    - This month's submissions
    """
    try:
        statistics = contact_repository.get_statistics()
        return statistics
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch statistics. Error: {str(e)}"
        )


# ===================== FAQ MANAGEMENT (ADMIN ONLY) =====================

@router.post("/faqs", response_model=FAQResponse, status_code=status.HTTP_201_CREATED)
def create_faq(
    faq: FAQRequest,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Create a new FAQ (ADMIN ONLY)
    
    Required fields:
    - category: FAQ category (loans, insurance, investments, tax)
    - question: The question
    - answer: The answer
    - highlight: Optional highlight text
    - isActive: Whether FAQ is active (default: true)
    """
    try:
        faq_in_db = FAQInDB(
            category=faq.category,
            question=faq.question,
            answer=faq.answer,
            highlight=faq.highlight,
            isActive=faq.isActive,
            order=0,
            createdAt=datetime.utcnow()
        )
        
        created_faq = contact_repository.create_faq(faq_in_db)
        return created_faq
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create FAQ. Error: {str(e)}"
        )


@router.get("/faqs/all", response_model=List[FAQResponse])
def get_all_faqs_admin(
    category: Optional[str] = Query(None, description="Filter by category"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Get all FAQs including inactive ones (ADMIN ONLY)
    """
    try:
        faqs = contact_repository.get_all_faqs(category=category, is_active=is_active)
        
        return [
            FAQResponse(
                id=str(faq["_id"]),
                category=faq["category"],
                question=faq["question"],
                answer=faq["answer"],
                highlight=faq.get("highlight"),
                isActive=faq.get("isActive", True),
                order=faq.get("order", 0),
                createdAt=faq["createdAt"],
                updatedAt=faq.get("updatedAt")
            )
            for faq in faqs
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch FAQs. Error: {str(e)}"
        )


@router.get("/faqs/{faq_id}", response_model=FAQResponse)
def get_faq_by_id(
    faq_id: str,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Get a specific FAQ by ID (ADMIN ONLY)
    """
    faq = contact_repository.get_faq_by_id(faq_id)
    
    if not faq:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="FAQ not found"
        )
    
    return FAQResponse(
        id=str(faq["_id"]),
        category=faq["category"],
        question=faq["question"],
        answer=faq["answer"],
        highlight=faq.get("highlight"),
        isActive=faq.get("isActive", True),
        order=faq.get("order", 0),
        createdAt=faq["createdAt"],
        updatedAt=faq.get("updatedAt")
    )


@router.put("/faqs/{faq_id}", response_model=FAQResponse)
def update_faq(
    faq_id: str,
    faq: FAQRequest,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Update a FAQ (ADMIN ONLY)
    """
    existing_faq = contact_repository.get_faq_by_id(faq_id)
    
    if not existing_faq:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="FAQ not found"
        )
    
    faq_data = faq.dict()
    success = contact_repository.update_faq(faq_id, faq_data)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update FAQ"
        )
    
    # Fetch and return updated FAQ
    updated_faq = contact_repository.get_faq_by_id(faq_id)
    
    return FAQResponse(
        id=str(updated_faq["_id"]),
        category=updated_faq["category"],
        question=updated_faq["question"],
        answer=updated_faq["answer"],
        highlight=updated_faq.get("highlight"),
        isActive=updated_faq.get("isActive", True),
        order=updated_faq.get("order", 0),
        createdAt=updated_faq["createdAt"],
        updatedAt=updated_faq.get("updatedAt")
    )


@router.delete("/faqs/{faq_id}", status_code=status.HTTP_200_OK)
def delete_faq(
    faq_id: str,
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Delete a FAQ (ADMIN ONLY)
    """
    faq = contact_repository.get_faq_by_id(faq_id)
    
    if not faq:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="FAQ not found"
        )
    
    success = contact_repository.delete_faq(faq_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete FAQ"
        )
    
    return {"message": "FAQ deleted successfully"}


@router.patch("/faqs/{faq_id}/order", status_code=status.HTTP_200_OK)
def update_faq_order(
    faq_id: str,
    order: int = Query(..., ge=0, description="New order position"),
    current_user: dict = Depends(get_current_user_optional)
):
    """
    Update FAQ display order (ADMIN ONLY)
    
    Lower order numbers appear first in the list.
    """
    faq = contact_repository.get_faq_by_id(faq_id)
    
    if not faq:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="FAQ not found"
        )
    
    success = contact_repository.update_faq_order(faq_id, order)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update FAQ order"
        )
    
    return {"message": "FAQ order updated successfully", "order": order}

