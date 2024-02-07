from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotion():
    promo = '''Человечество вырастает из детства.
    Человечеству мала одна планета.
    Мы сделаем обитаемыми безжизненные пока планеты.
    И начнем с Марса!
    Присоединяйся!'''
    promo = '<br>'.join(i for i in promo.split('\n'))
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="static/css/style.css" />
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/img/mars.jpg" 
                            alt="здесь должен был быть марс, но картинки нет">
                        <br>Вот она какая, красная планета.</br>
                        {promo}
                      </body>
                    </html>"""
    return '</br>'.join(i for i in promo.split('\n'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
