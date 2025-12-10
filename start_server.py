#!/usr/bin/env python
"""
Test startup and keep server alive
"""
import sys
import os
from pathlib import Path

# Add the backend directory to the Python path
backend_dir = Path(__file__).parent / "cashper_backend"
sys.path.insert(0, str(backend_dir))

import uvicorn
from app import app

if __name__ == "__main__":
    # Run uvicorn without reload
    try:
        print("[*] Starting Cashper API Server...")
        print("[*] Server running on http://127.0.0.1:8000")
        print("[*] Press Ctrl+C to stop\n")
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
        print("\n\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nServer error: {e}")
        sys.exit(1)
