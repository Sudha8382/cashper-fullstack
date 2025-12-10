#!/usr/bin/env python
"""
Wrapper script to start the FastAPI server with proper PYTHONPATH configuration
"""
import sys
import os
from pathlib import Path

# Add the backend directory to the Python path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

# Now import and run uvicorn
import uvicorn
from app import app

if __name__ == "__main__":
    # Run uvicorn with specific settings for Windows
    try:
        uvicorn.run(
            app,
            host="127.0.0.1",
            port=8000,
            reload=False,
            log_level="info",
            access_log=True,
            use_colors=True
        )
    except KeyboardInterrupt:
        print("\n\nServer shutdown initiated by user...")
        sys.exit(0)

