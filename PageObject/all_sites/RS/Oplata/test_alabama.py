from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.all_sites.RS.Oplata.pagePayRS import pagePayRS

#____________________________________Screen___________________________________________________

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
link = 'https://alabamaonlinedivorce.com/'
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
time.sleep(2)
#Payment

pagePayRS(browser, )


#Platinum/Vip page
try:
    browser.find_element_by_xpath('/html/body/main/main/div[5]/a').click()
except:
    browser.find_element_by_xpath('/html/body/main/main/div/div[1]/a').click()

browser.quit()


#Tunel after payment

#time.sleep(2)
#Pop up "Prepare your will"

#browser.find_element_by_xpath('//*[@id="willModal"]/div/div/button/span').click()

#Thank you page

#browser.find_element_by_xpath('/html/body/main/section/div/div[2]/div/a').click()

#Modal window Welcom

#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="welcomeModal"]/div/div/button/span').click()

#Case Progress

#browser.find_element_by_xpath('//*[@id="progressStep1"]/div[2]/div/div[2]/div[3]/button').click()

#Step 14

#* Who will be the petitioning party in this action?
#browser.find_element_by_xpath('//*[@id="id_divorce_petitioner_who"]/option[2]').click()
#* Will the grounds for divorce be no-fault?
#browser.find_element_by_xpath('//*[@id="id_divorce_grounds"]/option[2]').click()
#browser.find_element_by_xpath('//*[@id="screenForm"]/div[2]/div/div/button').click()

#Step 15

#* In what county are you going to file your case?
#browser.find_element_by_xpath('//*[@id="id_venue"]').send_keys('Alupka')
#* In what city are you going to file your case?
#browser.find_element_by_xpath('//*[@id="id_venue_city"]').send_keys('Alupka city')
#* Which spouse lives in the state where you will be filing your case?
#browser.find_element_by_xpath('//*[@id="id_state_resident_who"]/option[3]').click()
#browser.find_element_by_xpath('//*[@id="screenForm"]/div[2]/div/div/button').click()
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="idFirstLowerWarning"]/div/div/div[2]/button[2]').click()
#time.sleep(2)


#Step 17

#* How long has the husband lived in the state where you will be filing your case?
#browser.find_element_by_xpath('//*[@id="id_husband_state_residence_length"]').send_keys('6 months')
#* How long has the husband lived in the county where you will be filing your case?
#browser.find_element_by_xpath('//*[@id="id_husband_county_residence_length"]').send_keys('6 months')
#browser.find_element_by_xpath('//*[@id="screenForm"]/div[2]/div/div/button').click()
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="idFirstLowerWarning"]/div/div/div[2]/button[2]').click()
#time.sleep(2)


#Step 18

#time.sleep(2)
#* How long has the wife lived in the state where you will be filing your case?
#browser.find_element_by_xpath('//*[@id="id_wife_state_residence_length"]').send_keys('6 months')
#* How long has the wife lived in the county where you will be filing your case?
#browser.find_element_by_xpath('//*[@id="id_wife_county_residence_length"]').send_keys('6 months')
#browser.find_element_by_xpath('//*[@id="screenForm"]/div[2]/div/div/button').click()
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="idFirstLowerWarning"]/div/div/div[2]/button[2]').click()
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="idFirstLowerWarning"]/div/div/div[2]/button[2]').click()

#Step 19

#* Are you the husband or the wife?
#browser.find_element_by_xpath('//*[@id="id_husband_or_wife"]/option[1]').click()
#* What is your social security number?
#browser.find_element_by_xpath('//*[@id="id_petitioner_ssn"]').send_keys('13579')
#* What is your driver's license number?
#browser.find_element_by_xpath('//*[@id="id_petitioner_dol"]').send_keys('246810')
#* What state issued your driver's license?
#browser.find_element_by_xpath('//*[@id="id_petitioner_dol_state"]').send_keys('258852')
#* What is your date of birth?
#browser.find_element_by_xpath('//*[@id="id_petitioner_dob"]').send_keys('01011990')
#* How old are you?
#browser.find_element_by_xpath('//*[@id="id_petitioner_age"]').send_keys('30')
#* What is your address?
#browser.find_element_by_xpath('//*[@id="id_petitioner_address_0"]').send_keys('Karla Marksa')
#browser.find_element_by_xpath('//*[@id="id_petitioner_address_3"]').send_keys('Dnipro')
#browser.find_element_by_xpath('//*[@id="id_petitioner_address_4"]').click()
#browser.find_element_by_xpath('//*[@id="id_petitioner_address_4"]/option[2]').click()
#browser.find_element_by_xpath('//*[@id="id_petitioner_address_5"]').send_keys('49000')
#* Which county do you reside in?
#browser.find_element_by_xpath('//*[@id="id_petitioner_address_county"]').send_keys('Yes')
#* What is your telephone number?
#browser.find_element_by_xpath('//*[@id="id_petitioner_phone"]').send_keys('7777777777')
#* Are you in the military?
#browser.find_element_by_xpath('//*[@id="screenForm"]/div[1]/div/fieldset/div/div[11]/div[3]/label[2]').click()
#* Are you employed?
#browser.find_element_by_xpath('//*[@id="screenForm"]/div[1]/div/fieldset/div/div[12]/div[3]/label[2]').click()
#browser.find_element_by_xpath('//*[@id="screenForm"]/div[2]/div/div/button').click()

#Step 21
#time.sleep(2)
#Pop up "Premium Subscription"
#browser.find_element_by_xpath('//*[@id="closeModal"]/span').click()
