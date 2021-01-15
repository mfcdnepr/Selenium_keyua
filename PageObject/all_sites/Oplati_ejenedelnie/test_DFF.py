from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay
from PageObject.OD.payment_plan import payment_plan_od


# -----------------------------------------Screen size--------------------------------------------------------------
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
# link = 'https://staging.completecase.com:8001/'
link = 'https://divorceformsfiller.com/'
browser.get(link)
browser.implicitly_wait(25)

#def payment_divorce_df():
    #browser = webdriver.Chrome()
    #browser.maximize_window()
    #link = 'https://divorceformsfiller.com/'
    #browser.get(link)
    #browser.implicitly_wait(25)

email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'

browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('first_na')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('last_na')
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="homeDivorceButton"]').click()

# Processing page
try:
    browser.find_element_by_xpath('//*[@id="next"]').click()
except:
    time.sleep(10)

# Step 1

browser.find_element_by_xpath('//*[@id="funnelForm"]/div[1]/div[1]/div/div[1]/label').click()
browser.find_element_by_xpath('//*[@id="funnelForm"]/div[2]/div[1]/div/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="funnelForm"]/div[3]/div[1]/div/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="funnelForm"]/div[2]/div[2]/div/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="id_date_of_separation"]').send_keys('11111999')
browser.find_element_by_xpath('//*[@id="id_marriage_country"]').send_keys('MCounty')
browser.find_element_by_xpath('//*[@id="id_filing_district"]').send_keys('DCounty')
browser.find_element_by_xpath('//*[@id="submitForm"]').click()

# Step 2

browser.find_element_by_xpath('//*[@id="funnelForm"]/div[1]/div/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="funnelForm"]/div[2]/div/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="submitForm"]').click()

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
browser.find_element_by_xpath('//*[@id="funnelForm"]/div[1]/div/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="submitForm"]').click()

# 4
browser.find_element_by_xpath('//*[@id="id_number_of_children"]/option[5]').click()
browser.find_element_by_xpath('//*[@id="id_wife_pregnant_primarily"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="submitForm"]').click()

# 5
browser.find_element_by_xpath('//*[@id="funnelForm"]/div[2]/div/div[2]/label').click()
browser.find_element_by_xpath('//*[@id="submitForm"]').click()

# 6
browser.find_element_by_xpath('//*[@id="funnelForm"]/div[2]/div/div[2]/label').click()
#browser.find_element_by_xpath('//*[@id="id_has-credit-suffered-as-result-of-marriage"]/option[3]').click()
#browser.find_element_by_xpath('//*[@id="id_check-credit-score-for-free"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="submitForm"]').click()
# 7
browser.find_element_by_xpath('//*[@id="summarySubmit"]').click()

# 8
browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
browser.find_element_by_xpath('//*[@id="id_re_password"]').send_keys('11111')
browser.find_element_by_xpath('//*[@id="submitDetailsForm"]').click()

time.sleep(20)
try:
    browser.find_element_by_xpath('//*[@id="next"]').click()
except:
    time.sleep(1)



coupone_url = browser.current_url
new_params = ('?coupon=gregrublev13899')
browser.get(coupone_url + new_params)

# Paymant
browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[10]').click()
#browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169 3600 0448 0400	')
browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578')
# browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')

browser.find_element_by_xpath('//*[@id="id_street_address_shipping"]').send_keys('Adress1')
browser.find_element_by_xpath('//*[@id="id_city_shipping"]').send_keys('City')
browser.find_element_by_xpath('//*[@id="id_zip_shipping"]').send_keys('111')
browser.find_element_by_xpath('//*[@id="submitForm"]').click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/main/div[7]/a').click()
#browser.find_elements_by_link_text('/html/body/main/div[1]/div/h2').text
#page_thank_you = 'Thank you for your order!'
#page_thank_you_actual = browser.find_elements_by_link_text('/html/body/main/div[1]/div/h2').text
#page_thank_you = 'Thank you for your order!'

#assert page_thank_you_actual == page_thank_you, f'Нет страницы Platinum после оплаты'
time.sleep(3)
browser.quit()

