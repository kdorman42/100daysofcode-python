from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, 'html.parser')
movie_tags = soup.find_all(name="h3", class_="title")
movies_list = [item.getText() for item in movie_tags]
movies_list.reverse()

with open("top_100_movies.txt", mode='w') as file:
    for movie in movies_list:
        file.write(f"{movie}\n")





