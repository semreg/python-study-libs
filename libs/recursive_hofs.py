def reduce(reducer, iterable, initial_val=None):
    if len(iterable) < 2:
        return iterable[0] if initial_val is None else reducer(initial_val, iterable[0])

    if initial_val is None:
        return reduce(reducer, iterable[1:], iterable[0])

    return reduce(reducer, iterable[1:], reducer(initial_val, iterable[0]))


def rec_map(func, iterable):
    return reduce(lambda acc, curr: [*acc, func(curr)], iterable, [])


def rec_filter(func, iterable):
    return reduce(lambda acc, curr: [*acc, curr] if func(curr) else acc, iterable, [])


if __name__ == '__main__':
    spam = [1, 2, 3, 4, 6]
    eggs = [1]

    print(rec_filter(lambda el: el % 2 == 0, spam))

    
   
