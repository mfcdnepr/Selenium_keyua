from selenium.webdriver.chrome import webdriver
from datetime import datetime
from datetime import timedelta
import time


def payment_plan_od(browser, data):
    # Paymant
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]').click()
    #browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[8]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_m"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]').click()
    #browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[6]').click()
    browser.find_element_by_xpath('//*[@id="id_ccexp_y"]/option[10]').click()

    browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_key
    browser.find_element_by_xpath('//*[@id="id_addr1"]').send_keys('Adress1')
    browser.find_element_by_xpath('//*[@id="id_city"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_zip"]').send_keys('111')
    s('4731 1856 1731 8578')
    # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('5375 4141 0434 0475')
    # browser.find_element_by_xpath('//*[@id="id_ccnum"]').send_keys('4111 1111 1111 1111')

    #browser.find_element_by_xpath('//*[@id="payment-form"]/div/div[5]/div[2]/div[1]/div/button').click()
    browser.find_element_by_xpath('//*[@id="payment-form"]/div/div[5]/div[2]/div[1]/button').click()

    time.sleep(5)
    #_____________Текст на поп апе пеймент плана актуальный__________________________

    actual_payment_plan_pop_up_text_1 = browser.find_element_by_xpath('//*[@id="modalPaymentPlan"]/div/div/div/div/h2').text
    actual_payment_plan_pop_up_text_2 = browser.find_element_by_xpath('//*[@id="modalPaymentPlan"]/div/div/div/div/p[2]').text
    actual_payment_plan_pop_up_text_3 = browser.find_element_by_xpath('//*[@id="modalPaymentPlan"]/div/div/div/div/p[3]').text
    #_______________________________________

    #_____________Текст на поп апе пеймент плана ожидаемый__________________________
    payment_plan_pop_up_text_1 = 'Sorry, your payment for $139.00 didn’t go through.'
    payment_plan_pop_up_text_2 = 'You can choose a comfortable monthly payment plan.'
    payment_plan_pop_up_text_3 = "No hidden commissions, you lose nothing.\n" \
                                 "We’re here for you!"
    #_______________________________________

    assert actual_payment_plan_pop_up_text_1 == payment_plan_pop_up_text_1, f'Показывает: {actual_payment_plan_pop_up_text_3}, \n' \
                                                                            f'а должно быть: {payment_plan_pop_up_text_3}'
    assert actual_payment_plan_pop_up_text_2 == payment_plan_pop_up_text_2, f'Показывает: {actual_payment_plan_pop_up_text_3}, \n' \
                                                                            f'а должно быть: {payment_plan_pop_up_text_3}'
    assert actual_payment_plan_pop_up_text_3 == payment_plan_pop_up_text_3, f'Показывает: {actual_payment_plan_pop_up_text_3}, \n' \
                                                                            f'а должно быть: {payment_plan_pop_up_text_3}'

    text_pop_up_payment_plan = browser.find_element_by_xpath('//*[@id="modalPaymentPlan"]/div/div/div/div/h2').text

    browser.find_element_by_xpath('//*[@id="modalPaymentPlan"]/div/div/div/div/p[4]/button').click()

    #____________Проверка ошибки на пеймент страницы
    error_payment = 'General issue: This transaction has been declined.'
    actual_error_payment = browser.find_element_by_xpath('//*[@id="payment-form"]/div[2]/ul/li').text
    assert actual_error_payment == error_payment, f'Показывает ошибку: {actual_error_payment},\n ' \
                                                  f'а должен: {error_payment}'

    #__________________________________________________________

    # date_now = int(date.strftime("%d"))

    # Определяет дату создания диворса и последующие даты
    date = datetime.now()
    date.strftime("%Y-%m-%d")
    date_for_admin = date.strftime("%m/%d/%Y")
    day = timedelta(days=1)
    week = timedelta(days=7)
    week_2 = timedelta(days=14)
    day_1 = (date + day)

    first_payment_date_1 = browser.find_element_by_xpath('//*[@id="id_date_1"]').get_attribute("value")
    pp_first_payment = (date + day).strftime("%Y-%m-%d")

    #Проверки на соответсвие дат
    assert first_payment_date_1 == pp_first_payment, f'Не правильный "First payment"'

    first_payment_date_2 = browser.find_element_by_xpath('//*[@id="id_date_2"]').get_attribute('value')
    pp_second_payment = (day_1 + week).strftime("%Y-%m-%d")

    assert first_payment_date_2 == pp_second_payment, f'Не правильный "Second payment"'

    first_payment_date_3 = browser.find_element_by_xpath('//*[@id="id_date_3"]').get_attribute('value')
    pp_third_payment = (day_1 + week_2).strftime("%Y-%m-%d")

    assert first_payment_date_3 == pp_third_payment, f'Не правильный "Third payment"'


    browser.find_element_by_xpath('//*[@id="page"]/div[2]/div[2]/div/div/div[5]/button').click()


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

    #--------------------Проверка на наличие partial access---------------------------------------------------------------------------------
    info_pop_up_partial_access = browser.find_element_by_xpath('/html/body/header/div[3]/p').text
    info_pop_up_partial_access_expected = 'You have partial access to our platform. Please pay for the service to receive full access to your documents.'
    assert info_pop_up_partial_access == info_pop_up_partial_access_expected, f'Актуальный результат: {info_pop_up_partial_access}, \n' \
                                                                              f'Ожидаемый результат{info_pop_up_partial_access_expected}'

    # Welcom
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="nav"]/li[2]/a').click()

    # Voronka
    if data['state_summary_changed'] == ['Florida']:
        browser.find_element_by_xpath('//*[@id="id_petitioner_who"]/option[3]').click()
    else:
        browser.find_element_by_xpath('//*[@id="id_divorce_petitioner_who"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()
    time.sleep(3)
    browser.quit()


    # #--------------------Admin-----------------------------------------------------
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # #link = 'https://staging.completecase.com:8001/admin/login/?next=/admin/'
    # link = 'https://www.completecase.com/admin/login/?next=/admin/'
    # browser.get(link)
    # browser.implicitly_wait(10)
    #
    # #_____________________________Live____________________________________________________________________
    # # browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('cmo0lkamd0jqflzrm49u6yin601kc1wn')
    # # browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    # # browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    # # browser.implicitly_wait(10)
    # #_____________________________________________________________________________________________________
    # browser.find_element_by_xpath('//*[@id="id_username"]').send_keys('leonid.keyua@gmail.com')
    # browser.find_element_by_xpath('//*[@id="id_password"]').send_keys('11111')
    # browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    # time.sleep(2)
    #
    # browser.find_element_by_xpath('//*[@id="search"]').send_keys(email)
    # browser.find_element_by_xpath('//*[@id="submit"]').click()
    #
    # #---для лайва---
    # browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()
    # #browser.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()
    #
    # first_name = browser.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value")
    # last_name = browser.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value")
    # number_fone = browser.find_element_by_xpath('//*[@id="id_phone"]').get_attribute("value")
    # state = browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[5]/div[2]/div[1]/div').text
    # fone_main = fone_1 + fone_2 + fone_3
    #
    # state_summary_changed = state_summary_changed[0]
    # print(state_summary_changed)
    # assert state_summary_changed == state, f"State in Admin: {state}, State Divirce: {state_summary_changed}"
    # assert first_name_summary_changed == first_name, f"Pokazyvayet: {first_name}, a dolzhen bít: {first_name_summary_changed}"
    # assert last_name_summary_changed == last_name, f"Pokazyvayet: {last_name}, a dolzhen bít: {last_name_summary_changed}"
    # assert fone_main == number_fone, f"Pokazyvayet: {number_fone}, a dolzhen bít: {fone_main}"
    # browser.find_elements_by_class_name('text')
    #
    # # ----------------------------Отправка комента в HelpScout------------------------------------------------------------
    # browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[16]/div/div[3]/a[1]').click()
    # send_help_scout_subject = browser.find_element_by_xpath(
    #     '//*[@id="user_form"]/div/fieldset[16]/div/div[3]/ng-form/input')
    # send_help_scout_subject.send_keys('Autotest')
    # send_help_scout_body = browser.find_element_by_xpath(
    #     '//*[@id="user_form"]/div/fieldset[16]/div/div[3]/ng-form/textarea')
    # send_help_scout_body.send_keys('Autotest')
    # browser.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[16]/div/div[3]/ng-form/button').click()
    #
    # # ----------------------Проверка DIVORCE CASES в Админке------------------------------------------------------------
    #
    # status_divorce = 'Partial access'
    # status_divorce_in_admin = browser.find_element_by_xpath('//*[@id="divorcecase_set-0"]/fieldset/div[1]/div/div').text
    # assert status_divorce == status_divorce_in_admin, f'Статус Divorce case: {status_divorce_in_admin}, адолжен быть {status_divorce} '
    #
    # # ----------------------Проверка Order в Админке  ------------------------------------------------------------------
    # pp_first_payment_for_admin = (date + day).strftime("%m/%d/%Y")
    # pp_second_payment_for_admin = (day_1 + week).strftime("%m/%d/%Y")
    # pp_third_payment_for_admin = (day_1 + week_2).strftime("%m/%d/%Y")
    # payment_plan_info_expected = f'Amount: $46.34, Automated Date {pp_first_payment_for_admin}, Amount: $46.34, Paid: None\n' \
    #     f'Amount: $46.33, Automated Date {pp_second_payment_for_admin}, Amount: $46.33, Paid: None\n' \
    #     f'Amount: $46.33, Automated Date {pp_third_payment_for_admin}, Amount: $46.33, Paid: None'
    # display_order_items_expected = 'Divorce: $139.00'
    #
    # browser.find_element_by_xpath('//*[@id="fieldsetcollapser5"]').click()
    # payment_plan_info = browser.find_element_by_xpath('//*[@id="orders-0"]/fieldset/div[8]/div/div').text
    # assert payment_plan_info == payment_plan_info_expected, f'Актуальный результат: \n{payment_plan_info},\n ' \
    #     f'ожидаемый результат \n{payment_plan_info_expected}'
    # display_order_items = browser.find_element_by_xpath('//*[@id="orders-0"]/fieldset/div[3]/div/div').text
    # assert display_order_items_expected == display_order_items, f'Актуальный результат: \n{display_order_items},\n' \
    #     f'ожидаемый результат{display_order_items_expected}'
    #
    # browser.quit()
    # return text_pop_up_payment_plan
    #
    #
    #
