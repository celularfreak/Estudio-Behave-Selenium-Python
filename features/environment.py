from xvfbwrapper import Xvfb
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
	context.vdisplay = Xvfb()
	context.vdisplay.start()
	print("> Starting the browser")
	context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
	
def afer_all(context):
	print("> Closing the browser")
	context.driver.close()
	context.driver.quit()
	context.vdisplay.stop()