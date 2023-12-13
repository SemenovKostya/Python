'''# Demonstrating min() - Example 1:
print(min("The Knights Who Say Ni")) # probel

# Demonstrating the index() method
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the list() function
print(list("abcabc"))

# Demonstrating the count() method
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Example 1: Demonstrating the isapha() method
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method
print('2018'.isdigit())
print("Year2019".isdigit())

'''

def mysplit(string):
    """
    Разделяет строку на список слов, разделенных пробелами.
    """
    if len(string) == 0:
        return []

    words = []
    current_word = ""
    for char in string:
        if char == " ":
            if len(current_word) > 0:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
        print('current_word = ',current_word )
        print('words = ', words)

    if len(current_word) > 0:
        words.append(current_word)

    return words

# Пример использования
string = "Hello world! This is a test"
result = mysplit(string)
