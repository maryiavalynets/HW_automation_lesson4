from selenium.webdriver.common.by import By
from behave import given, when, then


HEADER = (By.XPATH, "//h1[@class='fs-heading bolded']")
BLOCK_LINKS = (By.CSS_SELECTOR, ".issue-card-wrapper")
SEARCH_HELP_LIBRARY = (By.XPATH,"//label//h2[@class='fs-heading bolded']")
INPUT_FIELD = (By.ID, 'hubHelpSearchInput')
ALL_HELP_TOPICS = (By.XPATH, "//label//h2[@class='fs-heading bolded']")
BLOCK_RECOMMEND_TOPICS_LINKS = (By.CSS_SELECTOR, ".help-topics li")

@given('Open Customer Service page')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('The header is present')
def verify_header_show(context):
    context.driver.find_element(*HEADER)


@then('Block has {block_link_count} links')
def verify_block_links_count(context,block_link_count):
    block_link_count = int(block_link_count)
    link = context.driver.find_elements(*BLOCK_LINKS)
    assert block_link_count == len(link), f'Expected {block_link_count}, but got {len(link)}'


@then('"Search our help library" is present')
def verify_search_help_library(context):
    context.driver.find_element(*SEARCH_HELP_LIBRARY)


@then('Input field is present')
def verify_input_field(context):
    context.driver.find_element(*INPUT_FIELD)


@then('"All help topics" is present')
def verify_all_help_topics(context):
    context.driver.find_element(*ALL_HELP_TOPICS)


@then('Block of the recommended topicts has {expected_link_count} links')
def verify_recommend_link_count(context,expected_link_count):
    expected_link_count = int(expected_link_count)
    link = context.driver.find_elements(*BLOCK_RECOMMEND_TOPICS_LINKS)
    assert expected_link_count == len(link), f'Error! Expected {expected_link_count}, but got {len(link)}.'