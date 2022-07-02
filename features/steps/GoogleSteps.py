from selenium.webdriver.common.by import By

@given('open google page')
def step_impl(context):
    context.driver.get("https://www.google.com/")

@then('verify that the logo present on page')
def step_impl(context):
    status=context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/img").is_displayed()
    assert status is True