
from tkinter import *
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Login_Site:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.url = website_entry.get()
        self.bot = webdriver.Firefox(executable_path="./Driver/geckodriver")
        self.bot.set_window_size(1000, 800)

    def login(self):
        bot = self.bot
        bot.get(self.url)
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
        time.sleep(3)
        while True:
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
def main():
    user = email_entry.get()
    password = password_entry.get()
    Login = Login_Site(user, password)
    Login.login()



window = Tk()
window.title("Login App")
window.config(padx=50, pady=50)

# Login Label
login_label = Label(text="Login App", font=("Arial", 25, "bold"), pady=10)
login_label.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.focus()
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_entry.focus()


# Buttons
add_button = Button(text="Add", width=36, command=main)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()