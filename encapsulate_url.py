from  flask import redirect, Flask, url_for
from dict_html import  dict_passer
from returnhtmlcode import html_returner
from insert_py_html import html_inserter

app = Flask(__name__)


@app.route('/demo/<route>')
def demo(route):
    #to call another file functions we have to assign it into a variable then we can return that variable
    #handling the multiple endpoints using the if cases
    if route == 'dict':
        a = dict_passer()
        return a
    elif route == 'html':
        f = html_returner()
        return f
    elif route == 'user':
        f=html_inserter
        return f
    else:
        return "hello world"

if __name__=='__main__':
    app.run(debug=True)