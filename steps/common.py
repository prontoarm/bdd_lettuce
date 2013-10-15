import time

from lettuce import step
from lettuce import world

from lettuce_webdriver.util import assert_true
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from lettuce_webdriver.util import find_button
from lettuce_webdriver.util import find_field
from lettuce_webdriver.util import find_option

from selenium.webdriver.support.ui import WebDriverWait

def wait_for_elem(browser, xpath, timeout=15):
    start = time.time()
    elems = []
    while time.time() - start < timeout:
        elems = browser.find_elements_by_xpath(xpath)
        if elems:
            return elems
        time.sleep(0.2)
    return elems

def wait_for_content(step, browser, content, timeout=15):
    start = time.time()
    while time.time() - start < timeout:
        if content in world.browser.page_source:
            return
        time.sleep(0.2)
    assert_true(step, content in world.browser.page_source)

## URLS
@step('I visit "(.*?)"$')
def visit(step, url):
    with AssertContextManager(step):
        world.browser.get(url)

@step('I go to "(.*?)"$')
def goto(step, url):
    with AssertContextManager(step):
        world.browser.get(url)

## Links
@step('I click "(.*?)"$')
def click(step, name):
    with AssertContextManager(step):
        w = WebDriverWait(world.browser, 10)
        w.until(lambda driver: driver.find_element_by_partial_link_text(name).is_displayed())
        elem = world.browser.find_element_by_partial_link_text(name)
        elem.click()

@step('I should see a link with the url "(.*?)"$')
def should_see_link(step, link_url):
    assert_true(step, world.browser.
            find_element_by_xpath('//a[@href="%s"]' % link_url))

@step('I should see a link to "(.*?)" with the url "(.*?)"$')
def should_see_link_text(step, link_text, link_url):
    assert_true(step, world.browser.find_element_by_xpath('//a[@href="%s"][./text()="%s"]' %
        (link_url, link_text)))

@step('I should see a link that contains the text "(.*?)" and the url "(.*?)"$')
def should_include_link_text(step, link_text, link_url):
    return world.browser.find_element_by_xpath('//a[@href="%s"][contains(., %s)]' %
        (link_url, link_text))

## General
@step('The element with id of "(.*?)" contains "(.*?)"$')
def element_contains(step, element_id, value):
    return world.browser.find_element_by_xpath('//*[@id="%s"][contains(., "%s")]' %
        (element_id, value))

@step('The element with id of "(.*?)" does not contain "(.*?)"$')
def element_not_contains(step, element_id, value):
    elem = world.browser.find_element_by_xpath('//*[@id="%s"]' % element_id)
    assert_true(step, value not in elem.text)

@step('I should see an element with id of "(.*?)" within (\d+) seconds?$')
def should_see_id_in_seconds(step, element_id, timeout):
    elem = wait_for_elem(world.browser, '//*[@id="%s"]' % element_id, int(timeout))
    assert_true(step, elem)
    elem = elem[0]
    assert_true(step, elem.is_displayed())

@step('I should see an element with id of "(.*?)"$')
def should_see_id(step, element_id):
    elem = world.browser.find_element_by_xpath('//*[@id="%s"]' % element_id)
    assert_true(step, elem.is_displayed())

@step('I should not see an element with id of "(.*?)"$')
def should_not_see_id(step, element_id):
    elem = world.browser.find_element_by_xpath('//*[@id="%s"]' % element_id)
    assert_true(step, not elem.is_displayed())

@step('I should see "([^"]+)" within (\d+) seconds?$')
def should_see_in_seconds(step, text, timeout):
    wait_for_content(step, world.browser, text, int(timeout))

@step('I should see "([^"]+)"$')
def should_see(step, text):
    assert_true(step, text in world.browser.page_source)

@step('I see "([^"]+)"$')
def see(step, text):
    assert_true(step, text in world.browser.page_source)

@step('I should not see "([^"]+)"$')
def should_not_see(step, text):
    assert_true(step, text not in world.browser.page_source)

@step('I should be at "(.*?)"$')
def url_should_be(step, url):
    assert_true(step, url == world.browser.current_url)
