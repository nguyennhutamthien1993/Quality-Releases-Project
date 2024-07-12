# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time 

def initDriver():
    print ('Starting the browser...')
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    webDriver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    webDriver.get('https://www.saucedemo.com/')

    return webDriver

# Start the browser and login with standard_user
def login (user, password):
    webDriver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    webDriver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    webDriver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()
    print ('Login successfully.')
    time.sleep(2)

def addCarts():
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bike-light']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-fleece-jacket']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    
    print ('Add carts successfully.')
    time.sleep(2)

def removeCarts():
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-backpack']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-bike-light']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-bolt-t-shirt']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-fleece-jacket']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-onesie']")
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-test.allthethings()-t-shirt-(red)']")

    print ('Remove carts successfully.')
    time.sleep(2)

def assertAddCarts():
    print ('Start assert')
    webDriver.find_element(By.CSS_SELECTOR, "div[id='shopping_cart_container'] > a > span.shopping_cart_badge")
    print ('Get element')
    addedCartsNumber = webDriver.find_element(By.CSS_SELECTOR, "div[id='shopping_cart_container'] > a > span.shopping_cart_badge").text
    print(addedCartsNumber)
    print ('Assert add carts successfully.')
    time.sleep(2)

def assertRemoveCarts():
    print ('Assert add carts successfully.')

webDriver = initDriver()
login('standard_user', 'secret_sauce')
addCarts()
assertAddCarts()

