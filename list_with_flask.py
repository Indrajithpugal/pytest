from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def list():
    a= '''list is a ordered, it allows duplicate,mutable,hetrogeneous data structure
        to declare a list either we can use "[" or we can use "list()"
    '''

    l = [4,5,7,'hello world',True,5]
    b = l[2]
    c = l[0:3]
    # l[2] = 11
    # l.append(4+5j)
    # l.insert(2,22)
    # l1 = [9,23]
    # l.extend(l1)
    # l2 = l+l1
    # l.pop(2)
    # l.pop()
    #l.remove(5)
    # a1=[8,3,12,78]
    # b1 = a1.copy()
    # b1.pop()
    # l1= [89,56,67,23,45,98,112]
    # l1.sort(reverse=True)
    a = len(l)
    b = l.count(5)
    return f'''{l} the second position data of the list {b} the slicing of 0:3 for our list {c}
        the lengthe l is  {a} in l 5 is occurring {b} 
        '''
@app.route('/listcomp')
def lict_comp():
    l = [4,7,12,17]
    result = [x*2 for x in l]
    c_list = result
    return render_template('list.html', name = c_list)


if __name__ == '__main__':
    app.run(debug=True)
