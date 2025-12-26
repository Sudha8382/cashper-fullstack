# 🚨 URGENT: Forgot Password Email नहीं जा रहा - QUICK FIX

## समस्या
✅ API: `POST /api/auth/forgot-password` काम कर रहा है  
✅ Response: `success: true` आ रहा है  
❌ **BUT**: User को email में OTP नहीं मिल रहा

## कारण (Root Cause)
```
Gmail credentials configured नहीं हैं!
```

---

## ⚡ QUICK FIX (5 मिनट में)

### 1️⃣ Gmail App Password बनाएं

**Link**: https://myaccount.google.com/apppasswords

1. इस link पर जाएं
2. 2-Step Verification enable करें (अगर नहीं है)
3. "Create App Password" click करें
4. 16-digit password copy करें

### 2️⃣ .env File Update करें

**File**: `cashper_backend\.env`

```env
# इन 2 lines को update करें:
GMAIL_USER=aapka-email@gmail.com
GMAIL_APP_PASSWORD=aapka-16-digit-password
```

**Example:**
```env
GMAIL_USER=john.doe@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```

### 3️⃣ Backend Restart करें

```bash
# Backend terminal में:
# 1. Stop करें (Ctrl+C)
# 2. Start करें:
cd cashper_backend
uvicorn app.main:app --reload --port 8000
```

### 4️⃣ Verify करें

```bash
python verify_gmail_config.py
```

✅ अगर सब सही है तो यह दिखेगा:
```
✅ ALL CHECKS PASSED!
```

---

## 🧪 Test करें

### Frontend से:
1. Login page → Forgot Password
2. Email enter करें
3. Submit
4. Email check करें (inbox और spam)

### या API से:
```http
POST http://localhost:8000/api/auth/forgot-password
{
    "email": "test@example.com"
}
```

---

## ✅ सफल होने पर

### Console में दिखेगा:
```
============================================================
✅ PASSWORD RESET OTP EMAIL SENT SUCCESSFULLY!
   Recipient: user@example.com
   OTP: 123456
============================================================
```

### User को email में OTP मिलेगा

---

## 🚨 Still Not Working?

### Check करें:
1. ✅ GMAIL_USER सही email है?
2. ✅ GMAIL_APP_PASSWORD में spaces नहीं हैं?
3. ✅ Regular password नहीं, **App Password** use किया?
4. ✅ Backend restart किया?
5. ✅ Spam folder check किया?

### Console Logs देखें:
अगर कोई error है तो console में clear message दिखेगा।

---

## 📚 Detailed Guides

- **Hindi Setup Guide**: `GMAIL_SETUP_HINDI.md`
- **Complete Summary**: `FORGOT_PASSWORD_FIX_SUMMARY.md`
- **Verification Script**: `python verify_gmail_config.py`

---

## 🎯 Bottom Line

**यह 3 चीजें करें:**
1. Gmail App Password बनाएं
2. .env update करें
3. Backend restart करें

**✅ Done! Email जाना शुरू हो जाएगा!**
