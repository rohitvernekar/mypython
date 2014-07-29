import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

baseurl="https://github.com/login"
username=""
pwd=""

xpaths={
        'usernameTxtBox' : "//input[@name='login']",
        'passwordTxtBox' : "//input[@name='password']",
        'submitButton' : "//input[@name='commit']"
       }




class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
         self.driver=webdriver.Firefox()
        


    def test_search_in_python_org(self):
        driver=self.driver
        driver.get(baseurl)
        #driver.maximize_window()
        driver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

        driver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys("grohit")

        driver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

        driver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys("Attitudere-defined4394")               
        driver.find_element_by_xpath(xpaths['submitButton']).click()
        driver.get("https://github.com/zeomega/bcbsma_build/pulls") 
        all_elements=driver.find_element_by_xpath("//a[@id='issues-container']/div/div[2]/div[1]/div/a[3]")
        for option in all_elements:
            print("value is : %s" % option.get_attribute("value"))
            #option.click()

    def tearDown(self):
        #self.driver.close()
        pass
        
        

if __name__=='__main__':
    unittest.main()

