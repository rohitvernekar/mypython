import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

baseurl="file:///home/grohit/index.html"
username=""
pwd=""

"""
    xpaths={
        'usernameTxtBox' : "//input[@name='login']",
        'passwordTxtBox' : "//input[@name='password']",
        'submitButton' : "//input[@name='commit']"
       }
"""



class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
         self.driver=webdriver.Firefox()
        


    def test_search_in_python_org(self):
        driver=self.driver
        driver.get(baseurl)
        element = driver.find_element_by_xpath("//select[@name='bus']")
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            print("Value is: %s" % option.get_attribute("value"))
            option.click()


      
    def tearDown(self):
        #self.driver.close()
        pass
        
        

if __name__=='__main__':
    unittest.main()

