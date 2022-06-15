import time
from selenium import webdriver
driver= webdriver.Chrome()
driver.get("http://sideeffects.embl.de/")
driver.find_element_by_id("searchBox").send_keys("Vomiting")
time.sleep(2)
w=driver.find_element_by_css_selector("#searchDrugList")
f=w.find_elements_by_tag_name("a")
for i in range(len(f)):
    f[i].click()
    result=[]
    table=driver.find_element_by_css_selector("body > div:nth-child(4) > div:nth-child(3)")
    y=table.find_elements_by_tag_name("a")
    for x in range(len(y)):
        print(y[x].text)
        time.sleep(2)
driver.close()





