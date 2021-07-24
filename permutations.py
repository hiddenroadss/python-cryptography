import cProfile

def find_factorial(n):
    if n <= 1:
        return n
    else:
        return find_factorial(n - 1) * n


def count(n):
    count = 0
    for i in range(n):
        count += 1
    return count


cProfile.run('count(find_factorial(12))')
