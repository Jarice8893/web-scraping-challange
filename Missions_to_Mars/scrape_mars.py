import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from flask import Flask
from selenium import webdriver
  
executable_path = {'executable_path':"C:/Users/jmarshall.000/Desktop/nu-chi-data-pt-04-2021-u-c/web-scraping-challange/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

news_url = 'https://redplanetscience.com/'
browser.visit(news_url)

news_title=soup.find("div",class_='content_title').text

news_p=soup.find("div",class_='article_teaser_body').text
print(f"Title: {news_title}")
print(f"Para: {news_p}")

featured_image_url = 'https://spaceimages-mars.com/image/mars/Icaria%20Fossae7.jpg'
browser.visit(featured_image_url)

html = browser.html
images_soup = BeautifulSoup(html, 'html.parser')

facts_url = 'https://galaxyfacts-mars.com/'

browser.visit(facts_url)

facts_html = browser.html

facts_soup = BeautifulSoup(facts_html, 'html.parser')

usgs_url='https://marshemispheres.com/'
browser.visit(usgs_url)
html=browser.html
soup=BeautifulSoup(html,'html.parser')

all_hemisphere=soup.find("div",class_='collapsible results')
items = soup.find_all('div', class_='item')

urls = []
titles = []
for item in items:
    urls.append(usgs_url + item.find('a')['href'])
    titles.append(item.find('h3').text.strip())


browser.visit(urls[0])
html = browser.html
soup = bs(html, 'html.parser')
allurl = usgs_url+soup.find('img',class_='wide-image')['src']

img_urls = []
for allurl in urls:
    browser.visit(allurl)
    html = browser.html
    soup = bs(html, 'html.parser')
    allurl = usgs_url+soup.find('img',class_='wide-image')['src']
    img_urls.append(allurl)
    

    hemisphere_image_urls = []

for i in range(len(titles)):
    hemisphere_image_urls.append({'title':titles[i],'img_url':img_urls[i]})


    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": str(mars_df),
        "hemisphere_images": hemisphere_image_urls
    }
