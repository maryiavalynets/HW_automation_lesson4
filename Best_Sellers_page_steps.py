from selenium.webdriver.common.by import By
from behave import given, when, then


BESTSELLERS_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')


@then('The BestSellers page has {expected_link_count} links')
def verify_link_count(context,expected_link_count):
    expected_link_count = int(expected_link_count)
    link = context.driver.find_elements(*BESTSELLERS_LINKS)

    assert len(link) == expected_link_count, f'Expected {expected_link_count} links, but got {len(link)}'

