import random
import re
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#__________________Screen size_______________________



links = []
file_open = open('regional_sites.txt', mode='r', encoding='latin_1')
list_regional_sites = file_open.readlines()
short_list_regional_sites = random.choices(list_regional_sites, k=2)
links.extend(short_list_regional_sites)





