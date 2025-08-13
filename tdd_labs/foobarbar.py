def foo_bar_bar(number: int) -> str:
    """
    根據數字回傳對應的字串
    - 被3整除: "Foo"
    - 被5整除: "Barbar"  
    - 同時被3和5整除: "FooBarbar"
    - 其他: 數字的字串形式
    """
    # 修正邏輯 - 先檢查複合規則！
    if number % 3 == 0 and number % 5 == 0:
        return "FooBarbar"
    if number % 3 == 0:
        return "Foo"
    if number % 5 == 0:
        return "Barbar"
    return str(number)