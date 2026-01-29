""" FastAPI is a modern, high-performance web framework for building APIs
    with Python 3.7+ based on open standards (OpenAPI and JSON Schema)."""

# Within our project we installed FastAPI and Uvicorn
""" To install: pip install fastapi uvicorn 
    Then we create a file called: main.py """

### Content of main.py ###

#Import fastapi
""" from fastapi import FastAPI """

# Create application name 
""" app = FastAPI() """

# create a route
""" @app.get('/') """

# Function that executes code when the route is accessed
""" def home():
        return 'Backend Environment' 
"""

# Run application: first, uvicorn, then file name, main, then application name
""" uvicorn main:app"""
