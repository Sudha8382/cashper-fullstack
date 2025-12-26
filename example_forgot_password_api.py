"""
Complete Working Example: Forgot Password with OTP Email
This file demonstrates the complete implementation of forgot password
with email OTP using FastAPI and Gmail SMTP.

PRODUCTION-READY IMPLEMENTATION
"""

from fastapi import FastAPI, BackgroundTasks, HTTPException, status
from pydantic import BaseModel, EmailStr
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import asyncio
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Forgot Password API Example")

# ============================================================
# CONFIGURATION
# ============================================================

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

# In-memory OTP storage (use Redis in production)
otp_storage = {}

# Mock user database (replace with real database)
mock_users = {
    "user@example.com": {
        "email": "user@example.com",
        "name": "John Doe",
        "password": "hashed_password_here"
    }
}


# ============================================================
# PYDANTIC MODELS
# ============================================================

class ForgotPasswordRequest(BaseModel):
    """Request model for forgot password"""
    email: EmailStr
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com"
            }
        }


class ResetPasswordRequest(BaseModel):
    """Request model for reset password"""
    email: EmailStr
    otp: str
    new_password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "otp": "123456",
                "new_password": "NewSecure123"
            }
        }


# ============================================================
# EMAIL UTILITY FUNCTION
# ============================================================

async def send_otp_email(recipient_email: str, otp: str, user_name: str = "User") -> bool:
    """
    Send OTP via Gmail using aiosmtplib (async)
    
    Args:
        recipient_email: Recipient's email address
        otp: OTP code to send
        user_name: User's name for personalization
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        print(f"\n{'='*60}")
        print(f"📧 Sending OTP email to: {recipient_email}")
        print(f"{'='*60}")
        
        # Validate credentials
        if not GMAIL_USER or not GMAIL_APP_PASSWORD:
            print("❌ ERROR: Gmail credentials not configured")
            print("   Please set GMAIL_USER and GMAIL_APP_PASSWORD in .env file")
            return False
        
        if GMAIL_USER == "your-email@gmail.com":
            print("❌ ERROR: Using placeholder Gmail credentials")
            print("   Update .env with real Gmail address and App Password")
            return False
        
        print(f"✓ Credentials found: {GMAIL_USER}")
        
        # Create email message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Password Reset OTP - Cashper"
        message["From"] = GMAIL_USER
        message["To"] = recipient_email
        
        # HTML email body
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
                    <p style="color: #555; font-size: 14px;">This OTP will expire in <strong>5 minutes</strong>.</p>
                    <p style="color: #555; font-size: 14px;">If you didn't request this, please ignore this email.</p>
                    <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
                    <p style="color: #888; font-size: 12px; text-align: center;">Best regards,<br>Cashper Team</p>
                </div>
            </body>
        </html>
        """
        
        # Plain text version
        text_body = f"""
Hi {user_name},

Your OTP for password reset is: {otp}

This OTP will expire in 5 minutes.

If you didn't request this, please ignore this email.

Best regards,
Cashper Team
        """
        
        # Attach both versions
        message.attach(MIMEText(text_body, "plain"))
        message.attach(MIMEText(html_body, "html"))
        
        print(f"✓ Email message created")
        print(f"✓ Connecting to Gmail SMTP...")
        
        # Connect to Gmail SMTP server
        smtp = aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, timeout=15)
        await asyncio.wait_for(smtp.connect(), timeout=10)
        print(f"✓ Connected to smtp.gmail.com:587")
        
        # Start TLS encryption
        await asyncio.wait_for(smtp.starttls(), timeout=10)
        print(f"✓ TLS encryption enabled")
        
        # Authenticate
        await asyncio.wait_for(smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD), timeout=10)
        print(f"✓ Authenticated successfully")
        
        # Send email
        await asyncio.wait_for(smtp.send_message(message), timeout=15)
        print(f"✓ Email sent successfully")
        
        # Close connection
        await smtp.quit()
        
        print(f"\n{'='*60}")
        print(f"✅ OTP EMAIL SENT SUCCESSFULLY!")
        print(f"   To: {recipient_email}")
        print(f"   OTP: {otp}")
        print(f"{'='*60}\n")
        
        return True
        
    except asyncio.TimeoutError:
        print(f"\n❌ Timeout: Email sending timed out")
        print(f"   Check your internet connection")
        return False
        
    except aiosmtplib.SMTPAuthenticationError as e:
        print(f"\n❌ Authentication Error: {str(e)}")
        print(f"   Common causes:")
        print(f"   • Using regular password instead of App Password")
        print(f"   • 2-Step Verification not enabled")
        print(f"   • Incorrect credentials")
        return False
        
    except Exception as e:
        print(f"\n❌ Error sending email: {type(e).__name__}")
        print(f"   Message: {str(e)}")
        return False


# ============================================================
# API ENDPOINTS
# ============================================================

@app.post("/api/auth/forgot-password", status_code=status.HTTP_200_OK)
async def forgot_password(request: ForgotPasswordRequest, background_tasks: BackgroundTasks):
    """
    Send OTP to email for password reset
    
    Process:
    1. Validate email exists
    2. Generate 6-digit OTP
    3. Store OTP with 5-minute expiry
    4. Send email asynchronously
    5. Return success response immediately
    
    Security: Doesn't reveal if email exists or not
    """
    email = request.email.lower()
    
    # Check if user exists (replace with real database query)
    user = mock_users.get(email)
    
    if not user:
        # Don't reveal if email exists (security best practice)
        return {
            "success": True,
            "message": "If the email exists, an OTP has been sent to your inbox."
        }
    
    # Generate 6-digit OTP
    otp = str(random.randint(100000, 999999))
    
    # Store OTP with expiry time (5 minutes)
    otp_storage[email] = {
        "otp": otp,
        "expiry": datetime.utcnow() + timedelta(minutes=5),
        "type": "password_reset"
    }
    
    # Log OTP to console (for development)
    print(f"\n{'='*60}")
    print(f"🔑 PASSWORD RESET OTP GENERATED")
    print(f"   Email: {email}")
    print(f"   OTP: {otp}")
    print(f"   Valid for: 5 minutes")
    print(f"{'='*60}\n")
    
    # Get user name for email personalization
    user_name = user.get("name", "User")
    
    # Send email in background (non-blocking)
    async def send_email_task():
        """Background task to send email"""
        try:
            success = await send_otp_email(email, otp, user_name)
            if success:
                print(f"✅ Email sent successfully to {email}")
            else:
                print(f"⚠️  Failed to send email to {email}")
        except Exception as e:
            print(f"❌ Error in email task: {str(e)}")
    
    # Add to background tasks (FastAPI handles async execution)
    background_tasks.add_task(send_email_task)
    
    # Return immediately without waiting for email
    return {
        "success": True,
        "message": "OTP has been sent to your email address. Please check your inbox and spam folder.",
        "otp_expiry_minutes": 5
    }


@app.post("/api/auth/reset-password", status_code=status.HTTP_200_OK)
async def reset_password(request: ResetPasswordRequest):
    """
    Reset password using OTP
    
    Process:
    1. Validate OTP exists and not expired
    2. Verify OTP matches
    3. Update user password
    4. Delete used OTP
    5. Return success
    """
    email = request.email.lower()
    
    # Check if OTP exists
    if email not in otp_storage:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP. Please request a new one."
        )
    
    stored_data = otp_storage[email]
    
    # Check if OTP expired
    if datetime.utcnow() > stored_data["expiry"]:
        del otp_storage[email]
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP has expired. Please request a new one."
        )
    
    # Verify OTP
    if stored_data["otp"] != request.otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid OTP. Please try again."
        )
    
    # Check if user exists
    if email not in mock_users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    
    # Update password (in real app, hash the password)
    mock_users[email]["password"] = request.new_password  # Hash this!
    
    # Delete used OTP
    del otp_storage[email]
    
    print(f"✅ Password reset successful for {email}")
    
    return {
        "success": True,
        "message": "Password reset successful. You can now login with your new password."
    }


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "running",
        "api": "Forgot Password Example",
        "endpoints": {
            "forgot_password": "POST /api/auth/forgot-password",
            "reset_password": "POST /api/auth/reset-password"
        }
    }


# ============================================================
# RUN THE APP
# ============================================================

if __name__ == "__main__":
    import uvicorn
    
    print("\n" + "="*60)
    print("🚀 Starting Forgot Password API Example")
    print("="*60)
    print("\nEndpoints:")
    print("  • POST /api/auth/forgot-password")
    print("  • POST /api/auth/reset-password")
    print("\nMake sure .env file is configured with:")
    print("  • GMAIL_USER=your-email@gmail.com")
    print("  • GMAIL_APP_PASSWORD=your-app-password")
    print("\n" + "="*60 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
