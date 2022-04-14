answer = input("Headless? [Y] for Yes: ")

if answer == 'y':
  options = Options()
#  new options().setBinary("/usr/bin/brave-browser")

  options.binary_location = "/usr/bin/brave-browser"
  options.add_argument('--headless')
  
  options.add_argument('--disable-gpu')

  print(welcome)

  time.sleep(.5)

  print(going)

  time.sleep(.5)

  print(headless)

  time.sleep(.5)
  driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)