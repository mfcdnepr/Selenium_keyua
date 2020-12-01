import time

def voronka_posle_oplati_CA_OD_S_Platinum(browser,):

    try:
        browser.find_element_by_xpath('//*[@id="covidPremModal"]/div/div/div/div/a').click()
    except:
        browser.find_element_by_xpath('//*[@id="closeModal"]/span').click()

    browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/a').click()
    browser.find_element_by_xpath('//*[@id="welcomeModal"]/div/div/div[1]/button/span').click()
    browser.find_element_by_xpath('/html/body/header/nav/ul/li[3]/a').click()
    time.sleep(1)