#!/bin/bash

# check
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
./venv/bin/pip install -r requirements.txt

# optional Install 
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if ! command -v xdotool &> /dev/null; then
        echo "xdotool not found. Installing..."
        sudo apt install -y xdotool
    fi
fi

echo "Starting Auto Key Spammer..."
./venv/bin/python main.py
deactivate
