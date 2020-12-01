'''
Создать списсок [], в который добавлять со страницы саммари 
все значения. А за тем сравнить со списком в который записывались ответы 
на скринах.

Нужно проверить изминение ответов на странице саммари

'''


def edit_answer_on_sammary(browser, time):
    expected_answers_summary_changed = ['Florida', 'first_name', 'last_name', '8', 'You', 'Apart', 'Yes', 'Yes', 'No',
                                        'Yes', 'No', 'Yes']
    actual_answers_summary_changed = []

    # __________________Your state of Residence_______FLORIDA___________
    browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/a').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="state"]/option[10]').click()
    state_on_summary_changed = browser.find_element_by_xpath('//*[@id="state"]/option[10]').text
    browser.find_element_by_xpath('//*[@id="popup0"]/div/div/div/div[2]/button').click()
    time.sleep(3)
    state_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/span').text
    actual_answers_summary_changed.append(state_summary_changed)

    # ------------------Information about yourself--------FIRST_NAME LAST_NAME------------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_first_name"]').send_keys('me')
    browser.find_element_by_xpath('//*[@id="id_last_name"]').send_keys('me')
    #browser.find_element_by_xpath('//*[@id="popup1"]/div/div/div/div[6]/button').click()
    browser.find_element_by_xpath('//*[@id="popup1"]/div/div/div/div[5]/button').click()
    time.sleep(3)

    first_name_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[1]').text
    actual_answers_summary_changed.append(first_name_summary_changed)
    last_name_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[2]').text
    actual_answers_summary_changed.append(last_name_summary_changed)

    # ---Skip--------------------Date and Location of Your Marriage----------------------------------
    # ------------------Children and Pregnancy------------8--------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[4]/div[2]/a').click()

    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_number_of_children"]/option[10]').click()
    browser.find_element_by_xpath('//*[@id="popup3"]/div/div/div/div[3]/button').click()
    site_text = browser.find_element_by_xpath('//*[@id="field-number_of_children"]/div/div[3]/div/a').text
    site_text = site_text.lower()
    url_summary = browser.current_url
    url_summary = url_summary[12:29]
    assert site_text == url_summary, f'Отображается {site_text} на сайте {url_summary} при изменении раздела "Children and Pregnancy"  '
    time.sleep(3)

    children_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[4]/div[2]/span').text
    actual_answers_summary_changed.append(children_summary_changed)

    # ------------------Property & Debts-------YES-------------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[5]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_debts_any"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="popup4"]/div/div/div/div[3]/button').click()
    time.sleep(3)
    property_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[5]/div[2]/span').text
    actual_answers_summary_changed.append(property_summary_changed)

    # -------------------Your Information------WIFE-------------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[6]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_who_will_file"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="popup5"]/div/div/div/div[2]/button').click()
    time.sleep(3)
    petitioner_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[6]/div[2]/span').text
    actual_answers_summary_changed.append(petitioner_summary_changed)

    # --------------------Current Home-------APART-----------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[7]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_live_together_now"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="popup6"]/div/div/div/div[2]/button').click()
    time.sleep(3)
    current_home_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[7]/div[2]/span').text
    actual_answers_summary_changed.append(current_home_summary_changed)

    # ------------------Community Property----YES----------------------------------------------
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="step13"]/div[8]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_community_property_divide_equally"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="popup7"]/div/div/div/div[2]/button').click()
    time.sleep(3)
    community_property_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[8]/div[2]/span').text
    actual_answers_summary_changed.append(community_property_summary_changed)

    # ------------------Community Debts--------NO------------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[9]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_divide_debts"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="popup8"]/div/div/div/div[2]/button').click()
    time.sleep(3)
    community_debts_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[6]/div[2]/span').text
    actual_answers_summary_changed.append(community_debts_summary_changed)

    # -------------------Other Income Sources----YES---------------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[10]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_my_additional_income_sources"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="popup9"]/div/div/div/div[3]/button').click()
    time.sleep(3)
    income_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[10]/div[2]/span').text
    actual_answers_summary_changed.append(income_summary_changed)

    # -------------------Money Owed-------NO------------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[11]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_i_owe_spouse_money"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="popup10"]/div/div/div/div[3]/button').click()
    time.sleep(3)
    money_owed_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[11]/div[2]/span').text
    actual_answers_summary_changed.append(money_owed_summary_changed)

    # -------------------Military Information----YES---------------------------------------------
    browser.find_element_by_xpath('//*[@id="step13"]/div[12]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_either_party_military_member"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="popup11"]/div/div/div/div[2]/button').click()
    time.sleep(3)
    military_summary_changed = browser.find_element_by_xpath('//*[@id="step13"]/div[12]/div[2]/span').text
    actual_answers_summary_changed.append(military_summary_changed)
    assert set(actual_answers_summary_changed) == set(expected_answers_summary_changed), f'Проблемы с изминением данных на саммари.' f'Актуальный результат: {actual_answers_summary_changed} Ожидаемый результат: {expected_answers_summary_changed}'
    return state_summary_changed, last_name_summary_changed, first_name_summary_changed
