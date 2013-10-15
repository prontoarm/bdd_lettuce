import time

from lettuce import step
from lettuce import world

from lettuce_webdriver.util import assert_true
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from lettuce_webdriver.util import find_button
from lettuce_webdriver.util import find_field
from lettuce_webdriver.util import find_option

## Forms
@step('I should see a form that goes to "(.*?)"$')
def see_form(step, url):
    return world.browser.find_element_by_xpath('//form[@action="%s"]' % url)

@step('I fill in "(.*?)" with "(.*?)"$')
def fill_in_textfield(step, field_name, value):
    with AssertContextManager(step):
        text_field = find_field(world.browser, 'text', field_name) or \
            find_field(world.browser, 'textarea', field_name) or \
            find_field(world.browser, 'password', field_name)
        assert_false(step, text_field is False,'Can not find a field named "%s"' % field_name)
        text_field.clear()
        text_field.send_keys(value)

@step('I press "(.*?)"$')
def press_button(step, value):
    with AssertContextManager(step):
        button = find_button(world.browser, value)
        button.click()

@step('I check "(.*?)"$')
def check_checkbox(step, value):
    with AssertContextManager(step):
        check_box = find_field(world.browser, 'checkbox', value)
        if not check_box.is_selected():
            check_box.click()

@step('I uncheck "(.*?)"$')
def uncheck_checkbox(step, value):
    with AssertContextManager(step):
        check_box = find_field(world.browser, 'checkbox', value)
        if check_box.is_selected():
            check_box.click()

@step('The "(.*?)" checkbox should be checked$')
def assert_checked_checkbox(step, value):
    check_box = find_field(world.browser, 'checkbox', value)
    assert_true(step, check_box.is_selected())


@step('The "(.*?)" checkbox should not be checked$')
def assert_not_checked_checkbox(step, value):
    check_box = find_field(world.browser, 'checkbox', value)
    assert_true(step, not check_box.is_selected())

@step('I select "(.*?)" from "(.*?)"$')
def select_single_item(step, option_name, select_name):
    with AssertContextManager(step):
        option_box = find_option(world.browser, select_name, option_name)
        option_box.click()

@step('I select the following from "(.*?)"$')
def select_multi_items(step, select_name):
    with AssertContextManager(step):
        # Ensure only the options selected are actually selected
        option_names = step.multiline.split('\n')
        select_box = find_field(world.browser, 'select', select_name)
        option_elems = select_box.find_elements_by_xpath('./option')
        for option in option_elems:
            if option.get_attribute('id') in option_names or \
               option.get_attribute('name') in option_names or \
               option.get_attribute('value') in option_names or \
               option.text in option_names:
                option.select()
            else:
                if option.is_selected():
                    option.toggle()

@step('The "(.*?)" option from "(.*?)" should be selected$')
def assert_single_selected(step, option_name, select_name):
    option_box = find_option(world.browser, select_name, option_name)
    assert_true(step, option_box.is_selected())

@step('The following options from "(.*?)" should be selected$')
def assert_multi_selected(step, select_name):
    with AssertContextManager(step):
        # Ensure its not selected unless its one of our options
        option_names = step.multiline.split('\n')
        select_box = find_field(world.browser, 'select', select_name)
        option_elems = select_box.find_elements_by_xpath('./option')
        for option in option_elems:
            if option.get_attribute('id') in option_names or \
               option.get_attribute('name') in option_names or \
               option.get_attribute('value') in option_names or \
               option.text in option_names:
                assert_true(step, option.is_selected())
            else:
                assert_true(step, not option.is_selected())

@step('I choose "(.*?)"$')
def choose_radio(step, value):
    with AssertContextManager(step):
        box = find_field(world.browser, 'radio', value)
        box.select()

@step('The "(.*?)" option should be chosen$')
def assert_radio_selected(step, value):
    box = find_field(world.browser, 'radio', value)
    assert_true(step, box.is_selected())

@step('The "(.*?)" option should not be chosen$')
def assert_radio_not_selected(step, value):
    box = find_field(world.browser, 'radio', value)
    assert_true(step, not box.is_selected())
