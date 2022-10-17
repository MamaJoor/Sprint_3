from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *


class TestStellarBurgersLogIn:
    def test_log_in_from_main_page_enter_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['main_page'])

        driver.find_element(By.XPATH, main_page_log_in_button_).click()
        driver.find_element(By.XPATH, log_in_email_field).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, log_in_password_field).send_keys('qwerqwe')
        driver.find_element(By.XPATH, log_in_login_button).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, transition_to_personal_account)))

        driver.find_element(By.XPATH, transition_to_personal_account).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'

        driver.quit()

    def test_log_in_from_main_page_personal_account_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['main_page'])

        driver.find_element(By.XPATH, transition_to_personal_account).click()
        driver.find_element(By.XPATH, log_in_email_field).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, log_in_password_field).send_keys('qwerqwe')
        driver.find_element(By.XPATH, log_in_login_button).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, transition_to_personal_account)))

        driver.find_element(By.XPATH, transition_to_personal_account).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'

        driver.quit()

    def test_log_in_from_reg_page_enter_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['registration_page'])

        driver.find_element(By.XPATH, reg_log_in_button).click()
        driver.find_element(By.XPATH, log_in_email_field).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, log_in_password_field).send_keys('qwerqwe')
        driver.find_element(By.XPATH, log_in_login_button).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, transition_to_personal_account)))

        driver.find_element(By.XPATH, transition_to_personal_account).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'

        driver.quit()

    def test_log_in_from_password_recovery_page_enter_button_log_in_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['password_recovery_page'])

        driver.find_element(By.XPATH, password_recovery_enter_button).click()
        driver.find_element(By.XPATH, log_in_email_field).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, log_in_password_field).send_keys('qwerqwe')
        driver.find_element(By.XPATH, log_in_login_button).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, transition_to_personal_account)))

        driver.find_element(By.XPATH, transition_to_personal_account).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'

        driver.quit()
