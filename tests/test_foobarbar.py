"""
Test for foo_bar_bar function
"""
from tdd_labs.foobarbar import foo_bar_bar

def test_should_return_number_string_for_non_multiples():
    """
    測試基本規則：當數字不是 3 或 5 的倍數時，應回傳其字串形式
    """
    assert foo_bar_bar(1) == "1"
    assert foo_bar_bar(2) == "2"
    assert foo_bar_bar(4) == "4"


def test_should_return_foo_for_multiples_of_3():
    """
    測試 Foo 規則：當數字是 3 的倍數時，應回傳 "Foo"
    """
    assert foo_bar_bar(3) == "Foo"
    assert foo_bar_bar(6) == "Foo"


def test_should_return_barbar_for_multiples_of_5():
    """
    測試 Barbar 規則：當數字是 5 的倍數時，應回傳 "Barbar"
    """
    assert foo_bar_bar(5) == "Barbar"
    assert foo_bar_bar(10) == "Barbar"
