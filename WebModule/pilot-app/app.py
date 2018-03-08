from flask import *
# from mongoengine import Document, StringField, IntField, BooleanField

import mlab
from models.service import Service
mlab.connect()

app = Flask(__name__)

# # Create collection
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField() # 0: female, 1: male
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()
# service = Service(name = 'Kiều Anh',
#                 yob = 1998,
#                 gender = 0,
#                 height = 160,
#                 phone = '09696969696',
#                 address = 'Hà Nội',
#                 status = True)
# service.save()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    services = Service.objects(gender = gender, address__icontains = 'hà nội')
    return render_template('search.html', all_services = services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services = services)

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects().with_id(service_id)
    return render_template('detail.html', service = service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects().with_id(service_id)
    if service_to_delete is None:
        return "Not found!"
    else:
        service_to_delete.delete()
        return redirect(url_for('admin'))

@app.route('/new-service', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        # new_service = Service(name = name,
        #                         yob = yob,
        #                         phone = phone,
        #                         )
        # new_service.save()
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        new_service = Service(name = name,
                                yob = yob,
                                phone = phone,
                                gender = 1,
                                height = 170,
                                address = 'Hà Nội',
                                status = True
                                )
        new_service.save()
        return "Saved"


if __name__ == '__main__':
  app.run(debug=True)
