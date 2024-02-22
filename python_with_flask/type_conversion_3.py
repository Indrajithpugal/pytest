from  flask import Flask

app = Flask(__name__)

@app.route('/typecasting')
def var():
    '''
    int()- to convert any data type into integer
    bin()- to convert any data type into binary
    oct() -to convert any data type into octal
    hex()-to convert any data type into hexadecimal
    str()- to convert any data type into string
    bool()- to convert any data type into bool
    float()--to convert any data type into float
    complex() --to convert any data type into complex
    :return:
    '''
    b = 8
    print(f"real data {b} binary:{bin(b)},  octal:{oct(b)}, hexa:{hex(b)} string:{str(b)}, bool:{bool(8)}, float {float(b)},complex:{complex(b)})")
    return f"real data {b} binary:{bin(b)},  octal:{oct(b)}, hexa:{hex(b)} string:{str(b)}, bool:{bool(8)}, float {float(b)},complex:{complex(b)})"


if __name__=="__main__":
    app.run(debug=True)