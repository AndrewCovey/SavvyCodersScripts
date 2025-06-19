# Task 1

def greet(name):
    def format_name(name):
        return name.title()
    print('Hello, ' + format_name(name) + '!')

greet('person')


#Task 2

times_called = 0

def blargh():

    global times_called
    times_called+=1
    print('You have called blargh() ' + str(times_called) + ' times so far.')

blargh()
blargh()
blargh()
blargh()


#Task 3

def show_evens(lon):
    numbers = list(filter(lambda x: x % 2 == 0, lon))
    return numbers

lon=[1,2,3,4,5,6,7,8,9,10]

print('Here are your numbers sir! ... ' +  str(show_evens(lon)))

# or if you want, also ...

print('Here are your numbers sir! ... ' +  str(show_evens(range(1,11))))

# or if you want, also ...

print('Here are your numbers sir! ... ' +  str(show_evens([1,2,3,4,5,6,7,8,9,10])))