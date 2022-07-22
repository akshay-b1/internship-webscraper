# https://www.youtube.com/watch?v=XVv6mJpFOb0&ab_channel=freeCodeCamp.org

from re import X
from bs4 import BeautifulSoup

with open ('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    html_tags = soup.find_all('h1')
    for tags in html_tags:
        intro_tag = tags.text

    print(intro_tag)
