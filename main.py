import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from art import *

#new webdriver.ChromeOptions().setBinary("/usr/bin/brave-browser")
sleep = time.sleep(2)
options = Options()
options.binary_location = "/usr/bin/brave-browser"
  
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
url =("https://Duckduckgo.com/")

def intro():  
  welcome = text2art("Welcome")
  going = text2art("Going")
  headless = text2art("Headless!")
  opening = text2art("Opening")
  browser = text2art("Browser!")
  print(welcome)
  time.sleep(.5)
  print(opening)
  time.sleep(.5)
  print(browser)
  time.sleep(1.5)

intro()
driver.get(url)
buttonSearch = driver.find_element(By.ID,"search_button_homepage")
searchBox = driver.find_element(By.ID,"search_form_input_homepage")
driver.execute_script("return arguments[0].scrollIntoView();", searchBox)
time.sleep(1)
searchBox.click()
sleep
searchBox.send_keys("crypto")
sleep
buttonSearch.click()

'''def getLinks():
  search_results = driver.find_elements(By.XPATH,"//div[@id='links']/div/div/h2/a[@class='result__a']")
  print(len(search_results))
  for result in search_results:
    print(result.text)
    
  urls = []
  for result in search_results:
    urls.append(result.get_attribute("href"))
  for link in urls:
    print(link)
    
getLinks()'''

search_results = driver.find_elements(By.XPATH,"//div[@id='links']/div/div/h2/a[@class='result__a']")
print(len(search_results))
for result in search_results:
  print(result.text)
    
urls = []
for result in search_results:
  urls.append(result.get_attribute("href"))
for link in urls:
  print(link)