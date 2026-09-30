def find_fib(n):
    if n <= 2:
        return 1

    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next

    return fib_next


def list_fib(n):
    fib_list = [1, 1]
    if n <= 2:
        return fib_list[:n]

    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
        fib_list.append(fib_next)

    return fib_list


print(find_fib(10))
print(list_fib(1))
print(list_fib(2))
print(list_fib(10))
