import requests
from bs4 import BeautifulSoup

# задаём параметры запроса
url = 'https://hh.ru'
params = {
    'text': 'Python разработчик',
    'area': 1,
    'st': 'searchVacancy',
    'page': 0
}

# отправляем GET-запрос
response = requests.get(url + '/search/vacancy', params=params)

# парсим HTML-страницу
soup = BeautifulSoup(response.text, 'html.parser')

# находим все блоки с вакансиями
vacancy_blocks = soup.find_all('div', {'class': 'vacancy-serp-item'})

# выводим найденные вакансии
for vacancy_block in vacancy_blocks:
    vacancy_title_element = vacancy_block.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
    vacancy_href = vacancy_title_element['href']
    vacancy_title = vacancy_title_element.getText()
    employer_name = vacancy_block.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).getText()
    print(f'{vacancy_title}\n'
          f'{employer_name}\n'
          f'{vacancy_href}\n')