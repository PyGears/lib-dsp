'''
conftest.py 
'''
import logging
import numpy as np
import random
from math import log, pi, sin

from pygears import reg
# in pytest clear pygears tree between tests to allow running mutliple tests
from pygears.util.test_utils import clear
from pygears.util.test_utils import synth_check_fixt, lang

import pytest


def pytest_addoption(parser):
    parser.addoption('--cosim', action='store')
    parser.addoption('--seed', action='store')
    parser.addoption('--num', action='store')
    parser.addoption('--random', action='store')
    # parser.addoption('--dbginfo', action = 'store')


def pytest_generate_tests(metafunc):
    seed_value = metafunc.config.option.seed
    test_num_value = metafunc.config.option.num
    random_value = metafunc.config.option.random
    cosim_value = metafunc.config.option.cosim
    # dbginfo_value = metafunc.config.option.dbginfo

    # print(f' dbgfo :{dbginfo_value}')
    # if dbginfo_value == 1:
    #     print(f' changing dbgfo :{dbginfo_value}')
    #     reg['logger/sim/level'] = logging.DEBUG
    # print(f"re {reg['logger/sim/level']}")

    if 'do_cosim' in metafunc.fixturenames:
        mark = metafunc.definition.get_closest_marker('parametrize')
        # check if do_cosim was already parametrize in the test itself
        print("-----------------------------", mark)
        if mark is not None:
            print(mark.args[0])
        if not mark or 'do_cosim' not in mark.args[0]:
            if cosim_value is not None:
                if int(cosim_value) == 1:
                    metafunc.parametrize("do_cosim", [True])
                elif int(cosim_value) == 0:
                    metafunc.parametrize("do_cosim", [False])
            else:
                metafunc.parametrize("do_cosim", [True, False])

    if 'seed' in metafunc.fixturenames:
        if seed_value is not None:
            if seed_value == 'random':
                seed_value = None  # seed will be randomized
            metafunc.parametrize("seed", [seed_value])
        else:
            if test_num_value is not None:
                if (random_value is not None):
                    metafunc.parametrize("seed", [
                        random.randrange(100_000_000)
                        for i in range(int(test_num_value))
                    ])
                else:
                    metafunc.parametrize("seed",
                                         list(range(int(test_num_value))))
            else:  # default seed will be set to '1'
                metafunc.parametrize("seed", [1])


