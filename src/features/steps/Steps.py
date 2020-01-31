# -*- coding: utf-8 -*-
from behave import *
import pytest
import unittest
from behave import *
from selenium.webdriver.common.keys import Keys
from functions.Functions import Functions as Selenium
from functions.Inicializar import Inicializar
use_step_matcher("re")

class StepsDefinitions():

    @given("Abrir la aplicacion")
    def abrir_navegador(self):
        Selenium.abrir_navegador(self)
        Selenium.page_has_loaded(self)

    @given("Inicilizo la app en la URL (.*)")
    def step_impl(self, URL):
        Selenium.abrir_navegador(self, URL=URL)


    @given("Abro la app con el navegador (.*)")
    def step_impl(self, navegador):
        Selenium.abrir_navegador(self, navegador=navegador)


    @then("cierro la app")
    def step_impl(self):
        Selenium.tearDown(self)

    @step("Cargo el DOM de la App: (.*)")
    def step_impl(self, DOM):
       Selenium.get_json_file(self, DOM)


    @step("En el campo (.*) escribo (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_elements(self, locator).send_keys(text)

    @step("Capturo pantalla: (.*)")
    def step_impl(self, descripcion):
        Selenium.captura(self, descripcion)


    @step("Tomar Captura: (.*)")
    def step_impl(self, Captura):
        Selenium.captura(self, Captura)


    @step("En el dropdown (.*) selecciono (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_select_elements(self, locator).select_by_visible_text(text)

    @step("En el combobox (.*) selecciono (.*)")
    def step_impl(self, locator, value):
        Selenium.esperar_elemento(self, locator)
        Selenium.get_select_elements(self, locator).select_by_value(value)

    @step("Me desplazo al frame: (.*)")
    def step_impl(self, frame):
        Selenium.switch_to_iframe(self, frame)

    @step("Vuelvo al frame padre")
    def step_impl(self):
         Selenium.switch_to_parentFrame(self)

    @step("Hago clic en (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self, locator)


    @step("Cliqueo en Texto: (.*)")
    def step_impl(self, Text):
        Selenium.get_elements(self, "text", MyTextElement=Text).click()

    @then("Hago scroll hacia el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.scroll_to(self, locator)


    @step("Esperar que finalice la carga")
    def step_impl(self):
        Selenium.page_has_loaded(self)

    @step("Espero (.*) segundos")
    def step_impl(self, segundos):
        segundos = int(segundos)
        Selenium.esperar(self, segundos)

#######################################################
############### _ = - WEB API - = _ ###################
#######################################################
    @step("I do API login with Admin credentials")
    def step_impl(self):
        self.Authorization = Selenium.get_loginToken(self)
        return self.Authorization

    @step("I do the login with User (.*) and Password (.*)")
    def step_impl(self, User, Password):
        self.Authorization = Selenium.get_loginToken(self, User, Password)
        return self.Authorization


    @given('I connect with endpoint (.*)')
    def step_impl(self, host):
        self._endpoint = Selenium.get_full_host(self, host)
        return self._endpoint

    @when("I do a Get")
    def step_impl(self):
        self._response = Selenium.do_a_get(self)
        return self._response

    @when("I do a Put")
    def step_impl(self):
        Selenium.do_a_put(self)


    @when("I do a Post")
    def step_impl(self):
        Selenium.do_a_post(self)

    @step("I print out the results of the response")
    def step_impl(self):
        Selenium.print_api_response(self)

    @step("I set the entity (.*) with the value (.*)")
    def step_impl(self, entity, value):
        Selenium.set_body_values(self, entity, value)

    @then("The api response is 403 Unauthorized")
    def step_impl(self):
        Selenium.response_is_403(self)

    @then("The api response is 200 Ok")
    def step_impl(self):
        Selenium.response_is_200(self)


    @step("The result JSON has the fields and the values in (.*)")
    def step_impl(self, file):
        Selenium.expected_results_value(self, file)

    @step("The result JSON has this (.*) with (.*) value")
    def step_impl(self, PATH, VALUES):
        Selenium.compare_entity_values(self, PATH, VALUES)

    @step("Check path (.*) and value (.*)")
    def step_impl(self, path, entity):
        Selenium.get_response_by_entity(self, path, entity)

    @step("I assert response in entity (.*) is (.*)")
    def step_impl(self, entity, expected):
        Selenium.assert_response_expected(self, entity, expected)

    @step("I check StartDate of process is OK")
    def step_impl(self):
        Selenium.startDate_process_OK(self)

    @step("I check Progress is of process is 100")
    def step_impl(self):
        Selenium.Progress_is_100(self)

    @when("I set the body with (.*)")
    def step_impl(self, file):
        Selenium.set_initial_json_body(self, file)

    @step('The response JSON has this (.*) with (.*) value')
    def step_impl(self, PATH, VALUES):
        Selenium.new_compare_entity_values(self, PATH, VALUES)