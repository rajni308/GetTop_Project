from selenium.webdn.by import By
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#driver = webdriver.Chrome(executable_path='/Users/rajni/PycharmProjects/GetTop_Project/chromedriver4')

SEARCH_INPUT = (By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
SEARCH_RESULTS = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
SEARCH_ICON = (By.CSS_SELECTOR, 'a.is-small i.icon-search')



@given('Open home page')
def open_homepage(context):
    context.driver.get('https://gettop.us/')
    #context.app.get_tophomepage.open_homepage()


@when('Mouse hover on search icon')
def search_icon_hover(context):
    #context.app.get_topheader.search_icon_hover()
    actions = ActionChains(context.driver)
    search_icon = context.find_element(*context.SEARCH_ICON)
    actions.move_to_element(search_icon)
    actions.perform()
    sleep(7)

@when('Search for {query}')
def search_gettop(context, query):
     context.driver.find_element(*SEARCH_INPUT).send_keys(query)
    # context.driver.find_element(*SEARCH_BTN).click()
    #context.app.get_topheader.search_gettop(search_word)



@then('Click on search icon')
def click_search_icon(context):
    context.find_element(*context.SEARCH_ICON).click()




@then('Verify search results have {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*context.SEARCH_RESULTS).text
    # print(f'Search results are: {actual_result[14:]}')
    # expected_txt = f'SEARCH RESULTS FOR “{expected_result}”'
    #expected_txt = expected_txt.upper()
    #print(f'Expected results are: {expected_txt}')
    assert actual_result == expected_result, f'Error, actual{actual_result} did not match {expected_result}'



    # @when('Search for {search_word}')
    # def search_gettop(context, search_word):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    # context.app.gettop_header.search_gettop(search_word)




