#Conversion of fractions into binary 
x=float(input("Enter a decimel number between 0 and 1: "))

p=0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p +=1

num=int(x*(2**p))

result='' 
if num=='0':
    result='0'
if num >0:
    result=str(num%2)+result
    num=num//2
for i in range(p-len(result)):
    result='0'+result

result=result[0:-p]+'.'+result[-p:]

print('The binary represntation of binary decimel'+str(x)+'is'+str(result))

#Normal case
x=0
for i in range(10):
    x+=0.234
print(x == 2.34)                   #True

#Special 0.1 case
x=0
for i in range(10):
    x+=0.1
print(x == 0.1)                   #False
print(x,'==',10*0.1)

#Approximation Implementation
x=100
epilson=0.01
num_guess=0
guess=0.0
increment=0.0001
while abs(guess**2 - x) >= epilson:
    guess+= increment
    num_guess+=1
print('Number of guesses', num_guess)
print(guess,'is close to square root of',x)

#Approxiamtion method to find the 'Close Enough' sqaure root
x=54321
epilson=0.01
num_guesses=0
guess=0
increment=0.0001
while abs(guess**2 -x)>= epilson and guess**2<= x:
    guess += increment 
    num_guesses+=1
print("Number of guess are",num_guesses)
if abs(guess**2-x )>=epilson:
    print("Failed on the sqaure root of",x)
else:
    print(guess,"is clsoe enough to",x)
        