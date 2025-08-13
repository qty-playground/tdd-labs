"""
FooBarbar TDD 練習
"""

def foo_bar_bar(number: int) -> str:
    """
    根據數字回傳對應的字串
    - 被3整除: "Foo"
    - 被5整除: "Barbar"
    - 同時被3和5整除: "FooBarbar"
    - 其他: 數字的字串形式
    """
    if number % 3 == 0:
        return "Foo"
    elif number % 5 == 0:
        return "Barbar"
    return str(number)
