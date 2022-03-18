
import random
import numpy as np
from pygears import reg


def set_seed(seed):
    """Unify all seeds"""
    reg['sim/rand_seed'] = seed
    random.seed(reg['sim/rand_seed'])
    np.random.seed(seed)
