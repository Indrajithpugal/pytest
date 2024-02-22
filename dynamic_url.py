from flask import Flask

app = Flask(__name__)

#the variable  part declared as <endpoint>
# @app.route('/user/<username>')
# def user_name(username):
#     return f'hello ther user{username}'
#
# if __name__=='__main__':
#     app.run(debug=True)

#int-- will accept the integer same way we can use str, float
@app.route('/user/<int:userid>')
def user_id(userid):
    return  f'the given user id is {userid}'

if __name__ == '__main__':
    app.run(debug=True)