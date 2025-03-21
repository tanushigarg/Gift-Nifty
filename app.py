import os
from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

URL = "https://www.moneycontrol.com/markets/global-indices/"

def get_driver():
    """Sets up and returns a headless Chrome WebDriver instance."""
    chrome_options = Options()
    chrome_options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/google-chrome-stable")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents crashes in Render
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/local/bin/chromedriver")
    return webdriver.Chrome(executable_path=driver_path, options=chrome_options)

def fetch_market_data():
    """Fetches the GIFT NIFTY market data from the website."""
    driver = get_driver()
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        row_xpath = "//tr[td//a[@title='GIFT NIFTY']]"
        row_element = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        if row_element:
            value_xpath = f"{row_xpath}/td[3]"
            value_element = driver.find_element(By.XPATH, value_xpath)
            market_value = value_element.text.strip()
            return {"GIFT NIFTY": market_value}
        else:
            return {"error": "Market data not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()

@app.route("/", methods=["GET"])
@app.route("/getGiftNifty", methods=["GET"])
def get_gift_nifty():
    """API endpoint to return the GIFT NIFTY market value."""
    return jsonify(fetch_market_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
