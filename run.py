from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rooms.library.gsu.edu/spaces?lid=5862&gid=24804&c=0")

title = driver.find_element(By.CLASS_NAME, 'banner-title')

print(title.text)

driver.find_element(By.CLASS_NAME, 'fc-goToDate-button').click()
driver.find_element(By.CLASS_NAME, 'datepicker-switch').click()
driver.find_element(By.XPATH, '//span[@class="month" and text()="Nov"]').click()
driver.find_element(By.XPATH, '//table[@class="table-condensed"]/tbody/tr/td[@class="day" and text()="16"]').click()

classs =  "fc-timeline-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future s-lc-eq-avail"

date = "Tuesday, November 16"
room = "N518"
title = "Available"
start_time = 12
end_time = 5
all_avail = []
inter_check = ((end_time+12)-start_time)*2
check = 0

f = open('/Users/thuanvo/Desktop/myproject/roomr/export/availables.txt', 'w')

while (start_time < end_time+12):
    
    if start_time < 12:
        start_time_form = f"{start_time}:00am"
        start_time_half_form = f"{start_time}:30am"
    elif start_time == 12:
        start_time_form = f"12:00pm"
        start_time_half_form = f"12:30pm"
    else: 
        start_time_form = f"{start_time-12}:00pm"
        start_time_half_form = f"{start_time-12}:30pm"

    try:
        available_time = driver.find_element(By.XPATH, f'//a[contains(@title, "{start_time_form}") and contains(@title, "{date}") and contains(@title, "{room}") and contains(@title, "{title}")]')
        f.write(f"{available_time.get_attribute('title')} - {available_time}\n")
        check+=1
    except:
        f.write(f"[{start_time_form} not available]\n")

    try:
        available_half_time = driver.find_element(By.XPATH, f'//a[contains(@title, "{start_time_half_form}") and contains(@title, "{date}") and contains(@title, "{room}") and contains(@title, "{title}")]')
        f.write(f"{available_half_time.get_attribute('title')} - {available_half_time}\n")
        check+=1
    except:
        f.write(f"[{start_time_half_form} not available]\n")

    start_time += 1

print(inter_check, check-2)
f.close()
WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, f'//a[contains(@title, "{date}") and contains(@title, "{room}") and contains(@title, "{title}")]')))
#wait
driver.quit()