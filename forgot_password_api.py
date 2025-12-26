"""
FastAPI Forgot Password Implementation with Gmail OTP
This module provides endpoints for password reset functionality using OTP sent via Gmail.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, Dict
import random
import string
from datetime import datetime, timedelta
import asyncio
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import hashlib

# Load environment variables
load_dotenv()

app = FastAPI(title="Forgot Password API", version="1.0.0")

# ==================== Configuration ====================
GMAIL_USER = os.getenv("GMAIL_USER")  # Your Gmail address
GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")  # Gmail app password (not regular password)
OTP_EXPIRY_MINUTES = 10  # OTP expires after 10 minutes

# ==================== In-Memory Storage ====================
# Mock user database (replace with real database later)
mock_users_db: Dict[str, dict] = {
    "user@example.com": {
        "email": "user@example.com",
        "password": hashlib.sha256("oldpassword123".encode()).hexdigest(),
        "name": "Test User"
    },
    "test@gmail.com": {
        "email": "test@gmail.com",
        "password": hashlib.sha256("test123".encode()).hexdigest(),
        "name": "Test Account"
    }
}

# OTP storage with expiry time
# Structure: {email: {"otp": "123456", "expires_at": datetime_obj}}
otp_storage: Dict[str, dict] = {}


# ==================== Pydantic Models ====================
class RequestOTPModel(BaseModel):
    """Model for requesting OTP"""
    email: EmailStr = Field(..., description="User's email address")
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com"
            }
        }


class VerifyOTPModel(BaseModel):
    """Model for verifying OTP and resetting password"""
    email: EmailStr = Field(..., description="User's email address")
    otp: str = Field(..., min_length=6, max_length=6, description="6-digit OTP")
    new_password: str = Field(..., min_length=8, description="New password (minimum 8 characters)")
    
    @validator('otp')
    def validate_otp(cls, v):
        """Validate that OTP contains only digits"""
        if not v.isdigit():
            raise ValueError('OTP must contain only digits')
        return v
    
    @validator('new_password')
    def validate_password(cls, v):
        """Validate password strength"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isalpha() for char in v):
            raise ValueError('Password must contain at least one letter')
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "otp": "123456",
                "new_password": "NewSecure123"
            }
        }


class ResponseModel(BaseModel):
    """Generic response model"""
    success: bool
    message: str
    data: Optional[dict] = None


# ==================== Helper Functions ====================
def generate_otp(length: int = 6) -> str:
    """
    Generate a random numeric OTP
    
    Args:
        length: Length of OTP (default: 6)
    
    Returns:
        String containing random digits
    """
    return ''.join(random.choices(string.digits, k=length))


def hash_password(password: str) -> str:
    """
    Hash password using SHA-256
    (In production, use bcrypt or argon2)
    
    Args:
        password: Plain text password
    
    Returns:
        Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def check_email_exists(email: str) -> bool:
    """
    Check if email exists in database
    
    Args:
        email: Email address to check
    
    Returns:
        True if email exists, False otherwise
    """
    return email.lower() in mock_users_db


def store_otp(email: str, otp: str) -> None:
    """
    Store OTP with expiry time
    
    Args:
        email: User's email address
        otp: Generated OTP
    """
    expires_at = datetime.now() + timedelta(minutes=OTP_EXPIRY_MINUTES)
    otp_storage[email.lower()] = {
        "otp": otp,
        "expires_at": expires_at
    }


def verify_otp(email: str, otp: str) -> tuple[bool, str]:
    """
    Verify OTP for given email
    
    Args:
        email: User's email address
        otp: OTP to verify
    
    Returns:
        Tuple of (is_valid, message)
    """
    email = email.lower()
    
    # Check if OTP exists for this email
    if email not in otp_storage:
        return False, "No OTP found for this email. Please request a new OTP."
    
    stored_data = otp_storage[email]
    
    # Check if OTP has expired
    if datetime.now() > stored_data["expires_at"]:
        del otp_storage[email]  # Clean up expired OTP
        return False, "OTP has expired. Please request a new OTP."
    
    # Check if OTP matches
    if stored_data["otp"] != otp:
        return False, "Invalid OTP. Please try again."
    
    return True, "OTP verified successfully"


def update_user_password(email: str, new_password: str) -> bool:
    """
    Update user password in database
    
    Args:
        email: User's email address
        new_password: New password (will be hashed)
    
    Returns:
        True if successful, False otherwise
    """
    email = email.lower()
    if email in mock_users_db:
        mock_users_db[email]["password"] = hash_password(new_password)
        # Clean up used OTP
        if email in otp_storage:
            del otp_storage[email]
        return True
    return False


async def send_email_otp(recipient_email: str, otp: str, user_name: str = "User") -> None:
    """
    Send OTP via Gmail using aiosmtplib (async)
    
    Args:
        recipient_email: Recipient's email address
        otp: OTP to send
        user_name: User's name for personalization
    
    Raises:
        Exception: If email sending fails
    """
    # Validate Gmail credentials
    if not GMAIL_USER or not GMAIL_PASSWORD:
        raise Exception("Gmail credentials not configured. Please set GMAIL_USER and GMAIL_APP_PASSWORD in .env file")
    
    # Create email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Password Reset OTP - Cashper"
    message["From"] = GMAIL_USER
    message["To"] = recipient_email
    
    # Email body (HTML and plain text versions)
    text_body = f"""
    Hi {user_name},
    
    Your OTP for password reset is: {otp}
    
    This OTP will expire in {OTP_EXPIRY_MINUTES} minutes.
    
    If you didn't request this, please ignore this email.
    
    Best regards,
    Cashper Team
    """
    
    html_body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4;">
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                <h2 style="color: #333; text-align: center;">Password Reset Request</h2>
                <p style="color: #555; font-size: 16px;">Hi {user_name},</p>
                <p style="color: #555; font-size: 16px;">Your OTP for password reset is:</p>
                <div style="background-color: #f0f0f0; padding: 20px; text-align: center; border-radius: 5px; margin: 20px 0;">
                    <h1 style="color: #007bff; letter-spacing: 5px; margin: 0; font-size: 36px;">{otp}</h1>
                </div>
                <p style="color: #555; font-size: 14px;">This OTP will expire in <strong>{OTP_EXPIRY_MINUTES} minutes</strong>.</p>
                <p style="color: #555; font-size: 14px;">If you didn't request this, please ignore this email.</p>
                <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
                <p style="color: #888; font-size: 12px; text-align: center;">Best regards,<br>Cashper Team</p>
            </div>
        </body>
    </html>
    """
    
    # Attach both versions
    part1 = MIMEText(text_body, "plain")
    part2 = MIMEText(html_body, "html")
    message.attach(part1)
    message.attach(part2)
    
    # Send email using aiosmtplib (async)
    try:
        # Connect to Gmail SMTP server
        smtp = aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, timeout=30)
        await smtp.connect()
        await smtp.starttls()
        await smtp.login(GMAIL_USER, GMAIL_PASSWORD)
        await smtp.send_message(message)
        await smtp.quit()
        print(f"✅ Email sent successfully to {recipient_email}")
    except aiosmtplib.SMTPAuthenticationError as e:
        raise Exception(f"Gmail authentication failed. Please check GMAIL_USER and GMAIL_APP_PASSWORD in .env file. Error: {str(e)}")
    except aiosmtplib.SMTPException as e:
        raise Exception(f"SMTP error occurred: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")


# ==================== API Endpoints ====================
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Forgot Password API",
        "version": "1.0.0",
        "endpoints": {
            "request_otp": "/api/forgot-password/request-otp",
            "verify_otp": "/api/forgot-password/verify-otp"
        }
    }


@app.post(
    "/api/forgot-password/request-otp",
    response_model=ResponseModel,
    status_code=status.HTTP_200_OK,
    tags=["Password Reset"]
)
async def request_otp(request: RequestOTPModel):
    """
    Request OTP for password reset
    
    Process:
    1. Validate email exists in database
    2. Generate 6-digit OTP
    3. Store OTP with expiry time
    4. Send OTP via Gmail
    5. Return success response
    
    Args:
        request: RequestOTPModel containing user email
    
    Returns:
        ResponseModel with success status and message
    """
    try:
        email = request.email.lower()
        
        # Step 1: Check if email exists in database
        if not check_email_exists(email):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email address not found in our records"
            )
        
        # Step 2: Generate OTP
        otp = generate_otp()
        
        # Step 3: Store OTP with expiry
        store_otp(email, otp)
        
        # Get user name for email personalization
        user_name = mock_users_db[email].get("name", "User")
        
        # Step 4: Send OTP via email (async)
        try:
            await send_email_otp(request.email, otp, user_name)
        except Exception as e:
            # Clean up stored OTP if email fails
            if email in otp_storage:
                del otp_storage[email]
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to send OTP email: {str(e)}"
            )
        
        # Step 5: Return success response
        return ResponseModel(
            success=True,
            message=f"OTP sent successfully to {request.email}. It will expire in {OTP_EXPIRY_MINUTES} minutes.",
            data={
                "email": request.email,
                "otp_expiry_minutes": OTP_EXPIRY_MINUTES
            }
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


@app.post(
    "/api/forgot-password/verify-otp",
    response_model=ResponseModel,
    status_code=status.HTTP_200_OK,
    tags=["Password Reset"]
)
async def verify_otp_and_reset_password(request: VerifyOTPModel):
    """
    Verify OTP and reset password
    
    Process:
    1. Verify OTP validity and expiry
    2. Update user password
    3. Clear used OTP
    4. Return success response
    
    Args:
        request: VerifyOTPModel containing email, OTP, and new password
    
    Returns:
        ResponseModel with success status and message
    """
    try:
        email = request.email.lower()
        
        # Step 1: Check if email exists
        if not check_email_exists(email):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email address not found in our records"
            )
        
        # Step 2: Verify OTP
        is_valid, message = verify_otp(email, request.otp)
        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
            )
        
        # Step 3: Update password
        success = update_user_password(email, request.new_password)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update password. Please try again."
            )
        
        # Step 4: Return success response
        return ResponseModel(
            success=True,
            message="Password reset successfully. You can now login with your new password.",
            data={
                "email": request.email
            }
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


# ==================== Admin/Debug Endpoints (Optional) ====================
@app.get("/api/debug/mock-users", tags=["Debug"])
async def get_mock_users():
    """
    Get all mock users (for testing only - remove in production)
    """
    return {
        "users": [
            {"email": email, "name": data["name"]}
            for email, data in mock_users_db.items()
        ]
    }


@app.get("/api/debug/active-otps", tags=["Debug"])
async def get_active_otps():
    """
    Get all active OTPs (for testing only - remove in production)
    """
    return {
        "active_otps": [
            {
                "email": email,
                "otp": data["otp"],
                "expires_at": data["expires_at"].isoformat(),
                "is_expired": datetime.now() > data["expires_at"]
            }
            for email, data in otp_storage.items()
        ]
    }


# ==================== Startup/Shutdown Events ====================
@app.on_event("startup")
async def startup_event():
    """
    Run on application startup
    """
    print("=" * 50)
    print("Forgot Password API Started")
    print("=" * 50)
    print(f"Gmail User: {GMAIL_USER}")
    print(f"OTP Expiry: {OTP_EXPIRY_MINUTES} minutes")
    print(f"Mock Users Count: {len(mock_users_db)}")
    print("=" * 50)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Run on application shutdown
    """
    print("Shutting down Forgot Password API...")


# ==================== Run Application ====================
if __name__ == "__main__":
    import uvicorn
    
    # Run the application
    uvicorn.run(
        "forgot_password_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
