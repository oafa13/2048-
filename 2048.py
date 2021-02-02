# https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

# Using Firefox
browser = webdriver.Firefox()
browser.get('https://play2048.co/')


# Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
while True:
    a = browser.find_element_by_tag_name('body')

    def randomazingKeys():
        toBeRandomized = [a.send_keys(Keys.UP), a.send_keys(Keys.DOWN), a.send_keys(Keys.LEFT), a.send_keys(Keys.RIGHT)]
        play = toBeRandomized[random.randint(0,3)]


    randomazingKeys()
