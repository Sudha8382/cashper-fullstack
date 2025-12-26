"""
Quick Test Script to Verify Gmail OTP Setup
Run this to check if Gmail credentials are working
"""

import asyncio
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


async def test_gmail_connection():
    """Test Gmail SMTP connection"""
    print("\n" + "="*60)
    print("  GMAIL OTP SETUP VERIFICATION")
    print("="*60)
    
    # Check if credentials are set
    print("\n1. Checking environment variables...")
    if not GMAIL_USER or GMAIL_USER == "your-email@gmail.com":
        print("❌ GMAIL_USER not configured in .env file")
        print("   Please edit .env file and add your Gmail address")
        return False
    else:
        print(f"✅ GMAIL_USER found: {GMAIL_USER}")
    
    if not GMAIL_PASSWORD or GMAIL_PASSWORD == "your-app-password-here":
        print("❌ GMAIL_APP_PASSWORD not configured in .env file")
        print("   Please edit .env file and add your Gmail App Password")
        print("\n   Steps to get App Password:")
        print("   1. Go to: https://myaccount.google.com/security")
        print("   2. Enable 2-Step Verification")
        print("   3. Go to: https://myaccount.google.com/apppasswords")
        print("   4. Create app password for 'Mail'")
        print("   5. Copy the 16-character password to .env file")
        return False
    else:
        print(f"✅ GMAIL_APP_PASSWORD found: {'*' * len(GMAIL_PASSWORD)}")
    
    # Test SMTP connection
    print("\n2. Testing Gmail SMTP connection...")
    try:
        smtp = aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, timeout=30)
        await smtp.connect()
        print("✅ Connected to Gmail SMTP server")
        
        await smtp.starttls()
        print("✅ TLS encryption started")
        
        await smtp.login(GMAIL_USER, GMAIL_PASSWORD)
        print("✅ Authentication successful")
        
        await smtp.quit()
        print("✅ Connection closed properly")
        
        return True
        
    except aiosmtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed!")
        print(f"   Error: {str(e)}")
        print("\n   Possible issues:")
        print("   1. Wrong Gmail App Password")
        print("   2. 2-Step Verification not enabled")
        print("   3. Using regular password instead of App Password")
        return False
        
    except Exception as e:
        print(f"❌ Connection failed!")
        print(f"   Error: {str(e)}")
        return False


async def send_test_email():
    """Send a test email"""
    print("\n3. Sending test email...")
    
    recipient = input(f"Enter recipient email (press Enter to use {GMAIL_USER}): ").strip()
    if not recipient:
        recipient = GMAIL_USER
    
    try:
        # Create test message
        message = MIMEMultipart("alternative")
        message["Subject"] = "🧪 Test Email - OTP Setup Verification"
        message["From"] = GMAIL_USER
        message["To"] = recipient
        
        html_body = """
        <html>
            <body style="font-family: Arial, sans-serif; padding: 20px;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #f0f8ff; padding: 30px; border-radius: 10px;">
                    <h2 style="color: #007bff; text-align: center;">✅ Gmail OTP Setup Successful!</h2>
                    <p style="color: #333; font-size: 16px;">Congratulations!</p>
                    <p style="color: #555;">Your Gmail credentials are correctly configured and working.</p>
                    <div style="background-color: white; padding: 20px; border-left: 4px solid #28a745; margin: 20px 0;">
                        <p style="margin: 0; color: #28a745; font-weight: bold;">✓ SMTP Connection: Success</p>
                        <p style="margin: 0; color: #28a745; font-weight: bold;">✓ Authentication: Success</p>
                        <p style="margin: 0; color: #28a745; font-weight: bold;">✓ Email Sending: Success</p>
                    </div>
                    <p style="color: #555;">You can now use the Forgot Password API to send OTP emails!</p>
                    <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
                    <p style="color: #888; font-size: 12px; text-align: center;">Cashper - Forgot Password API</p>
                </div>
            </body>
        </html>
        """
        
        message.attach(MIMEText(html_body, "html"))
        
        # Send email
        smtp = aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, timeout=30)
        await smtp.connect()
        await smtp.starttls()
        await smtp.login(GMAIL_USER, GMAIL_PASSWORD)
        await smtp.send_message(message)
        await smtp.quit()
        
        print(f"✅ Test email sent successfully to {recipient}")
        print(f"   Please check your inbox!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send test email!")
        print(f"   Error: {str(e)}")
        return False


async def main():
    """Main test function"""
    # Test connection
    connection_ok = await test_gmail_connection()
    
    if not connection_ok:
        print("\n" + "="*60)
        print("❌ SETUP INCOMPLETE")
        print("="*60)
        print("\nPlease fix the issues above and run this script again.")
        return
    
    # Ask if user wants to send test email
    print("\n" + "="*60)
    send_email = input("\nDo you want to send a test email? (y/n): ").strip().lower()
    
    if send_email == 'y':
        email_ok = await send_test_email()
        
        if email_ok:
            print("\n" + "="*60)
            print("✅ SETUP COMPLETE!")
            print("="*60)
            print("\nYour Gmail OTP setup is working perfectly!")
            print("You can now run: python forgot_password_api.py")
        else:
            print("\n" + "="*60)
            print("⚠️  SETUP INCOMPLETE")
            print("="*60)
    else:
        print("\n" + "="*60)
        print("✅ CONNECTION TEST PASSED")
        print("="*60)
        print("\nYour credentials are correct. You can now run:")
        print("  python forgot_password_api.py")


if __name__ == "__main__":
    print("\n🔍 Gmail OTP Setup Verification Tool")
    asyncio.run(main())
