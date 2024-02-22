

from __main__ import app

@app.route('/variables')
def var():
    b = 8
    a = " a variable it is a container which stores some data "
    c=60
    print("addition of b,c",b+c)
    return a,b+c

@app.route('/rulesforvariables')
def rules():
    rule1 = "a variable must not start with integer, we can use integers in the middle or end"
    rule2 = "a vaiable must not contain any special characters"
    rule3 = "a keyword we cannot use it as a variable name"
    rule4 = "python case sensitive language"
    print(f'''1.{rule1},
    \n 2.{rule2} 
    \n 3. {rule3} ''')
    return f'''1.{rule1},
    \n 2.{rule2} 
    \n 3. {rule3}, {rule4} '''

