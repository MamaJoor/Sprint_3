from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

import locators
from locators import *


class TestStellarBurgersConstructorChapters:
    def test_construction_chapter_transition_to_bulki_bulki_is_visible(self):
        driver = webdriver.Chrome()
        driver.get(urls['main_page'])

        driver.find_element(By.XPATH, constructor_sousi_button).click()

        WebDriverWait(driver, 1)

        driver.find_element(By.XPATH, constructor_bulki_button).click()

        WebDriverWait(driver, 1)

        assert driver.find_element(By.XPATH, flag_bulki_visible).is_displayed()

        driver.quit()

    def test_construction_chapter_transition_to_sousi_sousi_is_visible(self):
        driver = webdriver.Chrome()
        driver.get(urls['main_page'])

        driver.find_element(By.XPATH, constructor_sousi_button).click()

        WebDriverWait(driver, 1)

        assert driver.find_element(By.XPATH, flag_sousi_visible).is_displayed()

        driver.quit()

    def test_construction_chapter_transition_to_nachinki_nachinki_is_visible(self):
        driver = webdriver.Chrome()
        driver.get(urls['main_page'])

        driver.find_element(By.XPATH, constructor_nachinki_button).click()

        WebDriverWait(driver, 1)

        assert driver.find_element(By.XPATH, flag_nachinki_visible).is_displayed()

        driver.quit()
