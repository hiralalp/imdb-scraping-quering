from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

sourse=requests.get('https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1').text

soup=BeautifulSoup(sourse,'lxml')

n=int(input("Enter the number of movies you want to extract:"))

raw_html = soup.find("tbody", {"class": "lister-list"}).findAll("tr")[0:n]

movies_list = []
for html in raw_html:
	title = html.find("td", {"class":"titleColumn"}).find("a").get_text()
	star_cast=html.find("td", {"class":"titleColumn"}).find("a").get('title')
	rating = html.find("td", {"class":"ratingColumn imdbRating"}).find("strong").get_text()
	rating = float(rating)
	star_cast=star_cast.split(",")[1]
	raw_list = [title, rating,star_cast]
	movies_list.append(raw_list)
    

for i in movies_list:
	print(i)
	print()

def create_csv(movies):
	with open('movies.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		row = ['Name', 'Rating','star cast']
		writer.writerow(row)
		for x in range(len(movies)):
			row = movies[x]
			writer.writerow(row)
	csvfile.close()


create_csv(movies_list)

import pandas as pd
df = pd.read_csv('movies.csv',engine='python')
df.to_csv('movies2.csv', index=False)
import os
os.remove('movies.csv')


star=input("enter the name of the star:")
m=int(input('enter the number of movies you want:'))

def striping(s):   
    return s.strip()

df2 = pd.read_csv('movies2.csv',engine='python')
df2['star cast']=df2['star cast'].apply(striping)
df1=df2[df2['star cast']==star]
print(df2)
print(df1)
print(df1.iloc[0:m,])
