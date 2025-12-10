#!/usr/bin/env python
import sys
import os

# Add cashper_backend to Python path
sys.path.insert(0, os.path.join(os.getcwd(), "cashper_backend"))

# Now start Uvicorn
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )
