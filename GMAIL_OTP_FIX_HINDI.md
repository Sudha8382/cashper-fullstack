# 📧 Gmail OTP Fix - Quick Setup Guide (Hindi + English)

## समस्या (Problem)
Gmail पर OTP नहीं जा रहा है / OTP not going to Gmail

## समाधान (Solution)

### Step 1: Gmail App Password बनाएं (Create Gmail App Password)

1. **2-Step Verification चालू करें:**
   - जाएं: https://myaccount.google.com/security
   - "2-Step Verification" खोजें और ON करें
   
2. **App Password बनाएं:**
   - जाएं: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Windows Computer" या "Other"
   - "Generate" पर क्लिक करें
   - 16 अक्षर का password मिलेगा (जैसे: abcd efgh ijkl mnop)
   - इसे कॉपी करें

### Step 2: .env File में Credentials डालें (Add Credentials)

1. `.env` file खोलें (project folder में)
2. अपनी Gmail ID और App Password डालें:

```env
GMAIL_USER=aapki-email@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```

**ध्यान दें:**
- ⚠️ Regular Gmail password **नहीं** डालें
- ✅ 16 character App Password डालें (बिना spaces के)
- ✅ असली email ID डालें

**उदाहरण:**
```env
GMAIL_USER=john.doe@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```

### Step 3: Setup Verify करें (Verify Setup)

Terminal में चलाएं:
```bash
python verify_gmail_setup.py
```

यह script check करेगा:
- ✅ Credentials सही हैं या नहीं
- ✅ Gmail connection काम कर रहा है या नहीं
- ✅ Test email भेज सकता है या नहीं

### Step 4: API Start करें (Start API)

```bash
python forgot_password_api.py
```

## 🧪 Testing

### Option 1: Test Script चलाएं
```bash
python test_forgot_password_api.py
```

### Option 2: API Documentation में Test करें
1. Browser में खोलें: http://localhost:8000/docs
2. "POST /api/forgot-password/request-otp" select करें
3. "Try it out" पर क्लिक करें
4. Email डालें और "Execute" करें
5. Email check करें - OTP आ गया होगा!

## 🔧 Common Issues / आम समस्याएं

### 1. "Authentication failed"
**कारण:** Wrong App Password या 2-Step Verification OFF है

**समाधान:**
- 2-Step Verification ON करें
- नया App Password बनाएं
- `.env` में सही password डालें (बिना spaces)

### 2. "Gmail credentials not configured"
**कारण:** `.env` file में credentials नहीं हैं

**समाधान:**
- `.env` file खोलें
- `GMAIL_USER` और `GMAIL_APP_PASSWORD` डालें
- File save करें
- API restart करें

### 3. "Failed to send email"
**कारण:** Internet connection या Gmail server issue

**समाधान:**
- Internet connection check करें
- Firewall check करें (port 587 open होना चाहिए)
- Antivirus temporarily disable करें

### 4. Email नहीं आ रहा (Email not received)
**Check करें:**
- ✅ Spam folder में देखें
- ✅ Email ID सही है या नहीं
- ✅ `verify_gmail_setup.py` चलाकर test email भेजें

## 📝 Quick Commands

```bash
# 1. Dependencies install करें
pip install -r requirements_forgot_password.txt

# 2. Gmail setup verify करें
python verify_gmail_setup.py

# 3. API start करें
python forgot_password_api.py

# 4. Test करें
python test_forgot_password_api.py
```

## 🎯 Mock Users for Testing

API में ये test users already हैं:
- **user@example.com** - Test User
- **test@gmail.com** - Test Account

## ✅ Success Indicators

जब सब कुछ सही है तो आपको दिखेगा:

```
✅ GMAIL_USER found: your-email@gmail.com
✅ GMAIL_APP_PASSWORD found: ****************
✅ Connected to Gmail SMTP server
✅ TLS encryption started
✅ Authentication successful
✅ Email sent successfully
```

## 🆘 Help

अगर फिर भी problem है तो:

1. `verify_gmail_setup.py` का output screenshot लें
2. `.env` file की setting check करें (password hide करके)
3. Error message पूरा पढ़ें

---

**📌 Important Notes:**
- ⚠️ कभी भी regular Gmail password use न करें
- ✅ हमेशा App Password use करें
- 🔒 `.env` file को git में commit न करें
- ✅ Production में अलग credentials use करें

**Happy Coding! 🚀**
