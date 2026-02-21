# break statment
# Example 
mysum=0
for i in range(5,11,2):
    mysum +=i
    if mysum ==5:
        break
    mysum += 1
print(mysum)

# Find number of even number in the range of 5
even_num=0
for i in range(5):
    if i%2==0:   ## Here it means "remainder is 0"
        even_num+=1
print(even_num)

# Check whelther i or u is present 
# All the codes are same 

#s = "demo loops - fruit loops"
#if index in range(len(s)):
#    if s[index]=='i' or s[index]=='u':
#        print("There is an i or u.")
# Robot Cheerleaders 
an_letters="aefhilmnorsxAEFHILMNORSX"
word=input("I will cheer for you. Enter a word: ")
times=int(input("Level: "))

for w in word:
    if w in an_letters:
        print("Give me an" + w + ":" + w)
    else :
        print("Give me a" + w + ":" + w)
print ("What does it spell?")
for i in range(times):
    print(word,"!!!")

#Assume you are given a string of lowercase letters in variable s. Count how many unique letters are there in the strings.
# For example s='abca'
# Output should be 3
s='abca'
seen=''
count=0
for char in s:
    if char not in seen:
        seen = seen + char
        count += 1              ## We can use len() other than count
print(count)

#Square Root Finder with while loop
guess = 0 
neg_value=False
x = int(input("Enter an integer: ")) 
if x<0:
    neg_value=True
while guess**2<x:
    guess = guess + 1
if guess**2 ==x:
    print("The square root of", x, "is",guess)
else:
    print(x, "does not have a square root")
    if neg_value:
        print("Just checking... Did you mean",-x,"?")

# Hard code a number as a secret number. Write a program that checks through all the numbers from 1 to 10 and prints the secret value if it's in that range. 
# If it's not found, it doesn't print anything.
guess=int(input("Enter a integer: "))                    #My approach
if guess in range(1,11):
    print(guess,"is in the range")
else:
    print(guess,"is not in the range")

found = False                                           #Professor's Approach
secret = 4

for i in range(1,11):
    if i == secret:
        found = True

if not found:
    print('not found')
else:
    print('found')

# Word Problem
#Alyssa, Ben, and Cindy are selling tickets to a fundraiser.
# Ben sells 2 fewer tickets than Alyssa.
# Cindy sells twice as many tickets as Alyssa.
# A total of 10 tickets were sold by the three people.
# How many tickets did Alyssa sell?

for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total=(alyssa+ben+cindy==10
                  )
            two_less=(ben == alyssa-2)
            twice=(cindy==2*alyssa)
            if total and two_less and twice:
                print(f'Alyssa sold {alyssa} tickets ')
                print(f'Ben sold {ben} tickets ')
                print(f'Cindy sold {cindy} tickets ')
            
 #For efficient
 for alyssa in range(1001):
    ben = max(alyssa-20,0)
    cindy = alyssa *2
    if alyssa + ben + cindy == 1000:
        print(f'Alyssa sold {alyssa} tickets ')
        print(f'Ben sold {ben} tickets ')
        print(f'Cindy sold {cindy} tickets ')
            
