def proverca_summary_OD (browser, ):

    #State_________________________________________________________________________
    Arkansas = browser.find_element_by_xpath('//*[@id="step13"]/div[1]/div[2]/span').text
    print(Arkansas)
    assert Arkansas == "Arkansas", f"WRONG."

    #Name__________________________________________________________________________
    First_Na = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[1]').text
    print(First_Na)
    assert First_Na == "First_Na", f"WRONG."
    Last_Na = browser.find_element_by_xpath('//*[@id="step13"]/div[2]/div[2]/div/span[2]').text
    print(Last_Na)
    assert Last_Na == "Last_Na", f"WRONG."

    #Date of your marriage__________________________________________________________
    # 05/12/1999 = browser.find_element_by_xpath('//*[@id="step13"]/div[3]/div[2]/span').data
    # print(05/12/1999)
    # assert 05/12/1999 == "05/12/1999", f"WRONG."

    #Children
    # 1 = browser.find_element_by_xpath('//*[@id="step13"]/div[4]/div[2]/span').text
    # print(1)
    # assert 1 == "1", "WRONG."

    #Property________________________________________________________________________
    No = browser.find_element_by_xpath('//*[@id="step13"]/div[5]/div[2]/span').text
    print(No)
    assert No == "No", f"WRONG."

    #Who will file divorce____________________________________________________________
    MySpouse = browser.find_element_by_xpath('//*[@id="step13"]/div[6]/div[2]/span').text
    print(MySpouse)
    assert MySpouse == "My Spouse", f"WRONG."

    #Current Home______________________________________________________________________
    Together = browser.find_element_by_xpath('//*[@id="step13"]/div[7]/div[2]/span').text
    print(Together)
    assert Together == "Together", f"WRONG."

    #Community Property_________________________________________________________________
    No = browser.find_element_by_xpath('//*[@id="step13"]/div[8]/div[2]/span').text
    print(No)
    assert No == "No", f"WRONG."

    #Community Debts____________________________________________________________________
    No = browser.find_element_by_xpath('//*[@id="step13"]/div[9]/div[2]/span').text
    print(No)
    assert No == "No", f"WRONG."

    #Other Income Sources_______________________________________________________________
    No = browser.find_element_by_xpath('//*[@id="step13"]/div[10]/div[2]/span').text
    print(No)
    assert No == "No", f"WRONG."

    #Money Owed_________________________________________________________________________
    Yes = browser.find_element_by_xpath('//*[@id="step13"]/div[11]/div[2]/span').text
    print(Yes)
    assert Yes == "Yes", f"WRONG."

    #Military Information_______________________________________________________________
    No = browser.find_element_by_xpath('//*[@id="step13"]/div[12]/div[2]/span').text
    print(No)
    assert No == "No", f"WRONG."



