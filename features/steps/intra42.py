from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('Launch chrome browser 1')
def step_impl(context):
	context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('open the url "https://www.intra.42.fr/"')
def step_impl(context):
	context.driver.implicitly_wait(5)
	context.driver.get("https://signin.intra.42.fr/users/sign_in")

@then('I enter my login')
def step_impl(context):
	context.driver.implicitly_wait(60)
	context.driver.find_element(By.XPATH, "//input[@placeholder='Login']").send_keys("dnunez-m")

@then('I enter my Password')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="user_password"]').send_keys("b-43535883-B")

@then('I click on the "Sign in" button')
def step_impl(context):
	context.driver.implicitly_wait(3)
	context.driver.find_element(By.XPATH, '//*[@id="new_user"]/div[2]/input').click()

@then('I enter "Gemartin" in the search field')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form/span/input").send_keys("Proche-c")


@then('I click on the "Search" button')
def step_impl(context):
	context.driver.implicitly_wait(3)
	context.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form/span/input").send_keys(Keys.ENTER)

@then('I click on the "Gemartin" profile')
def step_impl(context):
	context.driver.implicitly_wait(3)
	context.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/div/a/div[2]/h4").click()

@then('see the "Gemartin" profile')
def step_impl(context):
	test = True
	login = context.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div/h2/span[3]").text
	if login != "Gemartin":
		test = False
	assert test is True

@then('I close the browser')
def step_impl(context):
	context.driver.close()
