from faker import Faker

def generate_user():
    fake = Faker("ru_RU")
    payload = {
        "email": fake.unique.email(),
        "password": fake.unique.password(),
        "name": fake.unique.name()
    }
    return payload