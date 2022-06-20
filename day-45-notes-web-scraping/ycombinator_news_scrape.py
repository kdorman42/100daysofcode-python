from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="a", class_="titlelink")
article_texts = [tag.getText() for tag in articles]
article_links = [tag.get("href") for tag in articles]

# Workaround to handle item with no score
article_scores = ([int(item.find(name="span", class_="score").text.split()[0])
                 if (item.find(name="span", class_="score"))
                 else 0 for item in soup.find_all(name="td", class_="subtext")])

# print(f"texts len: {len(article_texts)},\n"
#       f"links len: {len(article_links)}, \n"
#       f"scores len: {len(article_scores)}")

highest_score_index = article_scores.index(max(article_scores))
print(article_texts[highest_score_index])
print(article_links[highest_score_index])



