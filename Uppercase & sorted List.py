def words(*args):
    lst=[]
    for x in args:
        letters = x.upper()
        lst.append(letters)
        lst.sort()
    return(lst)

print (words("Man utd", "Blackburn Rovers", "Liverpool", "Chelsea"))
