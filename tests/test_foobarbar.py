def test_should_return_string_1_when_input_is_1():
    """基本規則：數字應該回傳字串化的數字"""
    from tdd_labs.foobarbar import foo_bar_bar
    
    result = foo_bar_bar(1)
    assert result == "1"

def test_should_return_foo_when_input_is_3():
    """Foo 規則：能被 3 整除應該回傳 Foo"""
    from tdd_labs.foobarbar import foo_bar_bar
    
    result = foo_bar_bar(3)
    assert result == "Foo"