# Addressbook autotests
## Описание
Добро пожаловать в мой проект курса software-testing.ru по автоматизированному тестированию на Python.  
Проект тестирует веб-приложение "Addressbook": https://sourceforge.net/projects/php-addressbook/
## Используемые языки, инструменты и подходы:
- Python 3
- Pytest
- Selenium WebDriver
- ValueObject / ParameterObject pattern
- MySQL ORM
- Data Driven Testing
- Allure reports
- Jenkins
- Behavior Driven Testing
- Gherkin
- Keyword Driven Testing
- Robot Framework

<img src="https://user-images.githubusercontent.com/125028645/231808880-8c86c010-a3f9-48d0-ac04-f059afa9efc8.png" width="40" title="Python"><img src="https://user-images.githubusercontent.com/125028645/233774560-a3e2d06b-a8a0-4839-b2bc-950595923414.png" width="40" title="PyTest"><img src="https://user-images.githubusercontent.com/125028645/231809848-5fc170d4-2ed5-488b-8d46-b957abc3ee99.png" width="40" title="Selenium"><img src="https://user-images.githubusercontent.com/125028645/231810036-e2c7d063-3355-4c3f-9fd4-eb1f1fbd5bc7.png" width="40" title="PyCharm"><img src="https://user-images.githubusercontent.com/125028645/233774659-ea63195d-d95d-4e75-8189-1ea1ce6a8f1b.png" width="40" title="Jenkins"><img src="https://user-images.githubusercontent.com/125028645/233774771-7383cceb-07e5-4b3a-b411-7e0ffc467f15.png" width="40" title="Allure Report"><img src="https://user-images.githubusercontent.com/125028645/233775548-1f1f5270-e8fb-4444-9761-df83488fc09d.png" width="40" title="Gherkin"><img src="https://user-images.githubusercontent.com/125028645/233775688-0c9f7a41-b438-4875-bc9c-2b759041d665.png" width="40" title="Robot Framework">

##Запуск тестов локально:
Prerequisites: установите XAMPP Server (Apache + PHP + MySQL) и тестируемое приложение.
1. Склонируйте репозиторий
2. Установите virtualenv `pip install virtualenv`
3. Откройте проект в PyCharm, задайте Python Interpreter, задайте виртуальное окружение
4. Установите зависимости `pip install -r requirements.txt`
5. Запустите тесты в PyCharm или в командной строке:
`pytest . --alluredir=results\allure-results -s -v`
6. Чтобы посмотреть отчёт о тестах, выполните `allure serve results\allure-results`

##Примеры отчётов
![image](https://github.com/stbelaya/python-webui-tests/assets/125028645/64d4f56c-588d-46cc-9c14-a7e984cdbf7d)
![image](https://github.com/stbelaya/python-webui-tests/assets/125028645/1a812551-25c5-42c4-b77b-b5d2a7bfc5c8)


