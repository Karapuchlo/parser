import requests      # Для запросов по APi
import json
import argparse
class HHAPIParser():
    def __init__(self, search_text, area, access_token):
        self.search_text = search_text
        self.area = area
        self.access_token = access_token

    def fetch_vacancies(self):
        headers = {
            'User-Agent': 'HH-User-Agent',
            'accept': 'application/json, text/plain, */*',
        }

        params = {
            'text': 'Python разработчик',
            'area': 113,  # 113 - Россия
            'page': 0,
            'per_page': 100  # количество возвращаемых вакансий на странице
        }

        response = requests.get("https://api.hh.ru/vacancies", headers=headers, params=params)

        vacancies = []

        if response.status_code == 200:
            data = json.loads(response.text)
            for item in data["items"]:
                title = item["name"]
                link = item["alternate_url"]
                salary = item["salary"] if "salary" in item else None
                vacancies.append(Vacancy(title=title, salary=salary, link=link))
        return vacancies

class HHAPIExporter():
    def export_vacancies(self, vacancies):
        if self.export_type == 'csv':
            with open(self.export_file, 'w') as outfile:
                outfile.write("Title,Salary,Link\n")
                for vac in vacancies:
                    outfile.write(f"{vac.title},{vac.salary},{vac.link}\n")
        elif self.export_type == 'json':
            data = []
            for vac in vacancies:
                data.append({'Title': vac.title, 'Salary': vac.salary, 'Link': vac.link})
            with open(self.export_file, 'w') as outfile:
                json.dump(data, outfile, ensure_ascii=False)
        elif self.export_type == 'html':
            with open(self.export_file, 'w') as outfile:
                outfile.write("<html><head><title>Vacancy List</title></head><body><table>")
                outfile.write("<tr><th>Title</th><th>Salary</th><th>Link</th></tr>")
                for vac in vacancies:
                    outfile.write("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(vac.title, vac.salary, vac.link))
                outfile.write("</table></body></html>")

def run_parser(filename, file_type, method, search_text, area, access_token):
    if method == 'site':
        parser = HHParser(search_text=search_text, area=area, access_token=access_token)
    else:
        parser = HHAPIParser(search_text=search_text, area=area, access_token=access_token)
    vacancies = parser.fetch_vacancies()
    exporter = HHAPIExporter(export_type=file_type, export_file=filename)
    exporter.export_vacancies(vacancies=vacancies)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Vacancy parser')
    parser.a