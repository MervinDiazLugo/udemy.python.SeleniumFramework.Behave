# -*- coding: utf-8 -*-
'''
Created on 17 may. 2018

@author: MD432339
'''

class Inicio:

    img_Logo_xpath           = "//*[contains (@id, 'hplogo')]"
    #"//*[@id='hplogo']/a/img"
    txt_busqueda_xpath        = "//input[@name='q']"
    
    txt_resultStats_xpath = "//*[@id='resultStats']"

    link_Metallica_xpath = "//*[@href='https://www.metallica.com/']//*[contains(text(),'Metallica')]"

    link_Maiden_xpath = "//h3[contains(text(),'Iron Maiden - Official Website')]"

    txt_resultOne_xpath = "(//div[@id='rso']/div/div/div/div/div/div/a/h3)[1]"
    
    #Sin ingreso de usuario y clave
    #"CMN-10013: El nombre de usuario y la contrase�a son obligatorios."
    
    #Ingreso usuario valido y contrase�a invalida
    #"CMN-01002: El nombre de usuario y la contrase�a no son v�lidos. Tenga en cuenta que la contrase�a distingue entre may�sculas y min�sculas.
    