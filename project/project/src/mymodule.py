# coding: utf-8
"""
File       : mymodule.py
Author     : author (author@mail.com)
Date       : 2018/07/05
Summary    : 
    jp - モジュールの例．
    en - Example of module.
Description:
    jp - 外部から呼び出しをされる前提のモジュール例．
    en - Example module that is called from the other files.
"""

def calc_sum(x: int, y: str) -> int:
    """足し算． / Summamtion.

    xとyを足して返す.
    Returns summation of x and y.

    Args:
        x: １つ目の引数 / arg 1
        y: ２つ目の引数 / arg 2

    Returns:
        xとyの合計値．
        Summation of x and y.

    """
    return (x + y)

