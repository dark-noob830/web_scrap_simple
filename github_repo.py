import requests
from bs4 import BeautifulSoup
import re


url = 'https://github.com/{}'
username = 'dark-noob830'

r = requests.get(url.format(username), params={'tab': 'repositories'})
html_soup = BeautifulSoup(r.text, 'html.parser')
repos_element = html_soup.find(id='user-repositories-list')
repos = repos_element.find_all('li')

for repo in repos:
    name = repo.find('h3').get_text(strip=True)
    language = repo.find(attrs={'itemprop':"programmingLanguage"}).getText(strip=True)
    star = repo.find('a',attrs={'href':re.compile('\/stargazers')})
    star = int(star.getText(strip=True)) if star else 0
    print(name, language, star)