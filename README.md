# top_100_movies
100daysofcode-day74

## Web Scraping
Day 74 challenge was to use web scrapping to create a list of top 100 movies that one must watch in ones lifetime.

## What is Web Scraping?
Web scraping is basically parsing HTML data from websites to gather information.

## BeautifulSoup
BeautifulSoup is of python module used to scrape websites.
"Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping." -Google


## Project Description
In this project, I am using BeautifulSoup and python request module to scrape the top 100 movies list from "https://www.afi.com/afis-100-years-100-movies/" and create a movie list for myself.

## Code Breakdown

## Step1
Import the BeautifulSoup and requests the library.
```
from bs4 import BeautifulSoup
import requests

```

## Step2
Using the request module to get all the HTML data as text from the "https://www.afi.com/afis-100-years-100-movies/" website.

```
reponse = requests.get(url="https://www.afi.com/afis-100-years-100-movies/")
empire_webpage = reponse.text
```

## Step3
Time to create a soup with BeautifulSoup.
Call the BeautifulSoup module and pass in the data you want to parse and what type of data.
In this case, I am going to pass in empire_webpage data and html.parser. B/c I am parsing HTML data.

```
soup = BeautifulSoup(empire_webpage, "html.parser")
```
## Step4
Using BeautifulSoup to find the data I am looking to parse.
I this case I am looking for all move titles on the website.
After inspecting the website using the google dev tool, I found that all the title are using HTML "h6" tag and class "q_title"
using BeautifulSoup's find_all method to get all the h6 tags with the "q_title" class and saved them in a variable.
```
movie_title = soup.find_all(name="h6", class_="q_title")
```
# Step5
Create a text file with all the movie titles extracted from the website.

```
for movie in movie_title:
    with open("movies.txt", "a") as file:
        file.write(f"{movie.getText()}\n")
```
