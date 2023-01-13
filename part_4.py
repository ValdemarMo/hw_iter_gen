# (необязательное задание)
# Написать генератор аналогичный генератору из задания 2,
# но обрабатывающий списки с любым уровнем вложенности.
# Шаблон и тест в коде ниже:

# ????????????

import types

def flat_generator(list_x):

    x = list_x
    print(x)
    for xx in x:
        print(type(xx))
        if isinstance(xx, list):
            print(f'r-in <  >')
            # xxx = flat_generator(xx)
            xxx = next(flat_generator(xx))
            # print(f'yield inery <{xxx}>')
            print(f'r-ex <  >')
        else:
            xxx = xx
            print(f'yield out   <{xxx}>')
        yield xxx

list_x = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

if __name__ == '__main__':
    for elem in flat_generator(list_x):
        print(f'exit        <{elem}>>>\n')

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()