
from unyts import run_parser_hh, run_parser_Superjob
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
            if viborparsera == '1':
                run_parser_hh()
                # Экспортируем вакансии
                print('Данные успешно экспортированы в файл vacancies.csv')
                break
            elif viborparsera == '2':
                run_parser_Superjob()
                # Экспортируем вакансии
                print('Данные успешно экспортированы в файл vacancies.csv')
                break
        elif action == '2':
            # Выйти из программы
            break
        else:
            print('Неправильный выбор.')

if __name__ == '__main__':
    main()