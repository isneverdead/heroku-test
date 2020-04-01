from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
#from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("https://shopee.com/")

close_popup = driver.find_element_by_class_name("shopee-popup__close-btn").click()
login = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/div/div[1]/div/ul/li[5]").click()
time.sleep(5)

login_username = driver.find_element_by_name("loginKey")
login_username.clear()
login_username.send_keys("richart135@gmail.com")

login_password = driver.find_element_by_name("password")
login_password.clear()
login_password.send_keys("Akbar021993"+Keys.ENTER)
time.sleep(7)
# close_popup.click()
jualan = "https://shopee.co.id/JAS-HUJAN-SETELAN-ELMONDO-CERIA-935-934-(TEBAL)-ATASAN-PONCO-201-SETELAN-1-x-PAKAI-CAP-BECAK-i.38976170.6911106865"
# komentar = driver.find_element_by_class_name("shopee-product-comment-list")
# list_nama = komentar.find_elements_by_tag_name('a').text
# print (list_nama)
driver.get(jualan)
print("sleep 5 sec")
time.sleep(5)
body_scroll = driver.find_element_by_xpath("/html/body")
body_scroll.send_keys(Keys.END)
print("sleep 5 sec")
time.sleep(5)
print("selesai sleep")
i = 0
for a in driver.find_elements_by_class_name("shopee-product-rating"):
    i = i+1
    print("masuk for loop")
    time.sleep(10)
    body_scroll = driver.find_element_by_xpath("/html/body")
    body_scroll.send_keys(Keys.END)
    time.sleep(10)
    comment_list = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div["+str(i)+"]/div/a")
    link = comment_list.get_attribute('href')
    print("User " + str(i) + link)
    driver.get(link)
    time.sleep(5)
    follow_btn = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div[2]/div[1]/button")
    follow_btn.click()
    followers = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/div[1]")
    user_followers = followers.get_attribute('InnerText')
    following = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]")
    user_following = following.get_attribute('InnerText')
    print("Nama : " + str(link) + " followed ")
    driver.get(jualan)

# //*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[1]
# //*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/a

# //*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]
# //*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/a

# //*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[1]

# next = driver.find_element_by_class_name("shopee-icon-button--right")

# profile = driver.find_element_by_class_name("shopee-product-rating__author-name")
# href = profile.get_attribute('href')
# nama = profile.text
# ikuti = driver.find_element_by_class_name("shopee-button-outline--complement")
# pengikut = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/div[1]").text
# mengikuti = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]").text
# bergabung = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[3]/div[1]").text
# status_ikuti = driver.find_element_by_class_name("shopee-button-outline--complement").text

# print("terikuti") if status_ikuti == ("MENGIKUTI") else print("belum terikuti")
# google_login_button = driver.find_element_by_class_name("_1KZrge")
