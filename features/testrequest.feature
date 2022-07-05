Feature: Test with request
	Scenario: First Test
		Given I start the test
			When I request the JSON
			And I parse the JSON
			Then I get the expected result