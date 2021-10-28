
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import json

from functions.login import login
#-----------------------------SWBBL------------------------
def withdrawl():
        #set up appium
        desired_caps = {}  
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "emulator-5554"
        # desired_caps["appPackage"] = "np.com.infodev.blb.local"
        desired_caps["appPackage"] = "np.com.infodev.blb.swbbl"
        desired_caps["appActivity"] = "np.com.infodev.blb.ui.welcome.mvp.WelcomeActivity"
        desired_caps["noReset"] = "true"
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities= desired_caps)
        
        wait=driver.implicitly_wait(60) # seconds
        f= open('fixtures/login.json')
        # g=open('/fixtures/loan_demand_data.json')
        # data=json.load(g)
        login_data=json.load(f)   
            
        #---------------------------------------Login--------------------------
        # wait=driver.implicitly_wait(60) # seconds
        # el= driver.find_element_by_id("np.com.infodev.blb.local:id/ed_name_search")
        # el.send_keys(login_data['username'])
        # wait
        # el=driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_password")
        # el.send_keys(login_data['password'])   
        # driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_button").click()
        # wait
        wait
        login(driver, login_data, wait)
        wait
            
        #---------------------------------------Login--------------------------
        # wait=driver.implicitly_wait(60) # seconds
        # el= driver.find_element_by_id("np.com.infodev.blb.local:id/ed_name_search")
        # el.send_keys(login_data['username'])
        # wait
        # el=driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_password")
        # el.send_keys(login_data['password'])   
        # driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_button").click()
        # wait
        
        driver.find_element_by_accessibility_id("Deposit").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ImageView").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.swbbl:id/rowParentText").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.swbbl:id/rowSecondText").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ExpandableListView/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.view.ViewGroup").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.LinearLayout").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Spinner[2]/android.widget.TextView").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.swbbl:id/activity_single_transaction_amount_editText").send_keys("50")
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.swbbl:id/activity_single_transaction_submit_button").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.swbbl:id/ld_btn_no").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.swbbl:id/ld_btn_yes").click()
        wait
        
        print("Test Completed!!!")
        
        
        
if __name__ == '__main__':
    withdrawl()
    
        
        
        
        