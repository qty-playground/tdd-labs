def foo_bar_bar(number: int) -> str:
    """
    根據數字回傳對應的字串
    - 被3整除: "Foo"
    - 被5整除: "Barbar"  
    - 同時被3和5整除: "FooBarbar"
    - 其他: 數字的字串形式
    """
    # 業務邏輯常數
    FOO_DIVISOR = 3
    BARBAR_DIVISOR = 5
    COMPOUND_DIVISOR = 15  # 3 * 5
    
    # 優化後的邏輯 - 先檢查複合規則
    if number % COMPOUND_DIVISOR == 0:
        return "FooBarbar"
    if number % FOO_DIVISOR == 0:
        return "Foo"
    if number % BARBAR_DIVISOR == 0:
        return "Barbar"
    return str(number)