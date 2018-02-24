from flask import Flask, render_template
app = Flask(__name__) # Tạo 1 server trên máy mình

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/')
# def index():
#     return 'Hello world'# render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello C4E 15"

@app.route('/sayhi/<name>')
def sayhi(name):
    return "Hi {0}".format(name) #"Hi" + name

@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    return str(x + y)

@app.route('/html')
def heading():
    return "<h2> Gì cũng được </h2>"

@app.route('/blog')
def blog():
    article_name = 'Thơ con cóc'
    posts = [
        {
            'content': 'phấn khởi',
            'author': 'Nguyên'
        },
        {
            'content': 'a',
            'author': 'A'
        },
        {
            'content': 'b',
            'author': 'B'
        },
        {
            'content': 'c',
            'author': 'C'
        },
    ]
    return render_template('blog.html', article_title = article_name, posts = posts)

if __name__ == '__main__': # Khi file này được chạy trực tiếp, thì tất cả các đoạn code này mới được chạy
  app.run(debug=True) # host:'127.0.0.1', port=8000
