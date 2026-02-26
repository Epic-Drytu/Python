#Binary Search Method 
#It works for both 54321 and 0.5 type integers
x=54321
epsilon=0.01
num_guesses=0
if x>=1:
    low=1
    high=x
else:
    low=x
    high=1
guess=(high+low)/2
while abs(guess**2-x)>= epsilon:
    if guess**2<x:
        low=guess
    else:
        high=guess
    guess=(high+low)/2
    num_guesses+=1
print("Number of guesses is equal to",num_guesses)
print(guess,"is close to square root of",x)  
 
 #To find the square root of 27
cube=27
epsilon=0.01
low=0
high=cube
num_guesses=0
guess=0
while abs(guess**3-cube)>epsilon:
    if guess**3>cube:
        high=guess
    else:
        low=guess
    guess=(high+low)/2
    num_guesses+=1
print("number of guesses made:",num_guesses)
print(guess,"is close to cube root of",cube)

# Newton-Raphson Root Finder
#p(x)=x**2-24
epsilon=0.01
k=24.0
guess=24.0/2
num_guesses=0

while abs(guess**2-k)>epsilon:
    num_guesses+=1
    guess=guess-(((guess**2)-k)/(2*guess))
print("Number of guesses made is",num_guesses)
print(guess,"is close to root of x**2-24")