"""
Test Email Configuration for Forgot Password OTP
This script checks if Gmail credentials are properly configured
"""

import os
import sys
from dotenv import load_dotenv
import asyncio
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

# Load environment variables from cashper_backend/.env
backend_env_path = os.path.join(os.path.dirname(__file__), 'cashper_backend', '.env')
load_dotenv(backend_env_path)

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def check_env_configuration():
    """Check if environment variables are properly configured"""
    print("\n" + "="*60)
    print("📧 EMAIL CONFIGURATION CHECK")
    print("="*60 + "\n")
    
    # Check if .env file exists
    if not os.path.exists(backend_env_path):
        print("❌ ERROR: .env file not found!")
        print(f"   Expected location: {backend_env_path}")
        return False
    
    print(f"✅ .env file found: {backend_env_path}\n")
    
    # Check GMAIL_USER
    print("1️⃣ Checking GMAIL_USER...")
    if not GMAIL_USER:
        print("   ❌ GMAIL_USER not set in .env file")
        return False
    elif GMAIL_USER == "your-email@gmail.com":
        print(f"   ❌ GMAIL_USER is still using placeholder value: {GMAIL_USER}")
        print("   ⚠️  Please update with your real Gmail address")
        return False
    else:
        print(f"   ✅ GMAIL_USER configured: {GMAIL_USER}")
    
    # Check GMAIL_APP_PASSWORD
    print("\n2️⃣ Checking GMAIL_APP_PASSWORD...")
    if not GMAIL_APP_PASSWORD:
        print("   ❌ GMAIL_APP_PASSWORD not set in .env file")
        return False
    elif GMAIL_APP_PASSWORD == "your-app-password-here":
        print(f"   ❌ GMAIL_APP_PASSWORD is still using placeholder value")
        print("   ⚠️  Please update with your real Gmail App Password")
        print("\n   📖 How to get App Password:")
        print("      1. Go to: https://myaccount.google.com/apppasswords")
        print("      2. Enable 2-Step Verification first")
        print("      3. Generate app password for 'Mail'")
        print("      4. Copy the 16-character password")
        return False
    elif len(GMAIL_APP_PASSWORD) < 16:
        print(f"   ⚠️  GMAIL_APP_PASSWORD seems too short (length: {len(GMAIL_APP_PASSWORD)})")
        print("   ℹ️  Gmail App Passwords are typically 16 characters")
    else:
        # Mask the password for security
        masked = GMAIL_APP_PASSWORD[:4] + "*" * (len(GMAIL_APP_PASSWORD) - 8) + GMAIL_APP_PASSWORD[-4:]
        print(f"   ✅ GMAIL_APP_PASSWORD configured: {masked}")
    
    print("\n" + "="*60)
    return True


async def test_smtp_connection():
    """Test SMTP connection to Gmail"""
    print("\n" + "="*60)
    print("🔌 TESTING SMTP CONNECTION")
    print("="*60 + "\n")
    
    try:
        print("Connecting to smtp.gmail.com:587...")
        smtp = aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, timeout=15)
        
        await asyncio.wait_for(smtp.connect(), timeout=10)
        print("✅ Connected to SMTP server")
        
        await asyncio.wait_for(smtp.starttls(), timeout=10)
        print("✅ TLS encryption started")
        
        await asyncio.wait_for(smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD), timeout=10)
        print("✅ Authentication successful")
        
        await smtp.quit()
        print("✅ Connection closed properly")
        
        print("\n" + "="*60)
        print("🎉 ALL CHECKS PASSED! Email configuration is working!")
        print("="*60)
        return True
        
    except asyncio.TimeoutError:
        print("❌ Connection timeout")
        print("   Check your internet connection")
        return False
        
    except aiosmtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed: {str(e)}")
        print("\n   Possible reasons:")
        print("   1. Wrong email or app password")
        print("   2. Using regular password instead of App Password")
        print("   3. 2-Step Verification not enabled")
        print("   4. App Password not generated correctly")
        return False
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


async def send_test_email():
    """Send a test email"""
    print("\n" + "="*60)
    print("📨 SENDING TEST EMAIL")
    print("="*60 + "\n")
    
    test_email = input(f"Enter email to send test OTP (press Enter to use {GMAIL_USER}): ").strip()
    if not test_email:
        test_email = GMAIL_USER
    
    otp = "123456"  # Test OTP
    
    try:
        # Create email message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Test OTP - Cashper Password Reset"
        message["From"] = GMAIL_USER
        message["To"] = test_email
        
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; padding: 20px;">
                <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; border: 2px solid #007bff;">
                    <h2 style="color: #007bff; text-align: center;">🧪 Test Email - Password Reset OTP</h2>
                    <p style="color: #555; font-size: 16px;">This is a test email from Cashper backend.</p>
                    <p style="color: #555; font-size: 16px;">Your test OTP is:</p>
                    <div style="background-color: #f0f0f0; padding: 20px; text-align: center; border-radius: 5px; margin: 20px 0;">
                        <h1 style="color: #007bff; letter-spacing: 5px; margin: 0;">{otp}</h1>
                    </div>
                    <p style="color: #555; font-size: 14px;">✅ If you received this email, your Gmail OTP configuration is working correctly!</p>
                    <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
                    <p style="color: #888; font-size: 12px; text-align: center;">Cashper Team</p>
                </div>
            </body>
        </html>
        """
        
        part = MIMEText(html_body, "html")
        message.attach(part)
        
        # Send email
        print(f"Sending test email to {test_email}...")
        smtp = aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, timeout=15)
        await asyncio.wait_for(smtp.connect(), timeout=10)
        await asyncio.wait_for(smtp.starttls(), timeout=10)
        await asyncio.wait_for(smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD), timeout=10)
        await asyncio.wait_for(smtp.send_message(message), timeout=15)
        await smtp.quit()
        
        print(f"\n✅ Test email sent successfully to {test_email}!")
        print("   Check your inbox (and spam folder)")
        print("\n" + "="*60)
        return True
        
    except Exception as e:
        print(f"❌ Failed to send test email: {str(e)}")
        return False


async def main():
    """Main test function"""
    print("\n")
    print("█" * 60)
    print("█  CASHPER - EMAIL OTP CONFIGURATION TESTER  █")
    print("█" * 60)
    
    # Step 1: Check environment configuration
    if not check_env_configuration():
        print("\n❌ Configuration check failed!")
        print("\n📖 Please follow the instructions in FIX_EMAIL_OTP_PROBLEM.md")
        print("   Location: c:\\Users\\ASUS\\Desktop\\payloan\\full_proj\\FIX_EMAIL_OTP_PROBLEM.md")
        return
    
    # Step 2: Test SMTP connection
    print("\nPress Enter to test SMTP connection...")
    input()
    
    if not await test_smtp_connection():
        print("\n❌ SMTP connection test failed!")
        return
    
    # Step 3: Send test email
    print("\n")
    send_test = input("Do you want to send a test OTP email? (yes/no): ").strip().lower()
    if send_test in ['yes', 'y']:
        await send_test_email()
    
    print("\n")
    print("█" * 60)
    print("█  TEST COMPLETED  █")
    print("█" * 60)
    print("\nIf all tests passed, your forgot password OTP emails should work!")
    print("\n")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
