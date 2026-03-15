#What is the value of L1, L2, L3 and L after the following code is executed?
L1=['re']
L2=['mi']
L3=['do']
L4=L1+L2
L3.append(L4)
L=L1.append(L3)
print(L1)
print(L2)
print(L3)
print(L)

#Output: ['re', ['do', ['re', 'mi']]], ['mi'], ['do', ['re', 'mi']], None

#Write a function that meets the following specification:
def make_ordered_list(n):
    mylist=[]
    for i in range(1, n+1):
        mylist.append(i)
    return mylist

print(make_ordered_list(5))

#Output: [1, 2, 3, 4, 5]

def remove_element(L, e):
    newlist=[]
    for i in L:
        if i not in e:
            newlist.append(i)
    return newlist  
L=[1,2,3,4,5]
print(remove_element(L, 3))
