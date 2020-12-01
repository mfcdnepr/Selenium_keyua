from selenium import webdriver
import time
import re
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
link = 'https://staging.completecase.com:8003/'
# link = 'https://www.onlinedivorce.com'
browser.get(link)
browser.implicitly_wait(25)

browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[10]/a').click()