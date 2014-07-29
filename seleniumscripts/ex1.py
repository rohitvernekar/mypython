import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()


    def test_search_in_python_org(self):
        driver=self.driver
        driver.get('http://www.python.org')
        assert "Python" in driver.title
        elem=driver.find_element_by_name("q")
        #all_elements=elem.find_elements_by_tag_name("option")
        elem.send_keys("Facebook")
        elem.send_keys(Keys.RETURN)
        driver.find_element_by_name("submit").click()
        #for option in all_elements:
        #    print("value is : %s" % option.get_attribute("value"))
        #    option.click()

    def tearDown(self):
        #self.driver.close()
        pass
        

if __name__=='__main__':
    unittest.main()

