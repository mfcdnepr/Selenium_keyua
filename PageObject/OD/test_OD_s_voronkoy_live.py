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
browser.find_element_by_xpath('//*[@id="id_respondent_address_0"]').send_keys('Karla Marksa 100')
browser.find_element_by_xpath('//*[@id="id_respondent_address_3"]').send_keys('Dnipro')
browser.find_element_by_xpath('//*[@id="id_respondent_address_5"]').send_keys('49000')
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
time.sleep(3)

#Step 30
browser.find_element_by_xpath('//*[@id="parentingPlanModal"]/div/div/div/div/button/span').click() #PopUp Parenting Plan
time.sleep(1)
browser.find_element_by_xpath('//*[@id="id_parenting_plan"]').send_keys('None')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 33
browser.find_element_by_xpath('//*[@id="id_physical_custody3"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 34
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 35
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 40
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 42
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 44
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[1]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[3]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 47
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 50
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 51
time.sleep(2)
browser.find_element_by_xpath('//*[@id="willModal"]/div/div/div[1]/button/span').click() #Pop up Will
time.sleep(2)
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[1]').click()
browser.find_element_by_xpath('//*[@id="id_form-0-property_real_estate_ownership"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="id_form-0-property_real_estate_award_to"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(2)
#Pop UP Quitclaim
browser.find_element_by_xpath('//*[@id="submitModal"]').click()
time.sleep(3)
browser.find_element_by_xpath('/html/body/header/nav/ul/li[3]/a').click()

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
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 69
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 70
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
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
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 74
browser.find_element_by_xpath('//*[@id="id_property_division_fair"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 75
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 76
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 80
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 81
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 82
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 84
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 86
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 89
browser.find_element_by_xpath('//*[@id="id_petitioner_gross_wages"]').send_keys('125000')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 90
browser.find_element_by_xpath('//*[@id="id_petitioner_gross_income_last_month"]').send_keys('10000')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 91
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 93
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 95
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 97
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 99
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 101
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 103
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 105
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 107
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 109
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 111
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 113
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 115
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 117
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 120
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 122
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 124
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 126
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 128
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 129
browser.find_element_by_xpath('//*[@id="id_petitioner_expenses_type"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="id_petitioner_home_type"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 131
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 133
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/fieldset/div[1]/div[3]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 135
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 136
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 144
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 146
browser.find_element_by_xpath('//*[@id="id_petitioner_receive_welfare"]/option[5]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 147
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 149
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 154
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 155
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 156
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 157
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 159
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 161
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 164
browser.find_element_by_xpath('//*[@id="id_respondent_gross_wages"]').send_keys('95000')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 165
browser.find_element_by_xpath('//*[@id="id_respondent_gross_income_last_month"]').send_keys('8000')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 166
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 168
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 170
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 172
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 174
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 176
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 178
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 180
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 182
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 184
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 186
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 188
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 190
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 192
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 195
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 197
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 199
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 201
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 203
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="id_respondent_expenses_type"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="id_respondent_home_type"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 205
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 207
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/fieldset/div[1]/div[3]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 209
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 210
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 217
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 219
browser.find_element_by_xpath('//*[@id="id_respondent_receive_welfare"]/option[5]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 220
browser.find_element_by_xpath('//*[@id="id_net_income_notice"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 221
browser.find_element_by_xpath('//*[@id="id_non_custodial_who"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 223
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 227
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 230
browser.find_element_by_xpath(
    '//*[@id="id_children_uninsured_health_costs_future_shared_how"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 231
browser.find_element_by_xpath(
    '//*[@id="id_children_uninsured_health_costs_future_shared_percentage"]').send_keys('60')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 232
browser.find_element_by_xpath(
    '//*[@id="id_children_health_insurance_maintain_who"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 233
browser.find_element_by_xpath(
    '//*[@id="id_children_health_insurance_shared_how"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 234
browser.find_element_by_xpath(
    '//*[@id="id_children_health_insurance_shared_percentage"]').send_keys('45')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 235
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 238
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 241
browser.find_element_by_xpath(
    '//*[@id="screen-form"]/fieldset/div[1]/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 243
browser.find_element_by_xpath(
    '//*[@id="id_child_suppot_terminate_option"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 244
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 247 Parenting Class
browser.find_element_by_xpath('//*[@id="skip"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="parentingClassModalConfirmNO"]').click()#Pop up
time.sleep(2)

#Step 248
browser.find_element_by_xpath('//*[@id="id_shared_exp"]/option[4]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_trust_issues"]/option[3]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_physical_custody"]/option[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_second_post_divorce_family"]/option[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_babysitter"]/option[4]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="id_children_age"]/option[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(2)

#Step 249 Same Team
browser.find_element_by_xpath(
    '/html/body/main/div[1]/div[3]/div[1]/div/div[1]/div[3]/label/span[1]').click()
time.sleep(1)
browser.find_element_by_xpath(
    '/html/body/main/div[1]/div[3]/div[1]/div/div[1]/div[4]/input').click()
time.sleep(1)
browser.find_element_by_xpath(
    '/html/body/main/div[1]/div[3]/div[2]/div/div[2]/ul/li[2]/label/span[1]').click()
time.sleep(1)
browser.find_element_by_xpath(
    '/html/body/main/div[1]/div[3]/div[2]/div/div[2]/div[3]/ul/li[6]/label/span[1]').click()
time.sleep(1)
browser.find_element_by_xpath(
    '/html/body/main/div[1]/div[3]/div[2]/div/div[2]/div[5]/input[1]').click()
time.sleep(1)

#Step 250
browser.find_element_by_xpath(
    '//*[@id="id_declaration_of_disclosure_service_date"]').send_keys('12122021')
time.sleep(1)
browser.find_element_by_xpath(
    '//*[@id="id_declaration_of_disclosure_return_date"]').send_keys('12122022')
time.sleep(1)
browser.find_element_by_xpath(
    '//*[@id="id_document_exchange_method"]/option[4]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 251
browser.find_element_by_xpath(
    '//*[@id="id_document_exchange_method_other"]').send_keys('Car')
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 252
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 254
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 255
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 257
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[1]/div[3]/label[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div[2]/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 260
browser.find_element_by_xpath('//*[@id="screen-form"]/fieldset/div/div/div[3]/label[2]').click()
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

#Step 261
browser.find_element_by_xpath('//*[@id="screen-form"]/div/div/button').click()
time.sleep(1)

# Pop up Platinum
browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()
time.sleep(1)

# Pop up Covid - 19
try:
    browser.find_element_by_xpath('//*[@id="covidPremModal"]/div/div/div/div/button').click()
except:
    time.sleep(5)

#Platinum Page
browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div[4]/label').click()
browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div[7]/button').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/header/nav/ul/li[3]/a').click()
time.sleep(2)
# Pop up You have completed all answers required for your case and no additional
# questions need to be answered at this time.
# If you wish to edit your answers, please click Edit Answers
time.sleep(2)
browser.find_element_by_xpath('//*[@id="messageDone"]/div/div/div/button').click()
time.sleep(2)

# Pop up Feedback
time.sleep(5)
browser.find_element_by_xpath('//*[@id="feedbackFormModal"]/div[1]/label[1]').click()
browser.find_element_by_xpath('//*[@id="feedbackFormModal"]/div[2]/label[1]').click()
browser.find_element_by_xpath('//*[@id="feedbackFormModal"]/div[3]/label[1]').click()
browser.find_element_by_xpath('//*[@id="id_improve"]').send_keys('Test_Feedback')
browser.find_element_by_xpath('//*[@id="sendFeedback"]').click()
time.sleep(2)

# Second Pop up
browser.find_element_by_xpath('//*[@id="id_title"]').send_keys('Test')
browser.find_element_by_xpath('//*[@id="id_text"]').send_keys('Test')
browser.find_element_by_xpath('//*[@id="sendReview"]').click()
time.sleep(2)


# Submit
browser.find_element_by_xpath('/html/body/main/div[2]/div[2]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="submitFormConfirmation"]/div/div/div/div/button').click()
time.sleep(2)

# Pop up Shiping
browser.find_element_by_xpath('//*[@id="shippingUpsellModal"]/div/div/div[1]/button/span').click()

# Pop up Expedited
browser.find_element_by_xpath('//*[@id="upgradeModalStep1"]/div[2]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="upgradeModalStep2"]/div/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="upgradeModal"]/div/div/div[1]/button/span').click()
time.sleep(2)

# Pop up Parenting Class
browser.find_element_by_xpath('//*[@id="parentingClassModal"]/div/div/div[1]/button/span').click()


browser.quit()

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
