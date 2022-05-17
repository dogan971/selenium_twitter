import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = 'C:/Users/es_lo/Desktop/geckodriver.exe'

browser = webdriver.Firefox(executable_path=driver_path)
browser.get("https://twitter.com/")
browser.implicitly_wait(3)
login = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")
login.click()
browser.implicitly_wait(5)
user_input =  browser.find_element(By.NAME,"text")  
user_input.send_keys("mail input") # Mail
next_button = browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span").click()

# For Secure 
# phone_input = browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys("phone or mail")
# browser.implicitly_wait(5)
# next_button2 = browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/span/span").click()

password_input = browser.find_element(By.NAME,"password").send_keys("password") # password
next_button3 = browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span").click()
# Search area
search_area = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input").send_keys("account_name")
time.sleep(5)
clickUser = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[3]/div/div").click()
time.sleep(7)
followTheUser = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/span/span").click()
time.sleep(15)
browser.close()