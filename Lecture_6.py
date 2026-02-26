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
 
