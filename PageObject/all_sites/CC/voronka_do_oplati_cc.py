from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay
from PageObject.OD.payment_plan import payment_plan_od


# -----------------------------------------Screen size--------------------------------------------------------------
browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Chrome()
browser.maximize_window()
link = 'https://www.completecase.com/'
browser.get(link)
browser.implicitly_wait(25)
#def payment_divorce_cc():
    #browser = webdriver.Chrome(ChromeDriverManager().install())
    #browser.maximize_window()
    #link = 'https://staging.completecase.com:8001/'
    #link = 'https://www.completecase.com/'
#browser.get(link)
   # browser.implicitly_wait(25)
   # browser = webdriver.Chrome()
   # browser.maximize_window()
   # link = 'https://www.completecase.com/'
   # browser.get(link)
   # browser.implicitly_wait(25)

email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'

browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]/div/a').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="statesPopupId"]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/a').click()
browser.find_element_by_xpath('//*[@id="begin"]/fieldset/input').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="qualified"]/div/div/div[2]/button').click()

# browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
# browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('first_na')
# browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('last_na')
# browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)

# # Проверка выбранного штата в URL и Select
# selet_state = browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').get_attribute("value")
# state_in_url = browser.current_url
# state_in_url = coupone_url.split('/')
# state_in_url == state_in_url[-2]
# assert state_in_url == selet_state, f"State in URL: {state_in_url[-2]}, State in  field 'Your state of Residence': {selet_state}"
# browser.find_element_by_xpath('//*[@id="begin"]/fieldset/input').click()

# Step 1

browser.find_element_by_xpath('//*[@id="id_you_are"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('FName')
browser.find_element_by_xpath('//*[@id="id_middle_name"]').send_keys('MName')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('LName')
#browser.find_element_by_xpath('//*[@id="id_phone_0"]').send_keys('111')
#browser.find_element_by_xpath('//*[@id="id_phone_1"]').send_keys('111')
#browser.find_element_by_xpath('//*[@id="id_phone_2"]').send_keys('1111')
browser.find_element_by_xpath('//*[@id="id_spouse_first_name"]').send_keys('SFName')
browser.find_element_by_xpath('//*[@id="id_spouse_middle_name"]').send_keys('SMName')
browser.find_element_by_xpath('//*[@id="id_spouse_last_name"]').send_keys('SLName')
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()
#browser.find_element_by_xpath('//*[@id="offerToLoginModal"]/div/div/div[3]/button').click()

# Step 2

browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]/option[2]').click()
date_marridge_month = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]/option[2]').get_attribute("value")
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').send_keys('12')
date_marridge_date = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').get_attribute("value")
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').send_keys('1999')
date_marridge_year = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').get_attribute("value")
browser.find_element_by_xpath('//*[@id="id_city_of_marriage"]').send_keys('CityMarried')
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# ======================
# Back on step 1

# browser.find_element_by_xpath('//*[@id="screenForm"]/div/a').click()
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="offerToLoginModal"]/div/div/div[3]/button').click()
# date_marridge_month_back = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]').get_attribute("value")
# date_marridge_date_back = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').get_attribute("value")
# date_marridge_year_back = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').get_attribute("value")
#
# assert date_marridge_month == date_marridge_month_back,  f"Не сохраняются поле 'Month' в разделе 'Date and Location of Your Marriage'" \
#                                                          f" при нажатии кнопки Back на странице Children and Pregnancy"
# assert date_marridge_date == date_marridge_date_back, f"Не сохраняются поле 'Date' в разделе 'Date and Location of Your Marriage'" \
#                                                          f" при нажатии кнопки Back на странице Children and Pregnancy"
# assert date_marridge_year == date_marridge_year_back, f"Не сохраняются поле 'Year' в разделе 'Date and Location of Your Marriage'" \
#                                                          f" при нажатии кнопки Back на странице Children and Pregnancy"
# browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()
# ======================

# Step 3
browser.find_element_by_xpath('//*[@id="id_number_of_children"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="id_wife_pregnant_primarily"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 4
browser.find_element_by_xpath('//*[@id="id_assets_any"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="id_debts_any"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 5
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()
browser.find_element_by_xpath('//*[@id="id_who_will_file"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 6
browser.find_element_by_xpath('//*[@id="id_live_together_now"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="id_current_home_zip"]').send_keys('111ZIP')
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 7
browser.find_element_by_xpath('//*[@id="id_community_property_divide_equally"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 8
browser.find_element_by_xpath('//*[@id="id_divide_debts"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 9
browser.find_element_by_xpath('//*[@id="id_my_additional_income_sources"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="id_spouse_additional_income_sources"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 10
browser.find_element_by_xpath('//*[@id="id_i_owe_spouse_money"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="id_spouse_owes_me_money"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 11
browser.find_element_by_xpath('//*[@id="id_either_party_military_member"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()

# 12
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
browser.find_element_by_xpath('//*[@id="id_phone_0"]').send_keys('111')
browser.find_element_by_xpath('//*[@id="id_phone_1"]').send_keys('111')
browser.find_element_by_xpath('//*[@id="id_phone_2"]').send_keys('1111')
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div[7]/input').click()
browser.find_element_by_xpath('//*[@id="onlineRegistrationComplete"]/div/div/div[2]/div/div/input').click()
time.sleep(25)
#browser.find_element_by_xpath('//*[@id="onlineRegistrationComplete"]/div/div/div[2]/div/div/input').click()

time.sleep(3)
coupone_url = browser.current_url
new_params = ('?coupon=gregrublev29899')
browser.get(coupone_url + new_params)

# Paymant
browser.find_element_by_xpath('//*[@id="id_ccexp_m"]').click()
browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="id_ccexp_y"]').click()
browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[9]').click()

browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169 3600 0448 0400	')
# browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578')
# browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')

browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')

browser.find_element_by_xpath('//*[@id="mainPaymentForm"]/fieldset/div[2]/div/div[4]/input').click()
browser.find_element_by_xpath('/html/body/main/div[8]/a').click()
time.sleep(5)
#pop up Covid - 19
browser.find_element_by_xpath('//*[@id="covidPremModal"]/div/div/div[2]/div/a').click()

time.sleep(3)
#browser.quit()















