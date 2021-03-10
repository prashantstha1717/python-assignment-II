# 7. Create a list of tuples of first name, last name, and age for your friends and colleagues.
# If you don't know the age, put in None. Calculate the average age, skipping over any None values.
# Print out each name, followed by old or young if they are above or below the average age.

peoples = [('Ram', 'Karki', 50), ('Prabin', 'Bhandari', 19), ('Sita', "Poudel", 20), ('Hari', 'Gurung', 18)]

age = []
for i in range(len(peoples)):
    age.append(peoples[i][2])
print(age)
avg = sum(age)/len(age)
print(f"The average age is: {avg}")

for i in range(len(peoples)):
    if peoples[i][2] > avg:
        print(peoples[i][0] + " is old")
    else:

        print(peoples[i][0] + " is young")