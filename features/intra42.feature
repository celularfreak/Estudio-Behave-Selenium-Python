Feature: Login into 42 intra and search for Gemartin profile
	Scenario: Login into 42 intra and search a profile
		Given Launch chrome browser
		When open the url "https://www.intra.42.fr/"
			Then I enter my login
			And I enter my Password
			And I click on the "Sign in" button
			#Then I Click event on the agenda
			#And I click on the subscribe button
			Then I enter "Gemartin" in the search field
			And I click on the "Search" button
			Then I click on the "Gemartin" profile
			And see the "Gemartin" profile
			And I close the browser