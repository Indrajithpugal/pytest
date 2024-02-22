def aritmetic():
    '''
    has basic mathematical operators,+,-,*,/,//,**,%
    :return:
    '''
    a=13
    b=5
    return (f'value1:{a}, value2:{b}, add {a+b}, sub {a-b}, mul {a*b}, div {a/b}'
            f'floordiv {a//b}, exponen {b**3}, mod {a%b} ')

def assignment():
    '''
    assigning values to a var
    :return:
    '''
    a=5
    #a = a+5
    a +=5
    a -=3
    a *=2
    a /=7
    a //=0.3
    a %=4
    return f'{a}'

def comparison():
    a=7
    b=8
    c = a<b# >,>=,<,<=,==,!=
    print(c)
    return f" a is {a} and b is {b}: a>b {a!=b}"

def logical():
    '''
    logical and, or, not
    and-- if all comparing values true out come will be true
    or -- if all comparing values false out come will be false
    not -- if we pass true it will return false
    :return:
    '''
    a=True
    b=False
    c=[4]
    d=4
    #if both values stored in same address condition True
    #membership operators
    l = [7,3,2,1,5]
    return f'{c or d}, identical operator {id(d), id(c), d is not c}, membership in or not in {17 not in l}'

