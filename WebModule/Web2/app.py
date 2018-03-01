from flask import Flask, render_template
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


if __name__ == '__main__':
  app.run(debug=True)
