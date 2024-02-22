from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/admin')
def admin_user():
    return  'this user can access the admin panel'

@app.route('/staff')
def staff_user():
    return 'this user is a staff'

#we configure redirection for the above two functions using url based on condition
@app.route('/user/<name>')
def user_filter(name):
    if name == 'admin':
        return redirect(url_for('admin_user'))
    else:
        return redirect(url_for('staff_user'))

if __name__ == '__main__':
    app.run(debug=True)



