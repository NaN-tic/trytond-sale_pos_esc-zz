# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .sale import *
from .device import *
from .reporting import *


def register():
    Pool.register(
        Sale,
        PosDevice,
        module='sale_pos_esc', type_='model')
    Pool.register(
        Receipt,
        Display,
        module='sale_pos_esc', type_='report')
