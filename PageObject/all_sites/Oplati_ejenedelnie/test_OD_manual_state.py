from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay
from PageObject.Staging.voronka_posle_oplati_CA_OD import voronka_posle_oplati_CA_OD_S_Platinum
from PageObject.Staging.voronka_posle_oplati_CA_bez_Pl import voronka_posle_oplai_CA_bez_Pl
from PageObject.OD.proverca_summary_OD import proverca_summary_OD
from PageObject.all_sites.Voronki.california import voronka_california
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
browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[5]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Na')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_Na')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_email"]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()

# browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').click()
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
# browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Name')
# browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_Name')
# browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
#
# state_main_page = browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').get_attribute("value")
# state_main_page = state_main_page.title()
# first_name_main_page = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
# last_name_main_page = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
# email_main_page = email
#
# browser.find_element_by_xpath('//*[@id="beginForm"]/button').click()

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


# Сделать проверку введенных значений
proverca_summary_OD(browser, )
time.sleep(3)
browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/a').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="state"]/option[6]').click()
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
California = browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/span').text
print(California)
assert California == "California", f"WRONG."

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
time.sleep(1)
try:
    browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/a').click()
except:
    browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()
time.sleep(1)

try:
    voronka_posle_oplati_CA_OD_S_Platinum(browser, )
except:
    voronka_posle_oplai_CA_bez_Pl(browser, )

voronka_california(browser, )

time.sleep(25)

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

browser.find_element_by_xpath('//*[@id="search"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="submit"]').click()
browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()

browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/a[1]').click()
browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/input').send_keys('Test OD')
browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/textarea').send_keys('Test California OD')
time.sleep(5)
browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/button').click()
time.sleep(10)

#Добавляем экспедайтед и платинум
browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[8]/div/div/div/a').click()
time.sleep(5)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
browser.find_element_by_xpath('//*[@id="id_add_free"]').click()
time.sleep(3)
browser.find_element_by_xpath(
    '//*[@id="admindirectpaymentitem_set-group"]/div/fieldset/table/tbody/tr[2]/td/a').click()
time.sleep(2)
browser.find_element_by_xpath(
    '//*[@id="id_admindirectpaymentitem_set-0-product_types"]/option[4]').click()
time.sleep(2)
browser.find_element_by_xpath(
    '//*[@id="admindirectpaymentitem_set-group"]/div/fieldset/table/tbody/tr[3]/td/a').click()
time.sleep(2)
browser.find_element_by_xpath(
    '//*[@id="id_admindirectpaymentitem_set-1-product_types"]/option[11]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="admindirectpayment_form"]/div/div[2]/input').click()
time.sleep(2)

#Personal Info__________________________________________________________________________________
First_Name = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute('value')
print(First_Name)
assert First_Name == "First_Name", f"Wrong."
Last_Name = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute('value')
print(Last_Name)
assert Last_Name == "Last_Name", f"Wrong."
# Email = browser.find_element_by_xpath('//*[@id="id_email"]').get_attribute('value')
# print(Email)
# assert Email == "email", f"Wrong."
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

browser.quit()




browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
# link = 'https://staging.completecase.com:8003/'
link = 'https://www.onlinedivorce.com'
browser.get(link)
browser.implicitly_wait(25)
# Логинимся как клиент
browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[10]/a').click()
browser.find_element_by_xpath('//*[@id="id_login_email"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="id_login_password"]').send_keys('12345678')
browser.find_element_by_xpath('//*[@id="loginForm"]/button').click()
time.sleep(1900)

#Переходим на страницу форм
browser.find_element_by_xpath('/html/body/header/nav/ul/li[4]/a').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="willModalStep1"]/div[6]/a').click() #Pop up Will
time.sleep(1)
browser.find_element_by_xpath('//*[@id="select-all-js"]').click()
browser.find_element_by_xpath('//*[@id="forms-table-summary"]/tbody/tr/td[2]/img').click()
time.sleep(10)
browser.find_element_by_xpath('//*[@id="forms-confirm-shipping-modal"]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="submit-id-shipping_form"]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="select-all-js"]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="forms-table-summary"]/tbody/tr/td[4]/img').click()
time.sleep(10)
browser.find_element_by_xpath('//*[@id="forms-table-summary"]/tbody/tr/td[3]/img').click()
time.sleep(2)
browser.quit()
