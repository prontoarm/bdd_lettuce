import time

from lettuce import step
from lettuce import world

from lettuce_webdriver.util import assert_true

@step('I should see content on base theme')
def html_structure_on_base_theme(step):
    driver = world.browser
    assert_true(step, driver.find_element_by_xpath("//meta[@charset='UTF-8']"))
    assert_true(step, driver.find_element_by_xpath("//meta[@name='viewport' and @content='width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes']"))
    assert_true(step, driver.find_element_by_xpath("//link[contains(@href, 'font-awesome.min.css')]"))
    assert_true(step, driver.find_element_by_xpath("//link[contains(@href, 'main.css')]"))
    assert_true(step, driver.find_element_by_xpath("//link[contains(@href, 'style.css')]"))
    assert_true(step, driver.find_element_by_xpath("//link[contains(@href, 'color-palette=css')]"))
    assert_true(step, driver.find_element_by_xpath("//html/body"))
    assert_true(step, driver.find_element_by_xpath("//body/script[contains(@src, 'bootstrap.min.js')]"))
    assert_true(step, driver.find_element_by_xpath("//body/script[contains(@src, 'main.js')]"))
    assert_true(step, driver.find_element_by_xpath("//html/body/div/div/div[@class='page-wrap']"))
    assert_true(step, driver.find_element_by_xpath("//header[@id='header']"))
    assert_true(step, driver.find_element_by_xpath("//footer"))
