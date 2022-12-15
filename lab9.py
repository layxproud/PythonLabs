import time


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, args):
        date = time.strftime("%H:%M:%S", time.localtime())
        print(f'<{date}>: function {self.func.__name__} '
              'called with arguments {args}')
        start = time.time()
        self.func(args)
        end = time.time()
        diff = f"{end-start:01f}"
        print(f"Class-Decorator elapsed time = {diff} sec")
        with open(f"{self.func.__name__}.html", 'a', encoding='utf-8') as f:
            f.write(f"<html><body>Время: {diff} секунд</body></html>\n")
        f.close()


def gen_list(n):
    lst = list()
    for num in range(1, n):
        lst.append(num)
    return lst


@Decorator
def squares_for(lst: list) -> list:
    for i in range(len(lst)):
        lst[i] **= 2


@Decorator
def squares_list_comprehenshion(lst: list) -> list:
    lst = [i ** 2 for i in lst]


@Decorator
def squares_map(lst: list) -> list:
    lst = list(map(lambda x: x**2, lst))


def main():
    lst = gen_list(10000000)
    squares_for(lst)
    squares_list_comprehenshion(lst)
    squares_map(lst)


if __name__ == "__main__":
    main()
