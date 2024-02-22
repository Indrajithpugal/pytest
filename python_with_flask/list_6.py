def list():
    '''
    a list is mutable data structure  to create a list we can use [] or "list"
    key word, hetrogeneous, duplicates, ordered,mutable

    :return:
    '''
    l = [8,4,3,2]
    l[2]=55
    #append-- help me to add the data into my end of the list
    l.append(23)
    #insert -- will help you add the data in the specific position
    l.insert(1,9)
    #you can merge one list to another list using .extend()
    l1=[98,45,23,45]
    l.extend(l1)

    #delete--pop()-- if we pass the position it will remove the positioned data
    #l1.pop(1)
    #l1.pop()
    #l1.remove(45)#it will the specified data first occurance
    #list will support len, count, indexing
    #.sort keyword will ascending order sort
    #l1.sort()
    #it will give the mirror version
    l1.reverse()
    return f'the created list {l} l1 list is {l1}'

