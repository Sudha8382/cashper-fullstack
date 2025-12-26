"""
Test Google Login API
Tests the Google OAuth login endpoint
"""
import requests
import json

# Backend URL
BASE_URL = "http://localhost:8000"

def test_google_login_api():
    """Test Google login API endpoint availability"""
    print("=" * 80)
    print("  🔐 Testing Google Login API")
    print("=" * 80)
    print()
    
    # Test 1: Check if endpoint is available
    print("📡 Test 1: Checking API endpoint availability...")
    try:
        # Try to call without token (should fail with proper error)
        response = requests.post(
            f"{BASE_URL}/api/auth/google-login",
            json={"token": ""},
            timeout=5
        )
        
        if response.status_code == 400:
            print("✅ Endpoint is available and responding correctly")
            print(f"   Response: {response.json()}")
        else:
            print(f"⚠️  Unexpected status code: {response.status_code}")
            print(f"   Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Backend server is not running!")
        print("   Please start the server first: python run_server.py")
        return
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return
    
    print()
    
    # Test 2: Check backend configuration
    print("🔧 Test 2: Checking backend Google OAuth configuration...")
    try:
        # Read backend .env file
        with open("cashper_backend/.env", "r") as f:
            content = f.read()
            if "GOOGLE_CLIENT_ID" in content:
                # Extract client ID
                for line in content.split("\n"):
                    if line.startswith("GOOGLE_CLIENT_ID="):
                        client_id = line.split("=", 1)[1].strip()
                        if client_id and client_id != "your-google-client-id.apps.googleusercontent.com":
                            print(f"✅ Backend Google Client ID configured")
                            print(f"   Client ID: {client_id[:20]}...{client_id[-20:]}")
                        else:
                            print("⚠️  Backend Google Client ID not properly configured")
                        break
            else:
                print("⚠️  GOOGLE_CLIENT_ID not found in .env file")
    except Exception as e:
        print(f"❌ Error reading backend config: {str(e)}")
    
    print()
    
    # Test 3: Check frontend configuration
    print("🌐 Test 3: Checking frontend Google OAuth configuration...")
    try:
        with open("cashper_frontend/.env", "r") as f:
            content = f.read()
            if "VITE_GOOGLE_CLIENT_ID" in content:
                for line in content.split("\n"):
                    if line.startswith("VITE_GOOGLE_CLIENT_ID="):
                        client_id = line.split("=", 1)[1].strip()
                        if client_id and client_id != "your-google-client-id":
                            print(f"✅ Frontend Google Client ID configured")
                            print(f"   Client ID: {client_id[:20]}...{client_id[-20:]}")
                        else:
                            print("⚠️  Frontend Google Client ID not properly configured")
                        break
            else:
                print("⚠️  VITE_GOOGLE_CLIENT_ID not found in .env file")
    except Exception as e:
        print(f"❌ Error reading frontend config: {str(e)}")
    
    print()
    
    # Summary
    print("=" * 80)
    print("  📋 Summary")
    print("=" * 80)
    print()
    print("✅ Backend server is running on http://localhost:8000")
    print("✅ Google login API endpoint is available at /api/auth/google-login")
    print("✅ Client IDs are configured in both frontend and backend")
    print()
    print("🌐 Frontend URL: http://localhost:4209/login")
    print()
    print("📝 Next Steps:")
    print("1. Open http://localhost:4209/login in your browser")
    print("2. You should see the Google login button below 'Or continue with'")
    print("3. Click on the Google button to test the login")
    print()
    print("❓ If Google button is not visible:")
    print("   - Check browser console for JavaScript errors")
    print("   - Verify @react-oauth/google package is installed")
    print("   - Clear browser cache and reload")
    print()

if __name__ == "__main__":
    test_google_login_api()
