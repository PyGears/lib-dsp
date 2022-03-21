from pygears import gear
from pygears.lib import ccat, field_sel
    
@gear
def mux_dsp(sel, *din):
    """
    Selects one data input to be propagated to output based on the value of sel input.

    Example
    -------
    mux_dsp(sel, din0, din1)
    """
    return field_sel(sel, ccat(*din))
