# 5. Create a tuple with your first name, last name, and age.
# Create a list,people, and append your tuple to it.
# Make more tuples with the corresponding information from your friends and append them to the list.
# Sort the list. When you learn about sort method,
# you can use the key parameter to sort by any field in the tuple, first name, last name, or age.

me = ('Prashant', 'Shrestha', 19)
people = ('Chiraj', 'Khadhka', 26)
friend = ('Prabin', 'Bhandari', 18)
lis = list()
lis.append(me)
lis.append(people)
lis.append(friend)
print('printing the list')
print(lis)
print('Printing sorted list with key where key is first name.')
print(sorted(lis))
print('Printing sorted list with key where key is last name.')
print(sorted(lis, key=lambda lastname: lastname[1]))
print('Printing sorted list with key where key is age.')
print(sorted(lis, key=lambda age: age[2]))
