import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import json

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
        data=json.load(f)
        
        username=data['username']
        password=data['password']
         
         
         
        el= driver.find_element_by_id("np.com.infodev.blb.local:id/ed_name_search")
        el.send_keys(username)
        wait
        el=driver.find_element_by_id("np.com.infodev.blb.local:id/activity_login_password")
        el.send_keys(password)   
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
        el.send_keys("Nippun")
        wait
        el=driver.find_element_by_id("np.com.infodev.blb.local:id/frag_reg_pre_last_name")
        el.send_keys("Shrestha")
        wait 
        
        # swipe(startX, startY, endX, endY, duration)
        driver.swipe(150, 900, 150, 150, 1000)
        
        el=driver.find_element_by_id("np.com.infodev.blb.local:id/frag_reg_pre_alert_mob_number")
        el.send_keys("9843255977")
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
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/toleNameET").send_keys("bazar")
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/wardNumberET").send_keys("29")
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/blockNumberET").send_keys("2")
        wait
        
        driver.find_element_by_id("np.com.infodev.blb.local:id/streetNameET").send_keys("baglung khola")
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
    