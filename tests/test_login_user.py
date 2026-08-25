import requests
from data.data import Urls, ErrorMessage
from data.user_data_gen import generate_user
import allure

class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя')
    def test_login_user(self):
        with allure.step('Генерация данных пользователя'):
            payload = generate_user()
        
        with allure.step('Отправка запроса на создание пользователя'):
            requests.post(f'{Urls.MAIN_URL}{Urls.API_CREATE_USER}', data = payload)
        
        with allure.step('Авторизация пользователя'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.API_LOGIN}', data = payload)
        
        with allure.step('Проверка,что код ответа 200 и что авторизация прошла успешно'):
            assert response.status_code == 200 and response.json()['success'] == True

        with allure.step('Удаление созданного пользователя'):
            token = response.json()['accessToken']
            requests.delete(f'{Urls.MAIN_URL}{Urls.API_DELETE_USER}', headers = {'Authorization': token})

    @allure.title('Проверка неуспешной авторизации с неправильной почтой')
    def test_login_user_with_wrong_email(self):
        with allure.step('Генерация данных пользователя'):
            payload = generate_user()
        
        with allure.step('Отправка запроса на создание пользователя'):
            requests.post(f'{Urls.MAIN_URL}{Urls.API_CREATE_USER}', data = payload)
        
        with allure.step('Подмена почты на неправильную для запроса авторизации'):
            wrong_payload = payload.copy()
            wrong_payload['email'] = 'wrong@mail'
        
        with allure.step('Авторизация пользователя с некорректной почтой'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.API_LOGIN}', data = wrong_payload)
        
        with allure.step('Проверка,что код ответа 401 и получили сообщение об ошибке с текстом "email or password are incorrect"'):
            assert response.status_code == 401 and response.json()['message'] == ErrorMessage.TEXT_LOGIN_401

        with allure.step('Удаление созданного пользователя'):
            login_response = requests.post(f'{Urls.MAIN_URL}{Urls.API_LOGIN}', data = payload)
            token = login_response.json()['accessToken']
            requests.delete(f'{Urls.MAIN_URL}{Urls.API_DELETE_USER}', headers = {'Authorization': token})
    
    @allure.title('Проверка неуспешной авторизации с неправильным паролем')
    def test_login_user_with_wrong_password(self):
        with allure.step('Генерация данных пользователя'):
            payload = generate_user()
        
        with allure.step('Отправка запроса на создание пользователя'):
            requests.post(f'{Urls.MAIN_URL}{Urls.API_CREATE_USER}', data = payload)
        
        with allure.step('Подмена пароля на неправильный для запроса авторизации'):
            wrong_payload = payload.copy()
            wrong_payload['password'] = 'wrong password'
        
        with allure.step('Авторизация пользователя с некорректным паролем'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.API_LOGIN}', data = wrong_payload)
        
        with allure.step('Проверка,что код ответа 401 и получили сообщение об ошибке с текстом "email or password are incorrect"'):
            assert response.status_code == 401 and response.json()['message'] == ErrorMessage.TEXT_LOGIN_401

        with allure.step('Удаление созданного пользователя'):
            login_response = requests.post(f'{Urls.MAIN_URL}{Urls.API_LOGIN}', data = payload)
            token = login_response.json()['accessToken']
            requests.delete(f'{Urls.MAIN_URL}{Urls.API_DELETE_USER}', headers = {'Authorization': token})
