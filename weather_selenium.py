import os
import sys
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# path to chrome webdriver
driverpath = 'chromedriver'

# unittest class
class test_weather(unittest.TestCase, loc):
    # setUp method
    def setUp(self):
        
        print("Enter location")
        self.loc=input()
        self.driver=webdriver.Chrome(executable_path=os.path.abspath(driverpath))
        # getting the weather data home page
        self.driver.get('https://www.timeanddate.com/weather/')

    # funtion to get weather data
    def test_get_weather(self):
        driver=self.driver
        # locating the searchbar
        search=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_class_name('picker-city__input'))
        # entering location in the searchbar
        search.clear()
        search.send_keys(self.loc)
        search.send_keys(Keys.RETURN)
        # fetching the first search match, if any
        res=WebDriverWait(driver,10).until(lambda driver: driver.find_elements_by_xpath('/html/body/div[1]/div[6]/section[1]/div/section[2]/div[1]/div/table/tbody/tr[1]/td[1]/a'))
        res[0].send_keys(Keys.RETURN)
    # tearDown method
    def tearDown(self):
        self.driver.quit()
        
if __name__=='__main__':
    unittest.main()
        

    
