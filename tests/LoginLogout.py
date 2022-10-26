import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
        warnings.simplefilter('ignore', ResourceWarning)

    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="myNavbar"]/ul/li[3]/a').click()
        time.sleep(3)

        user = "team12"
        pwd = "team12"

        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="myNavbar"]/ul[2]/li[3]/a').click()
        time.sleep(3)

        try:
            elem = driver.find_element(By.LINK_TEXT, "Login")
            print("Test Passed - User logged in and logged out successfully")
            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()