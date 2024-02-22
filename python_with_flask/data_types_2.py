from  flask import Flask

app = Flask(__name__)

@app.route('/integers')
def integers():
    '''
    integers family will help to display a number in different formations
    :return:
    '''
    form1 = 89
    form2 = 0b001
    form3 = 0o0234
    form4 = 0x087ade
    return f'{bin(form1)}, {form2}, {form3}, {form4}'

@app.route("/strings")
def str():
    return 'hello'+"world"+'''
    this is 
    python'''+' 0b001' + " 56"+ " anything withing quotes in python is a string"

@app.route("/bool")
def boolean():
    '''
    in python all the values are true except
    0,(),{},[],''
    :return:
    '''
    a= ''
    print()
    return f'the boolen values in python { True}, { False} {bool(-90)}'

@app.route("/complex")
def comp():
    '''
    a real part along with a imaginary is a complex number
    :return:
    '''
    a= 6+4j
    return f'real part: {a.real}, imaginary part:{a.imag}'

@app.route("/float")
def floats():
    '''
    a number with a decimal format
    is a float value a=7.899006532467
    :return:
    '''
    return f'{6.45}'

@app.route("/type")
def dtypes():

    '''
    to get to know what is the type
    the variable value we can use
    type()
    :return:
    '''
    a,b,c,d = 89, 0b011, 0o453, 0x76de
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    e = 'hello world'
    print(type(e))
    f = 6+8j
    print(type(f))
    g = True
    print(type(g))
    return f'the {type(a), type(b), type(c), type(d)}'


if __name__ == "__main__":
    app.run(debug=True)