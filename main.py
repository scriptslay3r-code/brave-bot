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

'''for result in driver.find_elements(By.CSS_SELECTOR,'.result--ad'):
    title = result.find_element(By.CSS_SELECTOR,'.results--ads .result__title .result__a').text
    link = result.find_element(By.CSS_SELECTOR,'.results--ads .result__title .result__a').get_attribute('href')
    source = result.find_element(By.CSS_SELECTOR,'.results--ads .result__extras__url').text
    snippet = result.find_element(By.CSS_SELECTOR,'.results--ads .result__snippet').text
    print(f'{title}\n{link}\n{snippet}\n{source}\n')
search_results = driver.find_elements(By.XPATH,"//div[@id='links']/div/div/h2/a[@class='result__a']")
print(len(search_results))
for result in search_results:
  print(result.text)
    
urls = []
for result in search_results:
  urls.append(result.get_attribute("href"))
for link in urls:
  print(link)
  '''
  
results=driver.find_elements_by_xpath("//div[@id='links']/div/div/div[2]")
links = driver.find_elements(By.ID,'links')
description=[]

for result in results:
    description.append(result.text)
    print(result)
    print description
    
for link in links:
  print("These are the links": )
  print(link)