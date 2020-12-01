def pagePayRS(browser,):

    #Payment

    browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169360004480400')
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[9]').click()
    # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4731185617318578')
    # browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[2]').click()
    # browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[10]').click()
    browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Address1')
    browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('Dnipro')
    browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('49000')
    browser.find_element_by_xpath('//*[@id="id_referrer"]').send_keys('gregrublev13899')
    browser.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div[2]/div/div[1]/form/button').click()