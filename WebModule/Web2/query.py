import mlab
from models.service import Service

mlab.connect()

all_service = Service.objects()

first_service = all_service[0]

print(first_service.name) # first_service['name']
