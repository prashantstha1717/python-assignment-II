# 10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased).
# Modify the function by adding an argument, separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well.


def snake_case(camel):
    result1 = ''.join(['_'+ i.lower() if i.isupper()
                      else i for i in camel]).lstrip('_')
    return result1


def kebab_case(camel):
    result2 = ''.join(['-'+ i.lower() if i.isupper()
                      else i for i in camel]).lstrip('-')
    return result2


camel = str(input('Enter a camelcased letter: '))
print(snake_case(camel))
print(kebab_case(camel))
