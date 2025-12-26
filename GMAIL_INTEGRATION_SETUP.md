# 🚀 Gmail OTP Integration - Complete Setup Guide

## ✅ Changes Made

### 1. Backend Changes
- ✅ Created `email_service.py` for Gmail integration
- ✅ Updated `auth_routes.py` to send real emails
- ✅ Added `aiosmtplib` to requirements.txt
- ✅ Added Gmail credentials to `.env` file

### 2. Working Endpoints
- `POST /api/auth/forgot-password` - Send OTP to email
- `POST /api/auth/reset-password` - Verify OTP and reset password
- `POST /api/auth/send-otp` - Send OTP to mobile (for future)
- `POST /api/auth/verify-otp` - Verify mobile OTP (for future)

---

## 📋 Setup Steps (Hindi + English)

### Step 1: Gmail App Password बनाओ

1. **2-Step Verification चालू करो:**
   - जाओ: https://myaccount.google.com/security
   - "2-Step Verification" खोजो और ON करो
   
2. **App Password बनाओ:**
   - जाओ: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Windows Computer"
   - "Generate" पर click करो
   - 16 character password copy करो (जैसे: `abcd efgh ijkl mnop`)

### Step 2: Backend .env File Update करो

```bash
# File खोलो: cashper_backend/.env
```

**Add these lines at the end:**
```env
# Gmail Configuration for OTP Emails
GMAIL_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```

**Example:**
```env
GMAIL_USER=john.doe@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```

⚠️ **Important:** 
- Spaces hata do password se
- Regular password **nahi** - App Password use karo
- Real email ID dalo

### Step 3: Install Dependencies

```bash
cd cashper_backend
pip install aiosmtplib
```

या सब dependencies एक साथ install करो:
```bash
pip install -r requirements.txt
```

### Step 4: Backend Restart करो

Terminal में:
```bash
# पहले python process को stop करो (Ctrl+C)
# फिर restart करो:
python run.py
```

या:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🧪 Testing

### Method 1: Frontend से Test करो

1. Frontend खोलो
2. Login page पर जाओ
3. "Forgot Password" click करो
4. अपनी email ID डालो (जो database में registered है)
5. "Send OTP" click करो
6. Email check करो - OTP आ जाएगा! 📧

### Method 2: Postman/Thunder Client से Test करो

**Request 1: Send OTP**
```http
POST http://127.0.0.1:8000/api/auth/forgot-password
Content-Type: application/json

{
  "email": "user@example.com"
}
```

**Response:**
```json
{
  "message": "OTP has been sent to your email",
  "success": true
}
```

**Request 2: Verify OTP & Reset Password**
```http
POST http://127.0.0.1:8000/api/auth/reset-password
Content-Type: application/json

{
  "email": "user@example.com",
  "otp": "123456",
  "newPassword": "NewPassword123"
}
```

### Method 3: Browser से Test करो

जाओ: http://127.0.0.1:8000/docs

1. `/api/auth/forgot-password` endpoint खोलो
2. "Try it out" click करो
3. Email डालो
4. "Execute" click करो
5. Email check करो!

---

## 📧 Email Template Preview

Users को यह email मिलेगा:

```
Subject: Password Reset OTP - Cashper

Hi [Name],

Your OTP for password reset is:

╔════════════════╗
║   123456       ║
╚════════════════╝

This OTP will expire in 5 minutes.

If you didn't request this, please ignore this email.

Best regards,
Cashper Team
```

---

## 🔧 Troubleshooting

### Problem 1: "Gmail credentials not configured"

**Solution:**
```bash
# Check .env file:
cat cashper_backend/.env

# Should have:
GMAIL_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password
```

### Problem 2: "Authentication failed"

**Solution:**
- Check if 2-Step Verification is ON
- Generate new App Password
- Copy password **without spaces**
- Update `.env` file
- Restart backend

### Problem 3: Email नहीं आ रहा

**Check:**
1. ✅ Spam folder check करो
2. ✅ Email ID sahi है (database में registered)
3. ✅ Backend console में error देखो
4. ✅ Internet connection check करो

**Console में यह देखना चाहिए:**
```
✅ Password reset OTP email sent successfully to user@example.com
```

### Problem 4: "ModuleNotFoundError: No module named 'aiosmtplib'"

**Solution:**
```bash
pip install aiosmtplib
```

---

## 🎯 Console Output Examples

### ✅ Success Case:
```
==================================================
PASSWORD RESET OTP for user@example.com: 123456
Valid for 5 minutes
==================================================

✅ OTP email sent to user@example.com
```

### ❌ Error Case (No credentials):
```
⚠️  Gmail credentials not configured in .env file
   Email will not be sent. Please configure GMAIL_USER and GMAIL_APP_PASSWORD
```

### ❌ Error Case (Wrong password):
```
❌ Gmail authentication failed: (535, b'5.7.8 Username and Password not accepted')
   Please check GMAIL_USER and GMAIL_APP_PASSWORD in .env file
```

---

## 📱 Frontend Integration

Frontend में कोई change की जरूरत नहीं! 

Frontend already इन endpoints को call कर रहा है:
- ✅ `/api/auth/forgot-password` - OTP भेजने के लिए
- ✅ `/api/auth/reset-password` - Password reset करने के लिए

---

## 🔒 Security Features

1. ✅ OTP 5 minutes में expire हो जाता है
2. ✅ OTP use करने के बाद delete हो जाता है
3. ✅ Password minimum 8 characters
4. ✅ Email existence नहीं reveal होता (security)

---

## 🚀 Quick Start Commands

```bash
# 1. Backend folder में जाओ
cd cashper_backend

# 2. Dependencies install करो
pip install -r requirements.txt

# 3. .env file edit करो
# Add: GMAIL_USER and GMAIL_APP_PASSWORD

# 4. Backend start करो
python run.py

# 5. Frontend start करो (दूसरे terminal में)
cd ../cashper_frontend
npm start

# 6. Test करो!
```

---

## ✅ Verification Checklist

- [ ] 2-Step Verification ON है
- [ ] Gmail App Password बनाया
- [ ] `.env` में credentials डाले (without spaces)
- [ ] `aiosmtplib` installed है
- [ ] Backend restart किया
- [ ] Console में success message दिख रहा है
- [ ] Email receive हो रहा है

---

## 📞 Support

अगर अभी भी problem है तो:

1. Backend console में errors check करो
2. `.env` file verify करो
3. Gmail App Password फिर से generate करो
4. Backend restart करो

**Gmail App Password Link:**
https://myaccount.google.com/apppasswords

---

**Happy Coding! 🎉**

Ab OTP Gmail पर जाएगा! 📧✅
