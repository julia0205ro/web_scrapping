import requests
import bs4
from fake_headers import Headers


def get_headers():
    return Headers(browser='chrome', os='win').generate()


HEADERS = get_headers()

main_response = requests.get('https://habr.com/ru/articles/', headers=HEADERS)
main_html_data = main_response.text
main_soup = bs4.BeautifulSoup(main_html_data, 'lxml')

tag_articles = main_soup.find('div', class_='tm-articles-list')
articles = tag_articles.find_all('article')

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

for article in articles:
    description = article.find('div',
                               class_='tm-article-body tm-article-snippet__lead').text
    for word in KEYWORDS:
        if word in description.casefold():
            time, title, link = (article.find('time')['datetime'],
                                 article.find('h2', class_='tm-title tm-title_h2').
                                 find('a').text,
                                 f"https://habr.com"
                                 f'''{article.find('h2', class_='tm-title tm-title_h2').
                                 find('a')['href']}''')
            print(f'<{time}> – <{title}> – <{link}>')