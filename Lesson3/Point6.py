def int_func(word):
    word = word.lower()
    return word.capitalize()

def int_func_str(str):
    word_list = str.split()
    return ' ' .join(list(map(int_func, word_list)))

print(int_func('HeLLo'))
print(int_func('hello'))
print(int_func_str('Hello, world!'))
print(int_func_str('united states of america'))
print(int_func_str('i love you!'))
