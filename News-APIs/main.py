
import requests

query = input('Enter what type of news you want today?: ')
api = '7f535bb752dd410d963c4b97df92c5f2'

url = f'https://newsapi.org/v2/everything?q={query}&from=2026-03-21&sortBy=publishedAt&apiKey={api}'

# print(url)

r = requests.get(url)
data = r.json()

articles = data['articles']

for index, article in enumerate(articles):
    print(index + 1, article['title'], article['url'])
    print('\n************************************************\n')

