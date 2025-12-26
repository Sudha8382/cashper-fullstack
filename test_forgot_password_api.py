"""
Test script for Forgot Password API
This script demonstrates how to test the forgot password endpoints
"""

import requests
import time

# Configuration
BASE_URL = "http://localhost:8000"
TEST_EMAIL = "user@example.com"  # Use one of the mock emails

def print_response(response, title):
    """Pretty print API response"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(response.json())
    print("="*60)


def test_request_otp():
    """Test requesting OTP"""
    print("\n🔹 TEST 1: Request OTP")
    
    url = f"{BASE_URL}/api/forgot-password/request-otp"
    payload = {
        "email": TEST_EMAIL
    }
    
    response = requests.post(url, json=payload)
    print_response(response, "Request OTP Result")
    
    return response.status_code == 200


def test_request_otp_invalid_email():
    """Test requesting OTP with invalid email"""
    print("\n🔹 TEST 2: Request OTP with Non-existent Email")
    
    url = f"{BASE_URL}/api/forgot-password/request-otp"
    payload = {
        "email": "nonexistent@example.com"
    }
    
    response = requests.post(url, json=payload)
    print_response(response, "Request OTP with Invalid Email")
    
    return response.status_code == 404


def test_verify_otp(otp):
    """Test verifying OTP and resetting password"""
    print("\n🔹 TEST 3: Verify OTP and Reset Password")
    
    url = f"{BASE_URL}/api/forgot-password/verify-otp"
    payload = {
        "email": TEST_EMAIL,
        "otp": otp,
        "new_password": "NewSecure123"
    }
    
    response = requests.post(url, json=payload)
    print_response(response, "Verify OTP Result")
    
    return response.status_code == 200


def test_verify_wrong_otp():
    """Test verifying with wrong OTP"""
    print("\n🔹 TEST 4: Verify with Wrong OTP")
    
    url = f"{BASE_URL}/api/forgot-password/verify-otp"
    payload = {
        "email": TEST_EMAIL,
        "otp": "000000",
        "new_password": "NewSecure123"
    }
    
    response = requests.post(url, json=payload)
    print_response(response, "Verify Wrong OTP Result")
    
    return response.status_code == 400


def get_active_otps():
    """Get active OTPs from debug endpoint"""
    print("\n🔹 DEBUG: Get Active OTPs")
    
    url = f"{BASE_URL}/api/debug/active-otps"
    response = requests.get(url)
    print_response(response, "Active OTPs")
    
    # Extract OTP for test email if exists
    if response.status_code == 200:
        data = response.json()
        for otp_data in data.get("active_otps", []):
            if otp_data["email"] == TEST_EMAIL.lower():
                return otp_data["otp"]
    
    return None


def get_mock_users():
    """Get mock users from debug endpoint"""
    print("\n🔹 DEBUG: Get Mock Users")
    
    url = f"{BASE_URL}/api/debug/mock-users"
    response = requests.get(url)
    print_response(response, "Mock Users")


def run_all_tests():
    """Run all tests"""
    print("\n" + "🚀"*30)
    print("  FORGOT PASSWORD API TEST SUITE")
    print("🚀"*30)
    
    try:
        # Check if server is running
        response = requests.get(BASE_URL)
        print("\n✅ Server is running")
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Server is not running!")
        print("Please start the server first:")
        print("  python forgot_password_api.py")
        return
    
    # Show mock users
    get_mock_users()
    
    # Test 1: Request OTP with invalid email
    test_request_otp_invalid_email()
    
    # Test 2: Request OTP with valid email
    success = test_request_otp()
    if not success:
        print("\n❌ Failed to request OTP. Stopping tests.")
        return
    
    # Wait a moment for email to be sent
    print("\n⏳ Waiting for OTP to be sent...")
    time.sleep(2)
    
    # Get the OTP from debug endpoint
    otp = get_active_otps()
    if not otp:
        print("\n❌ Could not retrieve OTP. Check if email was sent successfully.")
        print("📧 Check your email for the OTP and use it manually in Test 3")
        return
    
    print(f"\n✅ Retrieved OTP: {otp}")
    
    # Test 3: Verify with wrong OTP
    test_verify_wrong_otp()
    
    # Test 4: Verify with correct OTP
    test_verify_otp(otp)
    
    print("\n" + "✅"*30)
    print("  ALL TESTS COMPLETED")
    print("✅"*30)


def manual_test():
    """Manual testing mode"""
    print("\n" + "🔧"*30)
    print("  MANUAL TEST MODE")
    print("🔧"*30)
    
    while True:
        print("\nSelect an option:")
        print("1. Request OTP")
        print("2. Verify OTP")
        print("3. View Active OTPs (Debug)")
        print("4. View Mock Users (Debug)")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            email = input("Enter email: ").strip()
            url = f"{BASE_URL}/api/forgot-password/request-otp"
            response = requests.post(url, json={"email": email})
            print_response(response, "Request OTP")
            
        elif choice == "2":
            email = input("Enter email: ").strip()
            otp = input("Enter OTP: ").strip()
            new_password = input("Enter new password: ").strip()
            url = f"{BASE_URL}/api/forgot-password/verify-otp"
            response = requests.post(url, json={
                "email": email,
                "otp": otp,
                "new_password": new_password
            })
            print_response(response, "Verify OTP")
            
        elif choice == "3":
            get_active_otps()
            
        elif choice == "4":
            get_mock_users()
            
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    import sys
    
    print("\nForgot Password API Test Script")
    print("="*60)
    print("Mode:")
    print("1. Automated Test Suite")
    print("2. Manual Testing")
    
    mode = input("\nSelect mode (1 or 2): ").strip()
    
    if mode == "1":
        run_all_tests()
    elif mode == "2":
        manual_test()
    else:
        print("\n❌ Invalid mode selected")
