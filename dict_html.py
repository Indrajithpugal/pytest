from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dict_passer():
    a = '''
        dictionary is a mapping data structure its mutable and unordered, hetrogeneous
        '''

    dicts={'tamil':70, 'english':67, 'maths':80}
    dicts['science'] = 90
    dicts['english'] = 85
    #dict.popitem()
    a = dicts['english']
    b = dicts.get('biology')
    d = dict(name='python', usage='everywhere')
    print(d)
    return render_template('dict.html', name=dicts,english=b, python=d)


if __name__=="__main__":
    app.run(debug=True)