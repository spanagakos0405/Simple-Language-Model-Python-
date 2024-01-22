author = 'Nathaniel Hobbs'

def sum(*args):
    my_sum=0
    for number in args:
        my_sum += number
    return my_sum

def product(a,b):
    return a*b

def power(a,b):
    return a**b

def doubleSum(a,b,c):
    return a+b+c
    return sum(a,sum(b,c)) # this would work for the bonus

# this line is TRUE if this file is given directly
# to the python interpreter (i.e. run as a script)
if __name__ == '__main__':
    print('welcome to calculator!')
    print('here is the result of 3+9', sum(3,9))
    print(sum(4,5,6,6,7,5,7,4,3,2,5,5,667,8,899954))
    print(sum(4,5,6,6,7,8,9,54,3,2,5,5,3,1,3,5,7,4,3,2,5,5,667,8,899954))
    print(sum(4,5,6,6,7,8,9,54,3,2,5,5,3,1,3,5,7,4,3,2,5,5,667,8,899954, 32843, 1238, 1832, 2183))
    # input('what do you want to do?')