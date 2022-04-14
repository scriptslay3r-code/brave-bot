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

options = Options()
options.binary_location = "/usr/bin/brave-browser"
  
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
url =("https://Duckduckgo.com/")
  
def Browse():  
  
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



