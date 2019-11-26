# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.spotify.com/ar/signup/?forward_url=https%3A%2F%2Fwww.spotify.com%2Far%2Fdownload%2F")
        driver.find_element_by_xpath("//div/div[2]/div").click()
        driver.find_element_by_id("register-email").clear()
        driver.find_element_by_id("register-email").send_keys("mervin.visma@gmail.com")
        driver.find_element_by_id("register-confirm-email").click()
        driver.find_element_by_id("register-confirm-email").clear()
        driver.find_element_by_id("register-confirm-email").send_keys("mervin.visma@gmail.com")
        driver.find_element_by_id("register-password").click()
        driver.find_element_by_id("register-password").clear()
        driver.find_element_by_id("register-password").send_keys("Mm111213")
        driver.find_element_by_id("register-displayname").clear()
        driver.find_element_by_id("register-displayname").send_keys(u"Mervin Díaz")
        driver.find_element_by_id("register-dob-day").click()
        driver.find_element_by_id("register-dob-day").clear()
        driver.find_element_by_id("register-dob-day").send_keys("14")
        driver.find_element_by_id("register-dob-month").click()
        Select(driver.find_element_by_id("register-dob-month")).select_by_visible_text("enero")
        driver.find_element_by_id("register-dob-month").click()
        driver.find_element_by_id("register-dob-year").click()
        driver.find_element_by_id("register-dob-year").clear()
        driver.find_element_by_id("register-dob-year").send_keys("1986")
        driver.find_element_by_id("register-male").click()
        driver.find_element_by_id("register-thirdparty").click()
        driver.find_element_by_id("register-button-email-submit").click()
        driver.find_element_by_id("li-recaptcha").click()
        try:
            self.assertEqual("Confirma que no eres un robot.", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='Términos y Condiciones de Uso'])[1]/preceding::label[1]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()