from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Загружаем пользователей из файла JSON
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

# Сохраняем пользователей в файле JSON
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = load_users()
        user = {
            'email': email,
            'password': password
        }

        users.append(user)
        save_users(users)

        return redirect(url_for('login'))

    return render_template('register.html')

# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = load_users()

        for user in users:
            if user['email'] == email and user['password'] == password:
                return redirect(url_for('profile'))

    return render_template('login.html')

# Страница профиля
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Страница главная
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
