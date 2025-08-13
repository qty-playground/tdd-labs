def test_should_return_string_1_when_input_is_1():
    """基本規則：數字應該回傳字串化的數字"""
    from tdd_labs.foobarbar import foo_bar_bar
    
    result = foo_bar_bar(1)
    assert result == "1"