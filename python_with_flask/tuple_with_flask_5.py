from flask import Flask

app = Flask(__name__)
def tuples():
    descr = '''
            we can declare tuples using () or we can create tuple using tuple()
            it is immutable, ordered, hetrogeneous, duplicates
    '''

    a = (67,34,53,2, "hello world", True,2)
    #a[2]=89

    return f"""the position of of the data 53 {a.index(53)} the length of the given tuple is {len(a)}
        the count of 34 in our tuple{a.count(34)}
    """
app.add_url_rule('/tuple', 'tuples',tuples)

@app.route("/tuple_unpack")
def unpack():
    '''
    tuple unpacking is if we have tuple of values we can assign them with tuple variables
    :return:
    '''
    fruit = ("apple", "orange","kiwi")
    (a,o,k)=fruit
    counts = (3,2,5,1,2,3,4,5)
    print(counts.count(3))
    print(fruit[1])
    return (f'a for {a}, o for {o}, k for {k}, The Number of elements in my tuploe {len(fruit)} '
            f'the count of "3" in my tuple count is : {counts.count(3)}')

if __name__ =="__main__":
    app.run(debug=True)