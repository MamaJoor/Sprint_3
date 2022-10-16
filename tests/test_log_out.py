import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *


class TestStellarBurgersLogOut:
    def test_log_out_from_personal_account_logout_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['log_in_page'])

        driver.find_element(By.XPATH, locators['log_in_email_field']).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, locators['log_in_password_field']).send_keys('qwerqwe')
        driver.find_element(By.XPATH, locators['lod_in_login_button']).click()

        time.sleep(1)

        driver.find_element(By.XPATH, locators['transition_to_personal_account']).click()

        time.sleep(1)

        driver.find_element(By.XPATH, locators['log_out_button']).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()
