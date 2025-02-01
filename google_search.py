from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the browser
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed

# Open Google
driver.get("https://www.google.com")
time.sleep(2)  # Wait for the page to load

# Find the search box and enter a query
search_box = driver.find_element("name", "q")
for char in "Best insurance software":
    search_box.send_keys(char)
    time.sleep(0.1)  # Adjust the delay as needed
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for results to load

# Extract search result titles
results = driver.find_elements("css selector", "h3")

print("\nTop Google Search Results:")
for i, result in enumerate(results[:5]):  # Print top 5 results
    print(f"{i+1}. {result.text}")

# Close the browser
driver.quit()
