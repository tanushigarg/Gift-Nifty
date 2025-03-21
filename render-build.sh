#!/bin/bash

# Install Chrome
echo "Installing Google Chrome..."
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
apt-get install -y ./google-chrome-stable_current_amd64.deb

# Install ChromeDriver
echo "Installing ChromeDriver..."
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
wget -q "https://chromedriver.storage.googleapis.com/${CHROME_VERSION}.0/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
mv chromedriver /usr/local/bin/chromedriver
chmod +x /usr/local/bin/chromedriver

# Clean up
rm -f google-chrome-stable_current_amd64.deb chromedriver_linux64.zip
