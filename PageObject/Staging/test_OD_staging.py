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
link = 'https://staging.completecase.com:8003/'
# link = 'https://www.onlinedivorce.com'
browser.get(link)
browser.implicitly_wait(25)

email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'
states = ['//*[@id="id_state_of_filing"]/option[3]', '//*[@id="id_state_of_filing"]/option[3]'],

browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('First_Name')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('Last_Name')
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

#Step 15
time.sleep(2)
browser.find_element_by_xpath('//*[@id="closeModal"]/span').click()
browser.find_element_by_xpath('//*[@id="id_husband_or_wife"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 16
browser.find_element_by_xpath('//*[@id="id_divorce_type_ca"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 18
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 19
browser.find_element_by_xpath('//*[@id="id_petitioner_social_security"]').send_keys('112233')
browser.find_element_by_xpath('//*[@id="id_petitioner_email_address"]').send_keys('husband@mail.com')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 20
browser.find_element_by_xpath('//*[@id="id_respondent_name_first"]').send_keys('Spouse_First')
browser.find_element_by_xpath('//*[@id="id_respondent_name_last"]').send_keys('Spouse_Last')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 21
browser.find_element_by_xpath('//*[@id="id_respondent_social_security"]').send_keys('223344')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 22
browser.find_element_by_xpath('//*[@id="id_date_separated"]').send_keys('01012019')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 23
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 24
browser.find_element_by_xpath('//*[@id="id_venue_court_zip"]').send_keys('90740')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 25
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[1]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[3]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[4]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 27
browser.find_element_by_xpath('//*[@id="id_form-0-child_name"]').send_keys('Test Junior')
browser.find_element_by_xpath('//*[@id="id_form-0-child_ssn"]').send_keys('557799')
browser.find_element_by_xpath('//*[@id="id_form-0-child_dob"]').send_keys('10102017')
browser.find_element_by_xpath('//*[@id="id_form-0-child_place_of_birth"]').send_keys('Los Angeles')
browser.find_element_by_xpath('//*[@id="id_form-0-child_gender"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[2]/div[2]/div[14]/div[2]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 28
browser.find_element_by_xpath('//*[@id="id_legal_custody"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 29
browser.find_element_by_xpath('//*[@id="id_parenting_plan"]').send_keys('None')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 32
browser.find_element_by_xpath('//*[@id="id_physical_custody3"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 33
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 34
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 37
browser.find_element_by_xpath('//*[@id="id_spousal_support_past_due"]').send_keys('1000')
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 39
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 41
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 43
browser.find_element_by_xpath(
    '/html/body/main/div[3]/div/div[1]/div/div[3]/form/fieldset/div/div[1]/div[3]/label[2]').click()
browser.find_element_by_xpath(
    '/html/body/main/div[3]/div/div[1]/div/div[3]/form/fieldset/div/div[3]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 46
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 49
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(2)

#Step 50
browser.find_element_by_xpath('//*[@id="willModal"]/div/div/div[1]/button/span').click() #Pop up Will
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()

#Step 51
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 52
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 53
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 54
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 55
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 56
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 57
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 58
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 59
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 60
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 61
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 62
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 63
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 64
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 65
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 66
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 67
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 68
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 69
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 70
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 71
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 72
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 73
browser.find_element_by_xpath('//*[@id="id_property_division_fair"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 74
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 75
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 79
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 80
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 81
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 83
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 85
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 88
browser.find_element_by_xpath('//*[@id="id_petitioner_gross_wages"]').send_keys('95000')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 89
browser.find_element_by_xpath('//*[@id="id_petitioner_gross_income_last_month"]').send_keys('7000')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 90
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 92
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 94
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 96
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 98
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 100
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 102
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 104
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 106
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 108
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 110
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 112
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 114
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 116
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 119
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 121
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 123
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 125
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 127
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 128
browser.find_element_by_id('//*[@id="id_petitioner_expenses_type"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="id_petitioner_home_type"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 130
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 132
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div[3]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 134
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 135
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)

#Step 143
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
time.sleep(1)













#browser.quit()


#browser = webdriver.Chrome(ChromeDriverManager().install())
#browser.maximize_window()
#link = 'https://staging.completecase.com:8001/admin/login/?next=/admin/'
#browser.get(link)

# browser.get(link)
# browser.implicitly_wait(10)


# _____________________________Live____________________________________________________________________
# browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('cmo0lkamd0jqflzrm49u6yin601kc1wn')
# browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
# browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
# browser.implicitly_wait(10)
# _____________________________________________________________________________________________________
#browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('zeleniyanton@gmail.com')
#browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('Niqepoccoqu')
#browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
#time.sleep(2)

#browser.find_element_by_xpath('//*[@id="search"]').send_keys(email)
#browser.find_element_by_xpath('//*[@id="submit"]').click()
#browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()

#browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[18]/div/div[3]/a[1]').click()
#browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[18]/div/div[3]/ng-form/input').send_keys('Test OD')
#browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[18]/div/div[3]/ng-form/textarea').send_keys('Test California OD')
#browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[18]/div/div[3]/ng-form/button').click()
#browser.quit()




#browser = webdriver.Chrome(ChromeDriverManager().install())
#browser.maximize_window()
#link = 'https://staging.completecase.com:8003/'
# link = 'https://www.onlinedivorce.com'
#browser.get(link)
#browser.implicitly_wait(25)
#Логинимся как клиент
#browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[10]/a').click()
#browser.find_element_by_xpath('//*[@id="id_login_email"]').send_keys(email)
#browser.find_element_by_xpath('//*[@id="id_login_password"]').send_keys('12345678')
#browser.find_element_by_xpath('//*[@id="loginForm"]/button').click()