from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *


class TestStellarBurgersTransitionToMainPage:
    def test_transition_from_personal_account_to_main_by_construction_button_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['log_in_page'])

        driver.find_element(By.XPATH, log_in_email_field).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, log_in_password_field).send_keys('qwerqwe')
        driver.find_element(By.XPATH, log_in_login_button).click()

        WebDriverWait(driver, 1)

        driver.find_element(By.XPATH, transition_to_personal_account).click()

        WebDriverWait(driver, 1)

        driver.find_element(By.XPATH, personal_account_to_construction_button).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_transition_from_personal_account_to_main_by_logo_button_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['log_in_page'])

        driver.find_element(By.XPATH, log_in_email_field).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, log_in_password_field).send_keys('qwerqwe')
        driver.find_element(By.XPATH, log_in_login_button).click()

        WebDriverWait(driver, 1)

        driver.find_element(By.XPATH, transition_to_personal_account).click()

        WebDriverWait(driver, 1)

        driver.find_element(By.XPATH, personal_account_to_construction_button).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()
