from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re

driver = webdriver.Chrome()
driver.get("https://rooms.library.gsu.edu/spaces?lid=5862&gid=24804&c=0")

title = driver.find_element(By.CLASS_NAME, 'banner-title')

print(title.text)

date_picker = driver.find_element(By.CLASS_NAME, 'fc-goToDate-button').click()

date_current = driver.find_element(By.CLASS_NAME, 'datepicker-switch').click()

month_picker = driver.find_element(By.XPATH, '//span[@class="month" and text()="Nov"]').click()

date_today = driver.find_element(By.XPATH, '//table[@class="table-condensed"]/tbody/tr/td[@class="day" and text()="1"]')

print(date_today.get_attribute('data-date'))

date_today.click()

all_rooms = driver.find_elements(By.XPATH, '//span[@class="fc-cell-text"]')

classs =  "fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail"

date = "Wednesday, November 3"
room = "N512"
title = "Available"
start_time = 8
end_time = 5
all_avail = []

f = open('export/availables.txt', 'w')
while (start_time <= end_time+12):
    if start_time < 12:
        start_time_com = f"{start_time}:00am"
        start_time_com_30 = f"{start_time}:30am"
    elif start_time == 12:
        start_time_com = f"12:00pm"
        start_time_com_30 = f"12:30pm"
    else: 
        start_time_com = f"{start_time-12}:00pm"
        start_time_com_30 = f"{start_time-12}:30pm"

    try:
        found = driver.find_element(By.XPATH, f'//a[contains(@title, "{start_time_com}") and contains(@title, "{date}") and contains(@title, "{room}") and contains(@title, "{title}")]')
        all_avail.append(found)
        f.write(f"{found.get_attribute('title')}\n")
        print(found.get_attribute('title'))
    except:
        f.write(f"[{start_time_com} not available]\n")

    try:
        found = driver.find_element(By.XPATH, f'//a[contains(@title, "{start_time_com_30}") and contains(@title, "{date}") and contains(@title, "{room}") and contains(@title, "{title}")]')
        all_avail.append(found)
        f.write(f"{found.get_attribute('title')}\n")
        print(found.get_attribute('title'))
        
    except:
        f.write(f"[{start_time_com_30} not available]\n")
    start_time += 1


driver.quit()