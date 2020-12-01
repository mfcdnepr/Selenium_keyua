from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from PageObject.OD.pagePay import pagePay
from PageObject.OD.payment_plan import payment_plan_od


# -----------------------------------------Screen size--------------------------------------------------------------

#=============================== Код практически не актуален.========================================================

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
# # link = 'https://staging.completecase.com:8001/'
link = 'https://divorce.itsovereasy.com/'
browser.get(link)
browser.implicitly_wait(25)


def payment_divorce_ioe():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    link = 'https://divorce.itsovereasy.com/'
    browser.get(link)
    browser.implicitly_wait(25)


    email = f'leonid+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@onlinedivorce.com'

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
    browser.find_element_by_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/button/div').click()
    browser.find_element_by_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div/div/ul/li[6]/a').click()
    browser.find_element_by_xpath('//*[@id="submitFormBtn"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="qualifiedBtn"]').click()

    #Step 1


    browser.find_element_by_xpath('//*[@id="id_you_are"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('FName')
    browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('LName')
    browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    browser.find_element_by_xpath('//*[@id="id_spouse_first_name"]').send_keys('SFName')
    browser.find_element_by_xpath('//*[@id="id_spouse_last_name"]').send_keys('SLName')
    time.sleep(2)


    # def check_exists_by_xpath(xpath):
    #     from selenium.common.exceptions import NoSuchElementException
    #     try:
    #         browser.find_element_by_xpath(xpath)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    #
    # if check_exists_by_xpath('/html/body/main/div[4]/section/form/div/button'):
    #     browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    # else:
    #     browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()


    try:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()

    #Step 2

    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]/option[2]').click()
    date_marridge_month = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]/option[2]').get_attribute("value")
    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').send_keys('12')
    date_marridge_date = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').get_attribute("value")
    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').send_keys('1999')
    date_marridge_year = browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').get_attribute("value")
    browser.find_element_by_xpath('//*[@id="id_city_of_marriage"]').send_keys('CityMarried')
    try:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    '''
    #browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    # Step 3
    browser.find_element_by_xpath('//*[@id="id_number_of_children"]/option[6]').click()
    browser.find_element_by_xpath('//*[@id="id_wife_pregnant_primarily"]/option[2]').click()
    try:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #4
    browser.find_element_by_xpath('//*[@id="id_assets_any"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_debts_any"]/option[2]').click()
    try:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #5
    try:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/fieldset/div/div[1]/button/div').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/fieldset/div/div[1]/button/div/div/div').click()
    
    browser.find_element_by_xpath('/html/body/main/div[3]/section/form/fieldset/div/div[1]/div/div/ul/li[2]/a/span').click()
    try:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #6
    browser.find_element_by_xpath('//*[@id="id_live_together_now"]/option[2]').click()
    try:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #7
    browser.find_element_by_xpath('/html/body/main/div[3]/section/form/fieldset/div/div[1]/button/div').click()
    browser.find_element_by_xpath('/html/body/main/div[3]/section/form/fieldset/div/div[1]/div/div/ul/li[3]/a').click()
    try:
        browser.find_element_by_xpath('/html/body/main/div[4]/section/form/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #browser.find_element_by_xpath('/html/body/main/div[3]/section/form/div/button').click()
    
    #8
    browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    browser.find_element_by_xpath('//*[@id="confirmSummary1"]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="confirmSummary2"]').click()
    
    # #9
    # browser.find_element_by_xpath('//*[@id="id_my_additional_income_sources"]/option[2]').click()
    # browser.find_element_by_xpath('//*[@id="id_spouse_additional_income_sources"]/option[3]').click()
    # browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()
    #
    # #10
    # browser.find_element_by_xpath('//*[@id="id_i_owe_spouse_money"]/option[2]').click()
    # browser.find_element_by_xpath('//*[@id="id_spouse_owes_me_money"]/option[2]').click()
    # browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()
    #
    # #11
    # browser.find_element_by_xpath('//*[@id="id_either_party_military_member"]/option[3]').click()
    # browser.find_element_by_xpath('//*[@id="screenForm"]/div/input').click()
    #
    # #12
    # browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    # browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    # browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div[7]/input').click()
    # browser.find_element_by_xpath('//*[@id="onlineRegistrationComplete"]/div/div/div[2]/div/div/input').click()
    # time.sleep(3)
    # browser.find_element_by_xpath('//*[@id="onlineRegistrationComplete"]/div/div/div[2]/div/div/input').click()
    
    browser.find_element_by_xpath('//*[@id="welcomeInviteUserModal"]/div/div/div[1]/button/span').click()
    browser.find_element_by_xpath('/html/body/header/div/div/div/div/div[2]/a').click()
    time.sleep(1)
    '''
    browser.get('https://divorce.itsovereasy.com/payment/california/')
    coupone_url = browser.current_url
    new_params = ('?coupon=gregrublev149999')
    browser.get(coupone_url + new_params)

    # Paymant
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[9]').click()
    browser.find_element_by_xpath('//*[@id="id_cvv"]').send_keys('111')

    browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169 3600 0448 0400')
    #browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578')
    # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')

    browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
    browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')
    browser.find_element_by_xpath('//*[@id="id_phone"]').send_keys('1111111111')
    browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    try:
        browser.find_element_by_xpath('//*[@id="paymentForm"]/div[12]/div/button').click()
    except NoSuchElementException:
        browser.find_element_by_xpath('//*[@id="paymentForm"]/div[15]/div/button').click()
    browser.find_element_by_xpath('/html/body/main/div/div/div[1]/a').click()
    # page_thankyou_actual = browser.find_elements_by_link_text('/html/body/main/div[2]/div/div/div/div[1]').text
    # page_thankyou = 'Court filing made easy.'
    #
    # assert page_thankyou_actual == page_thankyou, f'Нет страницы Thankyou после оплаты'
    time.sleep(5)
    browser.quit()















