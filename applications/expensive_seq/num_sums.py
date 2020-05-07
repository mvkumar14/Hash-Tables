import time

def num_sums(x):
    # input an x value and get 
    # the number of sums that will
    # have to be calculated
    # in order to produce the result

    if x == 0:
        return 1
    elif x == 1:
        return 3
    elif x == 2:
        return 5
    else:
        return num_sums(x-1) + num_sums(x-2) + num_sums(x-3)

one = 1
two = 3
three = 5
for i in range(3,150):
    temp = one + two + three
    print(i, temp)
    one = two
    two = three
    three = temp
