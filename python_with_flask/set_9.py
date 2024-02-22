def set():
    '''
    set is mutable, unordered, hetrogeneous datastructure,which will not allow the duplicates
    :return:
    '''
    s1 = {4,2,6,8,2,4}
    #we cannot access any data from set since set is unorder
    #print(s1[2])
    #we can user remove -- to remove elements from set
    #s1.remove(44)
    #discard-- if the element existe it will remove else it will nothing
    #s1.discard(88)
    #to add a data to set
    # s1.add(45)
    # s1.add(65)
    #merging sets
    s2={68,23}
    s3 = {23,43,12,8}
    #s1.update(s2)
    return (f'unique elements:{s2.union(s3)}, common element {s2.intersection(s3)}'
            f' ,difference: {s2.difference(s3)}, uncommon elements {s2.symmetric_difference(s3)}')
