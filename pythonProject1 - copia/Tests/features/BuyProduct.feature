Feature: Buy a product
  As user
  I want to buy a product the Store page
  So confirm purchase correctly

  Scenario: Confirm a purchase from the store
    Given open the Store webPage
    When complete "3774418046" and "4907"
    And the account page is displayed
    And complete "7002811"
    And press the search button
    And can check the product "Apple Watch 5 40mm LTE"
    And press add product button
    And the my cart page is displayed
    And press continue button
    And the personal information page is displayed
    And complete mail "mispruebas.testing@gmail.com"
    And accept terms and conditions
    And press continue button payments
    And the payments page is displayed
    And select payment method and amount of installments
    And press continue button purchase summary
    And the purchase summary page is displayed
    And press continue confirm
    Then the confirm page is displayed

