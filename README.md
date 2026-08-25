# Task_2

API-автотесты на **Pytest + Requests + Allure** для учебного сервиса «Stellar Burgers": https://qa-stellarburgers.education-services.ru

## Структура проекта

```
Task_2/
├── .gitignore                   # Файл для исключения служебных файлов из репозитория Git
├── requirements.txt             # Список внешних зависимостей проекта
├── README.md                    # Основной файл документации проекта (инструкция)
├── conftest.py                  # Общие фикстуры Pytest(настройка клиентов, генерация токенов)
│
├── data/                        # Модуль подготовки и хранения данных для тестов
│   ├── data.py                  # Статические тестовые данные(URL, эндпоинты, константы)
│   └── user_data_gen.py         # Динамические генераторы данных(креды для авторизации)
│
├── tests/                       # Основная директория с автоматизированными тестами
│   ├── test_create_user.py      # Тесты на ручку регистрации нового пользователя
│   ├── test_login_user.py       # Тесты на ручку авторизации пользователя в системе
│   ├── test_update_user.py      # Тесты на ручку изменения профиля(с токеном и без)
│   ├── test_create_order.py     # Тесты на ручку создания заказов(ингредиенты, авторизация)
│   └── test_get_order.py        # Тесты на ручку получения списка заказов пользователя
│
├── allure-results/              # Сырые файлы результатов тестирования (JSON), генерируемые Pytest
└── allure-report/               # Скомпилированный статический HTML-отчет, готовый для просмотра

```
## Технологический стек
* **Язык**: Python 3.14.4
* **Тест-раннер**: Pytest 8.3.5
* **Тестирование HTTP API**: Requests 2.32.3
* **Отчетность**: Allure 2.13.5
* **Генерация данных**: Faker 37.1

**Установка зависимостей**
```bash
pip install -r requirements.txt
```

## Запуск тестов
Запуск всех тестов с Allure:

```bash
pytest tests/ --alluredir=allure-results
```

Генерация Allure отчета:

```bash
allure generate allure-results -o allure-report --clean
```

Открытие Allure отчета:

```bash
allure open allure-report
```

Запуск конкретного тестового класса:

```bash
pytest tests/test_create_order.py -v
```