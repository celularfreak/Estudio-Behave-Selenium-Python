Feature: Search using Google and DuckDuckGo
	Search for LambaTest on Google
	Search for LambaTest on DuckDuckGo
	Compare the results


@LambaTestSearch

	Scenario: Search for LambaTest on DuckDuckGo
		Given I am on the DuckDuckGo home page
		When I search term as "LambdaTest" on DuckDuckGo
		Then Search results for LambaTest should appear

	Scenario: Search for LambdaTest on Google
		Given I am on the Google home page
		When I search term as "LambdaTest" on Google
		Then Search results for LambdaTest should appear
