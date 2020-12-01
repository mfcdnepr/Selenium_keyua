import time

def voronka_posle_oplai_CA_bez_Pl(browser, ):
    # browser.find_element_by_xpath('//*[@id="premiumExpModal"]/div/div/div[1]/button/span').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="welcomeModal"]/div/div/div[1]/button/span').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/header/nav/ul/li[3]/a').click()
    time.sleep(1)
