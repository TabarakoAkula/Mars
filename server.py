from flask import Flask, render_template

app = Flask(__name__, template_folder='static')


@app.route('/')
def start_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    n = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(n)


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="img/mars_image.png">
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image/index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
