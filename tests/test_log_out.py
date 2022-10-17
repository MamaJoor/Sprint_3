from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *


class TestStellarBurgersLogOut:
    def test_log_out_from_personal_account_logout_success(self):
        driver = webdriver.Chrome()
        driver.get(urls['log_in_page'])

        driver.find_element(By.XPATH, log_in_email_field).send_keys('regreg@mail.ru')
        driver.find_element(By.XPATH, log_in_password_field).send_keys('qwerqwe')
        driver.find_element(By.XPATH, log_in_login_button).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, transition_to_personal_account)))

        driver.find_element(By.XPATH, transition_to_personal_account).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, log_out_button)))

        driver.find_element(By.XPATH, log_out_button).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, log_in_login_button)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()
