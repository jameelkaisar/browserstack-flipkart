# Import the required libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys


# Create a new instance of the Chrome driver
options = ChromeOptions()
options.set_capability("sessionName", "Flipkart Test")
driver = webdriver.Chrome(options=options)


# Navigate to the URL
driver.get("https://www.flipkart.com/")


# Print the title of the page
print(driver.title)

# Search for Samsung Galaxy S10
# Click on the search bar
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input"))).click()

# Enter the search query
active_ele = driver.switch_to.active_element
active_ele.send_keys("Samsung Galaxy S10")

# Press Enter
active_ele.send_keys(Keys.ENTER)


# Filter the search results
# Select "Mobiles" category
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/div/section/div[3]/div/a"))).click()

# Select "Samsung" brand
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div/div/div/label"))).click()

# Select "Flipkart assured" filter
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/section[4]/label"))).click()

# Sort by "Price -- High to Low"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[4]"))).click()


# Get the search results
# Find all the elements containing the search results
elements = driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div")


# Iterate over the elements
for i, element in enumerate(elements):
    # Filter header elements
    if "cPHDOP" not in element.get_attribute("class"):
        continue

    # Filter footer elements
    if "75nlfW" not in element.find_element(By.XPATH, "div").get_attribute("class"):
        continue

    # Print the item number
    print(f"Item {i}:")

    # Print the name of the product
    print("-> Name:", element.find_element(By.XPATH, "div/div/div/a/div[2]/div[1]/div[1]").text)

    # Print the price of the product
    try:
        # Price format 1
        print("-> Price:", element.find_element(By.XPATH, "div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]").text)
    except NoSuchElementException:
        try:
            # Price format 2
            print("-> Price:", element.find_element(By.XPATH, "div/div/div/a/div[2]/div[2]/div[1]/div/div").text)
        except NoSuchElementException:
            try:
                # Price format 3
                print("-> Price:", element.find_element(By.XPATH, "div/div/div/a/div[2]/div[2]/div[1]/div[1]/div").text)
            except NoSuchElementException:
                print("-> Price:", "NA")

    # Print the link of the product
    print("-> Link:", element.find_element(By.XPATH, "div/div/div/a").get_attribute("href"))

    # Add a newline
    print()


# Stop the driver
driver.close()
