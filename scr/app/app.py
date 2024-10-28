from flask import Flask, request, render_template, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ

# Простой пользовательский словарь для проверки (в реальном приложении используйте базу данных)
users = {
    'user': 'password'  # Имя пользователя: пароль
}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['username'] = username  # Сохраните имя пользователя в сессию
        return redirect(url_for('welcome'))
    else:
        flash('Неправильное имя пользователя или пароль!')
        return redirect(url_for('home'))


@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f'Добро пожаловать, {session["username"]}!'
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)  # Удаление пользователя из сессии
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)



"""from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    file.save(f"./uploads/{file.filename}")
    return f'File {file.filename} uploaded successfully!'


if __name__ == '__main__':
    app.run(debug=True)"""