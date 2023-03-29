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


def fetch_vacancies():
    # Задаем параметры запроса
    params = {
        'text': 'Python разработчик',
        'area': 113,  # 113 - Россия
        'page': 0,
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
def export_vacancies(vacancies):
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