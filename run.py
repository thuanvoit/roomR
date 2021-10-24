from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rooms.library.gsu.edu/spaces?lid=5862&gid=24804&c=0")

title = driver.find_element(By.CLASS_NAME, 'banner-title')

print(title.text)

date_picker = driver.find_element(By.CLASS_NAME, 'fc-goToDate-button').click()

date_current = driver.find_element(By.CLASS_NAME, 'datepicker-switch').click()

month_picker = driver.find_element(By.XPATH, '//span[@class="month" and text()="Nov"]').click()

date_today = driver.find_element(By.XPATH, '//table[@class="table-condensed"]/tbody/tr/td[@class="day" and text()="1"]')

print(date_today.get_attribute('data-date'))

driver.quit()