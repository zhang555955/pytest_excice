#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_parametrize.py
# @Author: 橘子
# @Date  : 2021/1/18
# @Desc  : execise
import pytest

# @pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",35)])
# def test_eval(test_input,expected):
#     #eval 将字符串str当成有效的表达式来求值，并返回结果
#     assert eval(test_input) == expected


#两个装饰器分别提供两个参数值的列表2*3=6，pytest会生成6条测试用例。在测试中通常使用这处方法是所有变量、所有聚会的完全组合，可以实现全面的测试
# @pytest.mark.parametrize("x",[1,2])
# @pytest.mark.parametrize("y",[8,10,11])
# def test_foo(x,y):
#     print(f"测试数据组合x:{x},y:{y}")

#@pytest.fixture与@pytest.mark.parametrize结合用法，实现用例参数化
#当indirect=True 时，会将login_r作为参数，test_user_data被当作参数传入到login_r方法中，生成多条测试用例。通过return将结果返回，当调用login_r可以获取到login_r这个方法的返回数据。

test_user_data = ['Tom', 'Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    #通过request.param 获取参数
    user = request.param
    print(f"\n 登录用户：{user}")
    return user
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值;{a}")
    assert a !=""

