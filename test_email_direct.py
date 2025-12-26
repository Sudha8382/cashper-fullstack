"""
Direct email test to verify Gmail configuration
"""
import asyncio
import sys
import os

# Add backend to path
sys.path.insert(0, r'C:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend')

from app.utils.email_service import send_otp_email

async def test_email():
    """Test sending OTP email"""
    
    print("\n" + "="*60)
    print("🧪 TESTING EMAIL SENDING DIRECTLY")
    print("="*60 + "\n")
    
    test_email = "kumuyadav249@gmail.com"  # Sending to yourself for testing
    test_otp = "123456"
    test_name = "Test User"
    
    print(f"📧 Sending test email to: {test_email}")
    print(f"🔢 OTP: {test_otp}")
    print(f"👤 Name: {test_name}\n")
    
    try:
        result = await send_otp_email(test_email, test_otp, test_name)
        
        print("\n" + "="*60)
        if result:
            print("✅ EMAIL SENT SUCCESSFULLY!")
            print("="*60)
            print("\n📬 Please check your email inbox:")
            print(f"   Email: {test_email}")
            print(f"   Subject: Password Reset OTP - Cashper")
            print(f"   OTP: {test_otp}")
            print("\n⚠️  Also check SPAM folder if not in inbox")
        else:
            print("❌ EMAIL SENDING FAILED!")
            print("="*60)
            print("\nCheck the error messages above for details.")
        print("="*60 + "\n")
        
        return result
        
    except Exception as e:
        print("\n" + "="*60)
        print("❌ EXCEPTION OCCURRED")
        print("="*60)
        print(f"Error: {str(e)}")
        print("="*60 + "\n")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_email())
    sys.exit(0 if result else 1)
