
import random

import numpy as np
from math import log, pi, sin

from pygears import reg

def sine_seq(freq, fsample, num, t_b):
    """[Return sequence of float nubers as sine signal]

    Args:
        freq ([uns integer]): [clock freequency]
        fsample ([uns integer]): [sampling frequency]
        num ([uns integer]): [number of items to generate]
        t_b ([Fixp]): [item type used to saturate if needed]

    Returns:
        [list of floats]: [sequence as list of items in range [-1,t_b.fmax]]
    """
    seq = []
    for n in range(num):
        val = sin(2 * pi * freq / fsample * n)
        if val == 1:  # saturate to fmax if sine reaches '1'
            val = t_b.fmax
        seq.append(val)
    return seq


def random_seq(fixp_t, num=1):
    """Return defined numbert of random signal items of Fixp type"""
    seq = []
    for i in range(num + 1):
        seq.append(np.random.uniform(fixp_t.fmin, fixp_t.fmax))
    return seq


def random_choice_seq(seq_list, num):
    seq = []
    for i in range(10):
        choice = random.choice(range(len(seq_list)))
        seq.extend(seq_list[choice])
    return seq


def constant_seq(fixp_t, num=1, val=None):
    """Return constant signal as a sequence depending of Fixp type"""
    seq = []
    if val == None:
        val = np.random.uniform(fixp_t.fmin, fixp_t.fmax)
    for i in range(num):
        seq.append(val)
    return seq


def set_seed(seed):
    """Unify all seeds"""
    reg['sim/rand_seed'] = seed
    random.seed(reg['sim/rand_seed'])
    np.random.seed(seed)


def fixp_sat(f_type, val):
    try:
        # try to convert to filter implementation output type
        f_type(val)
    except ValueError:
        if (val > 0):
            val = f_type.fmax
        elif (val < 0):
            val = f_type.fmin
        else:
            log.error(f'Error when converting result {val} to {f_type}')
    return val