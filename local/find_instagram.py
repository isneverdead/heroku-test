from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("https://google.com/")
search_box =driver.find_element_by_name("q")
search_box.clear()
search_box.send_keys("instagram.com/frz_akbar"+Keys.ENTER)

first_link = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/a").click()

# submit_button = driver.find_element_by_id("search_button_homepage")
# submit_button.click()