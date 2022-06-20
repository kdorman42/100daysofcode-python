from bs4 import BeautifulSoup
# import lxml  # may need to be used instead depending on site

with open('website.html', 'rb') as site:
    soup = BeautifulSoup(site, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)  # only prints FIRST anchor tag
# all_anchor_tags = soup.find_all(name="a")  # returns a list of ALL anchor tags
#
# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    # pass


# find finds the first one, find_all finds mult
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class="heading")  # produces an error- "class" is reserved in python
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

# # Use CSS Selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)

