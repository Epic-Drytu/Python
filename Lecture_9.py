# Anonymous Function
def do_twice(n,fn):
    return fn(fn(n))                # Here it had created three environment as there is a function call inside return
print(do_twice(3,lambda x: x**2))

#Indices and Slices
seq=(1,'a',4,(1,2))
for e in seq:
    print(e)

# Return in Tuple Object form
def quo_and_reman(x,y):
    a=x//y
    b=x%y
    return(a,b)
(quot, reman)=quo_and_reman(20,3)
print("Quotient is",quot)
print("Remainder is",reman)

# Example

def char_counts(s):
    vowels='aeiou'
    (c,v)=(0,0)
    for char in s:
        if char in vowels:
            c+=1
        else:
            v+=1
    return(c,v)
print(char_counts("abcd"))

