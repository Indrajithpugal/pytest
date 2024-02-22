from  flask import Flask

app = Flask(__name__)

@app.route('/indexing')
def indexing():
    '''
    positive indexing -- goes from left to right starts with 0
    negative indesing -- goes from right to left starts with -1
    data based position access
    position based data access
    :return:
    '''
    a = 'hello world'
    return f'''the index position of "O" is : {a.index("o")} find keyword result: {a.find("z")}
        position based data access: the position of 6 in a var a "{a[6]}"
    negative indexing position -4 in var "a" "{a[-4]}"'''

@app.route('/slicing')
def slicing():
    '''
    creating a sub sequence of a
    existing sequence
    :return:
    '''
    a = 'hello world'
    return f''' the sequence value in between position from 3 to 7 "{a[3:8]}"
    negative slicing from -8 to -2 "{a[-8:-2]}"
    if you give start position only "{a[3:]}"
    if you give ending only "{a[:9]}"
'''

if __name__=="__main__":
    app.run(debug=True)