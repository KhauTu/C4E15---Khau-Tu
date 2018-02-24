from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<user_name>')
def user_profile(user_name):
    article_title = 'Profile C4E15'
    profiles = {
    'Huy':    {'Name':'Quang Huy',
        'Age': 29,
        'Gender': 'nam',
        'Hobby': 'sleeping',
        'Major':'Code',
        },
    'Tuan Anh':    {'Name':'Huynh Tuan Anh',
        'Age': 23,
        'Gender': 'nam',
        'Hobby': 'pingpong',
        'Major':'Web',
        },
    'Khau Tu':    {'Name':'Dong Khau Tu',
        'Age': 26,
        'Gender': 'nam',
        'Hobby': 'swimming',
        'Major':'Finance',
        },
    'Quy':    {'Name':'Dinh Quy',
        'Age': 20,
        'Gender': 'nam',
        'Hobby': 'boardgame',
        'Major':'Code',
        },
    'Quang':    {'Name':'Nhat Quang',
        'Age': 27,
        'Gender': 'nam',
        'Hobby': 'travel',
        'Major':'Admin',
        },
    'Nguyen':    {'Name':'Trung Nguyen',
        'Age': 22,
        'Gender': 'nam',
        'Hobby': 'selfie',
        'Major':'Code',
        },
    'San':    {'Name':'Ha San',
        'Age': 24,
        'Gender': 'nu',
        'Hobby': 'shopping',
        'Major':'Marketing',
        },
    }
    if user_name in profiles:
        user_info = profiles[user_name]
        return render_template('user_profile.html', article_title = article_title, user_info = user_info)
    else:
        return ('Not found!')
if __name__ == '__main__':
  app.run(debug=True)
