from flask import Flask, flash, render_template, request,redirect, url_for

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
    return  render_template('index_flash.html')


@app.route('/login', methods= ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error= 'this credentials not valid for admin access please try with proper credentials'
        else:
            flash('yay you logged in as a admin')
            return redirect(url_for('index'))
    return  render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
