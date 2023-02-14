
def mean(numbers):
    means = []
    for row in numbers:
        mean = sum(row)
        means.append(mean)
    return means

numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
print(mean(numbers))





