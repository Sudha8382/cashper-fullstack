# Copilot Instructions for Cashper MERN Application

## Project Overview

**Cashper** is a comprehensive financial services MERN application providing personal loans, mutual funds, insurance products, and financial planning tools. The architecture uses:
- **Frontend**: React + Vite with TailwindCSS (responsive design)
- **Backend**: FastAPI (Python) with MongoDB 
- **Key Pattern**: Multi-step forms with validation and field-level error display

---

## Critical Architecture Patterns

### 1. Multi-Step Form Implementation (Key Pattern)
**Location**: `cashper_frontend/src/components/Mutual_funds.jsx` (lines 65-450+)

**Pattern**: Forms are split into 4-step workflows with specific validation rules per step:
- **Step 1**: Personal info (name, email, phone, age, PAN)
- **Step 2**: Investment details (type, amount, goal, risk profile)
- **Step 3**: Address & KYC info (city, state, pincode)
- **Step 4**: Document uploads (PAN, Aadhaar, photo, bank proof)

**Critical Implementation Detail - Error Display**:
- Errors are stored per field in `errors` state object
- Each input field checks `errors[fieldName]` and displays error **immediately below the field**
- Error styling: Red border (`border-red-500`) + Red text error message with warning icon
- Validation happens on: `onChange` (if field was touched), `onBlur`, and `nextStep()`

**Example Pattern**:
```jsx
// Input field with error indication
<input
  name="email"
  onChange={handleApplicationChange}
  onBlur={() => handleBlur('email')}
  className={`border-2 rounded-lg ${
    errors.email 
      ? 'border-red-500 focus:border-red-600' 
      : 'border-gray-200 focus:border-green-500'
  }`}
/>
{errors.email && (
  <p className="mt-1 text-sm text-red-600 flex items-center">
    <span className="mr-1">⚠</span> {errors.email}
  </p>
)}
```

### 2. Validation Strategy
**Files**: `Mutual_funds.jsx`, `Term_Insurance.jsx`, `Personal_loan.jsx`

- `validateField(name, value)` - Validates single field with specific rules
- `validateStep(step)` - Validates ALL fields for current step before proceeding
- Returns object with `fieldName: errorMessage` pairs
- Validations include: regex patterns (email, phone, PAN), length checks, range checks

### 3. Frontend-Backend Data Flow
**Frontend → Backend API → MongoDB**

**Key APIs**:
- `submitMutualFundApplication(form)` - POST to `/api/applications`
- `submitPersonalLoanApplication(form)` - Loan applications with document upload
- `submitContactInquiry(form)` - Quick contact forms

**Files**: `cashper_frontend/src/services/` - API service layer with error handling

---

## Project Structure

```
cashper_backend/
├── app/
│   ├── routes/           # API endpoints organized by feature
│   ├── database/         # MongoDB connection & models
│   ├── utils/            # Validation, file upload, JWT helpers
│   └── config.py         # Environment & database config
├── requirements.txt      # FastAPI, pymongo, bcrypt, etc.
├── run_server.py        # Entry point (uvicorn on port 8000)

cashper_frontend/
├── src/
│   ├── components/       # React components (forms, pages, reusable)
│   ├── services/         # API calls & business logic
│   ├── pages/            # Page-level components
│   ├── utils/            # Helpers, validators
│   └── main.jsx         # Vite entry point
```

---

## Critical Workflows

### Starting Backend
```powershell
# From cashper_backend/
python run_server.py
# Runs on http://127.0.0.1:8000
```

### Starting Frontend
```powershell
# From cashper_frontend/
npm run dev
# Runs on http://localhost:5173
```

### Testing APIs
Use existing test files in `cashper_backend/`:
- `test_personal_loan_application.py` - Full loan flow
- `test_mutual_fund_apis.py` - Fund application tests
- `test_contact_apis.py` - Contact form submission

---

## Form Validation Patterns to Follow

### When Adding New Multi-Step Forms

1. **State Structure**:
   - `currentStep` (1-4)
   - `formData` object with all fields
   - `errors` object for field errors (keyed by field name)
   - `touched` object to track which fields user has interacted with

2. **Validation Rules Template**:
   ```javascript
   const validateField = (name, value) => {
     let error = '';
     switch(name) {
       case 'fieldName':
         if (!value) error = 'Field is required';
         else if (/* condition */) error = 'Specific error message';
         break;
     }
     return error;
   };
   ```

3. **Error Display Pattern** (Always use this):
   - Show error message directly below input field
   - Use `className={errors.fieldName ? 'border-red-500' : 'border-gray-200'}`
   - Display error text with warning icon: `<span>⚠</span> {errors.fieldName}`

4. **Step Validation**:
   - Before `nextStep()`, validate all fields in current step
   - Prevent progression if `Object.keys(stepErrors).length > 0`
   - Show toast: `toast.error('Please fix all errors before proceeding')`

---

## Backend Integration Points

### MongoDB Collections
- **LoanApplications** - All loan applications (status: Pending, Under Review, Approved, Rejected, Disbursed)
- **MutualFundApplications** - Mutual fund investments
- **InsuranceInquiries** - Insurance product inquiries
- **ContactInquiries** - General contact form submissions

### Authentication
- JWT tokens in request headers: `Authorization: Bearer <token>`
- Routes protected via `verify_token()` middleware
- Password hashing with bcrypt

### File Uploads
- Documents stored in `uploads/` directory
- Allowed types: JPG, PNG, PDF (5MB max per file)
- Validation on both frontend and backend

---

## Key Components & Their Patterns

| Component | Purpose | Key Pattern |
|-----------|---------|-------------|
| `Mutual_funds.jsx` | Investment planning + multi-step app | 4-step form validation |
| `Personal_loan.jsx` | Loan application | Conditional SIP fields |
| `Term_Insurance.jsx` | Insurance inquiry | Hero form + App form |
| `LoanManagement.jsx` | Admin dashboard | Pagination, filtering, status updates |
| `Contactus.jsx` | Quick contact form | Single-step validation |

---

## Common Development Tasks

### Adding Field to Multi-Step Form
1. Add field to `applicationForm` state initial value
2. Add `validateField()` case for new field
3. Add to `validateStep()` for appropriate step
4. Create input with error display pattern (see Validation Patterns)
5. Handle onChange → `handleApplicationChange()`
6. Handle onBlur → `handleBlur(fieldName)`

### Debugging
- **Frontend errors**: Check browser DevTools console & Network tab
- **Backend errors**: Check `cashper_backend/server.log` or console output
- **Form submission issues**: Verify `errors` object is empty before submit

### API Testing
- Use Python test files in `cashper_backend/`
- Or use Postman/Thunder Client with Bearer token auth
- Base URL: `http://localhost:8000`

---

## Design System & Conventions

### Colors
- **Primary**: `green-600`, `green-700` (trust, financial)
- **Accent**: White backgrounds, green text
- **Errors**: `red-500`, `red-600`
- **Success**: `green-600` text with checkmark icon

### Responsive Breakpoints (TailwindCSS)
- `xs`: < 640px (mobile phone)
- `sm`: 640px+ (large phone)
- `md`: 768px+ (tablet)
- `lg`: 1024px+ (desktop)
- `xl`: 1280px+ (large desktop)

### Common Icon Patterns
Use `react-icons/fa` (FontAwesome):
- Fields: `FaUser`, `FaEnvelope`, `FaPhone`, `FaIdCard`, `FaHome`, `FaMapMarkerAlt`
- Validation: `FaCheckCircle` (success), Warning `⚠` (errors)
- Actions: `FaUpload` (file upload), `FaChevronDown/Up` (accordions)

---

## Data Flow Architecture

```
User Input Form
    ↓
handleApplicationChange() → Update formData + Clear error
    ↓
handleBlur() → Validate field + Set error (if any)
    ↓
User clicks "Next Step"
    ↓
validateStep() → Check all fields in step
    ↓
If errors: Show toast + Prevent navigation
If clean: setCurrentStep(+1)
    ↓
Last step: handleApplicationSubmit()
    ↓
submitMutualFundApplication(form) [API call]
    ↓
Backend validation + MongoDB insert
    ↓
Response: Success/Error toast + Reset form
```

---

## Important Notes for AI Agents

1. **Always include error display directly below input fields** - Don't create global error panels
2. **Validate on blur** - Gives user immediate feedback after they leave field
3. **Prevent step progression** - Never allow moving to next step with invalid data
4. **Use toast notifications** - For success/error confirmations
5. **Handle file uploads** - Check size (5MB), type (JPG/PNG/PDF) on frontend + backend
6. **Environment variables** - Check `.env` files for API URL, MongoDB URI, JWT secret
7. **Responsive design required** - All forms must work on mobile (xs), tablet (md), desktop (lg)

---

## Testing Checklist

When implementing forms:
- [ ] All required fields show error if empty on blur
- [ ] Field-specific validation rules work (email regex, phone length, etc.)
- [ ] Errors clear when user corrects field
- [ ] Cannot proceed to next step with errors
- [ ] Toast notification shows on validation error
- [ ] Form submits successfully when all fields valid
- [ ] Success screen shows after submission
- [ ] File uploads validate size & type
- [ ] Form resets after successful submission
- [ ] Mobile responsive (test on xs/sm breakpoints)

---

## Document & Reference Files

- **README_LOAN_DASHBOARD.md** - Complete implementation guide
- **DATA_FLOW_ARCHITECTURE.md** - System architecture diagrams
- **LOAN_DASHBOARD_GUIDE.md** - User guide with examples
- **requirements.txt** - Backend dependencies (FastAPI, pymongo, etc.)

