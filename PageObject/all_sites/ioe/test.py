from PageObject.all_sites.ioe.oplata_divorce_ioe import browser
from selenium.common.exceptions import NoSuchElementException


def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True