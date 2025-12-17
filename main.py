from operator import index
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj=Service(r"C:\Users\arpan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(7)
driver.maximize_window()

booksname=[]
authotrname=[]
lengths=[]
dates=[]
ratings=[]
prices=[]
for page in range(1, 6):
    time.sleep(4)  
    driver.get(f'https://www.audible.in/charts/best?ref=a_search_t1_navTop_pl1cg0c1r0&page={page}&ref_pageloadid=O8Y4LWiYIa4Y9iEh&pf_rd_p=c7f10514-cfaf-4c77-9a3d-8fde61845b57&pf_rd_r=2MN48YFY08A9826KA374&plink=hpoStYiJLN598Nqu&pageLoadId=h284SsI1ejtapIU9&creativeId=6f63dfd1-2356-4eeb-975a-7b154c653c1f')
    #books name
    books = driver.find_elements(By.XPATH, "//li[@class='bc-list-item']/h3")
    for b in books:
        booksname.append(b.text)       
    #AUTHOR NAME
    writers=driver.find_elements(By.XPATH,"//li[contains(@class,'authorLabel')]")
    for writer in writers:
        authotrname.append(writer.text)
        
    #Audio length
    audiolengths=driver.find_elements(By.XPATH,"//li[contains(@class,'runtimeLabel')]")
    for audiolength in audiolengths:
        lengths.append(audiolength.text)
        
    #Release Date
    releaseDates=driver.find_elements(By.XPATH,"//li[contains(@class,'releaseDateLabel')]")
    for releaseDate in releaseDates:
        dates.append(releaseDate.text)
    #Ratings   
    bookratings=driver.find_elements(By.XPATH,"//li[contains(@class,'ratingsLabel')]")
    for bookrating in bookratings:
        clean_text = bookrating.text.replace("\n", " -- ")
        ratings.append(clean_text)
    #Prices
    bookprices=driver.find_elements(By.XPATH,"//p[contains(@class,'buybox-regular-price')]/span[1]")
    for bookprice in bookprices:
        prices.append(bookprice.text)
df=pd.DataFrame({"Audiobook Names":booksname,
                 "Author Names":authotrname,
                 "Audio Lengths":lengths,
                 "Release Dates":dates,
                 "Ratings":ratings,
                 "Prices":prices})
df.to_excel("AudiobooksData.xlsx",index=False)
