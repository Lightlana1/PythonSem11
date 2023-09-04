# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from Sem10.Task2 import Rectangle



class RectanglePro(Rectangle):
    """
    Дорабатываем класс прямоугольник из прошлого семинара.
    """

    def __add__(self, other):
        sum_perim: int = self.get_perin() + other.get_perin()
        side_a = self.side_a + other.side_a
        side_b = sum_perim / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __sub__(self, other):
        if self.get_perin() < other.get_perin():
            self, other = other, self

        diff = self.get_perin() - other.get_perin()
        side_a = abs(self.side_a - other.side_a)
        side_b = diff / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __le__(self, other):
        return self.get_square() <= other.get_square()


if __name__ == '__main__':
    rect = RectanglePro(2, 3)
    rect2 = RectanglePro(5)
    # print(rect.get_perin())
    # print(rect2.get_perin())
    # rect_sum = rect + rect2
    # print(rect_sum.get_perin())
    # rect_diff = rect - rect2
    # print(rect_diff.get_perin())
    print(rect.get_square())
    print(rect2.get_square())

    print(rect<rect2)
   

