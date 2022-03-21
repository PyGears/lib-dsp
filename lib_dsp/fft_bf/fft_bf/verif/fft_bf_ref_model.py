from pygears.typing import code
from scipy.fft import fft


def round_to_fixp(din, t):
    rounded = din * (2**t.fract) // 1
    if rounded == 2**(t.width - 1):
        rounded -= 1
    return code(int(rounded), cast_type=t)


def fft_bf_ref_model(input_points):
    """Calculate expected result based on FFT input points

    Args:
        input_points (_type_): _description_

    Returns:
        _type_: _description_
    """
    exp_res = []
    calc_res = fft(input_points)
    for calc_res_i in calc_res:
        exp_res.append(calc_res_i.real)
        exp_res.append(calc_res_i.imag)
    return exp_res