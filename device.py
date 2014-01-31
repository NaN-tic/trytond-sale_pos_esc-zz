# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import serial
from escpos import escpos

from trytond.model import ModelView, fields
from trytond.pool import Pool, PoolMeta
from trytond.rpc import RPC

__all__ = ['PosDevice']
__metaclass__ = PoolMeta


class PosDevice:
    __name__ = 'sale_pos.device'
    printer_port = fields.Char(string='Printer Port', help='Port type the '
            'receipt printer is conntected to.')
    display_port = fields.Char('Display port', help='Like /dev/ttyS0')
    display_baud = fields.Numeric('BAUD-Rate', digits=(10, 0))
    display_digits = fields.Numeric('Digits per Row', digits=(10, 0))
    logo = fields.Binary('Receipt Logo')

    @classmethod
    def __setup__(cls):
        super(PosDevice, cls).__setup__()
        cls.__rpc__.update({
                'test_printer': RPC(instantiate=0),
                'test_display': RPC(instantiate=0),
                })

        cls._error_messages.update({
                'device_unplugged': 'Device %s not found...!',
                })

    @staticmethod
    def default_printer_port():
        return '/dev/usb/lp0'

    @staticmethod
    def default_display_port():
        return '/dev/ttyS0'

    @staticmethod
    def default_display_baud():
        return 9600

    @classmethod
    @ModelView.button
    def test_printer(cls, devices):
        Receipt = Pool().get('sale_pos.receipt', 'report')
        receipt = Receipt()
        device = devices[0]
        if not device.printer_port or not receipt.device_active(device):
            cls.raise_user_error('device_unplugged', device.printer_port)
            return
        receipt.test_printer(device)

    @classmethod
    @ModelView.button
    def test_display(cls, devices):
        device = devices[0]
        if device.display_port:
            port = serial.Serial(device.display_port, device.display_baud)
            display = escpos.Display(port)
            display.set_cursor(False)
            display.clear()
            display.text('Display works!')
            display.new_line()
            display.text('Congratulations!')
            del display
            port.close()
