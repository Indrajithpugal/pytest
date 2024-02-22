def dictionary():
    '''
    dictionary is a mutable datastructure, we can use {} or dict keyword to create dictionary
    it is a key-value pair (mapping datastructure).un ordered data structure. it won't allow the
    duplicates
    :return:
    '''
    d1 = {"key":56, 2:'two',True:90}
    #d1.pop(True)
    #del d1[2]
    #to add a value in a dictionary if the key already exists it will override old value else it will add element
    d1["key"]=89
    d1['apple']=45
    print(d1.values())
    print(d1.get(2))
    #dict which help us to convert the variables into dict
    d2 = dict(a=67,b=56,c=90)


    return (f'{d2}, the key holding value in d1 is {d1["key"], d1.get("ke")}, to filter keys from dict {d1.keys()}'
            f'to filter values from your dict  {d1.values()},    converting each keys, values as a'
            f'tuple use "items()"\t {d1.items()}')