from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Headless Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open books site
driver.get("http://books.toscrape.com/")

# Get all book titles
books = driver.find_elements(By.CSS_SELECTOR, "h3 a")
for i, book in enumerate(books[:5], start=1):
    print(f"{i}. {book.get_attribute('title')}")

driver.quit()
