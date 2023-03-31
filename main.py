
from unyts import HHAPIExporter, fetch_vacancies_hh, SuperjobAPIParser
from unyts import HHAPIParser, export_vacancies_hh
import utils


def run_parser_hh():
    # Создаем экземпляр парсера
    parser_hh = HHAPIParser()

    # Получаем вакансии через API
    vacancies_hh = fetch_vacancies_hh()
    print(vacancies_hh)

    # Создаем экземпляр экспортера
    exporter_hh = HHAPIExporter()
    print(exporter_hh)
    # Экспортируем данные в нужном формате
    export_vacancies_hh(vacancies_hh)


run_parser_hh()


def fetch_vacancies_Superjob():
    pass


def run_parser_Superjob():
    # Создаем экземпляр парсера
    parser_Superjob = SuperjobAPIParser()

    # Получаем вакансии через API
    vacancies_Superjob = fetch_vacancies_Superjob()
    print(vacancies_Superjob)

    # Создаем экземпляр экспортера
    exporter_Superjob = HHAPIExporter()
    print(exporter_Superjob)
    # Экспортируем данные в нужном формате
    export_vacancies_hh(vacancies_Superjob)


class SuperjobAPIExporter:
    pass


def main():
    print('Выберите сайт для получения вакансий:')
    print('1. HeadHunter')
    print('2. Superjob')
    site_choice = input()

    if site_choice == '1':
        print('Введите параметры для поиска вакансий на HeadHunter:')
        args = utils.parse_arguments()

        parser = HHAPIParser()
        vacancies = parser.fetch_vacancies(args.keyword, args.location, args.salary, args.count)

        exporter = HHAPIExporter()
        exporter.export_vacancies(vacancies)

        print('Данные экспортированы в файл vacancies.csv')
    elif site_choice == '2':
        print('Введите параметры для поиска вакансий на Superjob:')
        args = utils.parse_arguments()

        parser = SuperjobAPIParser()
        vacancies = parser.fetch_vacancies(args.keyword, args.location, args.salary_from, args.salary_to, args.count)

        exporter = SuperjobAPIExporter()
        exporter.export_vacancies(vacancies)

        print('Данные экспортированы в файл vacancies.csv')
    else:
        print('Неправильный выбор.')

if __name__ == '__main__':
    main()