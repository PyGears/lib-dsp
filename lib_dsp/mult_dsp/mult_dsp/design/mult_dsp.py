from pygears import gear
from pygears.typing import Integer, Fixpnumber
from pygears.typing.math import ceil_div
from pygears.typing.base import typeof
from enum import IntEnum
from pygears.lib import trunc, saturate, qround, pipeline, cast

class Overflow(IntEnum):
    WRAP_AROUND = 0
    SATURATE = 1


class Quantization(IntEnum):
    TRUNCATE = 0
    ROUND = 1

@gear
def mult_dsp(a, b, *, t=None, quantization=Quantization.TRUNCATE, overflow=Overflow.WRAP_AROUND, latency=0):
    """
    Computes the product of the data on its inputs. Inputs can be of Integer or Fixed point type.

    Parameters
    ----------
    t : Integer, Fixpnumber
        Desired output data type. If omitted, output type will be infered from input types.

    quantization : Quantization.TRUNCATE | Quantization.ROUND
        Desired method for reducing the fractional portion of the product.

    overflow : Overflow.WRAP_AROUND | Overflow.SATURATE
        Desired method for dealing with overflow.

    latency : int
        Number of clock cycles by which the output is delayed.

    Example
    -------
    mult_dsp(din0, din1,
             t=Fixp[6, 14],
             overflow=Overflow.SATURATE,
             quantization=Quantization.ROUND,
             latency=4)
    """
    prod = a * b
    latency_iter = latency

    if t is None:
        res = prod
    elif typeof(t, Integer):

        if latency_iter:
            pipe_len = ceil_div(latency_iter, 3)
            prod = prod | pipeline(length=pipe_len)
            latency_iter -= pipe_len

        if typeof(prod.dtype, Integer):
            quant_prod = prod
        elif typeof(prod.dtype, Fixpnumber):
            if quantization == Quantization.TRUNCATE:
                quant_prod = cast(prod, t=t)
            elif quantization == Quantization.ROUND:
                quant_prod = qround(prod)
            else:
                raise Exception(f"Parameter quantization has to be chosen from Quantization.TRUNCATE|ROUND")
        else:
            raise Exception('t has to be either Integer or Fixpnumber')

        if latency_iter:
            pipe_len = ceil_div(latency_iter, 2)
            quant_prod = quant_prod | pipeline(length=pipe_len)
            latency_iter -= pipe_len

        if overflow == Overflow.WRAP_AROUND:
            res = trunc(quant_prod, t=t)
        elif overflow == Overflow.SATURATE:
            res = saturate(quant_prod, t=t)
        else:
            raise Exception(f"Parameter overflow has to be chosen from Overflow.WRAP_AROUND|SATURATE")
    elif type(t, Fixpnumber):

        if latency_iter:
            pipe_len = ceil_div(latency_iter, 3)
            prod = prod | pipeline(length=pipe_len)
            latency_iter -= pipe_len

        if quantization == Quantization.TRUNCATE:
            quant_prod = trunc(prod, t=t.base[prod.dtype.integer, prod.dtype.integer + t.fract])
        elif quantization == Quantization.ROUND:
            quant_prod = qround(prod, fract=t.fract)
        else:
            raise Exception(f"Parameter quantization has to be chosen from Quantization.TRUNCATE|ROUND")

        if latency_iter:
            pipe_len = ceil_div(latency_iter, 2)
            quant_prod = quant_prod | pipeline(length=pipe_len)
            latency_iter -= pipe_len

        if overflow == Overflow.WRAP_AROUND:
            res = trunc(quant_prod, t=t)
        elif overflow == Overflow.SATURATE:
            res = saturate(quant_prod, t=t)
        else:
            raise Exception(f"Parameter overflow has to be chosen from Overflow.WRAP_AROUND|SATURATE")
    else:
        raise Exception('t has to be either Integer or Fixpnumber')

    if latency_iter:
        return res | pipeline(length=latency_iter)
    else:
        return res