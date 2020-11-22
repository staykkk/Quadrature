from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
if prod([2,5])==10:
    print('success')
else:
    print('fail')