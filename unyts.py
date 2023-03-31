# parser
import requests
import csv
import json


class Vacancy:
    def __init__(self, employer_name, name, salary, alternate_url):
        self.employer_name = employer_name
        self.name = name
        self.salary = salary
        self.alternate_url = alternate_url


def fetch_vacancies_hh():
    # Задаем параметры запроса
    for i in range(10):
        params = {
            'text': 'Python разработчик',
            'area': 113,  # 113 - Россия
            'page': i,
            'per_page': 100  # количество возвращаемых вакансий на странице
        }

        # Отправляем GET-запрос на получение списка вакансий
        vacancies_url = 'https://api.hh.ru/vacancies'
        headers = {
            'User-Agent': 'HH-User-Agent',
            'accept': 'application/json, text/plain, */*',
        }
        response = requests.get(vacancies_url, headers=headers, params=params)

        # Обрабатываем полученные данные
        vacancies = []
        for vacancy_data in response.json()['items']:
            if vacancy_data['salary'] is not None:
                vacancy = Vacancy(vacancy_data["name"], vacancy_data["employer"]["name"], vacancy_data['salary'], vacancy_data["alternate_url"])
                vacancies.append(vacancy)

        # Возвращаем список вакансий
        return vacancies


# exporter
def export_vacancies_hh(vacancies):
    # Экспортируем вакансии в CSV-файл
    with open('vacancies.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Название', 'Работодатель', 'Зарплата', 'Ссылка'])
        for vacancy in vacancies:
            if vacancy.salary is not None:
                writer.writerow([vacancy.employer_name, vacancy.name, vacancy.salary, vacancy.alternate_url])


class HHAPIExporter:
    pass


class HHAPIParser:
    pass

# superjob_api_parser.py
class SuperjobAPIParser:
    def __init__(self):
        # Получаем токен авторизации приложения
        self.token = self.get_authorization_token()

    def get_authorization_token(self):
        # Задаем параметры запроса
        params = {'login': 'mc_gra_dy@mail.ru', 'password': '240615Nastya', 'client_id': '2270', 'client_secret': 'v3.r.137463232.a085bb1aaa3c51a9b7b88481b7075aa785b24619.5bc49efdee8512297bdf804e2d7b7cc7f3736ec3', 'scope': 'api'}

        # Отправляем POST-запрос на получение токена авторизации
        auth_url = 'https://api.superjob.ru/2.0/oauth2/password/'
        response = requests.post(auth_url, params=params)

        # Возвращаем токен авторизации
        return response.json()['access_token']

    def fetch_vacancies_Superjob(self, keyword, location, salary_from, salary_to, count):
        # Задаем параметры запроса
        headers = {'X-Api-App-Id': 'v3.r.137463232.a085bb1aaa3c51a9b7b88481b7075aa785b24619.5bc49efdee8512297bdf804e2d7b7cc7f3736ec3', 'Authorization': 'Bearer ' + self.token}
        params = {'town': location, 'keyword': keyword, 'count': count}

        # Отправляем GET-запрос на получение списка вакансий
        if salary_from and salary_to:
            # Если указана зарплата "от" и "до"
            params['payment_from'] = salary_from
            params['payment_to'] = salary_to
            vacancies_url = 'https://api.superjob.ru/2.0/vacancies/'
        elif salary_from:
            # Если указана только зарплата "от"
            params['payment_from'] = salary_from
            vacancies_url = 'https://api.superjob.ru/2.0/vacancies/?payment_from=%s' % salary_from
        elif salary_to:
            # Если указана только зарплата "до"
            params['payment_to'] = salary_to
            vacancies_url = 'https://api.superjob.ru/2.0/vacancies/?payment_to=%s' % salary_to
        else:
            # Если зарплата не указана
            vacancies_url = 'https://api.superjob.ru/2.0/vacancies/'

        # Отправляем запрос
        response = requests.get(vacancies_url, headers=headers, params=params)

        # Обрабатываем полученные данные
        vacancies = []
        for vacancy_data in response.json()['objects']:
            vacancy = Vacancy(id=vacancy_data['id'], name=vacancy_data['profession'], salary_from=vacancy_data['payment_from'], salary_to=vacancy_data['payment_to'])
            vacancies.append(vacancy)
        print(vacancies)
        # Возвращаем список вакансий
        return vacancies