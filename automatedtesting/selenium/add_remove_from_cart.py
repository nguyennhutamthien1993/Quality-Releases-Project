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
    print ('Start add carts')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']")
    print ('Add Sauce Labs Backpack successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bike-light']")
    print ('Add Sauce Labs Bike Light successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']")
    print ('Add Sauce Labs Bolt T-Shirt successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-fleece-jacket']")
    print ('Add Sauce Labs Fleece Jacket successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']")
    print ('Add Sauce Labs Onesie successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    print ('Add Test.allTheThings() T-Shirt (Red) successfully')
    
    print ('Add carts successfully.')
    time.sleep(2)

def removeCarts():
    print ('Start remove carts')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-backpack']")
    print ('Remove Sauce Labs Backpack successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-bike-light']")
    print ('Remove Sauce Labs Bike Light successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-bolt-t-shirt']")
    print ('Remove Sauce Labs Bolt T-Shirt successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-fleece-jacket']")
    print ('Remove Sauce Labs Fleece Jacket successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-onesie']")
    print ('Remove Sauce Labs Onesie successfully')
    webDriver.find_element(By.CSS_SELECTOR, "button[id='remove-test.allthethings()-t-shirt-(red)']")
    print ('Remove Test.allTheThings() T-Shirt (Red) successfully')

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

