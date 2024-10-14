import pytest
from main import parse_matrix

def test_parse_matrix_simple_case():
    # Тест для простого случая
    input_str = "1 2 | 3 4"
    expected = [[1.0, 2.0], [3.0, 4.0]]
    assert parse_matrix(input_str) == expected

def test_parse_matrix_single_row():
    # Тест для случая с одной строкой
    input_str = "1 2 3 4"
    expected = [[1.0, 2.0, 3.0, 4.0]]
    assert parse_matrix(input_str) == expected

def test_parse_matrix_single_element():
    # Тест для случая с одной строкой и одним элементом
    input_str = "42"
    expected = [[42.0]]
    assert parse_matrix(input_str) == expected

def test_parse_matrix_empty_matrix():
    # Тест для пустой строки
    input_str = ""
    expected = [[]]  # Определяем, что пустая строка возвращает пустую матрицу
    assert parse_matrix(input_str) == expected

def test_parse_matrix_multiple_rows():
    # Тест для случая с несколькими строками
    input_str = "1 2 | 3 4 | 5 6"
    expected = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
    assert parse_matrix(input_str) == expected

def test_parse_matrix_with_floats():
    # Тест для строки с числами с плавающей точкой
    input_str = "1.1 2.2 | 3.3 4.4"
    expected = [[1.1, 2.2], [3.3, 4.4]]
    assert parse_matrix(input_str) == expected

if __name__ == "__main__":
    pytest.main()