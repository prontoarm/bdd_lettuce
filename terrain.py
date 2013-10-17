from lettuce import *
from selenium import selenium
from selenium import webdriver
import lettuce_webdriver.webdriver
from random import randint
import sys

@before.all
def before_all():
  world.browser = webdriver.Firefox()
  world.browser.maximize_window()
  #options = webdriver.ChromeOptions()
  #options.add_argument("--start-maximized")
  #world.browser = webdriver.Chrome(chrome_options=options)

@after.all
def after_all(total):
  print "%d of %d scenarios passed" % (
      total.scenarios_ran,
      total.scenarios_passed
    )
  world.browser.quit()
  if total.scenarios_ran != total.scenarios_passed:
    sys.exit(1)

@before.each_scenario
def before_scenario(scenario):
  world.browser.delete_all_cookies()

@after.each_scenario
def after_scenario(scenario):
  if scenario.failed:
    world.browser.save_screenshot('screenshots/' + scenario.feature.name + '___' + scenario.name + '.png')
