from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

@given('I am on the DuckDuckGo home page')
def launchBrowserDuck(context):
	context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
	context.driver.get("https://www.duckduckgo.com/")


@when('I search term as "LambdaTest" on DuckDuckGo')
def wordSearchDuck(context):
	context.driver.find_element(By.XPATH, "//input[@id='search_form_input_homepage']").send_keys("LambdaTest")
	context.driver.find_element(By.XPATH, "//input[@id='search_form_input_homepage']").send_keys(Keys.ENTER)
	

@then('Search results for LambaTest should appear')
def resultsDuck(context):
	statusD=context.driver.find_element(By.XPATH, "//*[@id='links_wrapper']/div[1]").is_displayed()
	assert statusD is True
	context.driver.close()
	context.driver.quit()
	print("Test Passed")



@given('I am on the Google home page')
def launchBrowserGoogle(context):
	context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
	context.driver.get("https://www.google.com/")

@when('I search term as "LambdaTest" on Google')
def wordSearchGoogle(context):
	WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='L2AGLb']/div"))).click() 
	context.driver.find_element(By.CSS_SELECTOR, "input[name='q']").send_keys("LambdaTest")
	context.driver.find_element(By.CSS_SELECTOR, "input[name='q']").send_keys(Keys.ENTER)


@then('Search results for LambdaTest should appear')
def resultsGoogle(context):
	statusG=context.driver.find_element(By.XPATH, "//div[@class='g']").is_displayed()
	assert statusG is True
	context.driver.close()
	context.driver.quit()
	print("Test Passed")

