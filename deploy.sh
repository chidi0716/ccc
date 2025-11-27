#!/bin/bash

# Check if .venv exists to determine if it's the first run
if [ ! -d ".venv" ]; then
    echo "First run detected."
    
    # 1. Clone repository
    # If .git doesn't exist, we assume we need to clone. 
    # (Note: In a real scenario, you'd clone *then* cd into it, but this script might be the bootstrap)
    if [ ! -d ".git" ]; then
        echo "Cloning repository..."
        git clone https://github.com/your-repo/ME2025_Midterm3.git .
    fi

    # 2. Create virtual environment
    echo "Creating virtual environment..."
    python3 -m venv .venv

    # 3. Install requirements
    echo "Installing dependencies..."
    source .venv/bin/activate
    pip install -r requirements.txt

    # 4. Start app
    echo "Starting application..."
    python3 app.py
else
    echo "Subsequent run detected."
    
    # 1. Update repository
    echo "Updating repository..."
    git pull

    # 2. Check and install requirements
    echo "Checking dependencies..."
    source .venv/bin/activate
    pip install -r requirements.txt

    # 3. Restart app
    echo "Restarting application..."
    python3 app.py
fi
