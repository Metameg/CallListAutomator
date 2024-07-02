from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

QUERY = "houston hair salons"

def searchplace(query):
    Place = driver.find_element(By.CLASS_NAME, "searchboxinput")
    Place.send_keys(query)
    Submit = driver.find_element(
        By.ID, "searchbox-searchbutton")
    Submit.click()

def scrollToBottom(xpath):
    # Locate the scrollable element by its XPath
    scrollable = driver.find_element(By.XPATH, xpath)
    
    # Get the initial scroll height of the element
    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable)
    
    while True:
        # Scroll down to the bottom of the scrollable element
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable)
        
        # Wait to load page / use a better technique like `waitForPageLoad` etc., if possible
        sleep(2)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable)
        if new_height == last_height:
            break
        last_height = new_height

def getPlace(i):
    try:
        parent = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
        child_element = parent.find_element(By.XPATH, f".//div[{i}]/div/a")
    # child_elements = parent.find_elements(By.XPATH, ".//div[position() >= 3 and (position() - 1) mod 2 = 0]/div/a")
    except Exception as e:
        return None
    
    return child_element

def getPlaceDetails():
    name = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/h1').text
    reviews_avg = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]').text
    reviews_total = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[2]/span/span').text
    
    try:
        addr_parent = driver.find_element(By.XPATH, "//*[contains(@aria-label, 'Address:')]")
        addr = addr_parent.find_element(By.XPATH, ".//div/div[contains(@class, 'rogA2c')]/div").text
    except Exception as e:
        addr = "none found"

    try:
        website_parent = driver.find_element(By.XPATH, "//*[contains(@aria-label, 'Website:')]")
        website = website_parent.find_element(By.XPATH, ".//div/div[contains(@class, 'rogA2c')]/div").text
    except Exception as e:
        website = "none found"

    try:
        phone_parent = driver.find_element(By.XPATH, "//*[contains(@aria-label, 'Phone:')]")
        phone = phone_parent.find_element(By.XPATH, ".//div/div[contains(@class, 'rogA2c')]/div").text
    except Exception as e:
        phone = "none found"

    # back = driver.find_element(By.XPATH, '//*[@id="omnibox-singlebox"]/div/div[1]/button')
    # back.click()
    sleep(2)
    
    return [name, reviews_avg, reviews_total, addr, website, phone]
# Open Google Maps
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
sleep(2)

# Search
searchplace(QUERY)
sleep(2)
scrollToBottom('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
sleep(2)

i = 3
# for element in places:
while getPlace(i):
    element = getPlace(i)
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        sleep(2)
        details = getPlaceDetails()
    except Exception as e:
        details = ['ERROR','ERROR','ERROR','ERROR', 'ERROR']

    sleep(2)
    print(details)
    i += 2

driver.quit()