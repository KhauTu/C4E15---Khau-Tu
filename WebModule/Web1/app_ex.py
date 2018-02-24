from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/user/<user_name>')
def profile(user_name):
    article_title = 'Profile C4E15'
    profiles = [
        {
            'Name': 'Tuan Anh',
            'Age': 22,
            'Gender': 'nam',
            'Interest': 'pingpong'
        },
        {
            'Name': 'San beu',
            'Age': 24,
            'Gender': 'nu',
            'Interest': 'money'
        },
        {
            'Name': 'a Huy map',
            'Age': 29,
            'Gender': 'nam',
            'Interest': 'sleeping'
        },
        {
            'Name': 'Khau Tu',
            'Age': 26,
            'Gender': 'nam',
            'Interest': 'swimming'
        },    ]
    pr = []
    # JSOM: dictionary of dictionaries
    # found_user = user_list[user_name]
    for profile in profiles:
        if user_name == profile['Name']:
            pr.append(profile)
            return render_template('profile.html', article_title = article_title, profiles = pr)
        else:
            pass
    return 'Not found!'

if __name__ == '__main__':
  app.run(debug=True)
