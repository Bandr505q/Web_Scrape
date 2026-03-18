from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
driver = webdriver.Chrome()

#driver.maximize_window()

driver.get('https://www.google.com/')

#driver.find_element(By.LINK_TEXT,'صور').click()
google_search = driver.find_element(By.CLASS_NAME,'gLFyf')
google_search.send_keys('BMW')
google_search.send_keys(Keys.ENTER)

time.sleep(15)
driver.find_element(By.PARTIAL_LINK_TEXT,'صور').click()


time.sleep(10)
for _ in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
    


imgs = driver.find_elements(By.CSS_SELECTOR,'img')

img_ls = []
s = set()

for img in imgs: 
    src = img.get_attribute('src') or ""
    if src.startswith('http') and src not in s:
        s.add(src)
        img_ls.append(src)
        
df = pd.DataFrame({'query':'BMW','image url':img_ls})
df.to_csv('images_google.csv',index=False)
driver.title
print("DONE!")   
driver.quit()  


