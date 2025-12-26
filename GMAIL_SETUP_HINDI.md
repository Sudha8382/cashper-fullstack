# 📧 Gmail OTP Setup Guide (हिंदी में)

## समस्या
Forgot Password API सफलतापूर्वक response दे रहा है लेकिन user को email नहीं जा रहा।

## कारण
`.env` file में Gmail credentials सही से configure नहीं हैं।

## ✅ समाधान (Step by Step)

### Step 1: Gmail App Password बनाएं

1. अपने Gmail account से login करें
2. इस link पर जाएं: https://myaccount.google.com/apppasswords
3. अगर 2-Step Verification enable नहीं है, तो पहले enable करें:
   - https://myaccount.google.com/signinoptions/two-step-verification
4. App Password page पर:
   - **App name** में लिखें: `Cashper Backend`
   - **Create** button पर click करें
5. एक 16-digit password generate होगा (जैसे: `abcd efgh ijkl mnop`)
6. इस password को **copy** करें (spaces हटा दें: `abcdefghijklmnop`)

### Step 2: .env File Update करें

1. File खोलें: `cashper_backend\.env`
2. ये lines ढूंढें:
   ```
   GMAIL_USER=your-email@gmail.com
   GMAIL_APP_PASSWORD=your-app-password-here
   ```
3. Update करें:
   ```
   GMAIL_USER=aapka-email@gmail.com
   GMAIL_APP_PASSWORD=aapka-16-digit-app-password
   ```
   
   **उदाहरण:**
   ```
   GMAIL_USER=john.doe@gmail.com
   GMAIL_APP_PASSWORD=abcdefghijklmnop
   ```

### Step 3: Backend Server Restart करें

1. Backend server को **बंद करें** (Ctrl+C)
2. **फिर से चालू करें**:
   ```bash
   cd cashper_backend
   uvicorn app.main:app --reload --port 8000
   ```

## 🧪 Test करें

### Option 1: Frontend से
1. Login page पर जाएं
2. "Forgot Password" पर click करें
3. अपना email enter करें
4. Submit करें
5. अपना email inbox check करें

### Option 2: Postman/Thunder Client से
```
POST http://localhost:8000/api/auth/forgot-password
Content-Type: application/json

{
    "email": "test@example.com"
}
```

## ✅ सफल होने पर आपको दिखेगा:

### Backend Console में:
```
==================================================
PASSWORD RESET OTP for test@example.com: 123456
Valid for 5 minutes
==================================================

============================================================
📧 Attempting to send OTP email to: test@example.com
============================================================
✓ Gmail credentials found
✓ Email message prepared
✓ Connecting to Gmail SMTP server...
✓ Connected to smtp.gmail.com:587
✓ TLS encryption enabled
✓ Authenticated with Gmail
✓ Email sent successfully
✓ Connection closed

============================================================
✅ PASSWORD RESET OTP EMAIL SENT SUCCESSFULLY!
   Recipient: test@example.com
   OTP: 123456
============================================================
```

### User को Email में:
- Subject: "Password Reset OTP - Cashper"
- Body में OTP code
- 5 minutes की validity

## 🚨 अगर Email नहीं आए तो:

1. **Spam folder check करें**
2. **Gmail settings check करें:**
   - Filters या forwarding rules
   - Blocked addresses
3. **Backend console check करें:**
   - क्या error messages हैं?
   - क्या OTP print हो रहा है?
4. **.env file verify करें:**
   - GMAIL_USER सही है?
   - GMAIL_APP_PASSWORD में spaces नहीं हैं?
   - Regular password की जगह App Password use किया?

## 📝 Important Notes

1. **Regular Gmail password काम नहीं करेगा** - App Password चाहिए
2. **2-Step Verification enable होना चाहिए**
3. **Spaces remove करें** App Password से
4. **Server restart जरूरी है** .env update के बाद
5. **Development के दौरान:** OTP console में भी print होता है

## 🔐 Security Tips

1. App Password को **कभी भी share न करें**
2. `.env` file को **git में commit न करें**
3. Production में **different email** use करें
4. **Regular password update** करते रहें

## Support

अगर फिर भी problem है तो:
1. Backend console logs share करें
2. .env file check करें (password hide करके)
3. Gmail account settings verify करें

---

✅ **Setup complete होने पर** forgot password feature पूरी तरह काम करेगा!
