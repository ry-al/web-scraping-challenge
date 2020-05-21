#!/usr/bin/env python
# coding: utf-8

# Dependencies
# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# import time
# import pandas as pd


def scraper():
    # Initialize browser and open URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(5)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find_all('div', class_="content_title")[1].text
    news_title

    news_p = soup.find_all('div', class_="article_teaser_body")[0].text
    news_p

    browser.quit()


    # ### JPL Mars Space Images - Featured Image
    # https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    # Initialize browser and open URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(5)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)

    html = browser.html
    soup = bs(html, "html.parser")

    soup.find_all("img", class_="fancybox-image")[0]["src"]

    image_path = soup.find_all("img", class_="fancybox-image")[0]["src"]
    featured_img = url + image_path
    featured_img

    browser.quit()


    # ### Mars Weather
    # https://twitter.com/marswxreport?lang=en

    # Initialize browser and open URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5)

    html = browser.html
    soup = bs(html, "html.parser")

    weather = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").find_all('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")[0].text
    weather

    browser.quit()


    # ### Mars Facts
    # https://space-facts.com/mars/

    url = 'https://space-facts.com/mars/'

    table_df = pd.read_html(url)[0]
    table_df

    facts = table_df.to_html()
    facts


    # ### Mars Hemispheres
    # https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

    # Initialize browser and open URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(3)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(3)

    html = browser.html
    soup = bs(html, "html.parser")

    image_path = soup.find("div", id="wide-image").find_all('img')[1]["src"]
    cerberus = url + image_path
    cerberus

    browser.quit()

    # Initialize browser and open URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(3)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(3)

    html = browser.html
    soup = bs(html, "html.parser")

    image_path = soup.find("div", id="wide-image").find_all('img')[1]["src"]
    schiaparelli = url + image_path
    schiaparelli

    browser.quit()

    # Initialize browser and open URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(3)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(3)

    html = browser.html
    soup = bs(html, "html.parser")

    image_path = soup.find("div", id="wide-image").find_all('img')[1]["src"]
    syrtis = url + image_path
    syrtis

    browser.quit()

    # Initialize browser and open URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(3)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(3)

    html = browser.html
    soup = bs(html, "html.parser")

    image_path = soup.find("div", id="wide-image").find_all('img')[1]["src"]
    valles = url + image_path
    valles

    browser.quit()

    mars_dict= {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img": featured_img,
        "weather": weather,
        "facts": facts,
        "hemisphere_img": [
            {"title": "Cerberus Hemisphere", "img":cerberus},
            {"title": "Schiaparelli Hemisphere", "img":schiaparelli},
            {"title": "Syrtis Major Hemisphere", "img":syrtis},
            {"title": "Valles Marineris Hemisphere", "img":valles}
        ]
    }

    return mars_dict

