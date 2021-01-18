#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_fixture_scope.py
# @Author: 橘子
# @Date  : 2021/1/15
# @Desc  : execise

import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown")
    print("最后关闭浏览器")

@pytest.mark.usefixtures("open")
def test_search1():
    print("test_search1")
    raise NameError
    pass

def test_search2():
    print("test_search2")
    pass

def test_search3():
    print("test_search3")
    pass
