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

import math

def calc_sum(x: int, y: str) -> int:
    """足し算 / Summamtion.

    xとyを足して返す.
    Returns summation of x and y.

    Args:
        x (int): １つ目の引数 / arg 1
        y (int): ２つ目の引数 / arg 2

    Returns:
        xとyの合計値．
        Summation of x and y.
    """
    return (x + y)

class QudraticEquations(object):
    """２次方程式のクラス / Class for Quadratic Equations
    
    Args:
        object (object): object
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """コンストラクタ / Constructor

        以下の２次関数のための初期化関数．
        Initialize the quadratic equations for the equations below.
            a*x^2 + b*x + c
        
        Args:
            a (float): x^2の係数 / Coefficient for x^2
            b (float): xの係数 / Coefficient for x
            c (float): 定数 / Constant Value
        
        Returns:
            None: Returns nothing.
        """
        self.a = a
        self.b = b
        self.c = c
    
    def calc_root(self) -> str:
        """２次方程式の根を求める / Calculate Root.
        
        Returns:
            str: 根 / root
        """
        root = ""
        
        D = self._calc_D()
        if D > 0:
            # 判別式Dが正の時 / Where D > 0
            ans1 = ((-1 * self.b) + math.sqrt(D)) / (2 * self.a)
            ans2 = ((-1 * self.b) - math.sqrt(D)) / (2 * self.a)
            root += str(ans1) + ", "
            root += str(ans2)
        elif D == 0:
            # 判別式Dが0の時 / Where D = 0
            ans = ((-1 * self.b)) / (2 * self.a)
            root += str(ans)
        else:
            # 判別式Dが負の時 / Where D < 0
            real = ((-1 * self.b)) / (2 * self.a)
            imaginary = math.sqrt(-1 * D) / (2 * self.a)
            root += str(real) + " + i(" + str(imaginary) + "), "
            root += str(real) + " - i(" + str(imaginary) + ")"

        return root

    def calc_value(self, x: float) -> float:
        """f(x)の値を計算する / Calculate f(x).
        
        Args:
            x (float): 二次方程式にダウンロード / value for quadratic function
        
        Returns:
            float: 計算したf(x) / calculated value f(x)
        """
        value = self.a * x * x + self.b * x + self.c
        return value
    
    def _calc_D(self) -> float:
        """判別式の計算 / Calculate Discriminant
        
        Returns:
            float: 判別式の値 / Discriminant Value
        """
        D = (self.b * self.b) - 4 * self.a * self.c
        return D
