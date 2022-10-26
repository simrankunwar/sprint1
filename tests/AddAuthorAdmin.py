import unittest
import time
import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
        warnings.simplefilter('ignore', ResourceWarning)
    def test_ll(self):
        user = "team12"
        pwd = "team12"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)

        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)  # pause to allow screen to load

        elem = driver.find_element(By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a').click()
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="content-main"]/ul/li/a').click()
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="id_first_name"]').send_keys("Michelle")
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="id_last_name"]').send_keys("Obama")
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="id_bio"]').send_keys("Michelle LaVaughn Robinson Obama is an American attorney and author who served as the first lady of the United States from 2009 to 2017. She was the first African-American woman to serve in this position. She is the wife of former President Barack Obama.")
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="author_form"]/div/div/input[1]').click()
        time.sleep(3)

        try:
            elem = driver.find_element(By.XPATH, '//*[@id="main"]/div/ul/li')
            print("Test passed - Author added successfully")
            assert True

        except NoSuchElementException:
                self.fail("Author was not able to be added - test failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()