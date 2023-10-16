import pytest
from average_comparison import AverageComparator


def test_calculate_average():
    ac = AverageComparator()
    assert ac.calculate_average([1, 2, 3]) == 2.0
    assert ac.calculate_average([]) == 0
    assert ac.calculate_average([-1, 1]) == 0.0


def test_compare_averages():
    ac = AverageComparator()
    assert ac.compare_averages(
        [1, 2, 3], [1, 2, 3]) == "Средние значения равны"
    assert ac.compare_averages(
        [1, 2, 3], [4, 5, 6]) == "Второй список имеет большее среднее значение"
    assert ac.compare_averages(
        [4, 5, 6], [1, 2, 3]) == "Первый список имеет большее среднее значение"

# Отчет о покрытии кода тестами (команды для выполнения):

# Установка pytest и coverage:
# pip install pytest coverage

# Запуск тестов и создание отчета о покрытии:
# coverage run -m pytest test_average_comparison.py
# coverage report -m

# Объяснение:
# - В коде программы создан класс AverageComparator, который имеет два метода: calculate_average и compare_averages.
# - Метод calculate_average вычисляет среднее значение списка чисел.
# - Метод compare_averages сравнивает средние значения двух списков и возвращает соответствующее сообщение.
# - В тестах проверяется правильность работы обоих методов для разных сценариев, включая пустые списки и равные средние значения.
# - Для измерения покрытия кода тестами используется модуль coverage.py, который позволяет оценить процент покрытия кода тестами.
