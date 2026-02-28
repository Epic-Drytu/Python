# Write a function
def is_even(i):
    """ Input is i which is a postive int
"""
    if i%2==0:
        return True
    else:
        return False
#Examples
print(is_even(3))
print(is_even(8))

#Practise 
def div_by(n,d):
    if n%d==0:
        return True
    else:
        return False
    
print(div_by(195,13))

#Add all the odd numbers  
def sum_odd(a,b):
    sum_of_odd=0
    i=a
    while i<=b:
        if i%2==1:
            sum_of_odd+=i
        i+=1
    return sum_of_odd
print(sum_odd(2,4))