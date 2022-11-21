import time


def timer(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return result
    return wrapper


def gen_list(n):
    lst = list()
    for num in range(1, n):
        lst.append(num)
    return lst


@timer
def squares_for(lst: list) -> list:
    for i in range(len(lst)):
        lst[i] **= 2
    return lst


@timer
def squares_list_comprehenshion(lst: list) -> list:
    lst = [i ** 2 for i in lst]
    return lst


@timer
def squares_map(lst: list) -> list:
    lst = list(map(lambda x: x**2, lst))
    return lst


def main():
    lst = gen_list(10000000)
    squares_for(lst)
    squares_list_comprehenshion(lst)
    squares_map(lst)


if __name__ == "__main__":
    main()
