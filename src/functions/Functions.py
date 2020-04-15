# -*- coding: utf-8 -*-
import unittest
import allure
import openpyxl
import os
import shutil
import time
import json
import pytest
import re
import requests
import random
import string
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, \
    UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from functions.Inicializar import Inicializar
import pyodbc
import objectpath

diaGlobal = time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
horaGlobal = time.strftime("%H%M%S")  # formato 24 houras
NAVEGADOR = Inicializar.NAVEGADOR
Scenario = {}


class Functions(Inicializar):
    ##########################################################################
    ##############       -=_JSON     HANDLE _=-              #################
    ##########################################################################

    def __init__(self):
        self.json_GetFieldBy = None
        self.json_ValueToFind = None

    def get_json_file(self, file):

        json_path = Inicializar.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            Functions.tearDown(self)
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)

    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True

            except KeyError:
                self.msj = u"get_entity: No se encontro la key a la cual se hace referencia: " + entity
                Functions.tearDown(self, "fail")
                pytest.skip(self.msj)
                # self.driver.close()

    def xpath_elements(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements

    def id_elements(self, ID):
        elements = self.driver.find_element_by_id(ID)
        print("ID_Elements: Se interactuo con el elemento " + ID)
        return elements

    def link_elements(self, LINK):
        elements = self.driver.find_element_by_partial_link_text(LINK)
        print("Link_Elements: Se interactuo con el elemento " + LINK)
        return elements

    def select_elements_xpath(self, xpath):
        select = Select(self.driver.find_element_by_xpath(xpath))
        return select

        # USO

        #       select by visible text  #       select.select_by_visible_text('Banana')

        #       select by value  #       select.select_by_value('1')

    def esperar_xpath(self, XPATH):  # Esperar que un elemento sea visible
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            print(u"esperar_Xpath: Se mostró el elemento " + XPATH)
            return True

        except TimeoutException:
            self.msj = (u"esperar_Xpath: No presente " + XPATH)
            return False
            Functions.tearDown(self, "fail")

    def esperar_id(self, ID):  # Esperar que un elemento sea visible
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.ID, ID)))
        except TimeoutException:
            print(u"Esperar_ID: No presente")
            return False
            Functions.tearDown(self)
        print(u"Esperar_ID: Se mostró el elemento " + ID)
        return True

    def esperar_css(self, CSS):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS)))

        except TimeoutException:
            self.msj = (u"esperar_CSS: No presente " + CSS)
            Functions.tearDown(self, "fail")
            return False

        print(u"esperar_CSS: Se mostrará el elemento " + CSS)
        return True

    def alert_windows(self, accept="accept", time=8):
        try:
            wait = WebDriverWait(self.driver, time)
            wait.until(EC.alert_is_present(), print(f"Esperando alerta {time} seg."))

            alert = self.driver.switch_to.alert

            if accept.lower() == "accept":
                alert.accept()
                print("Click in Accept")
            else:
                alert.dismiss()
                print("Click in Dismiss")

        except NoAlertPresentException:
            print('Alerta no presente')
        except NoSuchWindowException:
            print('Alerta no presente')
        except TimeoutException:
            print('Alerta no presente')

    ##########################################################################
    ############       -=_BEHAVIOR DRIVEN TEST_=-              ###############
    ##########################################################################
    def get_elements(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "class":
                    elements = self.driver.find_element_by_class_name(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements

            except AttributeError:
                self.msj = ("get_elements AttributeError: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except NoSuchElementException:
                self.msj = ("get_elements NoSuchElementException: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except TimeoutException:
                self.msj = ("get_elements TimeoutException: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "get_elements: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def get_text(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_text: " + self.json_ValueToFind)
                print("Text Value : " + elements.text)
                return elements.text


            except NoSuchElementException:
                self.msj = ("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except TimeoutException:
                self.msj = ("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "get_text: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def get_all_elements(self, entity):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    self.all_elements = self.driver.find_elements_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    self.all_elements = self.driver.find_elements_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    self.all_elements = self.driver.find_elements_by_partial_link_text(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return self.all_elements

            except NoSuchElementException:
                self.msj = ("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except TimeoutException:
                self.msj = ("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "get_all_elements: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def get_select_elements(self, entity):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element_by_id(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element_by_name(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element_by_xpath(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element_by_partial_link_text(self.json_ValueToFind))

                print("get_elements: " + self.json_ValueToFind)
                return select

            # USO

            #       select by visible text  #       select.select_by_visible_text('Banana')

            #       select by value  #       select.select_by_value('1')

            except NoSuchElementException:
                self.msj = ("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except TimeoutException:
                self.msj = ("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "get_select_elements: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def esperar_elemento(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

            except TimeoutException:
                self.msj = u"TimeoutException: Esperar_Elemento: No presente " + locator
                Functions.tearDown(self, "fail")
            except NoSuchElementException:
                self.msj = u"NoSuchElementException: Esperar_Elemento: No presente " + locator
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "esperar_elemento: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def page_has_loaded(self):
        driver = self.driver
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState;')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completo la carga"

    def descartar_elemento(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.invisibility_of_element((By.ID, self.json_ValueToFind)))
                    print(u"Descartar_elemento: Se invisivilizo " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.invisibility_of_element((By.XPATH, self.json_ValueToFind)))
                    print(u"Descartar_elemento: Se invisivilizo " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.invisibility_of_element((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Descartar_elemento: Se invisivilizo " + locator)
                    return True

            except TimeoutException:
                self.msj = (u"Esperar_Elemento: Presente " + locator)
                Functions.tearDown(self, "fail")
                # self.driver.close()

    ##########################################################################
    ##############       -=_JS     CLICKS _=-              ###################
    ##########################################################################
    def remove_with_js(self, locator, key, value, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].removeAttribute('{key}', '{value}')").format(key=key, value=value)
                    print(instruccion_js)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].removeAttribute('{key}', '{value}')").format(key=key, value=value)
                    print(instruccion_js)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].removeAttribute('{key}', '{value}')").format(key=key, value=value)
                    print(instruccion_js)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].removeAttribute('{key}', '{value}')").format(key=key, value=value)
                    print(instruccion_js)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

            except TimeoutException:
                print(u"set_with_js: No presente " + locator)
                Functions.tearDown(self)
                # self.driver.close()

    def set_with_js(self, locator, key, value, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].setAttribute('{key}', '{value}')").format(key=key, value=value)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].setAttribute('{key}', '{value}')").format(key=key, value=value)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].setAttribute('{key}', '{value}')").format(key=key, value=value)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    instruccion_js = ("arguments[0].setAttribute('{key}', '{value}')").format(key=key, value=value)
                    self.driver.execute_script(instruccion_js, localizador)
                    return True

            except TimeoutException:
                print(u"set_with_js: No presente " + locator)
                Functions.tearDown(self)
                # self.driver.close()

    def js_clic(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)
        Functions.esperar_elemento(self, locator, MyTextElement)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    localizador = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

            except TimeoutException:
                self.msj = (u"js_clic: No presente " + locator)
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "js_clic: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def js_clic_xpath(self, xpath):
        try:
            localizador = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].click();", localizador)
            print("JS_Click_Xpath: Se hizo click en: " + xpath)
            return True

        except NoSuchElementException:
            print("JS_Click_Xpath: No se encontro " + xpath)
            return False

    def js_clic_id(self, ID):
        try:
            localizador = self.driver.find_element_by_id(ID)
            self.driver.execute_script("arguments[0].click();", localizador)
            print("JS_Click_ID: Se hizo click en: " + ID)
            return True

        except NoSuchElementException:
            print("JS_Click_ID: No se encontro " + ID)
            return False

    def js_clic_link(self, LINK):
        try:
            localizador = self.driver.find_element_by_partial_link_text(LINK)
            self.driver.execute_script("arguments[0].click();", localizador)
            print("JS_Click_Link: Se hizo click en: " + LINK)
            return True

        except NoSuchElementException:
            print("JS_Click_Link: No se encontro " + LINK)
            return False

    def js_clic__css(self, css):
        try:
            localizador = self.driver.find_element_by_css_selector(css)
            self.driver.execute_script("arguments[0].click();", localizador)

        except NoSuchElementException:
            print("JS_Click_CSS: No se encontro " + css)
            return False

    ##########################################################################
    ##############   -=_JS     IR     A _=-                ###################
    ##########################################################################
    def ir_a_xpath(self, elemento):
        try:
            localizador = self.driver.find_element(By.XPATH, elemento)
            self.driver.execute_script("arguments[0].scrollIntoView();", localizador)

        except TimeoutException:

            print(u"ir_a_xpath: No presente " + elemento)
            Functions.tearDown(self)
            # self.driver.close()

        print(u"ir_a_xpath: Se desplazÃ³ al elemento, " + elemento)
        return True

    def scroll_to(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

            except TimeoutException:
                self.msj = (u"scroll_to: No presente " + locator)
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "scroll_to: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    ##########################################################################
    ##############    -=_ACTION CHAINS _=-                ###################
    ##########################################################################
    def mouse_over(self, locator):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(localizador)
                    action.click(localizador)
                    action.perform()
                    print(u"mouse_over: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(localizador)
                    action.click(localizador)
                    action.perform()
                    print(u"mouse_over: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(localizador)
                    action.click(localizador)
                    action.perform()
                    print(u"mouse_over: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    action = ActionChains(self.driver)
                    action.move_to_element(localizador)
                    action.click(localizador)
                    action.perform()
                    print(u"mouse_over: " + locator)
                    return True

            except TimeoutException:
                print(u"mouse_over: No presente " + locator)
                Functions.tearDown(self)
                return None
            except UnexpectedAlertPresentException as e:
                self.msj = "mouse_over: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def mouse_over_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def mouse_over_css(self, css):
        element = self.driver.find_element_by_css_selector(css)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        ##########################################################################

    ##############    -=_VERIFICACION _=-                ###################
    ##########################################################################
    def verificar_xpath(self, xpath):  # devuelve true o false
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            print(u"Verificar: Elemento No presente " + str(xpath))
            return False
            Functions.tearDown(self)
        print(u"Verificar: Se visualizo el elemento, " + str(xpath))
        return True

    def verificar_id(self, ID):  # devuelve true o false
        try:
            self.driver.find_element_by_id(ID)
        except NoSuchElementException:
            print(u"Verificar: Elemento No presente " + str(ID))
            return False
        print(u"Verificar: Se visualizo el elemento, " + str(ID))
        return True

    def verificar_css(self, CSS):  # devuelve true o false
        try:
            self.driver.find_element_by_css_selector(CSS)
        except NoSuchElementException:
            print(u"Verificar: Elemento No presente " + str(CSS))
            return False
            Functions.tearDown(self)
        print(u"Verificar: Se visualizo el elemento, " + str(CSS))
        return True

    def verificar_texto(self, locator, TEXTO):  # devuelve true o false

        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:

            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                    ObjText = self.driver.find_element_by_id(self.json_ValueToFind).text

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                    ObjText = self.driver.find_element_by_name(self.json_ValueToFind).text

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                    ObjText = self.driver.find_element_by_xpath(self.json_ValueToFind).text

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    ObjText = self.driver.find_element_by_partial_link_text(self.json_ValueToFind).text

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    ObjText = self.driver.find_element_by_css_selector(self.json_ValueToFind).text

                self.msj = (
                            u"Assert Text: el valor mostrado en: " + locator + " es: " + ObjText + " el esperado es: " + TEXTO)
                assert TEXTO == ObjText, self.msj

            except AssertionError:
                Functions.tearDown(self, "fail")

            except TimeoutException:
                Functions.tearDown(self, "fail")

            except NoSuchElementException:
                Functions.tearDown(self, "fail")

            except UnexpectedAlertPresentException as e:
                self.msj = "verificar_texto: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def verificar_texto_xpath(self, xpath, TEXTO):  # devuelve true o false
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), TEXTO))
        except NoSuchElementException:
            print(u"Verificar Texto: No presente Xpath" + xpath + " el texto, " + TEXTO)
            # self.driver.close()
            Functions.tearDown(self)
        print(u"Verificar Texto: Se visualizó en, " + xpath + " el texto, " + TEXTO)
        return True

    def verificar_texto_id(self, ID, TEXTO):  # devuelve true o false
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.ID, ID), TEXTO))
        except TimeoutException:
            print(u"Verificar Texto: No presente en" + ID + " el texto, " + TEXTO)
            # self.driver.close()
            Functions.tearDown(self)
        print(u"Verificar Texto: Se visualizó en, " + ID + " el texto, " + TEXTO)
        return True

    def switch_to_iframe(self, Locator):
        iframe = Functions.get_elements(self, Locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_relative_windows(self, x):
        windows = self.driver.window_handles
        print(windows)
        if x == "Principal":
            self.driver.switch_to.window(self.principal)
            print("volviendo a " + x + " : " + self.principal)
        else:
            self.window_after = self.driver.window_handles[int(x)]
            self.driver.switch_to.window(self.window_after)
            Functions.page_has_loaded(self)
            Functions.alert_windows(self, "accept", 4)
            print("Estas en " + x + " : " + self.window_after)
            self.ventanas[x] = self.window_after

    def close_all_alerts(self):
        title = self.driver.title
        self.nWindows = 0
        while self.nWindows < len(self.driver.window_handles):
            title = self.driver.title
            print("El titulo es ---------> " + title)
            self.driver.switch_to.window(self.driver.window_handles[int(self.nWindows)])
            Functions.page_has_loaded(self)
            Functions.alert_windows(self, "accept", 4)
            self.nWindows = self.nWindows + 1
            continue

    def save_windows_name(self, name):
        title = self.driver.title
        self.nWindows = 0
        while title != name:
            title = self.driver.title
            print("El titulo es ---------> " + title)

            if (self.nWindows > len(self.driver.window_handles)):
                break

            self.driver.switch_to.window(self.driver.window_handles[int(self.nWindows)])
            Functions.page_has_loaded(self)
            Functions.alert_windows(self, "accept", 1)

            if self.driver.title == name:
                self.ventanas[name] = self.driver.current_window_handle
                print(f"Se almaceno el valor de la ventana: {self.ventanas[name]}")
                break

            self.nWindows = self.nWindows + 1
            continue

    def switch_to_windows_name(self, ventana):
        EXIST = False
        if ventana in self.ventanas:
            Functions.esperar(self, 5)
            self.driver.switch_to.window(self.ventanas[ventana])
            Functions.page_has_loaded(self)
            print("volviendo a " + ventana + " : " + self.ventanas[ventana])
        else:
            try:
                Functions.esperar(self)
                wtime = 0
                self.nWindows = len(self.driver.window_handles) - 1
                EXIST = self.driver.window_handles[int(self.nWindows)] in self.ventanas.values()
                print("---------> " + self.driver.window_handles[int(self.nWindows)])
                print("---------> " + str(self.ventanas.values()))
                print("---------> " + str(EXIST))

                while EXIST:
                    self.nWindows = 0
                    while (self.nWindows <= len(self.driver.window_handles)):
                        print("---------> window_handles TOTAL while " + str(self.driver.window_handles))
                        print("---------> window_handles while " + self.driver.window_handles[int(self.nWindows)])
                        print("---------> ventanas while " + str(self.ventanas.values()))
                        print("---------> in EXIST while " + str(EXIST))
                        # self.nWindows = len(self.driver.window_handles) - 1
                        EXIST = self.driver.window_handles[int(self.nWindows)] in self.ventanas.values()
                        if EXIST == False:
                            break
                        wtime = wtime + 1
                        self.nWindows = self.nWindows + 1
                        Functions.esperar(self, 1)

                        if wtime == 30:
                            break
                        continue
                if EXIST == False:
                    self.ventanas[ventana] = self.driver.window_handles[int(self.nWindows)]
                    print(EXIST)

                print(self.ventanas)
                self.driver.switch_to.window(self.ventanas[ventana])
                Functions.page_has_loaded(self)
                Functions.alert_windows(self, "accept", 4)
                self.driver.maximize_window()
                print("Estas en " + ventana + " : " + self.ventanas[ventana])

            except KeyError:
                self.msj = f"KeyError: La ventana: {ventana} no existe en {self.ventanas}"
                Functions.tearDown(self, "fail")
            except IndexError:
                self.msj = f"IndexError: No se encontraron nuevas ventanas"
                Functions.tearDown(self, "fail")
            except NoSuchWindowException:
                self.msj = f"NoSuchWindowException: Error retrieving window"
                Functions.tearDown(self, "fail")
            except UnexpectedAlertPresentException as e:
                self.msj = "switch_to_windows_name: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")

    def save_variable_scenary(self, element, variable):
        Scenario[variable] = Functions.get_text(self, element)
        print(Scenario)
        print("Se almaceno el valor " + variable + " : " + Scenario[variable])

    def save_text_variable_scenary(self, MyText, variable):
        Scenario[variable] = MyText
        print(Scenario)
        print("Se almaceno el valor " + variable + " : " + Scenario[variable])

    def compare_with_variable_scenary(self, element, variable):
        variable_scenary = str(Scenario[variable])
        element_text = str(Functions.get_text(self, element))
        _exist = (variable_scenary in element_text)
        print(f'Comparando los valores... verificando si {variable_scenary} esta presente en {element_text} : {_exist}')
        assert variable_scenary in element_text, f'{variable_scenary} != {element_text}'

    def compare_be_diferent(self, element, expected):
        element_text = str(Functions.get_text(self, element))
        _diff = (expected != element_text)
        print(f'Comparando los valores... verificando si {expected} es diferente a {element_text} : {_diff}')
        assert _diff == True, f'{variable_scenary} = {element_text}'

    def new_ventana(self, ventana="new_ventana"):
        new_window = self.driver.current_window_handle
        self.ventanas[ventana] = new_window
        self.driver.switch_to.window(self.ventanas[ventana])
        self.driver.maximize_window()
        print(self.ventanas)
        print("Estas en " + ventana + " : " + self.ventanas[ventana])

    def switch_to_parentFrame(self):
        self.driver.switch_to.parent_frame()

    def switch_to_active_element(self):
        self.driver.switch_to.active_element

    def send_especific_keys(self, element, key):
        if key == 'Enter':
            Functions.get_elements(self, element).send_keys(Keys.ENTER)
        if key == 'Tab':
            Functions.get_elements(self, element).send_keys(Keys.TAB)
        if key == 'Space':
            Functions.get_elements(self, element).send_keys(Keys.SPACE)
        time.sleep(3)

    ##############   -=_CAPTURA DE PANTALLA_=-   #############################
    ##########################################################################
    def crear_path(self):
        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 horas
            return hora

        dia = time.strftime("%d-%m-%Y")  # formato aaaa/mm/dd

        GeneralPath = Inicializar.Path_Evidencias
        DriverTest = Inicializar.NAVEGADOR
        TestCase = self.__class__.__name__
        horaAct = horaGlobal
        x = re.search("Context", TestCase)
        if (x):
            path = GeneralPath + "/" + dia + "/" + DriverTest + "/" + horaAct + "/"
        else:
            path = GeneralPath + "/" + dia + "/" + TestCase + "/" + DriverTest + "/" + horaAct + "/"

        if not os.path.exists(path):  # si no existe el directorio lo crea

            os.makedirs(path)

        return path

    def capturar_pantalla(self):
        img = self.crear_path()
        self.driver.get_screenshot_as_file(img)
        print(img)
        return img

    def captura(self, Descripcion):
        self.Descripcion = Descripcion
        path = Functions.crear_path(self)
        TestCase = self.__class__.__name__
        x = re.search('Context', TestCase)
        if (x):
            TestCase = Descripcion

        def hora_Actual():
            hora = time.strftime("%H%M%S")  # formato 24 horas
            return hora

        img = f'{path}{TestCase}_(' + str(hora_Actual()) + ')' + '.png'
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), Descripcion, attachment_type=allure.attachment_type.PNG)

    ##############   -=_Wait Elements_=-   #############################
    ##########################################################################
    def esperar(self, timeLoad=8):
        print("Esperar: Inicia (" + str(timeLoad) + ")")
        try:
            totalWait = 0
            while (totalWait < timeLoad):
                # print("Cargando ... intento: " + str(totalWait))
                time.sleep(1)
                totalWait = totalWait + 1
        finally:
            print("Esperar: Carga Finalizada ... ")

    def modificar_xml_enviroments(self):

        print("--------------------------------------")
        print("Estableciendo Datos del Reporte...")
        JOB_NAME = 'VARIABLE DE JENKINS JOB_NAME'
        # os.environ['JOB_NAME']
        NODE_NAME = 'VARIABLE DE JENKINS NODE_NAME'
        # os.environ['NODE_NAME']
        NAVEGADOR = Inicializar.NAVEGADOR
        print(NODE_NAME)
        print(JOB_NAME)
        print(NAVEGADOR)
        print("--------------------------------------")

        Enviroment = open('../data/environment.xml', 'w')
        Template = open('../data/environment_Template.xml', 'r')

        with Template as f:
            texto = f.read()

            texto = texto.replace("JOB_NAME", JOB_NAME)
            texto = texto.replace("NODE_NAME", NODE_NAME)
            texto = texto.replace("NAVEGADOR", NAVEGADOR)

        with Enviroment as f:
            f.write(texto)

        Enviroment.close()
        Template.close()

        time.sleep(5)

        if os.path.exists("../allure-results"):  # si no existe el directorio lo crea

            shutil.rmtree("../allure-results")

        try:
            os.makedirs("../allure-results")
        except OSError:
            print("No se pudo generar la carpeta ../allure-results")

        shutil.copy("../data/environment.xml", "../allure-results")

    # Excel
    def leer_celda(self, celda):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        sheet = wb["DataTest"]
        valor = str(sheet[celda].value)
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es de es: " + Inicializar.Excel)
        print(u"El valor de la celda es: " + valor)
        print(u"------------------------------------")
        return valor

    def escribir_celda(self, celda, valor):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        hoja = wb["DataTest"]
        hoja[celda] = valor
        wb.save(Inicializar.Excel)
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es de es: " + Inicializar.Excel)
        print(u"Se escribio en la celda " + str(celda) + u" el valor: " + str(valor))
        print(u"------------------------------------")

    ##########################################################################
    ##############   -=_ASSERTION_=-   #######################################
    ##########################################################################

    def validar_elemento(self, locator):

        Get_Entity = Functions.get_entity(self, locator)

        TIME_OUT = 10

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

            except TimeoutException:
                print(u"Assert_xpath: Elemento No presente " + locator)
                return False


    def assert_xpath(self, xpath):
        try:

            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        except TimeoutException:
            print(u"Assert_xpath: Elemento No presente " + xpath)
            self.assertTrue(False)

        print(u"Assert_xpath: Se visualizo el elemento, " + xpath)
        self.assertTrue(True)

    def assert_id(self, id):
        try:

            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.visibility_of_element_located((By.ID, id)))

        except TimeoutException:
            print(u"Assert_xpath: Elemento No presente " + id)
            self.assertTrue(False)

        print(u"Assert_xpath: Se visualizo el elemento, " + id)
        self.assertTrue(True)

    ##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print(Inicializar.basedir)
        print("---------------")

        if navegador == ("IExplorer"):
            caps = DesiredCapabilities.INTERNETEXPLORER
            caps['ignoreProtectedModeSettings'] = True
            self.driver = webdriver.Ie(Inicializar.basedir + "\\drivers\\IEDriverServer.exe", caps)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options,
                                           executable_path=Inicializar.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("CHROME_headless"):
            options = OpcionesChrome()
            options.add_argument('headless')
            options.add_argument('--start-maximized')
            options.add_argument('--lang=es')
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("CHROME_GRID"):
            options = OpcionesChrome()
            options.add_argument('--start-maximized')
            options.add_argument('--lang=es')
            options.add_argument('window-size=1920x1080')
            self.driver = driver = webdriver.Remote(desired_capabilities=options.to_capabilities())
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("FIREFOX_GRID"):
            self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                           desired_capabilities=DesiredCapabilities.FIREFOX)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        elif navegador != ("CHROME_headless") and navegador != ("CHROME") and navegador != ("FIREFOX"):
            print("----------------")
            print("Define el DRIVER")
            print("----------------")
            pytest.skip("Define el DRIVER")
            exit

    def tearDown(self, test="pass"):
        print("Se cerrará  el DRIVER")
        self.driver.quit()
        if test == "fail":
            testFail = False
            msj = self.msj
            if self.msj == "":
                assert testFail == True, "Test Fail"
            else:
                assert testFail == True, msj

    def textDateEnvironmentReplace(self, text):
        meDateFormat = '%d/%m/%Y'
        if text == 'today':
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'LastMonth':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'format_today':
            self.today = datetime.date.today()
            text = self.today.strftime(meDateFormat)

        if text == 'format_yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(meDateFormat)

        if text == 'format_LastMonth':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(meDateFormat)

        print(text)
        return text


    # -------------------------------------------------------------------------------------------#
    ########## ########## ##########  Database ########## ########## ########## ########## ##########
    # -------------------------------------------------------------------------------------------#

    def pyodbc_conn(self, _host=Inicializar.DB_HOST, _dbname=Inicializar.DB_DATABASE, _user=Inicializar.DB_USER, _pass=Inicializar.DB_PASS):
        try:
            self.conn = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=' + _host + ';'
                                    'Database=' + _dbname + ';'
                                                            'uid=' + _user + ';'
                                                                             'pwd=' + _pass + ';'
                                                                                              'Trusted_Connection=no'
            )
            self.cursor = self.conn.cursor()
            print("Always Connected")

        except (pyodbc.OperationalError) as error:
            self.conn = None
            self.cursor = None
            pytest.skip("Error en connection strings: " + str(error))

        return self.conn

    def pyodbc_query(self, _query):
        if self.conn is not None:
            try:
                self.cursor.execute(_query)
                self.Result = self.cursor.fetchall()
                for row in self.Result:
                    print(row)

            except (pyodbc.Error) as error:
                print("Error en la consulta", error)

            finally:
                if (self.conn):
                    self.cursor.close()
                    self.conn.close()
                    print("pyodbc Se cerró la conexion")

    ##########################################################################
    #########################   -=_WEB API TEST_=-   #########################
    ##########################################################################

    def get_loginToken(self, user=Inicializar.API_User, password=Inicializar.API_Pass):
        _baseApi = Inicializar.API_hostAddressBase + "authentication/login"

        data = {
            'grant_type': 'password',
            'username': user,
            'password': password
        }

        _response = requests.post(_baseApi, data=data, headers=Inicializar.API_headers)
        self.json_response = json.loads(_response.text)
        self.access_token = self.json_response['access_token']
        print(self.access_token)
        return self.access_token

    def get_full_host(self, _PartHost):
        _RegexPartHost = str(Functions.ReplaceWithContextValues(self, _PartHost))
        self._endpoint = Inicializar.API_hostAddressBase + _RegexPartHost
        print(self._endpoint)
        return self._endpoint

    def ReplaceWithContextValues(self, text):
        PatronDeBusqueda = r"(?<=Scenario:)\w+"
        variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
        for variable in variables:
            if variable == 'today':
                dateToday = str(datetime.date.today().strftime("%Y-%m-%dT%H:%M:%S"))
                text = re.sub('(Scenario:)([^&.]+)', dateToday, text, re.IGNORECASE)
                continue
            text = re.sub('(Scenario:)([^.]+)', Scenario[variable], text, re.IGNORECASE)
        return text

    def do_a_get(self):
        #Inicializar.API_headers['Authorization'] = "Bearer " + self.access_token
        new_header = Inicializar.API_headers
        self._response = requests.get(self._endpoint, headers=new_header)
        return self._response

    def do_a_put(self):
        Inicializar.API_headers['Authorization'] = "Bearer " + self.access_token
        new_header = Inicializar.API_headers
        print(self._new_body)
        self._response = requests.put(self._endpoint, headers=new_header, data=json.dumps(self._new_body))
        return self._response

    def do_a_post(self):
        Inicializar.API_headers['Authorization'] = "Bearer " + self.access_token
        new_header = Inicializar.API_headers
        print(self._new_body)
        self._response = requests.post(self._endpoint, headers=new_header, data=json.dumps(self._new_body))
        return self._response

    def print_api_response(self):
        self.json_response = json.loads(self._response.text)
        print(json.dumps(self.json_response, indent=3))

    def get_response_by_entity(self, path, entity):
        self.json_response = json.loads(self._response.text)
        print(self.json_response[int(path)][entity])

    def assert_response_expected(self, entity, expected, subPath = 0):
        self.json_response = json.loads(self._response.text)
        PATH_VALUE = self.json_response[entity]
        list =  isinstance(PATH_VALUE, list)
        dict = isinstance(PATH_VALUE, dict)
        if list:
            PATH_VALUE = self.json_response[entity][int(subPath)]

        if dict:
            PATH_VALUE = self.json_response[entity][subPath]

        assert str(PATH_VALUE) == expected, f"El valor no es el esperado: {PATH_VALUE} != {expected}"


    class json_value(object):
        def __init__(self, data):
            self.__dict__ = json.loads(data)

    def new_compare_entity_values(self, path="''", values="''"):
        esperado = str(values)
        json_res = Functions.json_value(self._response.text)

        try:
            tree_obj = objectpath.Tree(self.json_response)
            entity = tuple(tree_obj.execute('$.' + path))
            print(entity)

        except SyntaxError:
            entity = str(None)
            print("No se pudo obtener ningun valor de la busqueda")

        if entity == esperado:
            unittest.TestCase.assertTrue(self, str(entity) == esperado, path + u"Es igual a " + str(entity))
            print(path + u" es igual a " + entity)
            print("-------------------------------")
        else:
            print(u"El valor esperado en " + path + " es  " + esperado + ". El valor recibido fue " + str(entity))
            unittest.TestCase.assertTrue(self, str(entity) == esperado, path + u"Es igual a " + str(entity))
            print("-------------------------------")


    def response_is_200(self):
        print("status code is: " + str(self._response.status_code))
        assert self._response.status_code == 200

    def response_is_403(self):
        print("status code is: " + str(self._response.status_code))
        assert self._response.status_code == 403

    def set_body_values(self, entity, value):
        def set_ramdon_values(self):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(10))

        if value.lower() == "random":
            value = set_ramdon_values(self)
            if entity.lower() == "userid":
                value = set_ramdon_values(self) + ".test"
            if entity.lower() == "email":
                value = set_ramdon_values(self) + "@raet.com"

        Inicializar.API_body[entity] = value
        self._new_body = Inicializar.API_body
        print((json.dumps(self._new_body, indent=4)))
        return self._new_body

    def get_json_inData(self, file):
        json_path = Inicializar.JsonResponseData + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_inData: " + file)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)

    def set_initial_json_body(self, file):
        self.New_Body = Functions.get_json_inData(self, file)
        Inicializar.API_body = self.New_Body
        print(Inicializar.API_body)

    def expected_results_value(self, file):
        self.json_strings = Functions.get_json_inData(self, file)
        try:
            assert self.json_strings == self.json_response
            print(u"Se cumplió con el valor esperado")
            verificar = True
        except AssertionError:
            verificar = False
            print("La respuesta fue: ")
            print(json.dumps(self.json_response, indent=4))
            print("Se esperaba: ")
            print(json.dumps(self.json_strings, indent=4))
            assert verificar == True