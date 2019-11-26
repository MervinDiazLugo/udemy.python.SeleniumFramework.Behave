# Created by Mervin at 25/11/2019
@selenium
Feature: Funciones basicas de selenium con BDD

  @Navegador
  Scenario: Abrir el navegador
    Given Abrir la aplicacion

  @Navegador
  Scenario: Abrir url
    Given Inicilizo la app en la URL https://www.toolsqa.com/cucumber/behavior-driven-development/

  @Navegador
  Scenario: Abrir con Navegador
    Given Abro la app con el navegador FIREFOX
    Then cierro la app

  @FuncionesSelenium
  @DOM
  Scenario: Setear el DOM y trabajar con el
    Given Abrir la aplicacion
    And Cargo el DOM de la App: Spotify_registro
    And En el campo Email escribo mervindiazlugo@gmail.com
    Then cierro la app

  @Capturas
  Scenario: Tomar capturas de pantalla
    Given Abrir la aplicacion
    And Cargo el DOM de la App: Spotify_registro
    And En el campo Email escribo mervindiazlugo@gmail.com
    And Capturo pantalla: EmailSpoty
    And Tomar Captura: Test003
    Then cierro la app

  @TextyDrop
  Scenario: Dropdowns y textbox
    Given Abrir la aplicacion
    And Cargo el DOM de la App: Spotify_registro
    And En el campo Email escribo mervindiazlugo@gmail.com
    And En el dropdown Mes de Nacimiento selecciono febrero
    And En el combobox Mes de Nacimiento selecciono 03
    Then cierro la app

   Scenario: clics Frames y Ventanas
     Given Inicilizo la app en la URL https://chercher.tech/practice/frames-example-selenium-webdriver
     And Cargo el DOM de la App: frames
     And Me desplazo al frame: Frame2
     And En el dropdown Frame2 Select selecciono Avatar
     And Vuelvo al frame padre
     And Me desplazo al frame: Frame1
     And En el campo Frame1 input escribo Hola Chicos de Udemy
     And Me desplazo al frame: Frame3
     And Hago clic en Frame3 input
     And Tomar Captura: Test005
     Then cierro la app

   Scenario: Buscar por texto scroll y waits
     Given Abrir la aplicacion
     And Cargo el DOM de la App: Spotify_registro
     Then Hago scroll hacia el elemento: Already
     And Cliqueo en Texto: Iniciar ses
     And Espero 8 segundos
     And Esperar que finalice la carga
     Then cierro la app