import time
def pagePay(browser,):
    # if options:
    #     state_main_page = options.get('state_main_page')
    #Копирую урл и добавляю купон
    # coupone_url = browser.current_url
    # new_params = ('?coupon=gregrublev13899')
    # browser.get(coupone_url + new_params)


    # Paymant
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[8]').click()

    # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578')
    browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169 3600 0448 0400 ')
    # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')
    browser.find_element_by_xpath('//*[@id="id_referrer"]').send_keys('gregrublev13899')
    # browser.find_element_by_xpath('//*[@id="id_referrer"]').send_keys('ff32ceaa-3edb-4e82-9839-859aab2c3d89	')
    browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
    browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="payment-form"]/div/div[6]/div[2]/div[1]/div[2]/button').click()
