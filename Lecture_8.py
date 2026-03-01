def add(x,y):
    return x+y
def mult(x,y):
    print (x*y)
add(1,2)
print(add(2,3))
mult(4,5)
print(mult(2,3))

# Cool thing 
print(print(5))                         #It will give output as 5 and NONE

#Debug
def is_triangular(n):
    """if n is int and greater than 0
    Returns True if n is Triangular, i.e. summation of natural numbers
    (1+2+3+.....+k)
    Else False"""
    total=0
    for i in range(n+1):
        total+=i
        if total ==n:
            return True
    return False
print(is_triangular(1))            