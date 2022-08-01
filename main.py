import os
import sys
import time

# Selenium Specific imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.bot = webdriver.Firefox(executable_path="./Driver/geckodriver")
        #self.bot.set_window_position(0,0)
        self.bot.set_window_size(1000, 800)

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        # Wait for 3 seconds
        time.sleep(3)

        # Input User Name
        user_box = bot.find_element_by_name("username")
        user_box.send_keys(self.user)

        # Input Password Name
        pass_box = bot.find_element_by_name("password")
        pass_box.send_keys(self.password)

        # # Login
        login_btn = bot.find_element_by_class_name("L3NKy") # sqdOP  L3NKy   y3zKF
        login_btn.click()  

        # # Save
        # save_btn = bot.find_elements_by_class_name("f5C5x") # sqdOP  L3NKy   y3zKF 
        # save_btn.click()     

        # # Enter Click
        # pass_box.send_keys(keys.RETURN)

        time.sleep(3)
        # like_btn = bot.find_elements_by_class_name("wpO6b")
        # for btn in like_btn:
        #     btn.click()

        while True:
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)




def main():
    user = "biplobdash014"
    password = "biplob420"

    insta = Instagram(user, password)
    insta.login()

if __name__ == "__main__":
    main()