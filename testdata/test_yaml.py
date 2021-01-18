#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_yaml.py.py
# @Author: 橘子
# @Date  : 2021/1/18
# @Desc  : execise

import pytest
import yaml

#yaml 文件里定义了列表数据，通过 open() 方法获取 data.yml 文件对象，使用 yaml.safe_load() 加载这个文件对象，将 YAML 格式文件转换为 Python 值，分别传到到用例中生成多条用例分别执行。
#运行结果中 [1-2] 和 [20-30] 代码传入的两组参数，分别传入 test_foo() 用例方法中执行，并且分别生成两条测试结果。
#pytest 组合 YAML 实现数据驱动，YAML 文件作为用例数据源，控制测试用例的执行，使测试用例数据维护更加方便快捷。
@pytest.mark.parametrize("a,b",yaml.safe_load(open("G:/pytest_excice/testdata/data.yml", encoding='utf-8')))
def test_foo(a, b):
    print(f"a + b = {a + b}")