from bs4 import BeautifulSoup
import requests


reponse = requests.get(url="https://www.afi.com/afis-100-years-100-movies/")
empire_webpage = reponse.text
# print(empire_webpage)

soup = BeautifulSoup(empire_webpage, "html.parser")

movie_title = soup.find_all(name="h6", class_="q_title")
# print(soup.prettify())

for movie in movie_title:
    with open("movies.txt", "a") as file:
        file.write(f"{movie.getText()}\n")
