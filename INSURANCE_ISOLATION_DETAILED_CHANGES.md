# Insurance User Isolation - Detailed Changes Reference

## Summary of All Changes

### Motor Insurance Schema
**File:** `cashper_backend/app/database/schema/motor_insurance_schema.py`

**Change:** Added userId field to response model
```python
class MotorInsuranceApplicationResponse(BaseModel):
    id: str
    userId: Optional[str] = None  # ← ADDED THIS LINE
    applicationNumber: str
    # ... rest of fields
```

---

### Motor Insurance Routes - Import
**File:** `cashper_backend/app/routes/motor_insurance_routes.py`

**Change:** Added get_optional_user import
```python
from app.utils.auth import get_optional_user  # ← ADDED THIS IMPORT
from app.database.db import get_database  # ← ALREADY PRESENT
```

---

### Motor Insurance Routes - POST Endpoint
**File:** `cashper_backend/app/routes/motor_insurance_routes.py`

**Change 1:** Updated dependency from required to optional auth
```python
# BEFORE
current_user: dict = Depends(get_current_user)

# AFTER
current_user: Optional[dict] = Depends(get_optional_user)  # ← CHANGED
```

**Change 2:** Added userId to response object
```python
response = MotorInsuranceApplicationResponse(
    id=application_id,
    userId=str(current_user["_id"]) if current_user else None,  # ← ADDED THIS LINE
    applicationNumber=app_number,
    # ... rest of fields
)
```

---

### Motor Insurance Routes - GET Endpoint
**File:** `cashper_backend/app/routes/motor_insurance_routes.py`

**Change:** Completely rewrote endpoint to filter by userId
```python
# BEFORE
@router.get("/application/all", response_model=List[dict])
def get_all_applications(skip: int = 0, limit: int = 100):
    """Get all motor insurance applications (Admin endpoint)."""
    try:
        applications = motor_insurance_repository.get_all_applications(skip, limit)
        return applications
    except Exception as e:
        raise HTTPException(...)

# AFTER
@router.get("/application/all", response_model=List[dict])
def get_all_applications(skip: int = 0, limit: int = 100, current_user: Optional[dict] = Depends(get_optional_user)):
    """Get motor insurance applications filtered by user."""
    try:
        db = get_database()
        
        if not current_user:
            return []
        
        is_admin = current_user.get("is_admin", False)
        
        if is_admin:
            applications = motor_insurance_repository.get_all_applications(skip, limit)
        else:
            user_id = str(current_user["_id"])
            collection = db["motor_insurance_applications"]
            applications = list(collection.find({"userId": user_id}).skip(skip).limit(limit))
            for app in applications:
                app["_id"] = str(app["_id"])
                if "userId" in app:
                    app["userId"] = str(app["userId"])
        
        return applications
    except Exception as e:
        raise HTTPException(...)
```

---

### Term Insurance Schema
**File:** `cashper_backend/app/database/schema/term_insurance_schema.py`

**Change:** Added userId field to response model
```python
class TermInsuranceApplicationResponse(BaseModel):
    id: str
    userId: Optional[str] = None  # ← ADDED THIS LINE
    applicationNumber: str
    # ... rest of fields
```

---

### Term Insurance Routes - Imports
**File:** `cashper_backend/app/routes/term_insurance_routes.py`

**Change:** Added get_optional_user and get_database imports
```python
from app.utils.auth_middleware import get_current_user
from app.utils.auth import get_optional_user  # ← ADDED THIS IMPORT
from app.database.db import get_database  # ← ADDED THIS IMPORT
```

---

### Term Insurance Routes - POST Endpoint
**File:** `cashper_backend/app/routes/term_insurance_routes.py`

**Change 1:** Updated dependency from required to optional auth
```python
# BEFORE
current_user: dict = Depends(get_current_user)

# AFTER
current_user: Optional[dict] = Depends(get_optional_user)  # ← CHANGED
```

**Change 2:** Added userId to response object
```python
response = TermInsuranceApplicationResponse(
    id=application_id,
    userId=str(current_user["_id"]) if current_user else None,  # ← ADDED THIS LINE
    applicationNumber=app_number,
    # ... rest of fields
)
```

---

### Term Insurance Routes - GET Endpoint
**File:** `cashper_backend/app/routes/term_insurance_routes.py`

**Change:** Completely rewrote endpoint to filter by userId
```python
# BEFORE
@router.get("/application/all", response_model=List[dict])
def get_all_applications(skip: int = 0, limit: int = 100):
    """Get all term insurance applications (Admin endpoint)."""
    try:
        applications = term_insurance_repository.get_all_applications(skip, limit)
        return applications
    except Exception as e:
        raise HTTPException(...)

# AFTER
@router.get("/application/all", response_model=List[dict])
def get_all_applications(skip: int = 0, limit: int = 100, current_user: Optional[dict] = Depends(get_optional_user)):
    """Get term insurance applications filtered by user."""
    try:
        db = get_database()
        
        if not current_user:
            return []
        
        is_admin = current_user.get("is_admin", False)
        
        if is_admin:
            applications = term_insurance_repository.get_all_applications(skip, limit)
        else:
            user_id = str(current_user["_id"])
            collection = db["term_insurance_applications"]
            applications = list(collection.find({"userId": user_id}).skip(skip).limit(limit))
            for app in applications:
                app["_id"] = str(app["_id"])
                if "userId" in app:
                    app["userId"] = str(app["userId"])
        
        return applications
    except Exception as e:
        raise HTTPException(...)
```

---

## Notes on Health Insurance
Health Insurance was already updated in the previous session and has all the same changes as Motor and Term Insurance:
- ✓ Schema has userId field
- ✓ Routes imports get_optional_user and get_database
- ✓ POST endpoint uses optional auth and includes userId
- ✓ GET endpoint filters by userId with admin check

---

## Database Collections
All three collections persist the userId field:

1. **health_insurance_applications**
   - Document structure includes userId field
   - Already set by schema when application is created

2. **motor_insurance_applications**
   - Document structure includes userId field
   - Already set by schema when application is created

3. **term_insurance_applications**
   - Document structure includes userId field
   - Already set by schema when application is created

---

## Flow Diagram

```
User Login → get JWT token with user ID

Submit Insurance Application
    ↓
POST /*/application/submit (with Authorization header)
    ↓
get_optional_user extracts user ID from JWT
    ↓
userId added to request data
    ↓
Application saved to database with userId
    ↓
Response returns userId to frontend

Retrieve Insurance Applications
    ↓
GET /*/application/all (with Authorization header)
    ↓
get_optional_user extracts user ID from JWT
    ↓
Check if user is admin
    ├─ If Admin: Return all applications
    └─ If Regular User: Query database with {userId: current_user["_id"]}
    ↓
Return filtered applications
```

---

## Testing Strategy
See `test_insurance_isolation.py` for comprehensive testing:
1. Create two test users
2. Login both users
3. Each user submits applications for all 3 insurance types
4. Retrieve applications for each user
5. Verify each user only sees their own applications
6. Verify userId is correctly set in response objects

**Expected Result:** Each user sees exactly 3 applications (1 of each type) with correct userId values.
