from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.all_sites.RS.Oplata.pagePayRS import pagePayRS

#____________________________________Screen___________________________________________________

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
link = 'http://westvirginiaonlinedivorce.com/'
browser.get(link)
browser.implicitly_wait(15)

email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'

#Start scren

browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Name')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_name')
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
browser.find_element_by_xpath('/html/body/main/section[1]/div/div/div/div[2]/div/form/button').click()

#Step1

browser.find_element_by_xpath('//*[@id="id_you_are_0"]').click()
browser.find_element_by_xpath('/html/body/main/div/div[2]/div/div[2]/section/form/div[3]/div/button/div').click()
browser.find_element_by_xpath('/html/body/main/div/div[2]/div/div[2]/section/form/div[3]/div/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('/html/body/main/div/div[2]/div/div[2]/section/form/button').click()

#Step2

browser.find_element_by_xpath('//*[@id="id_date_of_marriage"]').click()
browser.find_element_by_xpath('//*[@id="id_date_of_marriage"]').send_keys('01011990')
browser.find_element_by_xpath('//*[@id="id_were_you_in_a_same-sex_marriage_1"]').click()
browser.find_element_by_xpath('//*[@id="id_who_will_file_0"]').click()
browser.find_element_by_xpath('/html/body/main/div/div[2]/div/div/section/form/button').click()

#Step3

browser.find_element_by_xpath('//*[@id="id_minor_children_0"]').click()
browser.find_element_by_xpath('//*[@id="id_wife_pregnant_primarily_1"]').click()
browser.find_element_by_xpath('/html/body/main/div/div[2]/div/div/section/form/button').click()

#Step4

browser.find_element_by_xpath('//*[@id="id_live_together_now_1"]').click()
browser.find_element_by_xpath('//*[@id="id_property_any_1"]').click()
browser.find_element_by_xpath('//*[@id="id_debts_any_1"]').click()
browser.find_element_by_xpath('/html/body/main/div/div[2]/div/div/section/form/button').click()

#Step5

browser.find_element_by_xpath('//*[@id="id_phone1"]').click()
browser.find_element_by_xpath('//*[@id="id_phone1"]').send_keys('123')
browser.find_element_by_xpath('//*[@id="id_phone2"]').send_keys('456')
browser.find_element_by_xpath('//*[@id="id_phone3"]').send_keys('7890')
browser.find_element_by_xpath('//*[@id="id_password"]').click()
browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('12345678')
browser.find_element_by_xpath('/html/body/main/div/div[2]/div/div[2]/section/form/button').click()

#Payment

pagePayRS(browser, )

#Platinum/Vip page
try:
    browser.find_element_by_xpath('/html/body/main/main/div[5]/a').click()
except:
    browser.find_element_by_xpath('/html/body/main/main/div/div[1]/a').click()
browser.quit()
