#from webdriver_manager.chrome import ChromeDriverManager
import datetime
from datetime import date
from tkinter import *
today = date.today()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pdfplumber
import pandas as pd
Path = 'C:/Program Files (x86)/webdriver/chromedriver'
driver = webdriver.Chrome(executable_path=Path)
driver.get("https://tenders.etimad.sa/Tender/AllTendersForVisitor")
driver.maximize_window()

tender_list1 = []
root =Tk()
lbl = Label(root, text = "Print").pack
def etmad_bid_information3():
    bid = driver.find_elements(By.XPATH, '//*[@id="cardsresult"]/div[1]/div/div')
    for i in bid:
        #time.sleep(10)
        a = (i.text).splitlines()
        a1 = (a[0].split())
        a2 = a1[2].replace(":", "")
        a5 = a[5].replace('النشاط الأساسي', '')
        a7 = a[7].replace('الرقم المرجعي', '')
        a8 = a[8].replace('اخر موعد لإستلام الاستفسارات', '')
        a9 = a[9].replace('آخر موعد لتقديم العروض', '')
        if len(a) == 13:
            bid = a2, a[1], a[2],a[3], a5, a[6], a7, a8, a9,a[12]
            tender_list1.append(bid)
        #print(tender_list)
        bid_list = pd.DataFrame(tender_list1)
        bid_list.to_excel(str(today)+'information_technology_tender_list3.xlsx')

btn = Button(root, text = "Print", command = etmad_bid_information3)
btn.pack()
root.mainloop()

