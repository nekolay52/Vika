from bs4 import BeautifulSoup
import requests


url = "https://ru.wikipedia.org/wiki/Rust_(игра)"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, features="html.parser")
some_headline = soup.find('h1', class_="firstHeading mw-first-heading")
divan = soup.find('div', class_="mw-content-ltr mw-parser-output")
tosh_divan = divan.find_all(['p', "h1", "h2", "h3", "h4", "h5"])

print(some_headline.text)
for i in tosh_divan:
    print(i.text)