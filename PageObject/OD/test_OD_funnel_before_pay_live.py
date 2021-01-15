from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay
from PageObject.Staging.voronka_posle_oplati_CA_OD import voronka_posle_oplati_CA_OD_S_Platinum
from PageObject.Staging.voronka_posle_oplati_CA_bez_Pl import voronka_posle_oplai_CA_bez_Pl
from PageObject.OD.proverca_summary_OD import proverca_summary_OD

# -----------------------------------------Screen size--------------------------------------------------------------

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
#link = 'https://staging.completecase.com:8003/'
link = 'https://www.onlinedivorce.com'
browser.get(link)
browser.implicitly_wait(25)

email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'
states = ['//*[@id="id_state_of_filing"]/option[3]', '//*[@id="id_state_of_filing"]/option[3]'],

browser.find_element_by_xpath('//*[@id="why-us"]/div/div/div[2]/div/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="why-us"]/div/div/div[1]/div/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="popupContested"]/div/div/div[2]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="why-us"]/div/div/div[3]/div/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="popupBasicOnline"]/div/div/div[2]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="dropdownMenuLink"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="dropdownMenuHeader"]/div/a[3]').click()
time.sleep(1)
# Need a Will
Protect = browser.find_element_by_xpath('/html/body/main/div/section[1]/div/div[2]/div/p').text
print(Protect)
assert 'Protect' == "Protect", f"WRONG."
# Next Chapter
browser.find_element_by_xpath('//*[@id="dropdownMenuLink"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="dropdownMenuHeader"]/div/a[4]').click()
time.sleep(1)
Chapter = browser.find_element_by_xpath('/html/body/main/div/section[1]/div/div/div/h2/span').text
print(Chapter)
assert 'Chapter' == "Chapter", f"WRONG."
# About Us
browser.find_element_by_xpath('//*[@id="dropdownMenuLink"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="dropdownMenuHeader"]/div/a[5]').click()
time.sleep(1)
Us = browser.find_element_by_xpath('/html/body/main/section[1]/div/div/div/h2').text
print(Us)
assert 'Us' == "Us", f"WRONG."
# Affiliates
browser.find_element_by_xpath('//*[@id="dropdownMenuLink"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="dropdownMenuHeader"]/div/a[6]').click()
time.sleep(1)
Become = browser.find_element_by_xpath('/html/body/main/section[1]/div/div/div[1]/h3').text
print(Become)
assert 'Become' == "Become", f"WRONG."
# Reviews
browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[2]/a').click()
time.sleep(1)
Recent = browser.find_element_by_xpath('/html/body/main/div[1]/h1').text
print(Recent)
assert 'Recent' == "Recent", f"WRONG."
# FAQ
browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()
time.sleep(1)
FAQ = browser.find_element_by_xpath('/html/body/main/div[1]/div[1]/div[1]/h1').text
print(FAQ)
assert 'FAQ' == "FAQ", f"WRONG."
# Blog
browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/a').click()
time.sleep(1)
Divorce = browser.find_element_by_xpath('/html/body/div[1]/div/main/h1').text
print(Divorce)
assert 'Divorce' == "Divorce", f"WRONG."
# Contact Us
browser.find_element_by_xpath('//*[@id="navbar"]/ul/li[5]/a').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Na')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_Na')
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="id_user_phone"]').send_keys('1234567891')
browser.find_element_by_xpath('//*[@id="id_state"]/option[5]').click()
browser.find_element_by_xpath('//*[@id="id_message"]').send_keys('Test')
browser.find_element_by_xpath('/html/body/main/div/div/div[2]/form/button').click()
time.sleep(2)
Thank = browser.find_element_by_xpath('/html/body/main/div/div/div[2]/div/p[1]').text
print(Thank)
assert 'Thank' == "Thank", f"WRONG."
# Disclaimer
browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[6]/a').click()
time.sleep(2)
Disclaimer = browser.find_element_by_xpath('/html/body/main/section/div/div/div/h1').text
print(Disclaimer)
assert 'Disclaimer' == "Disclaimer", f"WRONG."
# Get Started
browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[8]/a').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[5]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="beginForm"]/div[1]/a').click()
time.sleep(2)
# browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Na')
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_Na')
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="id_email"]').click()
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()
#
# # browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').click()
# # time.sleep(1)
# # browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
# # browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Name')
# # browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_Name')
# # browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
# #
# # state_main_page = browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').get_attribute("value")
# # state_main_page = state_main_page.title()
# # first_name_main_page = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
# # last_name_main_page = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
# # email_main_page = email
# #
# # browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()

# Step 1
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()
time.sleep(2)

# # Step 2
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


# Сделать проверку введенных значений
proverca_summary_OD(browser, )
time.sleep(3)
browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/a').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="state"]/option[8]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="popup0"]/div/div/div/div[2]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/a').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('me')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('me')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="popup1"]/div/div/div/div[5]/button').click()
time.sleep(2)
#Proverca posle izmeneniy

#State_________________________________________________________________________
Connecticut = browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/span').text
print(Connecticut)
assert Connecticut == "Connecticut", f"WRONG."

#Name__________________________________________________________________________
First_Name = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[1]').text
print(First_Name)
assert First_Name == "First_Name", f"WRONG."
Last_Name = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[2]').text
print(Last_Name)
assert Last_Name == "Last_Name", f"WRONG."

browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('12345678')
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
time.sleep(3)
try:
    browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/a').click()
except:
    browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()
time.sleep(1)

try:
    voronka_posle_oplati_CA_OD_S_Platinum(browser, )
except:
    voronka_posle_oplai_CA_bez_Pl(browser, )

