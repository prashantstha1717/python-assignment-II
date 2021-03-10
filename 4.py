# 4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed?
# Sort the list. What is the first item on the list? What is the second item on the list?

lis = ['Ram', 'Shyam']
lis.append('Anu')
print('Before sorting')
print(lis)
for ind, name in enumerate(lis):
    print(ind, name)
lis.sort()
print("After sorting")
print(lis)
for ind, name in enumerate(lis):
    print(ind, name)