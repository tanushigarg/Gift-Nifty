1. Install Python
Check if Python is Installed:
Open Command Prompt (Windows) or Terminal (Mac/Linux).
Run:
python --version
or
python3 --version
If Python is not installed, download and install it from https://www.python.org/downloads/.
Verify Pip Installation:
Pip is required to install Python packages.
pip --version
If pip is not installed, install it using:

cpp
Copy
Edit
python -m ensurepip --default-pip
2. Install VS Code
Download and install Visual Studio Code (VS Code) from https://code.visualstudio.com/.
Open VS Code after` installation.
3. Open Terminal in VS Code
Click View > Terminal (or press Ctrl + ~).
You can switch between PowerShell and Command Prompt (Windows) or use the default Terminal (Mac/Linux).
4. Create a Project Folder and Open It
Open Terminal in VS Code.
Create a folder for the project:
bash
Copy
Edit
mkdir selenium_project
cd selenium_project
Open the folder in VS Code:
css
Copy
Edit
code .
5. Create a Virtual Environment
Run:
nginx
Copy
Edit
python -m venv venv
Activate the virtual environment:
Windows (PowerShell):
mathematica
Copy
Edit
venv\Scripts\Activate
Mac/Linux:
bash
Copy
Edit
source venv/bin/activate
6. Install Required Dependencies
Run:

nginx
Copy
Edit
pip install selenium
For Mac M1/M2 Users, install ChromeDriver:

nginx
Copy
Edit
brew install chromedriver
For Windows Users, download ChromeDriver from: https://sites.google.com/chromium.org/driver/

Download the correct version matching your Chrome.
Extract and place it in C:\chromedriver\chromedriver.exe.
Add it to system PATH.
7. Save the Selenium Script
In VS Code, create a new file main.py inside the selenium_project folder.
Copy and paste the provided script into main.py.
8. Run the Selenium Script
In the terminal, execute:

css
Copy
Edit
python main.py
If you face any errors, ensure:

Chrome is updated.
ChromeDriver version matches your Chrome version.