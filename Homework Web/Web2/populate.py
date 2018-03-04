import mlab
from models.customer import Customer
from random import randint, choice
from faker import Faker

mlab.connect()

fake = Faker()

for i in range(50):
    print('Saving customer', i + 1, '...')
    customer = Customer(name = fake.name(),
                gender = randint(0, 1),
                email = fake.email(),
                phone_number = fake.phone_number(),
                job = fake.job(),
                company = fake.company(),
                contacted = choice([True, False]))
    customer.save()
