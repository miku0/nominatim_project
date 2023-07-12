def count_values(file):
    counts1 = {'False': 0, 'plus': 0, 'minus': 0, 'zero': 0}
    counts2 = {'False': 0, 'plus': 0, 'minus': 0, 'zero': 0}
    counts3 = {'False': 0, 'plus': 0, 'minus': 0, 'zero': 0}

    with open(file, 'r') as f:
        for line in f:
            values = line.split()[2:]
            counts1 = count_values_in_column(values[0], counts1)
            counts2 = count_values_in_column(values[1], counts2)
            counts3 = count_values_in_column(values[2], counts3)

    return counts1, counts2, counts3


def count_values_in_column(value, counts):
    if value == 'False':
        counts['False'] += 1
    else:
        num = int(value)
        if num > 0:
            counts['plus'] += 1
        elif num < 0:
            counts['minus'] += 1
        else:
            counts['zero'] += 1

    return counts


# path
file = 'comparison.dat'

# count the number
counts1, counts2, counts3 = count_values(file)

# print the results
print("result1:", counts1)
print("result2:", counts2)
print("result3:", counts3)
