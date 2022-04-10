import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from art import *

#new webdriver.ChromeOptions().setBinary("/usr/bin/brave-browser")

welcome = text2art("Welcome")

going = text2art("Going")

headless = text2art("Headless!")

opening = text2art("Opening")

browser = text2art("Browser!")


url =("https://Duckduckgo.com/")

#emailList = open(emailList.txt, 'r')

answer = input("Headless? [Y] for Yes: ")

if answer == 'y':
  options = Options()
#  new options().setBinary("/usr/bin/brave-browser")

#  options.binary_location = "/usr/bin/brave-browser"
  options.add_argument('--headless')
  
  options.add_argument('--disable-gpu')

  print(welcome)

  time.sleep(.5)

  print(going)

  time.sleep(.5)

  print(headless)

  time.sleep(.5)
  driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
  i = 0
  times_scrolled = 0
  while i < 10:
        driver.get(url); time.sleep(1)
        while times_scrolled < 15:
        		label.send_keys(keys.PAGE_DOWN)
        		time.sleep(2)
        		i = i + 1
        		print("The value of your variable is: " + str(i))
        		times_scrolled = times_scrolled + 1
        		print("We have scrolled " + str(times_scrolled) + "times")
        driver.quit()


else:
  options = Options()
#  options.binary_location = "/usr/bin/brave-browser"
  
  driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
  print(welcome)

  time.sleep(.5)

  print(opening)

  time.sleep(.5)

  print(browser)

  time.sleep(.5)
  i = 0
  times_scrolled = 0
  while i < 10:
        	driver.get(url); time.sleep(1) #Delay a second  let page load make seem more human maybe
        	while times_scrolled < 15:
        		label.send_keys(keys.PAGE_DOWN)
        		time.sleep(2)
        		i = i + 1
        		times_scrolled = times_scrolled + 1
        		print("The value of your variable is: " + str(i))
        		print("We have scrolled " + str(times_scrolled) + "times")
        		
        	driver.quit()



