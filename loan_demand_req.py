import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import json

from functions.login import login

# class SimpleCalculatorTests(unittest.TestCase):

def blb():
        #set up appium
        desired_caps = {}  
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps["appPackage"] = "np.com.infodev.blb.local"
        desired_caps["appActivity"] = "np.com.infodev.blb.ui.welcome.mvp.WelcomeActivity"
        desired_caps["noReset"] = "true"
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities= desired_caps)
        
        wait=driver.implicitly_wait(60) # seconds
        f= open('fixtures/login.json')
        g=open('/fixtures/loan_demand_data.json')
        data=json.load(g)
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
        
        login(driver, login_data, wait)

        #-----------------------------------Loan 
        
        driver.find_element_by_accessibility_id("Loan").click()
        wait
        #------------------------------------Loan Demand request-------------------------
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageView").click()
        wait
        
        #----------------------------------------------MFI-----------------------
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[1]").click()
        wait
        #-------------------------------------------Center List----------------------

        driver.find_element_by_id("np.com.infodev.blb.local:id/rowParentText").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ExpandableListView/android.widget.ExpandableListView/android.widget.LinearLayout[1]/android.widget.TextView").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ExpandableListView/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.TextView").click()
        wait
        
        #----------------------------------------------Saili Waiba--------------------
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/sp_loan").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()
        wait
        
        #------------------------------------period--------------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/fragment_load_information_period_ed").send_keys(data['loan_period'])
        wait                                                                        
        
        #-------------------------------------request amount------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/fragment_load_information_request_amount_ed").send_keys(data['request_amt'])
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]/android.widget.Spinner[1]/android.widget.TextView").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()
        wait
        
         # swipe(startX, startY, endX, endY, duration)
        driver.swipe(150, 900, 150, 150, 1000)
        wait
        
        #-----------------------------Add insurance
        driver.find_element_by_id("np.com.infodev.blb.local:id/fragment_loan_information_next_btn").click()
        wait
        
        driver.swipe(150, 950, 150, 150, 1000)
        TouchAction(driver)   .press(x=642, y=1613)   .move_to(x=655, y=721)   .release()   .perform()
        wait
        driver.find_element_by_id("np.com.infodev.blb.local:id/go_to_attachment_btn").click()
        wait
        #-----------------------------submit----------
        driver.find_element_by_id("np.com.infodev.blb.local:id/confirm_btn").click()
        wait
    
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_delete").click()
        
        print("Test Completed")
        
        
        
        
if __name__ == '__main__':
    blb()
    
        