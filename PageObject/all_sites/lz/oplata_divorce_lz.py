from idlelib import browser
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay
from PageObject.OD.payment_plan import payment_plan_od


# -----------------------------------------Screen size--------------------------------------------------------------

#def payment_divorce_lz():
# browser = webdriver.Chrome()
# browser.maximize_window()
# link = 'https://divorce.legalzoom.com/'
# browser.get(link)
# browser.implicitly_wait(25)

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
#link = 'https://staging.completecase.com:8001/'
link = 'https://divorce.legalzoom.com/'
browser.get(link)
browser.implicitly_wait(25)

email = f'testanton35+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@gmail.com'



browser.find_element_by_xpath('//*[@id="state"]').click()
browser.find_element_by_xpath('//*[@id="state"]/option[6]').click()

browser.find_element_by_xpath('//*[@id="submitFormBtn"]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="qualifiedBtn"]').click()

#Step 1

browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div[2]/div/button/div').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div[2]/div/div/div/ul/li[3]/a/span').click()
browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('FName')
browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('LName')
browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="id_spouse_first_name"]').send_keys('SFName')
browser.find_element_by_xpath('//*[@id="id_spouse_last_name"]').send_keys('SLName')
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()


#Step 2

browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]/option[2]').click()
date_marridge_month = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]/option[2]').get_attribute("value")
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').send_keys('12')
date_marridge_date = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').get_attribute("value")
browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').send_keys('1999')
date_marridge_year = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').get_attribute("value")
browser.find_element_by_xpath('//*[@id="id_city_of_marriage"]').send_keys('CityMarried')
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()

# Step 3
browser.find_element_by_xpath('//*[@id="id_number_of_children"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="id_wife_pregnant_primarily"]/option[2]').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()

#4
browser.find_element_by_xpath('//*[@id="id_assets_any"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="id_debts_any"]/option[2]').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()

#5
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div/div[1]/button/div/div/div').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div/div[1]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()

#6
browser.find_element_by_xpath('//*[@id="id_live_together_now"]/option[2]').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()

#7
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div/div[1]/button/div/div/div').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div/div[1]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()

#8
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div/div[1]/button/div/div/div').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div/div[1]/div/div/ul/li[3]/a').click()
browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()



#9
browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
browser.find_element_by_xpath('//*[@id="confirmSummary1"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="confirmSummary2"]').click()

coupone_url = browser.current_url
new_params = ('?coupon=gregrublev49899')
browser.get(coupone_url + new_params)
time.sleep(1)
# Paymant
browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[9]').click()
browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169 3600 0448 0400')
#browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578')
#browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')

browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')
browser.find_element_by_xpath('//*[@id="id_phone"]').send_keys('1111111111')

browser.find_element_by_xpath('//*[@id="paymentForm"]/div[12]/div/input').click()
#                               //*[@id="paymentForm"]/div[12]/div/input

# page_thankyou_actual = browser.find_elements_by_link_text('/html/body/main/div[2]/div/div/div/div[1]').text
# page_thankyou = 'Court filing made easy.'

# assert page_thankyou_actual == page_thankyou, f'Нет страницы Thankyou после оплаты'
time.sleep(5)
browser.find_element_by_xpath('/html/body/main/main/div[9]/a').click()
time.sleep(3)
try:
    browser.find_element_by_xpath('//*[@id="covidPremModal"]/div/div/div[2]/div/a').click()
except:
    time.sleep(2)
browser.find_element_by_xpath('/html/body/main/div/div/section[1]/a').click()
time.sleep(2)
browser.quit()