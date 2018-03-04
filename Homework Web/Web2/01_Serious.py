from flask import Flask, render_template

import mlab
from models.customer import Customer

mlab.connect()
app = Flask(__name__)


@app.route('/customer')
def search():
    all_customer = Customer.objects() # Find by id
    return render_template('customer.html', all_customer = all_customer)

@app.route('/tenmales')
def tenmales():
    all_customer = Customer.objects(gender = 1, contacted = False) # Find by id
    return render_template('customer_10male.html', all_customer = all_customer)

if __name__ == '__main__':
  app.run(debug=True)
