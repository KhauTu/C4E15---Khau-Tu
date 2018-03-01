from flask import Flask, render_template

import mlab
from models.customer import Customer

mlab.connect()
app = Flask(__name__)


@app.route('/<find_id>')
def search(find_id):
    customer = Customer.objects.get(id = find_id) # Find by id
    return render_template('test.html', customer = customer)

if __name__ == '__main__':
  app.run(debug=True)


# customer_list = Customer.objects()
