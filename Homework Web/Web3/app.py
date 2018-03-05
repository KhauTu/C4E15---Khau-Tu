from flask import *
# import json

# def str_to_bool(s):
#     if s == 'true':
#          return True
#     elif s == 'false':
#          return False
#     else:
#          raise ValueError

import mlab
from models.service import Service
mlab.connect()

app = Flask(__name__)

# Web3_Ex3:
@app.route('/')
def index():
    services = Service.objects()
    return render_template('service.html', services = services)

@app.route('/detail/<service_id>')
def detail(service_id):
    service_detail = Service.objects().with_id(service_id)
    return render_template('service_detail.html', service_detail = service_detail)

# Web4_Ex4:
@app.route('/new-service', methods = ['GET', 'POST'])
def new_service():
    if request.method == 'GET':
        return render_template('/input_tag_gender.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service = Service(name = name,
                                yob = yob,
                                phone = phone,
                                gender = gender,)
        new_service.save()
        return "Saved"

@app.route('/update-service/<service_id>', methods = ['GET', 'POST'])
def update(service_id):
    service_update = Service.objects().with_id(service_id)
    if request.method == 'GET':
        return render_template('update_form.html', service_update = service_update)
    elif request.method == 'POST':
        form = request.form
        # print(*form.items())
        # print(form['status'])
        # status = form['status']
        measure1 = int(form['measure1'])
        measure2 = int(form['measure2'])
        measure3 = int(form['measure3'])
        set_measure = [measure1, measure2, measure3]
        # if status == 1:
        #     set_status = True
        # else:
        #     set_status = False

        service_update.update(set__name = form['name'],
                                set__yob = form['yob'],
                                set__gender = "1" if form['gender'] == "1" else "0",
                                set__height = form['height'],
                                set__phone = form['phone'],
                                set__address = form['address'],
                                set__status = True if form['status'] == "1" else False, # set__status == set_status
                                set__image = form['image'],
                                set__desciption = form['desciption'],
                                set__measurements = set_measure # form['measurements'].split('-')
                                )

        service_update.reload()
        # # new_service = Service(name = name,
        # #                         yob = yob,
        # #                         gender = gender,
        # #                         height = height,
        # #                         phone = phone,
        # #                         address = address,
        # #                         desciption = desciption,
        # #                         measurements = measurements,
        # #                         )
        # new_service.save()
        return "Updated"


if __name__ == '__main__':
  app.run(debug=True)
