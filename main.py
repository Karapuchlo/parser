
from unyts import HHAPIExporter, fetch_vacancies_hh
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

from unyts import SuperjobAPIParser


def main():
    # Создаем экземпляр парсера
    parser = SuperjobAPIParser()

    while True:
        # Выводим список доступных действий
        print('1. Парсить вакансии')
        print('2. Выход')

        # Запрашиваем у пользователя номер действия
        action = input('Введите номер действия: ')

        # Выполняем соответствующее действие
        if action == '1':
            # Парсим вакансии
            print('С какого сайта парсим?')
            print("1. HH")
            print("2. Superjob")
            viborparsera = input('Введите номер сайта: ')
            if viborparsera == 1:
                run_parser_hh()
                # Экспортируем вакансии
                print('Данные успешно экспортированы в файл vacancies.csv')
            elif viborparsera == 2:
                run_parser_Superjob()
                # Экспортируем вакансии
                print('Данные успешно экспортированы в файл vacancies.csv')

        elif action == '2':
            # Выйти из программы
            break
        else:
            print('Неправильный выбор.')

if __name__ == '__main__':
    main()