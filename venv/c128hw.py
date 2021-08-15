import bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
#print('PAGE: ',page)

soup = BeautifulSoup(page.text,'html.parser')

time.sleep(10)

star_table = soup.find_all('table')
print(len(star_table))

#print('TABLES : ',star_table)

temp_list= []
table_rows = star_table[8].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    print('td: ',td)
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

print('temp list : ',temp_list)

Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][8])
    if temp_list[i][8] == '':
        Radius.append('Not given')
    else:
        Radius.append(temp_list[i][8])

    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarfs.csv')
