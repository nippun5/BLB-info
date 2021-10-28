
#----------------------blb local----------------
def login(driver,login_data,wait):
    # el= driver.find_element_by_id("np.com.infodev.blb.local:id/ed_name_search")
    # el.send_keys(login_data['username'])
    # wait
    # el=driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_password")
    # el.send_keys(login_data['password'])   
    # driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_button").click()
    
    el= driver.find_element_by_id("np.com.infodev.blb.swbbl:id/ed_name_search")
    el.send_keys(login_data['username'])
    wait
    el=driver.find_element_by_id("np.com.infodev.blb.swbbl:id/activity_login_password")
    el.send_keys(login_data['password'])   
    wait
    driver.find_element_by_id("np.com.infodev.blb.swbbl:id/activity_login_button").click()