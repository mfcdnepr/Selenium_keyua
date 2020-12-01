# from datetime import datetime
# from selenium import webdriver
# import time
# from selenium.common.exceptions import (NoSuchElementException, )
# from pagePay.py import pagePay
# # -----------------------------------------Screen size--------------------------------------------------------------
# Полное прохождение воронки штата Вирджиния можно применять на сс дизе

def voronka_virginia(browser, time):

    browser.find_element_by_xpath('//*[@id="nav"]/li[2]/a').click()

    #Screen 14   Достоем название выбраного элемента
    petitionerWho = browser.find_element_by_xpath('//*[@id="id_divorce_petitioner_who"]').get_attribute("value")
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 15   проверка на заполнение полей с маленькой буквы (pop-up)
    browser.find_element_by_xpath('//*[@id="id_state_resident_who"]').click()
    browser.find_element_by_xpath('//*[@id="id_state_resident_who"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_venue"]').send_keys('countygoingcase')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="idFirstLowerWarning"]/div/div/div[2]/button[1]').click()

    #Screen 16
    dateMarred = browser.find_element_by_xpath('//*[@id="id_marriage_date_and_time"]').get_attribute("value")
    cityMared = browser.find_element_by_xpath('//*[@id="id_marriage_city"]').get_attribute("value")
    #assert
    browser.find_element_by_xpath('//*[@id="id_marriage_county"]').send_keys('Countymarried')
    browser.find_element_by_xpath('//*[@id="id_marriage_state"]').send_keys('Statemarried')
    browser.find_element_by_xpath('//*[@id="id_marriage_city"]').send_keys('Cityweremarried')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 17
    fullLegalName = browser.find_element_by_xpath('//*[@id="id_petitioner_name"]').get_attribute("value")
    browser.find_element_by_xpath('//*[@id="id_petitioner_military_1"]').click()
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_4"]/option[6]').click()
    browser.find_element_by_xpath('//*[@id="id_husband_or_wife"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_petitioner_dob"]').send_keys('11/11/1999')
    browser.find_element_by_xpath('//*[@id="id_petitioner_ssn"]').send_keys('social2security8num')
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_0"]').send_keys('29719 ')
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_1"]').send_keys('Aberdeen')
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_2"]').send_keys('Ln')
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_3"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_5"]').send_keys('4807')
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_6"]').send_keys('Z6')
    browser.find_element_by_xpath('//*[@id="id_petitioner_dol"]').send_keys('driverlicensenum0')
    browser.find_element_by_xpath('//*[@id="id_petitioner_address_county"]').send_keys('Countyresidein')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="idFirstLowerWarning"]/div/div/div[2]/button[1]').click()

    #Screen 18
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 19
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_address_4"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_name"]').send_keys('Employer Name')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_describe"]').send_keys('Nature employment')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_address_0"]').send_keys('Adress')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_address_1"]').send_keys('256')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_address_2"]').send_keys('Pr.')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_address_3"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_address_5"]').send_keys('1111')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_address_6"]').send_keys('Zx')
    browser.find_element_by_xpath('//*[@id="id_petitioner_employer_phone"]').send_keys('111 111 1111')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen
    browser.find_element_by_xpath('//*[@id="id_petitioner_former_name_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 21
    browser.find_element_by_xpath('//*[@id="id_petitioner_resume_former_name_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 22
    browser.find_element_by_xpath('//*[@id="id_petitioner_full_former_name"]').send_keys('Full Maiden Name')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 24
    browser.find_element_by_xpath('//*[@id="id_respondent_military_1"]').click()
    browser.find_element_by_xpath('//*[@id="id_respondent_address_4"]/option[5]').click()
    browser.find_element_by_xpath('//*[@id="id_respondent_name"]').send_keys('Spouse\'s Legal Name')
    browser.find_element_by_xpath('//*[@id="id_respondent_dob"]').send_keys('11 11 1999')
    browser.find_element_by_xpath('//*[@id="id_respondent_ssn"]').send_keys('Spousesocialsecuritynum9')
    browser.find_element_by_xpath('//*[@id="id_respondent_address_0"]').send_keys('Street')
    browser.find_element_by_xpath('//*[@id="id_respondent_address_1"]').send_keys('Pr')
    browser.find_element_by_xpath('//*[@id="id_respondent_address_2"]').send_keys('267')
    browser.find_element_by_xpath('//*[@id="id_respondent_address_3"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_respondent_address_5"]').send_keys('4562')
    browser.find_element_by_xpath('//*[@id="id_respondent_address_6"]').send_keys('Zx')
    browser.find_element_by_xpath('//*[@id="id_respondent_phone"]').send_keys('222 222 2222')
    browser.find_element_by_xpath('//*[@id="id_respondent_dol"]').send_keys('Spousedriverlicense9')
    browser.find_element_by_xpath('//*[@id="id_respondent_address_county"]').send_keys('Countyspreside')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 25
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 26
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_address_4"]/option[8]').click()
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_name"]').send_keys('Name Spouse Employer')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_describe"]').send_keys('Spouse employment')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_address_0"]').send_keys('Street')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_address_1"]').send_keys('123')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_address_2"]').send_keys('Pr')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_address_3"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_address_5"]').send_keys('1111')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_address_6"]').send_keys('Zx')
    browser.find_element_by_xpath('//*[@id="id_respondent_employer_phone"]').send_keys('333 333 3333')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 27
    browser.find_element_by_xpath('//*[@id="id_respondent_former_name_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 28
    browser.find_element_by_xpath('//*[@id="id_respondent_resume_former_name_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 29
    browser.find_element_by_xpath('//*[@id="id_respondent_full_former_name"]').send_keys('SpFirst Middle Last')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 31
    browser.find_element_by_xpath('//*[@id="id_claims_pending_yn_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 32
    browser.find_element_by_xpath('//*[@id="id_related_claims_description"]').send_keys('Cases 756/2114/17 and / '
                                                                                        '911/3386/17 Supreme Court')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 33
    browser.find_element_by_xpath('//*[@id="id_form-0-child_prior_orders_1"]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-child_health_insurance"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-child_tax_exemption"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-child_residential_parent"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-child_gender"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-child_name"]').send_keys('Fell Name Children')
    browser.find_element_by_xpath('//*[@id="id_form-0-child_dob"]').send_keys('11 11 1999')
    browser.find_element_by_xpath('//*[@id="id_form-0-child_ssn"]').send_keys('Childsocialnumber9')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 34
    browser.find_element_by_xpath('//*[@id="id_child_support_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 35
    browser.find_element_by_xpath('//*[@id="id_child_support_both_life_insurance_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()


    #Screen 36
    browser.find_element_by_xpath('//*[@id="id_child_support_calculate_yn"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 38
    browser.find_element_by_xpath('//*[@id="id_child_support_who"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 39
    browser.find_element_by_xpath('//*[@id="id_petitioner_pay_interval"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_petitioner_gross_pay"]').send_keys('100')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 40
    browser.find_element_by_xpath('//*[@id="id_petitioner_other_income_any_0"]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_form-0-petitioner_other_income_nature"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-petitioner_other_income_interval"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-petitioner_other_income_other_description"]').send_keys('Natural')
    browser.find_element_by_xpath('//*[@id="id_form-0-petitioner_other_income_amount"]').send_keys('')
    browser.find_element_by_xpath('//*[@id="id_form-0-petitioner_other_income_amount"]').send_keys('1000.50')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()


    #Screen 41
    browser.find_element_by_xpath('//*[@id="id_petitioner_deduction_amount_total"]').send_keys('200.98')
    browser.find_element_by_xpath('//*[@id="id_petitioner_deduction_amount_fica"]').send_keys('200.10')
    browser.find_element_by_xpath('//*[@id="id_petitioner_deduction_amount_non_voluntary"]').send_keys('none')
    browser.find_element_by_xpath('//*[@id="id_petitioner_deduction_amount_lst"]').send_keys('200.00')
    browser.find_element_by_xpath('//*[@id="id_petitioner_deduction_amount_union"]').send_keys('200')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 42
    browser.find_element_by_xpath('//*[@id="id_respondent_pay_interval"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="id_respondent_gross_pay"]').send_keys('1000.36')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 43
    browser.find_element_by_xpath('//*[@id="id_respondent_other_income_any_0"]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="id_form-0-respondent_other_income_nature"]/option[7]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-respondent_other_income_interval"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-respondent_other_income_other_description"]').send_keys('Natural')
    browser.find_element_by_xpath('//*[@id="id_form-0-respondent_other_income_amount"]').send_keys('1000.23')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 44
    browser.find_element_by_xpath('//*[@id="id_respondent_deduction_amount_total"]').send_keys('100.23')
    browser.find_element_by_xpath('//*[@id="id_respondent_deduction_amount_fica"]').send_keys('199.2')
    browser.find_element_by_xpath('//*[@id="id_respondent_deduction_amount_non_voluntary"]').send_keys('0')
    browser.find_element_by_xpath('//*[@id="id_respondent_deduction_amount_lst"]').send_keys('none')
    browser.find_element_by_xpath('//*[@id="id_respondent_deduction_amount_union"]').send_keys('none')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 46
    browser.find_element_by_xpath('//*[@id="id_child_care_both_life_insurance_amount"]').send_keys('100000')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 47
    browser.find_element_by_xpath('//*[@id="id_child_support_childcare_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 49
    browser.find_element_by_xpath('//*[@id="id_child_support_child_care_amount"]').send_keys('300')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 50
    browser.find_element_by_xpath('//*[@id="id_children_other_litigation_any_0"]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="id_form-0-children_other_litigation_court"]').send_keys('Supreme Court Virginia')
    browser.find_element_by_xpath('//*[@id="id_form-0-children_other_litigation_case_number"]').send_keys('756/2114/17')
    browser.find_element_by_xpath('//*[@id="id_form-0-children_other_litigation_date"]').send_keys('11 11 1999')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 51
    browser.find_element_by_xpath('//*[@id="id_children_information_custody_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 52
    browser.find_element_by_xpath('//*[@id="id_children_information_custody_info"]').send_keys('5516vfvf-fv')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 53
    browser.find_element_by_xpath('//*[@id="id_children_other_party_custody_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-children_other_party_custody_name"]').send_keys('Name Custody')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 54
    browser.find_element_by_xpath('//*[@id="id_children_legal_custody"]/option[4]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 55
    browser.find_element_by_xpath('//*[@id="id_children_standard_visitation_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 57
    browser.find_element_by_xpath('//*[@id="id_children_statement_conceal_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 58
    browser.find_element_by_xpath('//*[@id="id_children_statement_conceal_days"]').send_keys('2')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 59
    browser.find_element_by_xpath('//*[@id="id_children_statement_residence_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 60
    browser.find_element_by_xpath('//*[@id="id_children_statement_residence_county"]').send_keys('none')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 61
    browser.find_element_by_xpath('//*[@id="id_children_statement_surname_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 62
    browser.find_element_by_xpath('//*[@id="id_children_uninsured_health_care_shared_other"]').send_keys('25')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 63
    alert_text_expected = 'Quitclaim deed has been added to your case. You will find it on the Forms page along with ' \
                          'the other forms when they are ready. Meanwhile, please proceed with the divorce interview.'
    browser.find_element_by_xpath('//*[@id="id_property_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="submit_modal"]').click()
    time.sleep(4)
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    assert alert_text == alert_text_expected, f'Проблемы с покупкой Quitclaim deed на 63 шаге'

    #Screen 64
    browser.find_element_by_xpath('//*[@id="id_property_real_any_0"]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_mortgage_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_mortgage2_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_who"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_refi_0"]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_4"]/option[5]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_0"]').send_keys('Street')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_1"]').send_keys('Lenina')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_2"]').send_keys('2458a')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_3"]').send_keys('City')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_5"]').send_keys('2021')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_6"]').send_keys('Lp')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_address_county"]').send_keys('Chukotka')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_real_describe"]').send_keys('none')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 65
    browser.find_element_by_xpath('//*[@id="id_property_auto_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_auto_loan_any_1"]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_auto_who"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-property_auto_describe"]').send_keys('1995 Ford Escort')
    browser.find_element_by_xpath('//*[@id="id_form-0-property_auto_vin"]').send_keys('25255jhdvjd232')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 66
    browser.find_element_by_xpath('//*[@id="id_property_other_petitioner"]').send_keys("List any other items of property that the Husband will keep after the divorce. "
                                                                                       "it is not necessary to list each item if you can generalize. For example, computer, "
                                                                                       "dining table, mother's jewelry, all china, all tools and equipment, etc. In general terms,'"
                                                                                       "community or marital property is property obtained during the marriage. Usually, this "
                                                                                       "type of property is divided equally at the time of a divorce. Separate property is, "
                                                                                       "generally, property owned before the marriage. It is usually kept by the spouse which owned"
                                                                                       " it before the marriage.")
    browser.find_element_by_xpath('//*[@id="id_property_other_respondent"]').send_keys("List any other items of property that the Wife will keep after the divorce. It is not necessary "
                                                                                       "to list each item if you can generalize")
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 68
    browser.find_element_by_xpath('//*[@id="id_debts_petitioner"]').send_keys('MasterCard, Account #9999999, Balance $2000.45')
    browser.find_element_by_xpath('//*[@id="id_debts_respondent"]').send_keys('MasterCard, Account #8888888, Balance $2000.95')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 69
    browser.find_element_by_xpath('//*[@id="id_retirement_benefits_any_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="qdroModal"]/div/div/div[3]/div/div[2]/a').click()

    #Screen 70
    browser.find_element_by_xpath('//*[@id="id_retirement_benefits_divide_0"]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="id_form-0-retirement_benefits_who"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-retirement_benefits_type"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-retirement_benefits_divide_how"]/option[3]').click()
    browser.find_element_by_xpath('//*[@id="id_form-0-retirement_benefits_name"]').send_keys('Roth IRA, 401(K) Plan')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 71
    browser.find_element_by_xpath('//*[@id="id_spousal_support_0"]').click()
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 72
    browser.find_element_by_xpath('//*[@id="id_spousal_support_pay_who"]/option[2]').click()
    browser.find_element_by_xpath('//*[@id="id_spousal_support_amount"]').send_keys('500.23')
    browser.find_element_by_xpath('//*[@id="id_spousal_support_date_begin"]').send_keys('11 11 1999')
    browser.find_element_by_xpath('//*[@id="id_spousal_support_end"]').send_keys('July 15, 2005')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    #Screen 73
    browser.find_element_by_xpath('//*[@id="id_spouse_separated_date"]').send_keys('11 11 1999')
    browser.find_element_by_xpath('//*[@id="screen-form"]/div[2]/div/div/input').click()

    # Screen Platinum
    browser.find_element_by_xpath('//*[@id="carouselTestimonialsControls"]/a[2]').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/main/section[5]/div/div/div/a').click()