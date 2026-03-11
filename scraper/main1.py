from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
index = 0
for i in range(1,5):
    driver.get(f"https://www.flipkart.com/search?q={query}&page={i}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")
    time.sleep(3)
    elem = driver.find_elements(By.CLASS_NAME, 'jIjQ8S')
    for ele in elem:
        d = ele.get_attribute("outerHTML")
        with open(f"data/{query}_{index}.html", "w", encoding="utf-8") as f:
            f.write(d)
            index += 1
driver.quit()