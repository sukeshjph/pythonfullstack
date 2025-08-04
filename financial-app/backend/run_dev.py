#!/usr/bin/env python3
"""
Development server script for FastAPI application
Run this script to start the development server with hot reload
"""

import uvicorn
import sys
import os

if __name__ == "__main__":
    print("Starting FastAPI development server...")
    print("Server will be available at: http://localhost:8000")
    print("API documentation will be available at: http://localhost:8000/docs")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run(
        "books:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 