#!/usr/bin/env python
import sys
import os

# Get absolute path to cashper_backend
backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cashper_backend")
uploads_dir = os.path.join(backend_dir, "uploads")

print(f"[INFO] Backend directory: {backend_dir}")
print(f"[INFO] Uploads directory: {uploads_dir}")
print(f"[INFO] Uploads exists: {os.path.exists(uploads_dir)}")

# Add cashper_backend to Python path
sys.path.insert(0, backend_dir)

# Now start Uvicorn
import uvicorn

if __name__ == "__main__":
    # Change to backend directory before running
    os.chdir(backend_dir)
    
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )
