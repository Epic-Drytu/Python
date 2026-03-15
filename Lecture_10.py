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

