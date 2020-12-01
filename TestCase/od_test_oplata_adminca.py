import random
import re
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#from PageObject.Adminca.adminca_od import adminca_od_payment_plan
from PageObject.Adminca.adminca_od import adminca_od_pay_001

from PageObject.OD.edit_answer_on_sammary import edit_answer_on_sammary
from PageObject.OD.pagePay import pagePay
from PageObject.OD.payment_plan import payment_plan_od

# from selenium.common.exceptions import (NoSuchElementException, )
# -----------------------------------------Screen size--------------------------------------------------------------

# links = ['https://www.onlinedivorce.com', 'https://www.onlinedivorce.com/online-divorce-virginia/']
links = []
# ------------------------выбирает из списков по 3 сайта-----------------------------------------------------------------
file_open = open('county_sites.txt')
list_county_sites = file_open.readlines()
short_list_county_sites = random.choices(list_county_sites, k=2)
links.extend(short_list_county_sites)

file_open = open('state_ceo_sites.txt')
list_state_ceo_sites = file_open.readlines()
short_list_state_ceo_sites = random.choices(list_state_ceo_sites, k=2)
links.extend(short_list_state_ceo_sites)


# print(links)
# -----------------------------------------------------------------------------------------------------------------------

# link = 'https://www.onlinedivorce.com'
def process(link):
    browser = webdriver.Chrome(executable_path=ChromeDriverManager('83.0.4103.39').install())
    browser.maximize_window()
    browser.get(link)

    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # browser.get(link)
    browser.implicitly_wait(10)

    answers_funnel = ['first_na', 'last_na', '04/12/1999', '2', 'Your Spouse', 'Together', 'No', 'No', 'No', 'Yes', 'No',
                      'No',]
    answers_summary = []

    email = f'leonid+{"".join(i for i in datetime.now().isoformat() if i.isdigit())}@onlinedivorce.com'
    #print(email)

    # browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').click()
    time.sleep(1)
    #-------------------------в зависимости от URL разные селекторы одного элемента. Код ниже распознает URl и в
    # ------------------------зависимоти от колличестве симоволов выполняет тот или инной код---------------------------
    if len(link) <= 30:
        selected_state = browser.find_element_by_xpath('//*[@id="id_state_of_filing"]/option[47]')
        state_main_page = selected_state.get_attribute("value")
        selected_state.click()
        state_main_page = [state_main_page.title()]
        answers_funnel.extend(state_main_page)

        # print(selected_state)
    else:
        # selected_state = browser.find_element_by_xpath('//*[@id="id_state_of_filing"]').getAtttribute()
        state_main_page = str(
            Select(browser.find_element_by_xpath('//*[@id="id_state_of_filing"]')).first_selected_option.text)
        state_main_page = [state_main_page]
        answers_funnel.extend(state_main_page)
        # print(state_main_page)
        # print(answers_funnel)

    browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('first_na')
    browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('last_na')
    browser.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    # state_main_page = selected_state.get_attribute("value")
    # state_main_page = state_main_page.title()
    # print(selected_state)

    first_name_main_page = [browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")]
    last_name_main_page = [browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")]

    email_main_page = email

    # browser.find_element_by_class_name("//input[@class='btn w-100']").click()
    try:
        lnk111 = browser.find_element_by_xpath('//*[@id="beginForm"]/button')
    except:
        lnk111 = browser.find_element_by_xpath('//*[@id="begin"]/div[7]/div/input')
    print(lnk111)
    lnk111.click()

    # isPresent = driver.findElements(By.yourLocator).size() > 0

    # Step 2
    time.sleep(2)
    # try:
    #     lnk11 = browser.find_element_by_xpath(
    #     '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[2]/div/div/div/button').click()
    #     browser.find_element_by_xpath(
    #         '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[2]/div/div/div/div/ul/li[5]/a/span[1]').click()
    #
    # except:
    #     lnk11 = browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/button').click()
    #     browser.find_element_by_xpath(
    #         '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/button').click()
    # lnk11.click()

    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/button').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/div/div/ul/li[5]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_1"]').send_keys('12')
    browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').send_keys('1999')


    # answers_funnel.extend()
    # answers_funnel.extend(browser.find_element_by_xpath('//*[@id="id_date_of_marriage_2"]').get_attribute(value))
    # print(answers_funnel)
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 3
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[4]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button').get_attribute("title")
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 4

    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 5

    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 6

    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 7

    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 8

    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 9
    try:
        browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button').click()
    except:
        browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button').click()
        browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[1]').click()
        browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button').click()
        browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a').click()



    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[3]/a/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 10

    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[1]/div[3]/div/div/ul/li[2]/a/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div[2]/div[3]/div/div/ul/li[3]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 11

    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="screen-form"]/div[1]/div/fieldset/div[1]/div/div[3]/div/div/ul/li[3]/a/span[1]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()
    #browser.find_element_by_xpath('//*[@id="screen-form"]/div[1]/div/fieldset/div[2]/input').click()

    # Step 12

    # ----------------------------Записываю в пирименную все значения которые есть на странице саммари------------------

    state_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/span').text
    print(state_summary)

    # -----Удаляю дифис в названии штата----------------------
    del_line = re.compile("[^a-zA-Zа-яА-я,\d]")
    state_summary = del_line.sub(" ", state_summary)

    # --------------Записываю все данные на странице Саммари-------------------------------------------
    answers_summary.append(state_summary)
    first_name_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[1]').text
    answers_summary.append(first_name_summary)
    last_name_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[2]').text
    answers_summary.append(last_name_summary)
    date_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[3]/div[2]/span').text
    answers_summary.append(date_summary)
    children_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[4]/div[2]/span').text
    answers_summary.append(children_summary)
    property_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[5]/div[2]/span').text
    answers_summary.append(property_summary)
    petitioner_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[6]/div[2]/span').text
    answers_summary.append(petitioner_summary)
    current_home_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[7]/div[2]/span').text
    answers_summary.append(current_home_summary)
    community_property_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[8]/div[2]/span').text
    answers_summary.append(community_property_summary)
    community_debts_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[9]/div[2]/span').text
    answers_summary.append(community_debts_summary)
    income_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[10]/div[2]/span').text
    answers_summary.append(income_summary)
    money_owed_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[11]/div[2]/span').text
    answers_summary.append(money_owed_summary)
    military_summary = browser.find_element_by_xpath('//*[@id="step13"]/div[12]/div[2]/span').text
    answers_summary.append(military_summary)

    #------------Проверяю введенные значения в воронке и значения которые показываются на Саммари----------------------
    assert set(answers_summary) == set(answers_funnel), f'В воронке значения: {answers_funnel},\n ' \
        f'а на саммари: {answers_summary}'


    # ----------------------------Меняю значения на странице саммари ---------------------------------------------------------
    state_summary_changed, last_name_summary_changed, first_name_summary_changed = edit_answer_on_sammary(browser, time)
    state_summary_changed = [state_summary_changed]
    print(state_summary_changed)

    # ------------------------------------------------------------------------------------------------------------------

    browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    time.sleep(3)
    #browser.find_element_by_xpath('//*[@id="screen-form"]/div/div[2]/div[2]/input').click()

    try:
        browser.find_element_by_xpath('//*[@id="screen-form"]/div/div[2]/div[2]/input').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="number1"]').send_keys('111')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="number2"]').send_keys('111')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="number3"]').send_keys('1111')

        fone_1 = browser.find_element_by_xpath('//*[@id="number1"]').get_attribute("value")
        fone_2 = browser.find_element_by_xpath('//*[@id="number2"]').get_attribute("value")
        fone_3 = browser.find_element_by_xpath('//*[@id="number3"]').get_attribute("value")
        fone_main = fone_1 + fone_2 + fone_3
        browser.find_element_by_xpath('//*[@id="save-phone-js"]').click()

        # -----Удаляю дифис в телефоне----------------------
        del_line = re.compile("[^a-zA-Zа-яА-я,\d]")
        fone_main = del_line.sub("", fone_main)

    except:
        browser.find_element_by_xpath('//*[@id="id_phone"]').send_keys('1111111111')
        browser.find_element_by_xpath('//*[@id="screen-form"]/div/div[2]/div[3]/input').click()
        fone_main = browser.find_element_by_xpath('//*[@id="id_phone"]').get_attribute("value")

    # Pop up number fone

    # Записываю данные в переменную, которую передам при проверке данных в админке.
    data = {
        'fone_main': fone_main,
        'state_summary_changed': state_summary_changed,
        'last_name_summary_changed': last_name_summary_changed,
        'first_name_summary_changed': first_name_summary_changed,
        'email': email,
    }

    time.sleep(3)
    # Выдает случайное число. Было сделано для того что бы отрабатывал код ниже. если парное число то работает пеймент
    #план, а если не парное, то покупает диворс по купону.
    # data['browser'] = browser
    # x = randint(0, 10)

    x = 1
    print(x)
    if x % 2 == 0:
        payment_plan_od(browser, data)
    else:
        pagePay(browser,)
        # coupone_url = browser.current_url
        # new_params = ('?coupon=gregrublev13899')
        # browser.get(coupone_url + new_params)
        #
        #     # Paymant
        # browser.find_element_by_xpath('//*[@id="id_ccexp_m"]').click()
        # #
        # browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[2]').click()
        # browser.find_element_by_xpath('//*[@id="id_ccexp_y"]').click()
        # browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[10]').click()
        #
        # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5169 3600 0448 0400')
        # #browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111	')
        #
        #
        # browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
        # browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
        # browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')
        #
        # #browser.find_element_by_xpath('//*[@id="payment-form"]/div/div[5]/div[2]/div[1]/div/button').click()
        # browser.find_element_by_xpath('//*[@id="payment-form"]/div/div[5]/div[2]/div[1]/button').click()

        # Buying Platinum
        # browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div[2]/div[5]/button').click()
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="event-purchase-content"]/div/div/div/div[3]/a').click()
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div/div/div[2]/label[1]/span[2]').click()
        # browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div/div/div[3]/label[1]/span[2]').click()
        # browser.find_element_by_xpath('//*[@id="platinumLocation"]/div/div/div[2]/div/div/div[5]/a').click()

        # Skip Platinum
        # browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[3]/div/div/div/small/a').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="covidPremModal"]/div/div/div/div/a').click()

        # Skip Buying WILL
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="willModalStep1"]/button/span/i').click()
        # else:
        #     time.sleep(10)
        #     #Skip Buying WILL
        #     browser.find_element_by_xpath('//*[@id="willModalStep1"]/button/span/i').click()

        # #Buying WILL
        # #browser.find_element_by_xpath('//*[@id="willModalStep1"]/div[6]/div[2]/button').click()
        time.sleep(5)
        browser.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div[2]/a[1]').click()
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="welcomeModal"]/div/div/div[1]/button/span').click()

        # info_pop_up_partial_access = browser.find_element_by_xpath('/html/body/header/div[3]/p').text
        # info_pop_up_partial_access_expected = 'You have partial access to our platform. Please pay for the service to receive full access to your documents.'
        # assert info_pop_up_partial_access == info_pop_up_partial_access_expected, f'Актуальный результат: {info_pop_up_partial_access}, \n' \
        #                                                                         f'Ожидаемый результат{info_pop_up_partial_access_expected}           '
        # Welcom
        time.sleep(5)
        browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/a').click()
        # Voronka
        # if state_summary_changed == ['Florida']:
        #     browser.find_element_by_xpath('//*[@id="id_petitioner_who"]/option[3]').click()
        # else:
        #     browser.find_element_by_xpath('//*[@id="id_divorce_petitioner_who"]/option[2]').click()
        # browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()
        time.sleep(3)
        browser.quit()

    # В зависимости от случайного числа работают разные проверки в админке.
    if x % 2 == 0:
        adminca_od_payment_plan(browser, data)
    else:
        adminca_od_pay_001(browser, data)

# Когда цикл проходит успешно то в консоли выводится: Done: ', link
for link in links:
    process(link)
    print('Done: ', link)
