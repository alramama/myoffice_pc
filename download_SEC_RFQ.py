from datetime import date

from tkinter import *

from selenium.webdriver.common.alert import Alert

today = date.today()
root = Tk()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pdfplumber
import pandas as pd

Path = 'C:/Program Files (x86)/webdriver/chromedriver'
#driver = webdriver.Chrome(executable_path=Path)
import time
Path = 'C:/Program Files (x86)/webdriver/chromedriver'
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pdfplumber
import pandas as pd
#Path = 'C:\Program Files (x86)\chromedriver\chromedriver.exe'
chroomOption = Options()
chroomOption.add_experimental_option('prefs', { "download.default_ directory": "C:/Users/alramama/PycharmProjects/pythonProject/Webdriver/SEC_Portal", "download.prompt_for_download": False, "plugins.always_open_pdf_externally": True})
driver = webdriver.Chrome(Path,chrome_options=chroomOption)

driver.get("https://www.se.com.sa/e-Bid/account/Login")
time.sleep(2.5)
driver.find_element(By.CSS_SELECTOR,"#txtVendorId").send_keys("2001425")
driver.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("Naizak@2030")
lbl = Label(root, text = "Insert Number of bid").pack()
Ent = Entry(root)
Ent.pack()
def download():
    for i in range(1,int(Ent.get())):
        #driver.find_element(By.XPATH,'//tbody/tr['+str(i)+']/td[9]/div[1]/button[2]/span[1]').click()
        driver.find_element(By.XPATH,'//tbody/tr['+str(i)+']/td[9]/div[1]/button[4]/span[1]').click()
        time.sleep(8)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(8)
        driver.close()
        window_before = driver.window_handles[0]
        driver.switch_to.window(window_before)
        time.sleep(15)
btn = Button(root,text ="download",command=download)
btn.pack()


def decline():
    for i in range(1,100):
        if driver.find_element("//tbody/tr[+'str(i)'+]/td[5]/a[1]").text == today and driver.find_element("//tbody/tr[+'str(i)'+]/td[5]/a[1]").text == "Printed":
            driver.find_element('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[3]/div[1]/table[1]/tbody[1]/tr['+str(i)+']/td[1]/button[1]').click()
            time.sleep(7.5)
            alert = Alert(driver)
            alert.accept()
            time.sleep(10)
            driver.find_element("//a[@id='btnRetrieveBidLowHold']").click()
            time.sleep(7.5)
            driver.find_element("//a[@id='btnDeclineBidLow']").click()
            alert.accept()
            driver.find_element("//a[@id='btnBackToBidList']").click()
            time.sleep(7.5)
            
            
btn = Button(root,text ="decline",command=decline)
btn.pack()

root.mainloop()

