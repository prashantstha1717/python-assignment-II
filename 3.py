# 3. Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.

string = ["tod", "salt", "dot", "last", "mood", "doom"]
for i in string:
    for j in string:
        if len(i) == len(j) and i != j:
            for item in range(len(i)):
                for items in range(len(j)):
                    if i[item] == j[items]:
                        result = j
    print("The anagram of {} is:".format(i), result)
