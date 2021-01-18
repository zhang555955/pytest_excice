#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_autouse.py
# @Author: 橘子
# @Date  : 2021/1/15
# @Desc  : execise

import pytest

@pytest.fixture(autouse="true")     #它会自动应用到所有的测试方法中，只是这里没有办法返回值给测试用例。
def myfixture():
    print("this is my fixture")

class TestAutoUse:
    def test_one(self):
        print("执行test_one")
        assert 1 + 2 == 3

    def test_two(self):
        print("执行test_two")
        assert 1 == 1

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2