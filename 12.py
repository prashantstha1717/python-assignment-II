# 12. Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.

def is_palindrome(string):
    if string.lower() == string[::-1].lower():
        return f'The given word is palindrome.'
    else:
        return f'The given word in not palindrome'


print(is_palindrome('wow'))
print(is_palindrome('Level'))
print(is_palindrome('Hello'))
print(is_palindrome('refeR'))
print(is_palindrome('insight'))


