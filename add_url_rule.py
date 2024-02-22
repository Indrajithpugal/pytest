from flask import Flask

app = Flask(__name__)

def hello_world():
   print('this is the print statement message')
   return 'hello world'
app.add_url_rule('/hello', 'hello', hello_world)

@app.route("/comments")
def comments():
    #this is a single line comment
    '''
    used to write a
    bunch of lines comments
    :return:
    '''
    return "used to give some information about the written codes"

@app.route('/variables')
def var():
    a = 'a variable is a container which help you to'

if __name__== "__main__":
    app.run(debug=True)