#!/bin/bash

# Download prebuilt Google Chrome
wget -q -O /tmp/chrome.tar.gz https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
tar -xvzf /tmp/chrome.tar.gz -C /tmp/
mv /tmp/google-chrome /usr/local/bin/google-chrome
chmod +x /usr/local/bin/google-chrome

# Verify Chrome installation
/usr/local/bin/google-chrome --version

# Download a specific ChromeDriver version (compatible with Render)
wget -O /tmp/chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"

# Unzip and move to /usr/local/bin
unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

# Install Python dependencies
pip install -r requirements.txt

# Start the application
gunicorn app:app --bind 0.0.0.0:10000
