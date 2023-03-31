
from unyts import HHAPIExporter, fetch_vacancies_hh, SuperjobAPIParser
from unyts import HHAPIParser, export_vacancies_hh


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