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
    return render_template('image_mars/image_mars.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image/index.html')


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection/index.html')


@app.route('/choice/<planet_name>')
def planet(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <h3>Эта планета близка к Земле</h3>
                    <div class="alert alert-success" role="alert">
                  <h5>На ней много деревьев(было)</h5>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                  <h5>С водой наблюдаются проблемы</h5>
                    </div>
                    <div class="alert alert-warning" role="alert">
                  <h5>Полетим же на нее</h5>
                    </div>
                    <div class="alert alert-info" role="alert">
                  <h5>Ведь она такая красивая</h5>
                    </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претендент на участие в миссии {nickname}:</h3>
                    <div class="alert alert-success" role="alert">
                  <h5>Поздравляем! Ваш рейтинг после {level} этапа отбора</h5>
                    </div>
                    <h5>составляет {rating}!</h5>
                <div class="alert alert-warning" role="alert">
                  <h3>Желаем удачи!</h3>
                    </div>
                  </body>
                </html>'''


@app.route('/carousel')
def carousel():
    return render_template('carousel/index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
