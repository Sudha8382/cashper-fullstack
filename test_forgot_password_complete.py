"""
Test Forgot Password API
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_forgot_password():
    """Test forgot password endpoint"""
    
    print("\n" + "="*60)
    print("🧪 TESTING FORGOT PASSWORD API")
    print("="*60 + "\n")
    
    # Test with your email
    test_email = "kumuyadav249@gmail.com"
    
    url = f"{BASE_URL}/api/auth/forgot-password"
    payload = {"email": test_email}
    
    print(f"📤 Sending request to: {url}")
    print(f"📧 Email: {test_email}\n")
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        
        print(f"📥 Response Status: {response.status_code}")
        print(f"📄 Response Body:")
        print(json.dumps(response.json(), indent=2))
        
        if response.status_code == 200:
            print("\n" + "="*60)
            print("✅ API CALL SUCCESSFUL!")
            print("="*60)
            print("\n📬 Please check your email:")
            print(f"   Email: {test_email}")
            print(f"   Subject: Password Reset OTP - Cashper")
            print(f"   ⚠️  Check SPAM folder if not in inbox")
            print("="*60 + "\n")
            return True
        else:
            print("\n" + "="*60)
            print("❌ API CALL FAILED!")
            print("="*60 + "\n")
            return False
            
    except requests.exceptions.ConnectionError:
        print("\n" + "="*60)
        print("❌ CONNECTION ERROR")
        print("="*60)
        print("Backend server is not running!")
        print("Please start: python -m uvicorn app.main:app --reload --port 8000")
        print("="*60 + "\n")
        return False
        
    except Exception as e:
        print("\n" + "="*60)
        print("❌ ERROR OCCURRED")
        print("="*60)
        print(f"Error: {str(e)}")
        print("="*60 + "\n")
        return False

if __name__ == "__main__":
    import sys
    result = test_forgot_password()
    sys.exit(0 if result else 1)
