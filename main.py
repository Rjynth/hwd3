import types
import datetime


def logger(old_function):
	def new_function(*args, **kwargs):
		with open('previous.log', 'a') as log:
			func_time = datetime.datetime.now()
			func_name = old_function.__name__
			result = old_function(*args, **kwargs)
			log.write('-'*40 + '\n')
			log.write(
				f'Время вызова: {func_time}\n'
				f'Имя функции: {func_name}\n'
				f'Аргументы: {args}\n'
				f'Именованные аргументы: {kwargs}\n'
				f'Результат: {result}\n\n'
				)
			return result

	return new_function


@logger
def flat_generator(list_of_lists):
    for main_list in list_of_lists:
        for item in main_list:
            yield item

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()