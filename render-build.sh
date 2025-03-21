#!/usr/bin/env bash

# Create a writable directory in /tmp
mkdir -p /tmp/chrome

# Download Chrome (Portable)
wget -q -O /tmp/chrome/chrome.zip "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
unzip -o /tmp/chrome/chrome.zip -d /tmp/chrome/
chmod +x /tmp/chrome/google-chrome-stable

# Download Chromedriver (Portable)
wget -q -O /tmp/chrome/chromedriver.zip "https://chromedriver.storage.googleapis.com/$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip"
unzip -o /tmp/chrome/chromedriver.zip -d /tmp/chrome/
chmod +x /tmp/chrome/chromedriver

echo "Chrome and Chromedriver installed successfully in /tmp/chrome"
