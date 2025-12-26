"""
Quick Email Setup Script for Cashper Backend
This script helps you configure Gmail credentials for OTP emails
"""

import os
import re
from pathlib import Path

def main():
    print("\n" + "="*70)
    print("  📧 CASHPER - GMAIL OTP SETUP WIZARD")
    print("="*70)
    
    # Find .env file
    backend_path = Path(__file__).parent / "cashper_backend"
    env_file = backend_path / ".env"
    
    if not env_file.exists():
        print(f"\n❌ Error: .env file not found at {env_file}")
        print("   Please ensure cashper_backend/.env exists")
        return
    
    print(f"\n✓ Found .env file: {env_file}")
    
    # Read current .env content
    with open(env_file, 'r', encoding='utf-8') as f:
        env_content = f.read()
    
    # Check current values
    gmail_user_match = re.search(r'GMAIL_USER=(.+)', env_content)
    gmail_pass_match = re.search(r'GMAIL_APP_PASSWORD=(.+)', env_content)
    
    current_user = gmail_user_match.group(1).strip() if gmail_user_match else "NOT SET"
    current_pass = gmail_pass_match.group(1).strip() if gmail_pass_match else "NOT SET"
    
    print(f"\n📋 Current Configuration:")
    print(f"   GMAIL_USER: {current_user}")
    print(f"   GMAIL_APP_PASSWORD: {current_pass}")
    
    # Check if already configured
    if current_user not in ["your-email@gmail.com", "NOT SET"] and \
       current_pass not in ["your-app-password-here", "NOT SET"]:
        print("\n✅ Gmail credentials already configured!")
        change = input("\n   Do you want to change them? (yes/no): ").strip().lower()
        if change not in ['yes', 'y']:
            print("\n   Keeping existing configuration.")
            return
    
    # Instructions
    print("\n" + "="*70)
    print("  📖 SETUP INSTRUCTIONS")
    print("="*70)
    print("\nSTEP 1: Enable 2-Step Verification")
    print("   1. Go to: https://myaccount.google.com/security")
    print("   2. Find '2-Step Verification' and turn it ON")
    print("   3. Follow the prompts to verify your phone number")
    
    print("\nSTEP 2: Generate App Password")
    print("   1. Go to: https://myaccount.google.com/apppasswords")
    print("   2. Select app: 'Mail'")
    print("   3. Select device: 'Windows Computer'")
    print("   4. Click 'Generate'")
    print("   5. Copy the 16-character password (example: abcd efgh ijkl mnop)")
    print("   6. IMPORTANT: Remove all spaces from the password!")
    
    print("\n" + "="*70)
    input("\nPress Enter when you have completed the above steps...")
    
    # Get user input
    print("\n" + "="*70)
    print("  📝 ENTER YOUR GMAIL CREDENTIALS")
    print("="*70)
    
    while True:
        gmail_user = input("\n1️⃣ Enter your Gmail address: ").strip()
        if not gmail_user:
            print("   ❌ Email cannot be empty!")
            continue
        if "@gmail.com" not in gmail_user.lower():
            print("   ⚠️  Warning: This doesn't look like a Gmail address")
            confirm = input("   Continue anyway? (yes/no): ").strip().lower()
            if confirm not in ['yes', 'y']:
                continue
        break
    
    while True:
        gmail_password = input("\n2️⃣ Enter your Gmail App Password (16 characters, no spaces): ").strip()
        if not gmail_password:
            print("   ❌ Password cannot be empty!")
            continue
        
        # Remove spaces
        gmail_password = gmail_password.replace(" ", "")
        
        if len(gmail_password) < 16:
            print(f"   ⚠️  Warning: Password is only {len(gmail_password)} characters")
            print("   Gmail App Passwords are typically 16 characters")
            confirm = input("   Continue anyway? (yes/no): ").strip().lower()
            if confirm not in ['yes', 'y']:
                continue
        break
    
    # Update .env file
    print("\n" + "="*70)
    print("  💾 UPDATING .env FILE")
    print("="*70)
    
    # Replace or add Gmail credentials
    if gmail_user_match:
        env_content = re.sub(
            r'GMAIL_USER=.+',
            f'GMAIL_USER={gmail_user}',
            env_content
        )
    else:
        env_content += f"\nGMAIL_USER={gmail_user}"
    
    if gmail_pass_match:
        env_content = re.sub(
            r'GMAIL_APP_PASSWORD=.+',
            f'GMAIL_APP_PASSWORD={gmail_password}',
            env_content
        )
    else:
        env_content += f"\nGMAIL_APP_PASSWORD={gmail_password}"
    
    # Backup old file
    backup_file = env_file.with_suffix('.env.backup')
    with open(backup_file, 'w', encoding='utf-8') as f:
        with open(env_file, 'r', encoding='utf-8') as original:
            f.write(original.read())
    print(f"\n✓ Backup created: {backup_file}")
    
    # Write new file
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write(env_content)
    print(f"✓ Updated: {env_file}")
    
    # Verify
    print("\n" + "="*70)
    print("  ✅ CONFIGURATION UPDATED SUCCESSFULLY!")
    print("="*70)
    print(f"\n   GMAIL_USER: {gmail_user}")
    print(f"   GMAIL_APP_PASSWORD: {gmail_password[:4]}{'*' * (len(gmail_password) - 8)}{gmail_password[-4:]}")
    
    print("\n" + "="*70)
    print("  🚀 NEXT STEPS")
    print("="*70)
    print("\n1. Restart your backend server:")
    print("   • Stop current server (Ctrl+C if running)")
    print("   • Run: python run.py")
    
    print("\n2. Test the configuration:")
    print("   • Run: python test_email_config.py")
    print("   • Or test forgot password from frontend")
    
    print("\n3. If emails still not working:")
    print("   • Check spam folder")
    print("   • Verify 2-Step Verification is ON")
    print("   • Make sure you used App Password (not regular password)")
    print("   • Check backend console for error messages")
    
    print("\n" + "="*70)
    print("  🎉 SETUP COMPLETE!")
    print("="*70)
    print("\nYour forgot password OTP emails should now work!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
    except Exception as e:
        print(f"\n\n❌ Error: {str(e)}")
        print("Please update the .env file manually")
