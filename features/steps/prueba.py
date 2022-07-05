from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'estoy en la pagina')
def step_impl(context):
	context.driver.get("https://pypi.org/")

@when(u'busco "selenium" en el buscador')
def step_impl(context):
	context.driver.find_element(By.XPATH, '//*[@id="search"]').send_keys("behave")
	context.driver.find_element(By.XPATH, '//*[@id="search"]').send_keys(Keys.ENTER)

@then(u'tengo unos resultados')
def step_impl(context):
	status = context.driver.find_element(By.NAME, "behave")
	assert status is True