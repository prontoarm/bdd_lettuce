import time

from lettuce import step
from lettuce import world

from lettuce_webdriver.util import assert_true

## Browser
@step('The browser\'s URL should be "(.*?)"$')
def browser_url_should_be(step, url):
    assert_true(step, url == world.browser.current_url)

@step ('The browser\'s URL should contain "(.*?)"$')
def url_should_contain(step, url):
    assert_true(step, url in world.browser.current_url)

@step ('The browser\'s URL should not contain "(.*?)"$')
def url_should_not_contain(step, url):
    assert_true(step, url not in world.browser.current_url)
