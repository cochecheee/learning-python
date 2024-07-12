"""
        TARGET:
    1. Jump to this URL: http://orteil.dashnet.org/experiments/cookie/ and click cookie
    2. After five seconds if you have enough money to buy the most expensive in shop, buy it
    3. Play game in 5 minutes and check how much you've just get
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep chrome open when finished 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# open chrome browser
url = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# get object on game
cookie = driver.find_element(by=By.ID, value="cookie")

# get items id to buy
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

# price of items
all_prices = driver.find_elements(by=By.CSS_SELECTOR,value="#store b")
def filter_to_get_price(item):
    return int(item.text.split('-')[1].strip().replace(',',''))
item_prices = [filter_to_get_price(cost) for cost in all_prices if cost.text.strip() != '']

# dict to store items according to its price [price:id_item]
cookie_upgrades = {}
for n in range(len(item_prices)):
    cookie_upgrades[item_prices[n]] = item_ids[n]

# define the time
time_start = time.time()
time_out = time.time() + 5  #time to stop by upgrade item
time_end = time.time() + 60*5

while True:
    cookie.click()

    # check for upgrade
    if time.time() > time_out:
        
        # get current money that possess
        budgets = driver.find_element(by=By.ID, value='money')
        money = int(budgets.text.replace(',',''))

        # find affordable upgrade items
        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cost < money:
                affordable_upgrades[cost] = id

        # the most expensive affordable item
        if affordable_upgrades:
            highest_price_aff = max(affordable_upgrades)
            purchase_id = cookie_upgrades[highest_price_aff]

            driver.find_element(by=By.ID, value=purchase_id).click()

        time_out = time.time()+5

    if time.time() > time_end:
        break
