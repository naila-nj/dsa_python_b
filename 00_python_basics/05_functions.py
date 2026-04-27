import random

def max_min(mlist):
    minimum = mlist[0]
    for item in mlist:
        if item < minimum:
            minimum = item
            
    print(minimum)

def get_values():
    mlist = random.sample(range(20, 50),10)
    print(mlist)
    max_min(mlist)

get_values()
