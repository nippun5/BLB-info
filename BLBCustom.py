from appium.webdriver.webdriver import WebDriver
from src.testproject.sdk.drivers import webdriver
# import unittest
# from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import os
import json
# import time
os.environ['TP_DEV_TOKEN'] = 'iffgYJB9HzXcVFPf-W-337nUAskjK4m7cc_tLwc3lfw1' 
os.environ['TP_AGENT_URL']='http://127.0.0.1:8585'

# class SimpleCalculatorTests(unittest.TestCase):

def blb():
        #set up appium
        desired_caps = {}  
        # desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps["appPackage"] = "np.com.infodev.blb.local"
        desired_caps["appActivity"] = "np.com.infodev.blb.ui.welcome.mvp.WelcomeActivity"
        desired_caps["noReset"] = "false"
        driver = webdriver.Remote(desired_capabilities=desired_caps, project_name="BLB Project", job_name="Reporting Job")
            # command_executor='http://127.0.0.1:4723/wd/hub',
            # desired_capabilities= desired_caps)
        f=open('fixtures/login.json')
        g=open('fixtures/users.json')
        login_data=json.load(f)
        users=json.load(g)
    
        wait=driver.implicitly_wait(60) # seconds
        el= driver.find_element_by_id("np.com.infodev.blb.local:id/ed_name_search")
        el.send_keys(login_data['username'])
        wait
        el=driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_password")
        el.send_keys(login_data['password'])   
        driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_button").click()
        
        
        # wait
        # driver.find_element_by_id("android:id/button1").click()
        driver.implicitly_wait(90)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.ImageView").click()
        wait
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]").click()
        wait
        
        #------------------------------Create new-----------------------------------
        # driver.find_element_by_id("np.com.infodev.blb.local:id/createNewCustomer").click()
        driver.find_element_by_id("np.com.infodev.blb.local:id/createNewCustomer").click()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.Spinner/android.widget.TextView").click()
        wait
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[7]").click()
        wait
        el=driver.find_element_by_id("np.com.infodev.blb.local:id/frag_reg_pre_first_name")
        el.send_keys(users['first_name'])
        wait
        el=driver.find_element_by_id("np.com.infodev.blb.local:id/frag_reg_pre_last_name")
        el.send_keys(users['last_name'])
        wait 
        
        # swipe(startX, startY, endX, endY, duration)
        driver.swipe(150, 900, 150, 150, 1000)
        
        el=driver.find_element_by_id("np.com.infodev.blb.local:id/frag_reg_pre_alert_mob_number")
        el.send_keys(users['alert_mobile'])
        wait
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        
        
        #----------------Master information MF module---------------------------------
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Spinner/android.widget.TextView").click()
        
        wait
        
        #----------------------MD module picker-------------
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText").click()
        
        wait    

        # #------------------------Datepciker---------------------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_nepaliDatePicker_submit").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.Spinner/android.widget.TextView").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        
        #---------------------------------add address----------------------------------  
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_add_address").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Spinner[1]/android.widget.TextView").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Spinner/android.widget.TextView").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Spinner[2]/android.widget.TextView").click()
        
        #---------------------Local Body Type----------------------------
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]").click()
        wait
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Spinner/android.widget.TextView").click()
        
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[3]").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/toleNameET").send_keys(users['tole_name'])
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/wardNumberET").send_keys(users['ward_no'])
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/blockNumberET").send_keys(users['block_name'])
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/streetNameET").send_keys(users['street_name'])
        wait
        
        #-----------------------save address------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/saveButton").click()
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        #----------------------save identity-----------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        
        #---------------------save family tree---------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        
        #---------------------save nominee--------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        
        #---------------------save guardian----------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        
        #---------------------save others------------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        wait
        
        #----------------------save photo--------------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_next").click()
        
        #------------------------ save document ALL----------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/btn_save").click()
        
        #-------------------------confirm all-------------------
        driver.find_element_by_id("np.com.infodev.blb.local:id/ld_btn_no").click()
        wait
            
if __name__ == '__main__':
    blb()
    