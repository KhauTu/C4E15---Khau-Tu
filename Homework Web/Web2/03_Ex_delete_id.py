import mlab
from models.customer import Customer

mlab.connect()
find_id = '5a9772ffc0e89605287e4050'

customer = Customer.objects.get(id = find_id) # Find by id

customer.delete() # Delete by id
