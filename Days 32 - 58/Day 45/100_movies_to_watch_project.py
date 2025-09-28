import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
contents = response.text
# print(contents)

soup = BeautifulSoup(contents, "html.parser")
titles = soup.find_all(class_="landscape")

list_of_movies = list(reversed([item.get("title") for item in titles]))

with open("movies.txt", "w", encoding="ISO-8859-1") as text_file:
    for num in range (0, len(list_of_movies)):
        text_file.write(f"{list_of_movies[num]}\n")