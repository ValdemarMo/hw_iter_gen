# Доработать класс FlatIterator в коде ниже. Должен получиться итератор,
# который принимает список списков и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.
class FlatIterator:

    def __init__(self, list_x):
        self.cursor_x = 0
        self.list_x = list_x
        self.end_x = len(list_x)

    def __iter__(self):
        self.cursor_xx = 0
        return self

    def __next__(self):
        if self.cursor_x == self.end_x:
            raise StopIteration
        list_xx = self.list_x[self.cursor_x]
        item_xx = list_xx[self.cursor_xx]
        self.cursor_xx += 1
        if self.cursor_xx == len(list_xx):
            self.cursor_x += 1
            self.cursor_xx = 0
        return item_xx

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()