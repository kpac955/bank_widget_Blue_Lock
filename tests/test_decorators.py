from src.decorators import log


def test_log():
    @log()
    def my_test_func(a, b):
        return a + b

    assert my_test_func(1, 2) == 3
    assert my_test_func("a", 2) == "Произошла ошибка"


def test_log_capsys(capsys):
    @log()
    def my_test_func(a, b):
        return a + b

    my_test_func(1, 2)

    captured = capsys.readouterr()
    assert "Функция: my_test_func, результат: 3 - всё ОК" in captured.out
    assert "Время работы функции:" in captured.out


def test_log_invalid(capsys):
    @log()
    def my_test_func(a, b):
        return a + b

    my_test_func("a", 2)

    captured = capsys.readouterr()
    assert (
        captured.out
        == """Функция: my_test_func - ERROR: can only concatenate str (not "int") to str with inputs: ('a', 2), {}\n"""
    )
