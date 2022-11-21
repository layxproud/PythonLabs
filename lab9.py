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


def timer_all_methods(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            attr = self._obj.__getattribute__(s)
            if isinstance(attr, type(self.__init__)):
                return timer(attr)
            else:
                return attr
    return NewCls


@timer_all_methods
class Squares:
    def gen_list(self, n):
        lst = list()
        for num in range(1, n):
            lst.append(num)
        return lst

    def squares_for(self, lst: list) -> list:
        for i in range(len(lst)):
            lst[i] **= 2
        return lst

    def squares_list_comprehenshion(self, lst: list) -> list:
        lst = [i ** 2 for i in lst]
        return lst

    def squares_map(self, lst: list) -> list:
        lst = list(map(lambda x: x**2, lst))
        return lst


def main():
    f = Squares()
    lst = f.gen_list(10000000)
    f.squares_for(lst)
    f.squares_list_comprehenshion(lst)
    f.squares_map(lst)


if __name__ == "__main__":
    main()
