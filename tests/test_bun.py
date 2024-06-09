import pytest
from bun import Bun


class TestBun:
    @pytest.mark.parametrize('bun,price',(
        [
            ['Флюоресцентная булка R2-D3', 988],
            ['Краторная булка N-200i', 1255]
            ]
    ))
    def test_check_name_bun(self,bun,price):
        name_bun = Bun(bun,price)
        assert name_bun.get_name() ==  bun



    @pytest.mark.parametrize('bun, price', (
            [
                ['Флюоресцентная булка R2-D3', 988],
                ['Краторная булка N-200i', 1255]
            ]
    ))
    def test_check_price_bun(self,bun,price):
        price_bun = Bun(bun,price)
        assert price_bun.get_price() == price
