def pagePay(browser,):
    # if options:
    #     state_main_page = options.get('state_main_page')
    #Копирую урл и добавляю купон
    coupone_url = browser.current_url
    new_params = ('?coupon=gregrublev13899')
    browser.get(coupone_url + new_params)


    # Paymant
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[10]').click()

    #browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731 1856 1731 8578')
    browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')

    browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
    browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')

    browser.find_element_by_xpath('//*[@id="payment-form"]/div/div[5]/div[2]/div[1]/button').click()