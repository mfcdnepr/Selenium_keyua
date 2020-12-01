from _datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
#link = 'https://staging.completecase.com:8003/'
link = 'https://www.onlinedivorce.com'
browser.get(link)
email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'

browser.find_element_by_xpath('//*[@id="dropdownMenuLink"]').click()
browser.find_element_by_xpath('//*[@id="dropdownMenuHeader"]/div/a[4]').click()
aboutUs = browser.find_element_by_xpath('/html/body/main/section[1]/div/div/div/h2').text
print(aboutUs)
assert aboutUs == "About Us", f"WRONG."

#Contact Us
browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[5]/a').click()
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Name')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_Name')
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="id_user_phone"]').send_keys('1234567890')
browser.find_element_by_xpath('//*[@id="id_state"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="id_message"]').send_keys('Test Contact Us')
browser.find_element_by_xpath('/html/body/main/div/div/div[2]/form/button').click()
time.sleep(1)
thankyou = browser.find_element_by_xpath('/html/body/main/div/div/div[2]/div/p[1]').text
print(thankyou)
assert thankyou == "Thank you for request!", f"WRONG."