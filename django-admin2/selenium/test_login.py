from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("www.youtube.com")
# print "driver.title",driver.title
# assert "Python" in driver.title
elem = driver.find_element_by_id("q")

elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close() # close browser


#user admin pass admin123
