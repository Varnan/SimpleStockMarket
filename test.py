
import random
import unittest
from helper import Stock


class ApiTestCase(unittest.TestCase):

    symbols = [1,2,3,4,5]
    types = [1,2]
    quantities = range(0, 1000, 5)
    prices = [10, 10000, 73, 29.6, 1, 923, 0]



    @classmethod
    def record_trade(self):
        print('\n')
        for i in range(10):
            Stock().record_trade(random.choice(self.symbols),random.choice(self.quantities), random.choice(self.types), random.choice(self.prices))

    @classmethod
    def test_stock_price(self):
        print('\n')
        for symbol in self.symbols:
            print('Stock price for %s:' % symbol,
                  Stock().stock_price(int(symbol)))
    
    @classmethod
    def test_dividend_yield(self):
        print('\n')
        for symbol in self.symbols:
            print('Dividend yield for %s:' % symbol,
                  Stock().calculate_divident(int(symbol),float(random.choice(self.prices))))
    
    @classmethod
    def test_p_e_ratio(self):
        print('\n')
        for symbol in self.symbols:
            print('P/E Ratio for %s:' % symbol,
                  Stock().calculate_pe_ratio(int(symbol),float(random.choice(self.prices))))
    

    @classmethod
    def test_gbce(self):
        print('\n')
        print('GBCE:', Stock().share_index())



if __name__ == '__main__':
    unittest.main()
