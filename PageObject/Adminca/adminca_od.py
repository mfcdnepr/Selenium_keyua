#import day as day
from selenium import webdriver
import time
import re
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from datetime import timedelta


def adminca_od_pay_001(browser, data):
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # # link = 'https://staging.completecase.com:8001/admin/login/?next=/admin/'
    link = 'https://www.completecase.com/admin/login/?next=/admin/'
    # browser.get(link)
    # browser.implicitly_wait(10)

    #Скачивает конкретные драйвер и устанавливает его
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)
    # _____________________________Live____________________________________________________________________
    # browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('cmo0lkamd0jqflzrm49u6yin601kc1wn')
    # browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    # browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    # browser.implicitly_wait(10)
    # _____________________________________________________________________________________________________
    browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('zeleniyanton@gmail.com')
    browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('Niqepoccoqu')
    browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)

    # Поиск созданного юзера
    browser.find_element_by_xpath('//*[@id="search"]').send_keys(data['email'])
    browser.find_element_by_xpath('//*[@id="submit"]').click()

    # ---для лайва. Получаю данные которые записаны в админке ---
    browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()
    # browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()
    time.sleep(3)
    first_name = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
    last_name = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
    number_fone = browser.find_element_by_xpath('//*[@id="id_phone"]').get_attribute("value")
    state = browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[5]/div[2]/div[1]/div').text
    fone_main = data['fone_main']

    # -----Удаляю дифис в телефоне----------------------
    del_line = re.compile("[^a-zA-Zа-яА-я,\d]")
    fone_main = del_line.sub("", fone_main)

    state_summary_changed = data['state_summary_changed'][0]
    print(state_summary_changed)
    first_name_summary_changed_data = data['first_name_summary_changed']
    last_name_summary_changed_data = data['last_name_summary_changed']

    # Проверка вводных значений с записаными в админке
    assert state_summary_changed == state, f"State in Admin: {state}, State Divirce: {state_summary_changed}"
    assert first_name_summary_changed_data == first_name, f"Pokazyvayet: {first_name}, a dolzhen bít: {first_name_summary_changed_data}"
    assert last_name_summary_changed_data == last_name, f"Pokazyvayet: {last_name}, a dolzhen bít: {last_name_summary_changed_data}"
    assert fone_main == number_fone, f"Pokazyvayet: {number_fone}, a dolzhen bít: {fone_main}"
    #browser.find_elements_by_class_name('text')

# ----------------------------Отправка комента в HelpScout (нужно добавить пермишены админовскому юзеру )------------------------------------------------------------
#     help_scout_subject = 'Autotest'
#     browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/a[1]').click()
#     send_help_scout_subject = browser.find_element_by_xpath(
#         '//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/input')
#     send_help_scout_subject.send_keys(help_scout_subject)
#     time.sleep(0.5)
#     send_help_scout_body = browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/textarea')
#     send_help_scout_body.send_keys(help_scout_subject)
#     time.sleep(0.5)
#     browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/ng-form/button').click()
#     time.sleep(5)
#     #сделать проверку на оставление комента
#     help_scout_subject_actual = browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[17]/div/div[3]/div/div/a').text
#     assert help_scout_subject_actual == help_scout_subject, f'Актуальный результат: {help_scout_subject_actual}, ' \
#                                                            f'Ожидаемый результат: {help_scout_subject}'
    browser.quit()

'''
# Код для проверки данных в админке при условии что диворс куплен через пеймент план

def adminca_od_payment_plan(browser, data):
    #--------------------Admin-----------------------------------------------------
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # #link = 'https://staging.completecase.com:8001/admin/login/?next=/admin/'
    link = 'https://www.completecase.com/admin/login/?next=/admin/'
    # browser.get(link)
    # browser.implicitly_wait(10)

    browser = webdriver.Chrome(executable_path=ChromeDriverManager("80.0.3987.106").install())
    browser.maximize_window()
    browser.get(link)



    #_____________________________Live____________________________________________________________________
    # browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('cmo0lkamd0jqflzrm49u6yin601kc1wn')
    # browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    # browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    # browser.implicitly_wait(10)
    #_____________________________________________________________________________________________________
    browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('leonid.keyua@gmail.com')
    browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="search"]').send_keys(data['email'])
    browser.find_element_by_xpath('//*[@id="submit"]').click()

    #---для лайва---
    browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()
    #browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()

    first_name = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
    last_name = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
    number_fone = browser.find_element_by_xpath('//*[@id="id_phone"]').get_attribute("value")
    state = browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[5]/div[2]/div[1]/div').text
    fone_main = data['fone_main']

    state_summary_changed = data['state_summary_changed'][0]
    print(state_summary_changed)
    assert state_summary_changed == state, f"State in Admin: {state}, State Divirce: {state_summary_changed}"
    assert data['first_name_summary_changed'] == first_name, f"Pokazyvayet: {first_name}, a dolzhen bít: {data['first_name_summary_changed']}"
    assert data['last_name_summary_changed]' == last_name, f"Pokazyvayet: {last_name}, a dolzhen bít: {data['last_name_summary_changed']}"
    #assert fone_main == number_fone, f"Pokazyvayet: {number_fone}, a dolzhen bít: {fone_main}"
    #browser.find_elements_by_class_name('text')

    # ----------------------------Отправка комента в HelpScout------------------------------------------------------------
    browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[16]/div/div[3]/a[1]').click()
    send_help_scout_subject = browser.find_element_by_xpath(
        '//*[@id="user_form"]/div/fieldset[16]/div/div[3]/ng-form/input')
    send_help_scout_subject.send_keys('Autotest')
    send_help_scout_body = browser.find_element_by_xpath(
        '//*[@id="user_form"]/div/fieldset[16]/div/div[3]/ng-form/textarea')
    send_help_scout_body.send_keys('Autotest')
    browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[16]/div/div[3]/ng-form/button').click()

    # ----------------------Проверка DIVORCE CASES в Админке------------------------------------------------------------

    status_divorce = 'Partial access'
    status_divorce_in_admin = browser.find_element_by_xpath('//*[@id="divorcecase_set-0"]/fieldset/div[1]/div/div').text
    assert status_divorce == status_divorce_in_admin, f'Статус Divorce case: {status_divorce_in_admin}, адолжен быть {status_divorce} '

    # ----------------------Проверка Order в Админке  ------------------------------------------------------------------
    pp_first_payment_for_admin = (date + day).strftime("%m/%d/%Y")
    pp_second_payment_for_admin = (day_1 + week).strftime("%m/%d/%Y")
    pp_third_payment_for_admin = (day_1 + week_2).strftime("%m/%d/%Y")
    payment_plan_info_expected = f'Amount: $46.34, Automated Date {pp_first_payment_for_admin}, Amount: $46.34, Paid: None\n' \
        f'Amount: $46.33, Automated Date {pp_second_payment_for_admin}, Amount: $46.33, Paid: None\n' \
        f'Amount: $46.33, Automated Date {pp_third_payment_for_admin}, Amount: $46.33, Paid: None'
    display_order_items_expected = 'Divorce: $139.00'

    browser.find_element_by_xpath('//*[@id="fieldsetcollapser5"]').click()
    payment_plan_info = browser.find_element_by_xpath('//*[@id="orders-0"]/fieldset/div[8]/div/div').text
    assert payment_plan_info == payment_plan_info_expected, f'Актуальный результат: \n{payment_plan_info},\n ' \
        f'ожидаемый результат \n{payment_plan_info_expected}'
    display_order_items = browser.find_element_by_xpath('//*[@id="orders-0"]/fieldset/div[3]/div/div').text
    assert display_order_items_expected == display_order_items, f'Актуальный результат: \n{display_order_items},\n' \
        f'ожидаемый результат{display_order_items_expected}'

    browser.quit()
    return text_pop_up_payment_plan

'''


