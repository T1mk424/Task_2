import pytest
import time
import requests
from data.data import Urls
from data.user_data_gen import generate_user

@pytest.fixture()
def get_ingredient_hash():
    response = requests.get(f'{Urls.MAIN_URL}{Urls.API_GET_INGREDIENTS}')
    ingredients = response.json()
    return ingredients

@pytest.fixture()
def create_user_and_get_token(timeout = 10):
    start_time = time.time() 
    try:
        payload = generate_user()
        print("Payload for user creation:", payload) 

        create_response = requests.post(f'{Urls.MAIN_URL}{Urls.API_CREATE_USER}', data = payload)
        if not create_response.ok:
            print(f"Failed to create user: {create_response.status_code} - {create_response.text}")
        create_response.raise_for_status()  
        auth_payload = {key: value for key, value in payload.items() if key != 'name'}

        while True:
            login_response = requests.post(f'{Urls.MAIN_URL}{Urls.API_LOGIN}', data = auth_payload)
            if login_response.ok:
                response_data = login_response.json()
                if 'accessToken' in response_data:
                    token = response_data['accessToken']
                    yield token
                    break
            if time.time() - start_time > timeout:
                raise TimeoutError("Не удалось получить токен за отведенное время.")
            time.sleep(1)  

    finally:
        if 'token' in locals():
            requests.delete(f'{Urls.MAIN_URL}{Urls.API_DELETE_USER}', headers = {'Authorization': token})