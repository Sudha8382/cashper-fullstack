"""
Quick Gmail Setup Verification Script
यह script check करता है कि Gmail configuration सही है या नहीं
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv("cashper_backend/.env")

def check_gmail_setup():
    """Check if Gmail is properly configured"""
    
    print("\n" + "="*60)
    print("📧 Gmail Configuration Checker")
    print("="*60 + "\n")
    
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")
    
    issues = []
    warnings = []
    
    # Check GMAIL_USER
    print("1️⃣ Checking GMAIL_USER...")
    if not gmail_user:
        issues.append("❌ GMAIL_USER is not set")
        print("   ❌ NOT SET")
    elif gmail_user == "your-email@gmail.com":
        issues.append("❌ GMAIL_USER still has placeholder value")
        print(f"   ❌ Placeholder value: {gmail_user}")
    elif "@gmail.com" not in gmail_user:
        warnings.append("⚠️  GMAIL_USER doesn't contain @gmail.com")
        print(f"   ⚠️  {gmail_user} (not a Gmail address?)")
    else:
        print(f"   ✅ {gmail_user}")
    
    # Check GMAIL_APP_PASSWORD
    print("\n2️⃣ Checking GMAIL_APP_PASSWORD...")
    if not gmail_password:
        issues.append("❌ GMAIL_APP_PASSWORD is not set")
        print("   ❌ NOT SET")
    elif gmail_password == "your-app-password-here":
        issues.append("❌ GMAIL_APP_PASSWORD still has placeholder value")
        print("   ❌ Placeholder value")
    elif len(gmail_password) < 16:
        warnings.append("⚠️  GMAIL_APP_PASSWORD seems too short (should be 16 chars)")
        print(f"   ⚠️  Length: {len(gmail_password)} (should be 16)")
    elif " " in gmail_password:
        warnings.append("⚠️  GMAIL_APP_PASSWORD contains spaces (remove them)")
        print("   ⚠️  Contains spaces (remove them)")
    else:
        print(f"   ✅ Set (length: {len(gmail_password)})")
    
    # Summary
    print("\n" + "="*60)
    print("📊 Summary")
    print("="*60 + "\n")
    
    if not issues and not warnings:
        print("✅ ALL CHECKS PASSED!")
        print("\n💡 Next Steps:")
        print("   1. Make sure backend server is running")
        print("   2. Test forgot password API")
        print("   3. Check email inbox (and spam folder)")
        return True
    
    if issues:
        print("🚨 CRITICAL ISSUES FOUND:\n")
        for issue in issues:
            print(f"   {issue}")
        
        print("\n📖 TO FIX:")
        print("   1. Open: cashper_backend\\.env")
        print("   2. Update GMAIL_USER and GMAIL_APP_PASSWORD")
        print("   3. See: GMAIL_SETUP_HINDI.md for detailed guide")
        print("   4. Restart backend server after updating")
    
    if warnings:
        print("\n⚠️  WARNINGS:\n")
        for warning in warnings:
            print(f"   {warning}")
    
    print("\n" + "="*60)
    return False


if __name__ == "__main__":
    try:
        success = check_gmail_setup()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
