import requests

@given(u'I start the test')
def step_impl(context):
	print("I start the test")

@when(u'I request the JSON')
def step_impl(context):
	context.r = requests.get('https://www.elperiodico.com/es/')
	print(context.r)
@when(u'I parse the JSON')
def step_impl(context):
	context.json = context.r.json()
	#print(context.json)


@then(u'I get the expected result')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get the expected result')