Feature: Login into 42 intra and search for Gemartin profile
	Scenario: Login into 42 intra and search a profile
		Given open the url "https://www.intra.42.fr/"
			When I enter my login
			And I enter my Password
			And I click on the "Sign in" button
			Then I enter "Gemartin" in the search field
			And I click on the "Search" button
			Then I click on the "Gemartin" profile
			And see the "Gemartin" profile