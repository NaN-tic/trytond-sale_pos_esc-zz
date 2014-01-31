# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    @classmethod
    def __setup__(cls):
        super(Sale, cls).__setup__()
#        cls.__rpc__.update({
#                'add_sum': RPC(readonly=False, instantiate=0),
#                })

    @classmethod
    def add_sum(cls, sales):
        super(Sale, cls).add_sum(sales)
#        Configuration = Pool().get('sale_pos.configuration')
#        configuration = Configuration(1)
#        if configuration.display_port:
#            sale._display.show_total(cls.browse(sales))
