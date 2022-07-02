"""
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def step_impl(context):
	context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
"""
from selenium.webdriver.common.by import By

@given('open google page')
def step_impl(context):
    context.driver.get("https://www.google.com/")

@then('verify that the logo present on page')
def step_impl(context):
    status=context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/img").is_displayed()
    assert status is True