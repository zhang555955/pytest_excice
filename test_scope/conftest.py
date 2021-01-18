#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : conftest.py
# @Author: 橘子
# @Date  : 2021/1/15
# @Desc  : execise

import pytest

@pytest.fixture(scope="session")
def open():
    print("打开浏览器")
    yield

    print("执行teardown!")
    print("最后关闭浏览器")