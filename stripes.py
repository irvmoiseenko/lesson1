def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    delimiter = str(delimiter)
    return(one + delimiter + two)

p = get_summ('Learn','python')
print(p.upper())







