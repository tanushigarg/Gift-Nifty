#!/bin/bash

# Install dependencies
apt-get update && apt-get install -y wget unzip

# Install Google Chrome
wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y /tmp/google-chrome.deb

# Verify Chrome installation
google-chrome --version

# Install ChromeDriver (match the Chrome version)
CHROME_VERSION=$(google-chrome --version | grep -oP '[0-9]+\.[0-9]+\.[0-9]+')
CHROMEDRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION)
wget -O chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"

# Unzip and move to /usr/bin
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

# Install Python dependencies
pip install -r requirements.txt

# Start the application
gunicorn app:app --bind 0.0.0.0:10000
