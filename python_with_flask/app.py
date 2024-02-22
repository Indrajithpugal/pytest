from flask import Flask
from flask_restx import Api
from Resource import APIResource
from list_6 import list
from dictionary_8 import dictionary
from set_9 import set
from range_10 import ranges
from operator_12 import aritmetic,assignment,comparison,logical

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(APIResource):
    def get(self):
        return {'message':'Hello, world!'}

app.add_url_rule('/list', 'list',list)
app.add_url_rule('/dict', 'dict',dictionary)
app.add_url_rule('/set', 'set',set)
app.add_url_rule('/range', 'range',ranges)
app.add_url_rule('/arithmetic', 'arith',aritmetic)
app.add_url_rule('/assign', 'assign',assignment)
app.add_url_rule('/compare', 'compare',comparison)
app.add_url_rule('/logical', 'logical',logical)
# import declared routes

if __name__=="__main__":
    app.run(debug=True)

