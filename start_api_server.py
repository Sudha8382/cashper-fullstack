#!/usr/bin/env python3
"""
API Server Startup Script
Starts the Cashper Backend API Server
"""
import sys
import os

# Add cashper_backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=False,  # Disable reload to avoid shutdown issues
        log_level="info",
        access_log=True,
        use_colors=True
    )
