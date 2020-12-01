from datetime import datetime
from idlelib import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay
from PageObject.Staging.voronka_posle_oplati_CA_OD import voronka_posle_oplati_CA_OD_S_Platinum
from PageObject.Staging.voronka_posle_oplati_CA_bez_Pl import voronka_posle_oplai_CA_bez_Pl

# -----------------------------------------Screen size--------------------------------------------------------------




browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
link = 'https://www.completecase.com/admin/login/?next=/admin/'
#link = 'https://staging.completecase.com:8001/admin/login/?next=/admin/'
browser.get(link)

# browser.get(link)
# browser.implicitly_wait(10)


# _____________________________Live____________________________________________________________________
# browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('cmo0lkamd0jqflzrm49u6yin601kc1wn')
# browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
# browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
# browser.implicitly_wait(10)
# _____________________________________________________________________________________________________
browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('zeleniyanton@gmail.com')
browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('Niqepoccoqu')
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)

browser.find_element_by_xpath('//*[@id="search"]').send_keys("testanton35+20201021113420661639@gmail.com")
browser.find_element_by_xpath('//*[@id="submit"]').click()
browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()

# browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/a[1]').click()
# browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/input').send_keys('Test OD')
# browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/textarea').send_keys('Test California OD')
# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/button').click()
# time.sleep(10)

# Добавляем экспедайтед и платинум
# browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[8]/div/div/div/a').click()
# time.sleep(5)
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
# browser.find_element_by_xpath('//*[@id="id_sale_type"]/option[2]').click()
# browser.find_element_by_xpath('//*[@id="id_add_free"]').click()
# time.sleep(3)
# browser.find_element_by_xpath(
#     '//*[@id="admindirectpaymentitem_set-group"]/div/fieldset/table/tbody/tr[2]/td/a').click()
# time.sleep(2)
# browser.find_element_by_xpath(
#     '//*[@id="id_admindirectpaymentitem_set-0-product_types"]/option[4]').click()
# time.sleep(2)
# browser.find_element_by_xpath(
#     '//*[@id="admindirectpaymentitem_set-group"]/div/fieldset/table/tbody/tr[3]/td/a').click()
# time.sleep(2)
# browser.find_element_by_xpath(
#     '//*[@id="id_admindirectpaymentitem_set-1-product_types"]/option[11]').click()
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="admindirectpayment_form"]/div/div[2]/input').click()
# time.sleep(2)
#
#Personal Info__________________________________________________________________________________
First_Name = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute('value')
print(First_Name)
assert First_Name == "First_Name", f"Wrong."
Last_Name = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute('value')
print(Last_Name)
assert Last_Name == "Last_Name", f"Wrong."
Email = browser.find_element_by_xpath('//*[@id="id_email"]').get_attribute('value')
print(Email)
assert Email == "testanton35+20201021113420661639@gmail.com", f"Wrong."
Phone = browser.find_element_by_xpath('//*[@id="id_phone"]').get_attribute("value")
print(Phone)
assert Phone == "1111111111", f"WRONG."
#Location Info_________________________________________________________________________________
Addres = browser.find_element_by_xpath('//*[@id="id_address"]').get_attribute('value')
print(Addres)
assert Addres == "Adress1", f"WRONG."
City = browser.find_element_by_xpath('//*[@id="id_city"]').get_attribute('value')
print(City)
assert City == "City", f"WRONG."
Zip = browser.find_element_by_xpath('//*[@id="id_zip"]').get_attribute('value')
print(Zip)
assert Zip == "111", f"WRONG."
State = browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[5]/div[2]/div[1]/div').text
print(State)
assert State == "California", f"Wrong."
#DIVORCE CASES_________________________________________________________________________________
DivorceCase = browser.find_element_by_xpath(
    '//*[@id="divorcecase_set-empty"]/fieldset/div[1]/div/div').text
print(DivorceCase)
assert DivorceCase == "Full access", f"WRONG."

browser.find_element_by_xpath('//*[@id="fieldsetcollapser6"]').click()
time.sleep(2)

#ORDERS (HIDE)_________________________________________________________________________________
Displayorderitems = browser.find_element_by_xpath(
    '//*[@id="orders-empty"]/fieldset/div[3]/div/div').text
print(Displayorderitems)
assert Displayorderitems == "Divorce: $0.01", f"WRONG."

# #User has Platinum______________________________________________________________________________
# Platinum = browser.find_element_by_xpath('//*[@id="content"]/h1[6]/text()').text
# print(Platinum)
# assert Platinum == "User has Platinum", f"WRONG."






# browser.quit()




# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.maximize_window()
# # link = 'https://staging.completecase.com:8003/'
# link = 'https://www.onlinedivorce.com'
# browser.get(link)
# browser.implicitly_wait(25)
# # Логинимся как клиент
# browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[10]/a').click()
# browser.find_element_by_xpath('//*[@id="id_login_email"]').send_keys(email)
# browser.find_element_by_xpath('//*[@id="id_login_password"]').send_keys('12345678')
# browser.find_element_by_xpath('//*[@id="loginForm"]/button').click()