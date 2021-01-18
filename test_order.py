#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_order.py
# @Author: 橘子
# @Date  : 2021/1/15
# @Desc  : execise

import pytest

class TestPytest(object):

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("test_two,测试用例")

    @pytest.mark.run(order=3)
    def test_one(self):
        print("test_one,测试用例")

    @pytest.mark.run(order=1)
    def test_three(self):
        print("test_three,测试用例")

