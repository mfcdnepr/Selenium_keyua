from datetime import datetime

from selenium import webdriver
import time


# -----------------------------------------Screen size--------------------------------------------------------------
# browser = webdriver.Chrome(executable_path=ChromeDriverManager("80.0.3987.106").install())
# browser.maximize_window()
# link = 'https://onlinedivorcesolutions.com'
# browser.get(link)
# browser.implicitly_wait(25)

def payment_divorce_osd():
    browser = webdriver.Chrome()
    browser.maximize_window()
    link = 'https://onlinedivorcesolutions.com'
    browser.get(link)
    browser.implicitly_wait(25)


    email = f'leonid+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@onlinedivorce.com'
    states = ['//*[@id="id_state_of_filing"]/option[3]', '//*[@id="id_state_of_filing"]/option[3]'],

    browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[6]').click()
    browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('first_na')
    browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('last_na')
    browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    browser.find_element_by_xpath('//*[@id="mainFormWrapper"]/form/button').click()

    # Step 2
    browser.find_element_by_xpath('// *[ @ id = "id_date_of_marriage_0"]').click()
    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_0"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').send_keys('12')
    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').send_keys('1999')
    browser.find_element_by_xpath('//*[@id="stepForm"]/button').click()

    # Step 3
    browser.find_element_by_xpath('//*[@id="id_number_of_children"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_wife_pregnant_primarily"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="stepForm"]/button').click()

    # Step 4

    browser.find_element_by_xpath('//*[@id="id_assets_any"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_debts_any"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="stepForm"]/button').click()

    # Step 5

    browser.find_element_by_xpath('//*[@id="id_who_will_file"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="stepForm"]/button').click()


    # Step 6

    browser.find_element_by_xpath('//*[@id="id_my_additional_income_sources"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="id_spouse_additional_income_sources"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="stepForm"]/button').click()


    # Step 7

    browser.find_element_by_xpath('//*[@id="id_either_party_military_member"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="stepForm"]/button').click()

    # Step 8

    browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    browser.find_element_by_xpath('//*[@id="stepForm"]/div[1]/button').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="popupPhone"]/div/div/div[2]/div/a/u').click()

    #_______________________________________________________________________________________________________________________
    coupone_url = browser.current_url
    new_params = ('?coupon=gregrublev13899')
    browser.get(coupone_url + new_params)

    # Paymant
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[9]').click()


    browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169 3600 0448 0400	')
    #browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578')
    # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')

    browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
    browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')

    browser.find_element_by_xpath('//*[@id="paymentForm"]/div[2]/div[7]/button').click()
    time.sleep(2)
    browser.quit()
    #_______________________________________________________________________________________________________________________

    #Skip Platinum
    #browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/div/div/div/small/a').click()
    #browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()
