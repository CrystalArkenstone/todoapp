from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Маршрут для первой страницы (по адресу "/")
@app.route('/', methods=['GET', 'POST'])
def page1():
    from flask import request  # импортируем внутри функции для простоты
    if request.method == 'POST':
        # Если пользователь нажал кнопку — перенаправляем на вторую страницу
        return redirect(url_for('page2'))
    # Иначе показываем первую страницу
    return render_template('page1.html')

# Маршрут для второй страницы (по адресу "/page2")
@app.route('/page2')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True)