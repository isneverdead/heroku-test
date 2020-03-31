from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


driver.get("http://www.duckduckgo.com/")
print (driver.page_source)
#search_box = driver.get_element_by_id("search_form_input_homepage")
#search_box.driver.clear()
#search_box.send_keys("frz_akbar instagram")

#print (search_box)
#search_box.send_keys(Keys.RETURN)
#submit = driver.get_element_by_id("search_button_homepage")
#submit.click()
