from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

def amazon_demo_search(product_name):
    # Setup Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open Amazon
        driver.get("https://www.amazon.com")
        driver.maximize_window()
        sleep(2)

        # Find search bar
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
        sleep(3)

        # Collect first 5 product titles
        results = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")

        print("\nTop Search Results:\n")
        for i, item in enumerate(results[:5], start=1):
            print(f"{i}. {item.text}")

    finally:
        sleep(5)
        driver.quit()

if __name__ == "__main__":
    amazon_demo_search("wireless headphones")
