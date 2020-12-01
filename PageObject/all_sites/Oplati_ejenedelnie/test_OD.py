from datetime import datetime
from idlelib import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay



# -----------------------------------------Screen size--------------------------------------------------------------
#def payment_divorce_od():
   # browser = webdriver.Chrome()
   # browser.maximize_window()
   # link = 'https://www.onlinedivorce.com'
   # browser.get(link)
   # browser.implicitly_wait(25)

browser = webdriver.Chrome(ChromeDriverManager().install())
# browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
# link = 'https://staging.completecase.com:8003/'
link = 'https://www.onlinedivorce.com'
browser.get(link)
browser.implicitly_wait(25)

email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'
states = ['//*[@id="id_state_of_filing"]/option[3]', '//*[@id="id_state_of_filing"]/option[3]'],

browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('first_na')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('last_na')
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)

state_main_page = browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').get_attribute("value")
state_main_page = state_main_page.title()
first_name_main_page = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
last_name_main_page = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
email_main_page = email

browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()

# Step 2
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/button').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/div/ul/li[5]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').send_keys('12')
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').send_keys('1999')
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 3
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[4]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 4

browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 5

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 6

browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 7

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 8

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 9

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 10

browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 11

browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

# Step 12

browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('12345678')
# Сделать проверку введенных значений
time.sleep(3)
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div[2]/div[2]/input').click()

# Pop up number fone
time.sleep(1)
browser.find_element_by_xpath('//*[@id="number1"]').send_keys('111')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="number2"]').send_keys('111')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="number3"]').send_keys('1111')

fone_1 = browser.find_element_by_xpath('//*[@id="number1"]').get_attribute("value")
fone_2 = browser.find_element_by_xpath('//*[@id="number2"]').get_attribute("value")
fone_3 = browser.find_element_by_xpath('//*[@id="number3"]').get_attribute("value")

browser.find_element_by_xpath('//*[@id="save-phone-js"]').click()
time.sleep(3)
# _______________________________________________________________________________________________________________________
pagePay(browser, )
# payment_plan_od(browser, data)
# _______________________________________________________________________________________________________________________

# Skip Platinum
# browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/div/div/div/small/a').click()
try:
    browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/a').click()
except:
    browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()
time.sleep(3)
try:
    browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()
except:
    time.sleep(3)
# browser.quit()
# # Skip Buying WILL
# time.sleep(10)
# browser.find_element_by_xpath('//*[@id="willModalStep1"]/button/span/i').click()
# # else:
# #     time.sleep(10)
# #     #Skip Buying WILL
# #     browser.find_element_by_xpath('//*[@id="willModalStep1"]/button/span/i').click()
#
# # #Buying WILL
# # #browser.find_element_by_xpath('//*[@id="willModalStep1"]/div[6]/div[2]/button').click()
# time.sleep(5)
#
# browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div[2]/a[1]').click()
# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="welcomeModal"]/div/div/div[1]/button/span').click()
# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="nav"]/li[2]/a').click()
#
# text_pop_up_payment_plan = voronka_virginia(browser, time)
#pop up Covid - 19
try:
    browser.find_element_by_xpath('//*[@id="covidPremModal"]/div/div/div/div/a').click()
except:
    time.sleep(2)
try:
    browser.find_element_by_xpath('//*[@id="premiumExpModal"]/div/div/div[1]/button/span').click()
except:
    time.sleep(1)


browser.quit()