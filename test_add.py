#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_add.py
# @Author: 橘子
# @Date  : 2021/1/15
# @Desc  : execise

def add(x,y):
    return x + y

def test_add():
    assert add(1, 10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100

class TesClass:
    def test_one(self):
        x = "this"
        assert "o" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

