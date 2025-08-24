from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time,sleep
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
sleep(5)
# english=driver.find_element(By.ID,"langSelect-EN")
# english.click()
# time.sleep(5)
cookie=driver.find_element(By.ID,"bigCookie")
items=[f"product{i}" for i in range(18)]

end=time()+5
five_min=time()+60*5
while True:
    cookie.click()

    if time()>end:

        count=driver.find_element(By.ID,"cookies")
        print(count.text.split()[0].replace(",", ""))

        products = driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")
        best_item=None
        for product in reversed(products):

            best_item=product
            break
        if best_item:
            best_item.click()
        end=time()+5

    if time()>five_min:
        count = driver.find_element(By.ID, "cookies")
        print(f"Final cookie count:{count.text}")
        break

