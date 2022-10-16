import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import reg_gen
from locators import *


class TestStellarBurgersRegistration:
    def test_registration_with_correct_data_reg_success(self):
        driver = webdriver.Chrome()

        password = reg_gen.gen_password()
        email = reg_gen.gen_email()

        driver.get(urls['registration_page'])

        driver.find_element(By.XPATH, locators['reg_name_field']).send_keys("Артем")
        driver.find_element(By.XPATH, locators['reg_email_field']).send_keys(email)
        driver.find_element(By.XPATH, locators['reg_password_field']).send_keys(password)
        driver.find_element(By.XPATH, locators['reg_reg_button']).click()

        time.sleep(1)

        driver.find_element(By.XPATH, locators['log_in_email_field']).send_keys(email)
        driver.find_element(By.XPATH, locators['log_in_password_field']).send_keys(password)
        driver.find_element(By.XPATH, locators['lod_in_login_button']).click()
        driver.find_element(By.XPATH, locators['transition_to_personal_account']).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.quit()

    def test_registration_with_incorrect_password_password_error(self):
        driver = webdriver.Chrome()

        email = reg_gen.gen_email()

        driver.get(urls['registration_page'])

        driver.find_element(By.XPATH, locators['reg_name_field']).send_keys("Артем")
        driver.find_element(By.XPATH, locators['reg_email_field']).send_keys(email)
        driver.find_element(By.XPATH, locators['reg_password_field']).send_keys('Danm')
        driver.find_element(By.XPATH, locators['reg_reg_button']).click()

        time.sleep(1)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register' and driver.find_element(
            By.XPATH, locators['reg_password_error']).text == 'Некорректный пароль'

        driver.quit()
