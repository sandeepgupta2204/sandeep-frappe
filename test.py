from selenium import webdriver

from testseleniumfrappe import login
from testseleniumfrappe2 import dashboard

driver = webdriver.Chrome()

try:
    # Step 1 check for login
    login(driver)
    dashboard(driver)
except Exception as e:
    print("---------->", e)
finally:
    driver.quit()


