# Retail Inquiry APIs - Quick Integration Guide

## 🚀 Quick Start

All retail service hero section inquiry forms now have working backend APIs!

## 📍 Base URL
```
http://127.0.0.1:8000/api/retail-inquiry
```

## 📝 All 10 Service Endpoints

### 1. File Your ITR
```
POST /api/retail-inquiry/file-itr
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 2. Revise Your ITR
```
POST /api/retail-inquiry/revise-itr
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 3. Reply to ITR Notice
```
POST /api/retail-inquiry/reply-itr-notice
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 4. Apply for Individual PAN
```
POST /api/retail-inquiry/apply-individual-pan
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 5. Apply for HUF PAN
```
POST /api/retail-inquiry/apply-huf-pan
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 6. Withdraw Your PF
```
POST /api/retail-inquiry/withdraw-pf
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 7. Update Aadhaar or PAN Details
```
POST /api/retail-inquiry/update-aadhaar-pan
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 8. Online Trading & Demat
```
POST /api/retail-inquiry/online-trading-demat
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 9. Bank Account Services
```
POST /api/retail-inquiry/bank-account
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "message": "string (optional)"
}
```

### 10. Financial Planning & Advisory
```
POST /api/retail-inquiry/financial-planning
```
```json
{
  "name": "string",
  "email": "user@example.com",
  "phone": "9876543210",
  "age": "string (optional)",
  "currentIncome": "string (optional)",
  "investmentGoal": "string (optional)"
}
```

## ✅ Success Response (All Endpoints)
```json
{
  "success": true,
  "message": "Thank you! We've received your inquiry...",
  "inquiryId": "INQ1766300619FE8578",
  "status": "new",
  "data": {
    "id": "69479c4b87c242d1301a16a8",
    "inquiryId": "INQ1766300619FE8578",
    "serviceType": "bank-account",
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "createdAt": "2025-12-21T12:33:39.123456"
  }
}
```

## ❌ Error Response
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

## 📋 Validation Rules

- **name**: 2-100 characters, required
- **email**: Valid email format, required
- **phone**: Exactly 10 digits, required
- **message**: Max 500 characters, optional
- **age**: String, optional (Financial Planning only)
- **currentIncome**: String, optional (Financial Planning only)
- **investmentGoal**: String, optional (Financial Planning only)

## 💻 Frontend Integration Example (React)

```javascript
// Example for File ITR Inquiry
const handleHeroFormSubmit = async (e) => {
  e.preventDefault();
  setIsSubmittingHero(true);

  try {
    const response = await fetch('http://127.0.0.1:8000/api/retail-inquiry/file-itr', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: heroFormData.name,
        email: heroFormData.email,
        phone: heroFormData.phone,
        message: heroFormData.message
      })
    });

    const result = await response.json();

    if (response.ok && result.success) {
      toast.success(result.message);
      // Reset form
      setHeroFormData({ name: '', email: '', phone: '', message: '' });
    } else {
      toast.error('Failed to submit inquiry. Please try again.');
    }
  } catch (error) {
    console.error('Error submitting inquiry:', error);
    toast.error('Something went wrong. Please try again.');
  } finally {
    setIsSubmittingHero(false);
  }
};
```

## 🔧 Admin Endpoints

### Get All Inquiries
```
GET /api/retail-inquiry/admin/inquiries?service_type={type}&status={status}
```

### Get Single Inquiry
```
GET /api/retail-inquiry/admin/inquiries/{inquiry_id}
```

### Update Inquiry Status
```
PUT /api/retail-inquiry/admin/inquiries/{inquiry_id}/status
```
```json
{
  "status": "contacted" // new, contacted, in-progress, converted, closed
}
```

### Get Statistics
```
GET /api/retail-inquiry/admin/statistics
```

### Delete Inquiry
```
DELETE /api/retail-inquiry/admin/inquiries/{inquiry_id}
```

## 🎯 Testing Commands

```bash
# Run comprehensive test (all 10 services)
python test_all_10_services.py

# Run quick test (sample services)
python quick_test_retail_inquiry.py
```

## 📊 Test Results

```
✅ All 10 Endpoints: PASSING
✅ Total Inquiries Created: 18
✅ Admin Endpoints: WORKING
✅ Statistics API: WORKING
✅ Database: MONGODB CONNECTED
```

## 🔗 API Documentation

Interactive documentation available at:
```
http://127.0.0.1:8000/docs
```

## 📝 Status Workflow

```
new → contacted → in-progress → converted/closed
```

- **new**: Just submitted by user
- **contacted**: Team has reached out to the user
- **in-progress**: Inquiry is being processed
- **converted**: Converted to full application
- **closed**: Inquiry closed without conversion

## ⚡ Quick Copy-Paste for Each Service

### File ITR
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/file-itr', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Revise ITR
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/revise-itr', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Reply ITR Notice
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/reply-itr-notice', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Individual PAN
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/apply-individual-pan', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### HUF PAN
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/apply-huf-pan', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Withdraw PF
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/withdraw-pf', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Update Aadhaar/PAN
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/update-aadhaar-pan', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Trading & Demat
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/online-trading-demat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Bank Account
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/bank-account', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, message })
})
```

### Financial Planning
```javascript
fetch('http://127.0.0.1:8000/api/retail-inquiry/financial-planning', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, email, phone, age, currentIncome, investmentGoal })
})
```

---

✅ **All APIs are live and tested!**
🎉 **10/10 services working perfectly!**
📚 **Complete documentation at /docs**
