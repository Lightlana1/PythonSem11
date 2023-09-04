# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class MyString(str):
    """
    класс Моя Строка, где: будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания
    """
    def __new__(cls, text: str, creator: str):
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        return f'{super().__str__()} created by: {self.creator} at {self.time}'


if __name__ == '__main__':
    example = MyString('text', 'name2')
    example_1 = MyString('name', 'text2')

    print(example)
    print(example_1)
    print(MyString.__doc__)
