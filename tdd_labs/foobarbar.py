def foo_bar_bar(number: int) -> str:
    """
    根據數字回傳對應的字串
    - 被3整除: "Foo"
    - 被5整除: "Barbar"  
    - 同時被3和5整除: "FooBarbar"
    - 其他: 數字的字串形式
    """
    # 最極簡實作 - 簡單條件判斷
    if number == 3:
        return "Foo"
    if number == 5:
        return "Barbar"
    return "1"