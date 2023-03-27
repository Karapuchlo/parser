#parser
import requests
import csv
import json

class Vacancy:
    def __init__(self, id, name, salary_from, salary_to):
        self.id = id
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
class HHAPIParser:

    def fetch_vacancies(self):


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
            if vacancy_data['salary']['from'] is not None:
                vacancy = Vacancy(vacancy_data['id'], vacancy_data['name'], vacancy_data['salary']['from'], vacancy_data['salary']['to'])
                vacancies.append(vacancy)

        # Возвращаем список вакансий
        return vacancies

# exporter
class HHAPIExporter:
    def __init__(self):
        pass

    def export_vacancies(self, vacancies):
        # Экспортируем вакансии в CSV-файл
        with open('vacancies.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Название', 'Зарплата с', 'Зарплата до'])
            for vacancy in vacancies:
                if vacancy.salary_from is not None:
                    writer.writerow([vacancy.id, vacancy.name, vacancy.salary_from, vacancy.salary_to])