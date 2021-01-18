#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_params.py
# @Author: 橘子
# @Date  : 2021/1/15
# @Desc  : execise

import pytest

@pytest.fixture(params=[1,2,3])             #使用 fixture 的参数化功能，在 fixture 方法加上装饰器 @pytest.fixture(params=[1,2,3])，就会传入三个数据 1、2、3，分别将这三个数据传入到用例当中。这里可以传入的数据是个列表。传入的数据需要使用一个固定的参数名 request 来接收。
def data(request):
    return request.param

def test_not_2(data):
    print(f"测试数据：{data}")
    assert data < 5

