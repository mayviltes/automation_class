import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage
from Pages.HeaderPage import HeaderPage
from Pages.ProductPage import ProductPage
from Pages.MyCartPage import MyCartPage
from Pages.InfoPersonalPage import InfoPersonalPage
from Pages.PaymentPage import PaymentPage
from Pages.SummaryPage import SummaryPage
from Pages.ConfirmPage import ConfirmPage

# CONSTANTS
STORE_WEB = 'https://qa-tienda.claro.com.ar/catalogo/inicio#facet:&productBeginIndex:0&orderBy:6&pageView:grid&minPrice:&maxPrice:&pageSize:&'

# SCENARIOS
scenarios('../features/BuyProduct.feature')

# FIXTURES
@pytest.fixture
def browser():
    b = webdriver.Chrome('../../Drivers/chromedriver.exe')
    b.implicitly_wait(50)
    b.maximize_window()
    yield b
    b.quit()

# GIVEN STEPS
@given('open the Store webPage')
def go_login_page(browser):
    browser.get(STORE_WEB)

# WHEN STEPS
@when(parsers.parse('complete "{bill_number}" and "{password}"'))
def complete_user_pass(browser, bill_number, password):
    login_page = LoginPage(browser)

    login_page.getLogin_1().click()
    login_page.getUserInput().send_keys(bill_number)
    login_page.getPasswordBtn().send_keys(password)
    login_page.getLogin_2().click()

    print('Complete user and password')

@when('the account page is displayed')
def check_account(browser):
    account_page = AccountPage(browser)

    assert account_page.getNameTitle().text == 'Maria Lucinda Barboza'

    print('Account section is displayed')

@when(parsers.parse('complete "{product}"'))
def complete_product(browser, product):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(product)

    print('Complete product in search input')

@when('press the search button')
def press_button_lupa(browser):
    header_page = HeaderPage(browser)
    header_page.getLupaBtn().click()

    print('Press lupa button ')

@when(parsers.parse('can check the product "{title}"'))
def check_title_product(browser, title):
    product_page = ProductPage(browser)

    assert product_page.getProductTitle().text == title

    print('Check product title')

@when('press add product button')
def press_add_product(browser):
    product_page = ProductPage(browser)
    product_page.getAddProductBtn().click()

    print('The product is added to the cart')

@when('the my cart page is displayed')
def check_my_cart(browser):
    my_cart_page = MyCartPage(browser)

    assert my_cart_page.getTitleMyCart().text == 'Mi carrito'

    print('The section my cart is displayed')

@when('press continue button')
def press_button_continue(browser):
    my_cart_page = MyCartPage(browser)
    my_cart_page.getContinueBtn().click()

    print('Press continue button')

@when('the personal information page is displayed')
def check_personal_info(browser):
    personal_info_page = InfoPersonalPage(browser)
    assert personal_info_page.getTitleInfoPersonal().text == 'Datos Personales'

    print('The section personal information is displayed')

@when(parsers.parse('complete mail "{mail}"'))
def complete_mail(browser, mail):
    personal_info_page = InfoPersonalPage(browser)
    personal_info_page.getMailInput().send_keys(mail)

    print('Complete mail in the input')

@when('accept terms and conditions')
def terms_and_conditions(browser):
    personal_info_page = InfoPersonalPage(browser)
    personal_info_page.getTermAndCondCheck().click()

    print('terms and conditions are accepted')

@when('press continue button payments')
def press_continue_payments(browser):
    personal_info_page = InfoPersonalPage(browser)
    personal_info_page.getContinueBtn().click()

    print('advance to payment screen')

@when('the payments page is displayed')
def check_payments(browser):
    payment_page = PaymentPage(browser)
    assert payment_page.getTitlePayment().text == 'Pago'

    print('The section Payments is displayed')

@when('select payment method and amount of installments')
def select_quota(browser):
    payment_page = PaymentPage(browser)
    payment_page.getQuotaLabel().click()
    payment_page.getAmountQuota1().click()

    print('you choose the payment method and the amount of installments')

@when('press continue button purchase summary')
def press_continue_summary(browser):
    payment_page = PaymentPage(browser)
    payment_page.getContinueBtn().click()

    print('advance to summary screen')

@when('the purchase summary page is displayed')
def check_summary(browser):
    summary_page = SummaryPage(browser)
    assert summary_page.getTitleSummary().text == 'Resumen de Compra'

    print('The section summary is displayed')

@when('press continue confirm')
def confirm_purchase(browser):
    summary_page = SummaryPage(browser)
    summary_page.getConfirmBtn().click()

    print('advance to next confirmation screen')

@then('the confirm page is displayed')
def check_confirm(browser):
    confirm_page = ConfirmPage(browser)

    assert confirm_page.getTitleConfirm().text == 'Tu pedido se está procesando. En unos minutos recibirás un correo confirmando si tu operación fué exitosa.'

    print('Purchase is confirmed')
