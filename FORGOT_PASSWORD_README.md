# Forgot Password API - Complete Implementation Guide

## 📋 Overview

This is a complete FastAPI implementation of a "Forgot Password" feature using Gmail and OTP (One-Time Password). The system sends a 6-digit OTP to users' email addresses for password reset verification.

## 🚀 Features

- ✅ Email validation and verification
- ✅ 6-digit OTP generation
- ✅ Async email sending via Gmail (aiosmtplib)
- ✅ OTP expiry mechanism (10 minutes)
- ✅ Password strength validation
- ✅ Beautiful HTML email templates
- ✅ Mock database (ready for real DB integration)
- ✅ Comprehensive error handling
- ✅ Pydantic models for validation
- ✅ Debug endpoints for testing

## 📦 Files Included

1. **forgot_password_api.py** - Main FastAPI application
2. **.env.forgot_password_example** - Environment variables template
3. **requirements_forgot_password.txt** - Python dependencies
4. **test_forgot_password_api.py** - Test script
5. **FORGOT_PASSWORD_README.md** - This documentation

## 🛠️ Setup Instructions

### Step 1: Install Dependencies

```bash
pip install -r requirements_forgot_password.txt
```

### Step 2: Configure Gmail Credentials

1. **Enable 2-Step Verification** on your Gmail account:
   - Go to: https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the 16-character password

3. **Create `.env` file**:
   ```bash
   # Copy the example file
   cp .env.forgot_password_example .env
   ```

4. **Edit `.env` file**:
   ```env
   GMAIL_USER=your-email@gmail.com
   GMAIL_APP_PASSWORD=your-16-char-app-password
   ```

### Step 3: Run the Application

```bash
python forgot_password_api.py
```

The server will start at: http://localhost:8000

### Step 4: Test the API

Run the test script:
```bash
python test_forgot_password_api.py
```

Or test manually using the API documentation at: http://localhost:8000/docs

## 📡 API Endpoints

### 1. Request OTP

**Endpoint:** `POST /api/forgot-password/request-otp`

**Request Body:**
```json
{
  "email": "user@example.com"
}
```

**Response:**
```json
{
  "success": true,
  "message": "OTP sent successfully to user@example.com. It will expire in 10 minutes.",
  "data": {
    "email": "user@example.com",
    "otp_expiry_minutes": 10
  }
}
```

### 2. Verify OTP and Reset Password

**Endpoint:** `POST /api/forgot-password/verify-otp`

**Request Body:**
```json
{
  "email": "user@example.com",
  "otp": "123456",
  "new_password": "NewSecure123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Password reset successfully. You can now login with your new password.",
  "data": {
    "email": "user@example.com"
  }
}
```

### 3. Debug Endpoints (Remove in Production)

- `GET /api/debug/mock-users` - View all mock users
- `GET /api/debug/active-otps` - View active OTPs

## 🧪 Testing

### Mock Users Available

The system includes these test accounts:
- **user@example.com** - Test User
- **test@gmail.com** - Test Account

### Testing Flow

1. **Request OTP**:
   ```bash
   curl -X POST http://localhost:8000/api/forgot-password/request-otp \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com"}'
   ```

2. **Check email** for OTP (or use debug endpoint)

3. **Verify OTP**:
   ```bash
   curl -X POST http://localhost:8000/api/forgot-password/verify-otp \
     -H "Content-Type: application/json" \
     -d '{
       "email": "user@example.com",
       "otp": "123456",
       "new_password": "NewSecure123"
     }'
   ```

## 🔒 Security Features

### OTP Security
- ✅ 6-digit random numeric OTP
- ✅ 10-minute expiry
- ✅ One-time use (deleted after verification)
- ✅ Email-specific storage

### Password Validation
- ✅ Minimum 8 characters
- ✅ Must contain at least one letter
- ✅ Must contain at least one digit
- ✅ Passwords are hashed (SHA-256 for demo, use bcrypt in production)

### Email Validation
- ✅ Valid email format (via Pydantic EmailStr)
- ✅ Email existence check
- ✅ Case-insensitive email handling

## 🔄 Integration with Real Database

### Current Implementation (Mock)
```python
mock_users_db = {
    "user@example.com": {
        "email": "user@example.com",
        "password": "hashed_password",
        "name": "Test User"
    }
}
```

### MongoDB Integration Example

Replace the helper functions with:

```python
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["your_database"]
users_collection = db["users"]

async def check_email_exists(email: str) -> bool:
    """Check if email exists in MongoDB"""
    user = await users_collection.find_one({"email": email.lower()})
    return user is not None

async def update_user_password(email: str, new_password: str) -> bool:
    """Update password in MongoDB"""
    result = await users_collection.update_one(
        {"email": email.lower()},
        {"$set": {"password": hash_password(new_password)}}
    )
    if email in otp_storage:
        del otp_storage[email]
    return result.modified_count > 0
```

### SQL Database Integration Example

```python
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

async def check_email_exists(email: str, db: AsyncSession) -> bool:
    """Check if email exists in SQL database"""
    result = await db.execute(
        select(User).where(User.email == email.lower())
    )
    return result.scalar_one_or_none() is not None

async def update_user_password(email: str, new_password: str, db: AsyncSession) -> bool:
    """Update password in SQL database"""
    await db.execute(
        update(User)
        .where(User.email == email.lower())
        .values(password=hash_password(new_password))
    )
    await db.commit()
    if email in otp_storage:
        del otp_storage[email]
    return True
```

## 🎨 Email Template Customization

The system sends beautiful HTML emails. Customize the template in the `send_email_otp()` function:

```python
html_body = f"""
<html>
    <!-- Your custom HTML template -->
    <h1 style="color: #007bff;">{otp}</h1>
</html>
"""
```

## ⚙️ Configuration Options

Edit these constants in `forgot_password_api.py`:

```python
OTP_EXPIRY_MINUTES = 10  # OTP expiry time
# Change to 5, 15, or any value you prefer
```

### Change OTP Length
```python
def generate_otp(length: int = 6) -> str:
    # Change length parameter to 4, 8, etc.
```

## 🐛 Troubleshooting

### Issue: Email not sending

**Solution:**
1. Verify Gmail credentials in `.env`
2. Ensure 2-Step Verification is enabled
3. Use App Password, not regular password
4. Check if Gmail allows less secure app access

### Issue: OTP expired

**Solution:**
- Increase `OTP_EXPIRY_MINUTES`
- Request a new OTP

### Issue: Invalid OTP

**Solution:**
- Use the debug endpoint to view the OTP: `GET /api/debug/active-otps`
- Ensure you're using the latest OTP (old ones expire)

## 📈 Production Recommendations

### 1. Replace SHA-256 with bcrypt
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
```

### 2. Use Redis for OTP Storage
```python
import redis.asyncio as redis

redis_client = redis.from_url("redis://localhost")

async def store_otp(email: str, otp: str):
    await redis_client.setex(
        f"otp:{email}",
        OTP_EXPIRY_MINUTES * 60,
        otp
    )
```

### 3. Add Rate Limiting
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/api/forgot-password/request-otp")
@limiter.limit("3/hour")  # 3 requests per hour per IP
async def request_otp(request: Request, ...):
    ...
```

### 4. Add Logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"OTP requested for {email}")
logger.error(f"Failed to send email: {str(e)}")
```

### 5. Remove Debug Endpoints
Delete these endpoints before deploying to production:
- `/api/debug/mock-users`
- `/api/debug/active-otps`

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [aiosmtplib Documentation](https://aiosmtplib.readthedocs.io/)
- [Gmail App Passwords](https://support.google.com/accounts/answer/185833)

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the test script output
3. Check server logs for detailed error messages

## 📝 License

This code is provided as-is for educational and commercial use.

---

**Happy Coding! 🚀**
