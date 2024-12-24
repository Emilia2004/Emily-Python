def my_zip(*iterables):
    size = min(len(it) for it in iterables)
    result = []
    for i in range(size):
        result.append(tuple(iterable[i] for iterable in iterables))
    return result
print(my_zip([12,45,78],["Bob","Ann","Kate"]))
