'''
import requests      # Для запросов по APi
from unyts import HHAPIParser
from unyts import HHAPIExporter




# задаем параметры запроса
url = 'https://api.hh.ru/vacancies'
params = {
    'text': 'Python разработчик',
    'area': 113,  # 113 - Россия
    'page': 0,
    'per_page': 100  # количество возвращаемых вакансий на странице
}

# добавляем параметры авторизации
client_id = 'ваш Client ID'
client_secret = 'ваш Client Secret'
headers = {
    'User-Agent': 'HH-User-Agent',
    'accept': 'application/json, text/plain, */*',
}

# отправляем GET-запрос для получения списка вакансий
response = requests.get(url, headers=headers, params=params)

# выводим найденные вакансии
vacancies = response.json()
#print(vacancies)
for vacancy in vacancies['items']:
        print(f'{vacancy["name"]}\n'
             f'{vacancy["employer"]["name"]}\n'
             f'{vacancy["alternate_url"]}\n')
'''
from unyts import HHAPIParser, fetch_vacancies, export_vacancies
from unyts import HHAPIExporter


def run_parser():

    # Создаем экземпляр парсера
    parser = HHAPIParser()

    # Получаем вакансии через API
    vacancies = fetch_vacancies()
    print(vacancies)

    # Создаем экземпляр экспортера
    exporter = HHAPIExporter()
    print(exporter)
    # Экспортируем данные в нужном формате
    export_vacancies(vacancies)