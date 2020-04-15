@Integration
Feature: Test WebApi

  @WebApi
  Scenario: Login with Webapi
    Given I connect with endpoint pet/11
	#And I do API login with Admin credentials
    When I do a Get
    And I print out the results of the response
    Then The api response is 200 Ok

   Scenario: Retrieve pet information by Id
    Given I connect with endpoint pet/21
	#And I do API login with Admin credentials
    When I do a Get
    And I print out the results of the response
    Then The api response is 200 Ok
    And I assert response in entity name is Mervin
    And I assert response in entity id is 21
    And I assert that response in entity photoUrls path 0 is string
    And I assert that response in entity tags path 0 is {'id': 5, 'name': 'Animal'}

  @WebApi
  Scenario: Put Recovery Password - try Recovery with no admin user
    Given I connect with endpoint administration/tenants/users/passwordRecovery
	And I do the login with User mdiaz and Password Mm121666
    When I set the entity UserId with the value mervin.diaz
    When I do a Put
    And I print out the results of the response
    Then The api response is 403 Unauthorized

  @WebApi
  Scenario: Put - Update user password InternalUser vs InternalUser
  Given I do API login with Admin credentials
	And I do the login with User webapi and Password suipacha
    When I set the entity Password with the value Suipacha2018!
    When I do a Put
	Then I print out the results of the response
	Then The api response is 200 Ok

  @WebApi
  Scenario: Put - Update user password InternalUser vs InternalUser compare
  Given I connect with endpoint userManagement/users/internaluser/password
	And I do the login with User webapi and Password suipacha
    When I set the entity Password with the value Suipacha2018!
    When I do a Put
	Then I print out the results of the response
	Then The api response is 200 Ok
	And The result JSON has the fields and the values in InternalUserPassChange

    @WebApi
    Scenario: Post Clone - Clone a user
      Given I connect with endpoint userManagement/users/webapi/clone
      And I do API login with Admin credentials
      When I set the body with Send_Clone
      When I set the entity UserId with the value random
      When I set the entity FullName with the value random
      When I set the entity Email with the value random
      When I set the entity Password with the value Suipacha2018!
      When I do a Post
      Then I print out the results of the response
	  Then The api response is 200 Ok
      And The result JSON has the fields and the values in CloneUser

    @WebApi
    Scenario: Post Clone - Clone a user compare results
      Given I connect with endpoint userManagement/users/webapi/clone
      And I do API login with Admin credentials
      When I set the entity UserId with the value random
      When I set the entity FullName with the value random
      When I set the entity Email with the value random
      When I set the entity Password with the value Suipacha2018!
      When I do a Post
      Then I print out the results of the response
	  Then The api response is 200 Ok
