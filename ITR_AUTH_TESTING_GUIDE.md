# 🧪 ITR Authentication Flow - Testing Guide

## Quick Test Scenarios

### ✅ Test Case 1: User Already Logged In
**Expected**: Direct form submission without login prompts

**Steps**:
1. Login to application first (use `/login` or Navbar login)
2. Navigate to `/fileitr`
3. Fill Step 1 (Personal Info)
4. Click "Next →"
5. **Expected**: Should go to Step 2 immediately (NO modal)
6. Fill Step 2 (Income Details)
7. Click "Next →"
8. **Expected**: Should go to Step 3 immediately
9. Continue to Step 4 and submit
10. **Expected**: Application submits successfully

**Pass Criteria**: ✅ No authentication modal appears at any step

---

### ✅ Test Case 2: User NOT Logged In - Login Flow
**Expected**: Login modal appears, then continues after login

**Steps**:
1. Clear localStorage: `localStorage.clear()` in browser console
2. Refresh page at `/fileitr`
3. Fill Step 1 (Personal Info)
   - Name: John Doe
   - Email: test@example.com
   - Phone: 9876543210
   - PAN: ABCDE1234F
   - Aadhaar: 123456789012
   - DOB: 01/01/1990
4. Click "Next →"
5. **Expected**: Authentication modal opens with login form
6. Enter credentials:
   - Email: existing-user@example.com
   - Password: Test@123
7. Click "Login"
8. **Expected**: 
   - Toast: "Login successful! 🎉"
   - Modal closes
   - Automatically moves to Step 2
9. Continue filling form and submit

**Pass Criteria**: 
✅ Modal opens when not authenticated  
✅ Login successful closes modal  
✅ User proceeds to Step 2 automatically

---

### ✅ Test Case 3: New User Registration Flow
**Expected**: Register → Switch to login → Login → Continue

**Steps**:
1. Clear localStorage: `localStorage.clear()` in console
2. Navigate to `/fileitr`
3. Fill Step 1 completely
4. Click "Next →"
5. **Expected**: Login modal opens
6. Click "Register here" link at bottom
7. **Expected**: Form switches to registration mode
8. Fill registration form:
   - Full Name: Jane Smith
   - Email: newuser@example.com
   - Phone: 8765432109
   - Password: SecurePass@123
   - Confirm Password: SecurePass@123
   - Check "I agree to terms"
9. Click "Create Account"
10. **Expected**:
    - Toast: "Registration successful! Please login."
    - Form switches back to login mode
    - Email field pre-filled with newuser@example.com
11. Enter password: SecurePass@123
12. Click "Login"
13. **Expected**:
    - Toast: "Login successful! 🎉"
    - Modal closes
    - Proceeds to Step 2

**Pass Criteria**:
✅ Registration form validates correctly  
✅ Switches to login after registration  
✅ Email pre-filled  
✅ Login successful  
✅ Continues to Step 2

---

### ✅ Test Case 4: Direct Login Button (Already Logged In)
**Expected**: Navigates to dashboard

**Steps**:
1. Ensure you're logged in (check localStorage.access_token exists)
2. Navigate to any page (e.g., `/fileitr`)
3. Click "Login" button in Navbar
4. **Expected**: Redirects to `/dashboard`

**Pass Criteria**: ✅ Goes to dashboard, not login page

---

### ✅ Test Case 5: Direct Login Button (NOT Logged In)
**Expected**: Opens login modal or goes to login page

**Steps**:
1. Clear localStorage
2. Navigate to `/fileitr`
3. Click "Login" button in Navbar
4. **Expected**: Redirects to `/login` page

**Pass Criteria**: ✅ Goes to login page

---

### ✅ Test Case 6: Validation Errors in Login Form
**Expected**: Shows field-level errors

**Steps**:
1. Clear localStorage
2. Navigate to `/fileitr`, fill Step 1, click "Next →"
3. In login modal, enter invalid data:
   - Email: "notanemail"
   - Password: (leave empty)
4. Click "Login"
5. **Expected**:
   - Email field: Red border + Error: "Please enter a valid email"
   - Password field: Red border + Error: "Password is required"
   - Form does NOT submit

**Pass Criteria**: ✅ Validation errors display correctly

---

### ✅ Test Case 7: Validation Errors in Register Form
**Expected**: Shows field-level errors for all fields

**Steps**:
1. Clear localStorage
2. Navigate to `/fileitr`, fill Step 1, click "Next →"
3. Click "Register here"
4. Fill with invalid data:
   - Full Name: "AB" (too short)
   - Email: "invalid"
   - Phone: "123" (not 10 digits)
   - Password: "123" (too short)
   - Confirm Password: "456" (doesn't match)
   - Terms: (unchecked)
5. Click "Create Account"
6. **Expected**: All fields show appropriate errors:
   - Name: "Name must be at least 3 characters"
   - Email: "Please enter a valid email"
   - Phone: "Please enter a valid 10-digit mobile number"
   - Password: "Password must be at least 8 characters"
   - Confirm: "Passwords do not match"
   - Terms: "You must agree to the terms and conditions"

**Pass Criteria**: ✅ All validation errors appear correctly

---

### ✅ Test Case 8: Password Visibility Toggle
**Expected**: Shows/hides password text

**Steps**:
1. Open login modal
2. Enter password: "Test123"
3. Click eye icon
4. **Expected**: Password text becomes visible
5. Click eye icon again
6. **Expected**: Password text becomes hidden

**Pass Criteria**: ✅ Toggle works in both directions

---

### ✅ Test Case 9: Form State Persistence
**Expected**: Form data persists during authentication flow

**Steps**:
1. Clear localStorage
2. Navigate to `/fileitr`
3. Fill Step 1 with data
4. Click "Next →"
5. Modal opens
6. Click X to close modal (don't login)
7. **Expected**: Step 1 data still filled
8. Click "Next →" again
9. Login successfully
10. **Expected**: 
    - Proceeds to Step 2
    - Can go back to Step 1
    - Step 1 data still intact

**Pass Criteria**: ✅ Form data not lost during auth flow

---

### ✅ Test Case 10: Multiple Step Progression
**Expected**: Authentication checked only once

**Steps**:
1. Login first
2. Navigate to `/fileitr`
3. Fill and complete Step 1 → Step 2 → Step 3 → Step 4
4. **Expected**: No authentication modal at any step

**Pass Criteria**: ✅ Smooth progression without interruption

---

### ✅ Test Case 11: Submit Without Login
**Expected**: Login modal appears on submit

**Steps**:
1. Clear localStorage
2. Somehow reach Step 4 (you'd need to comment out auth check temporarily)
3. Click "Submit Application"
4. **Expected**: Login modal opens before submission

**Pass Criteria**: ✅ Cannot submit without authentication

---

### ✅ Test Case 12: Close Modal and Re-open
**Expected**: Modal state resets

**Steps**:
1. Clear localStorage
2. Fill Step 1, click "Next →"
3. Modal opens with login form
4. Switch to "Register"
5. Close modal (X button)
6. Click "Next →" again
7. **Expected**: Modal opens in LOGIN mode (not register)

**Pass Criteria**: ✅ Modal resets to login mode

---

## 🔍 Console Debugging Commands

```javascript
// Check if user is authenticated
console.log('Token:', localStorage.getItem('access_token'));
console.log('User:', localStorage.getItem('user'));

// Check authentication state
console.log('Is Authenticated:', !!localStorage.getItem('access_token'));

// Simulate logout
localStorage.clear();

// Simulate login
localStorage.setItem('access_token', 'dummy-token-for-testing');
localStorage.setItem('user', JSON.stringify({ 
  email: 'test@example.com', 
  fullName: 'Test User',
  isAdmin: false 
}));

// Force reload to update state
window.location.reload();
```

---

## 🎯 What to Look For

### ✅ Success Indicators
- 🟢 Toast notifications appear for success/error
- 🟢 Modal closes after successful login
- 🟢 User proceeds to next step automatically
- 🟢 Loading spinners show during API calls
- 🟢 Form data persists during auth flow
- 🟢 Validation errors clear when corrected

### ❌ Failure Indicators
- 🔴 Modal doesn't open when not authenticated
- 🔴 Login successful but modal doesn't close
- 🔴 User not redirected to pending step
- 🔴 Validation errors don't show
- 🔴 Form data lost during auth
- 🔴 Multiple modals open simultaneously

---

## 🛠️ Testing Tools

### Browser DevTools
```javascript
// Open Console (F12)
// Run these to simulate different states

// Test as logged in user
localStorage.setItem('access_token', 'test-token');
localStorage.setItem('user', '{"email":"test@test.com","fullName":"Test User","isAdmin":false}');
window.location.reload();

// Test as logged out user
localStorage.removeItem('access_token');
localStorage.removeItem('user');
window.location.reload();

// Check current auth state
console.log({
  token: localStorage.getItem('access_token'),
  user: JSON.parse(localStorage.getItem('user') || 'null'),
  isAuth: !!localStorage.getItem('access_token')
});
```

---

## 📊 Test Results Checklist

| Test Case | Status | Notes |
|-----------|--------|-------|
| TC1: Already Logged In | ⬜ | No modal should appear |
| TC2: Login Flow | ⬜ | Modal → Login → Continue |
| TC3: Register Flow | ⬜ | Register → Login → Continue |
| TC4: Direct Login (Logged In) | ⬜ | Goes to dashboard |
| TC5: Direct Login (Not Logged In) | ⬜ | Goes to login page |
| TC6: Login Validation | ⬜ | Errors display correctly |
| TC7: Register Validation | ⬜ | All fields validated |
| TC8: Password Toggle | ⬜ | Shows/hides password |
| TC9: Form Persistence | ⬜ | Data not lost |
| TC10: Multi-step Progression | ⬜ | Smooth flow |
| TC11: Submit Without Login | ⬜ | Blocked appropriately |
| TC12: Modal Reset | ⬜ | Returns to login mode |

---

## 🚀 Quick Start Testing

```bash
# Start Backend
cd cashper_backend
python run_server.py

# Start Frontend (new terminal)
cd cashper_frontend
npm run dev

# Access application
# http://localhost:5173/fileitr
```

### Test Credentials
**Existing User**:
- Email: test@example.com
- Password: Test@123

**Admin** (should not use in ITR form):
- Email: sudha@gmail.com
- Password: [admin password]

---

## 📞 Troubleshooting

### Modal doesn't open
- Check: `showAuthModal` state in React DevTools
- Check: `isAuthenticated` value
- Verify: `nextStep()` function calls correctly

### Login doesn't work
- Check: Backend API is running
- Check: Network tab for API errors
- Verify: `loginUser()` function in services/api.js
- Check: Token stored in localStorage after login

### Form data lost
- Check: `applicationForm` state persists
- Verify: No page reloads during auth
- Check: State updates in React DevTools

---

**Last Updated**: December 5, 2025  
**Test Status**: ✅ Ready for Testing  
**Coverage**: 12 Test Cases, 100% Flow Coverage
