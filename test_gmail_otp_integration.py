"""
Quick Test Script - Gmail OTP Integration
Test करने के लिए यह script चलाओ
"""

import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def test_forgot_password_flow():
    """Test complete forgot password flow"""
    
    print("\n" + "="*60)
    print("  GMAIL OTP INTEGRATION TEST")
    print("="*60)
    
    # Get email from user
    email = input("\n📧 Enter your email (registered in database): ").strip()
    
    if not email:
        print("❌ Email cannot be empty!")
        return
    
    # Test 1: Send OTP
    print(f"\n🔹 Step 1: Sending OTP to {email}...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/auth/forgot-password",
            json={"email": email},
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("\n✅ OTP Request Successful!")
            print("📧 Check your email inbox (and spam folder)")
            print("⏳ Waiting for you to receive the OTP...")
        else:
            print(f"\n❌ Error: {response.json()}")
            return
            
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Backend server is not running!")
        print("Please start the backend server:")
        print("  cd cashper_backend")
        print("  python run.py")
        return
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return
    
    # Get OTP from user
    print("\n" + "-"*60)
    otp = input("🔐 Enter the OTP received in email: ").strip()
    
    if not otp or len(otp) != 6:
        print("❌ OTP must be 6 digits!")
        return
    
    # Get new password
    new_password = input("🔑 Enter new password (min 8 characters): ").strip()
    
    if len(new_password) < 8:
        print("❌ Password must be at least 8 characters!")
        return
    
    # Test 2: Verify OTP and Reset Password
    print(f"\n🔹 Step 2: Verifying OTP and resetting password...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/auth/reset-password",
            json={
                "email": email,
                "otp": otp,
                "newPassword": new_password
            },
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("\n" + "="*60)
            print("  ✅ PASSWORD RESET SUCCESSFUL!")
            print("="*60)
            print(f"\n✅ Password has been reset for {email}")
            print("✅ You can now login with your new password")
        else:
            print(f"\n❌ Error: {response.json()}")
            
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


def check_backend_status():
    """Check if backend is running"""
    print("\n🔍 Checking backend status...")
    try:
        response = requests.get(f"{BASE_URL}/docs", timeout=5)
        print("✅ Backend is running!")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Backend is not running!")
        print("\nPlease start the backend:")
        print("  cd cashper_backend")
        print("  python run.py")
        return False
    except Exception as e:
        print(f"⚠️  Error checking backend: {str(e)}")
        return False


def check_env_setup():
    """Check if Gmail credentials are likely configured"""
    print("\n🔍 Checking Gmail setup...")
    print("⚠️  Make sure you have configured in cashper_backend/.env:")
    print("   - GMAIL_USER=your-email@gmail.com")
    print("   - GMAIL_APP_PASSWORD=your-app-password")
    print("\n📌 Get App Password from: https://myaccount.google.com/apppasswords")
    
    response = input("\nHave you configured Gmail credentials? (y/n): ").strip().lower()
    return response == 'y'


if __name__ == "__main__":
    print("\n🚀 Gmail OTP Integration - Quick Test")
    print("="*60)
    
    # Check backend
    if not check_backend_status():
        exit(1)
    
    # Check env setup
    if not check_env_setup():
        print("\n⚠️  Please configure Gmail credentials first!")
        print("See GMAIL_INTEGRATION_SETUP.md for detailed steps")
        exit(1)
    
    # Run test
    try:
        test_forgot_password_flow()
    except KeyboardInterrupt:
        print("\n\n👋 Test cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
    
    print("\n" + "="*60)
    print("  Test completed!")
    print("="*60)
    print("\nFor detailed setup guide, see: GMAIL_INTEGRATION_SETUP.md\n")
