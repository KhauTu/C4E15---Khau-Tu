from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('school'))

@app.route('/about-me')
def Info():
    return render_template('PersonalInfo.html')

@app.route('/school')
def school():
    return redirect('http://techkids.vn', code = 302)

if __name__ == '__main__':
  app.run(debug=True)
