import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *


class TestStellarBurgersLogIn:
    def test_log_in_from_main_page_enter_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['main_page'])

        driver.find_element(By.XPATH, locators['main_page_log_in_button_']).click()
        driver.find_element(By.XPATH, locators['log_in_email_field']).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, locators['log_in_password_field']).send_keys('qwerqwe')
        driver.find_element(By.XPATH, locators['lod_in_login_button']).click()

        time.sleep(1)

        driver.find_element(By.XPATH, locators['transition_to_personal_account']).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.quit()

    def test_log_in_from_main_page_personal_account_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['main_page'])

        driver.find_element(By.XPATH, locators['transition_to_personal_account']).click()
        driver.find_element(By.XPATH, locators['log_in_email_field']).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, locators['log_in_password_field']).send_keys('qwerqwe')
        driver.find_element(By.XPATH, locators['lod_in_login_button']).click()

        time.sleep(1)

        driver.find_element(By.XPATH, locators['transition_to_personal_account']).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.quit()

    def test_log_in_from_reg_page_enter_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['registration_page'])

        driver.find_element(By.XPATH, locators['reg_log_in_button']).click()
        driver.find_element(By.XPATH, locators['log_in_email_field']).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, locators['log_in_password_field']).send_keys('qwerqwe')
        driver.find_element(By.XPATH, locators['lod_in_login_button']).click()

        time.sleep(1)

        driver.find_element(By.XPATH, locators['transition_to_personal_account']).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.quit()

    def test_log_in_from_password_recovery_page_enter_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['password_recovery_page'])

        driver.find_element(By.XPATH, locators['password_recovery_enter_button']).click()
        driver.find_element(By.XPATH, locators['log_in_email_field']).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, locators['log_in_password_field']).send_keys('qwerqwe')
        driver.find_element(By.XPATH, locators['lod_in_login_button']).click()

        time.sleep(1)

        driver.find_element(By.XPATH, locators['transition_to_personal_account']).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.quit()
