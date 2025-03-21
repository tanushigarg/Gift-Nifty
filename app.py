from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

URL = "https://www.moneycontrol.com/markets/global-indices/"

# Set up Selenium WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Safari/537.36"
)

# Define the correct ChromeDriver path (for Mac)
service = Service("/opt/homebrew/bin/chromedriver")

def fetch_market_data():
    """Fetches the GIFT NIFTY market data from the website."""
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 10)
        
        row_xpath = "//tr[td//a[@title='GIFT NIFTY']]"
        row_element = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        if row_element:
            value_xpath = f"{row_xpath}/td[3]"
            value_element = driver.find_element(By.XPATH, value_xpath)
            market_value = value_element.text.strip()
            logging.info(f"Extracted Market Value for GIFT NIFTY: {market_value}")
            return {"GIFT NIFTY": market_value}
        else:
            logging.warning("Target row not found on the page.")
            return {"error": "Market data not found"}
    except Exception as e:
        logging.error(f"Error fetching the page: {e}")
        return {"error": str(e)}
    finally:
        driver.quit()

@app.route("/", methods=["GET"])
@app.route("/getGiftNifty", methods=["GET"])
def get_gift_nifty():
    """API endpoint to return the GIFT NIFTY market value."""
    return jsonify(fetch_market_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
