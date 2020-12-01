from PageObject.all_sites.CC.voronka_do_oplati_cc import browser

#Screen after questionnaire
time.sleep(1)
#Поп ап окно "фидбек"
browser.find_element_by_xpath('//*[@id="message-done"]/div/div/div[2]/button').click()
browser.find_element_by_xpath('//*[@id="feedback-form"]/div/div[2]/div[2]/div/div/label[3]/span').click()
browser.find_element_by_xpath('//*[@id="feedback-form"]/div/div[2]/div[3]/div/div/label[11]/span').click()
browser.find_element_by_xpath('//*[@id="feedback-form"]/div/div[2]/div[4]/div/div/label[17]/span').click()
browser.find_element_by_xpath('//*[@id="id_improve"]').send_keys('Test Test Test Test Test Test Test Test Test '
                                                                 'Test Test Test Test Test Test Test Test Test '
                                                                 'Test Test Test Test Test Test Test Test Test '
                                                                 'Test Test Test Test Test Test Test Test Test '
                                                                 'Test Test Test Test Test Test Test Test Test '
                                                                 'Test Test Test Test Test Test Test Test Test '
                                                                 'Test Test Test Test Test Test Test Test Test '
                                                                 'Test Test Test Test Test Test Test Test Test'
                                                                 '')
# Проверяю наличие текста на странице
browser.find_element_by_xpath('//*[@id="feedback-form"]/div/div[3]/button').click()
text_forms_page_actual = browser.find_element_by_xpath('//*[@id="content"]/div/div/text()[1]').text()
expected_text_forms_page_1 = 'If you have finished answering all questions to the best of your ability, please submit ' \
                           'your case for processing to receive your completed forms. Standard processing takes 2 business days.'
expected_text_forms_page_2 = 'Choose expedited processing to get them within 1 business day or less. NOTE: Please take' \
                             ' special care in making sure that all questions are answered. You can make minor changes' \
                             ' at any time, but major changes such as changing the filing party or the state of filing' \
                             ' will incur additional fees. Making changes will delay the overall filling of your divorce.' \
                             ' Therefore, it is best to verify all information before the initial submission.'
assert text_forms_page_actual == expected_text_forms_page_1, f'Не правильный текст на странице Forms'
browser.find_element_by_xpath('//*[@id="submit-answers-button"]').click()