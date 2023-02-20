# #Create a generator that generates the squares of numbers up to some number N.
N = 10
gen = (x*x for x in range( N ))
for i in gen:
    print( i )

# #Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def gen1( n ):
    x = 2
    while x < n: 
        yield x
        x += 2

n = input()
for i in gen1( int(n) ):
    print( i, end=', ')

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def gen2():
    x = 1
    while True:
        if x % 3 == 0 and x % 4 == 0:
            yield x
        x += 1

def function( n ):
    gen = gen2()
    for i in gen:
        print( i )
        if i >= n:
            gen.close()

function( 40 )

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    while a <= b:
        yield a*a
        a += 1

a, b = 3, 6
for x in squares( a, b):
    print(x, end=' ')

#Implement a generator that returns all numbers from (n) down to 0.
def generator( n ):
    x = n 
    while x >= 0:
        yield x
        x -= 1

n = 12
for i in generator( n ):
    print( i )