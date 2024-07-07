import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# 1. get method to request data from endpoint and return Response object
response = requests.get(URL)
contents = response.text

# soup now is like document
soup = BeautifulSoup(contents,"html.parser")
# find all h3 element with class "title"
movie_all = soup.find_all(name="h3", class_ = "title")

# reverse list with list comprehension
movie_titles = [movie.getText() for movie in movie_all][::-1]

# 2. write to file
with open("top-100-movies.txt", mode="a",encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")