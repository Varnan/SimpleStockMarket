import csv
import pickle
import os

from datetime import datetime, timedelta

symbol_mapping = {
    1: "TEA",
    2: "POP",
    3: "ALE",
    4: "GIN",
    5: "JOE"
}

indicator_mapping = {
    1: "BUY",
    2: "SELL"

}

gbce_csv_reader = list(csv.DictReader(open('gbce.csv')))


class TradeRecord():
    '''
        Class for Record Trade data
    
    '''

    def __init__(self, symbol, quantity, indicator, traded_price, created_time):
        self.symbol = symbol
        self.quantity = quantity
        self.indicator = indicator
        self.traded_price = traded_price
        self.created_time = created_time

    def trade_details(self):
        data = "Symbol : {0} \n Quantity : {1} \n Indicator : {2} \n Trade Price : {3} \n Created Time : {4}".format(
            self.symbol, self.quantity, self.indicator, self.traded_price, self.created_time)
        return data


class Stock():

    @classmethod
    def calculate_divident(self, symbol, price):
        '''
            Calculate dividend yield for given stock.
            The initial data about the dividends are static taken from csv file.

            :param symbol: of the stock
            :param price: price.
            :return: value or throw a Error msg if symbol not registered or the price is not valid
        '''

        stock_symbol = symbol_mapping.get(int(symbol), None)

        if stock_symbol is None:
            return False, "Enter Valid Stock Symbol"

        try:
            if float(price) == 0.0:
                return False, "Enter valid price"
        except:
            return False, "Enter valid price"

        for gbce_stock in gbce_csv_reader:
            if gbce_stock['stock_symbol'] == str(stock_symbol):
                if gbce_stock['stock_type'] == "Common":
                    try:
                        divident = float(gbce_stock.get('last_divident', 0)) / float(price)
                    except ZeroDivisionError:
                        divident = 0
                else:
                    try:
                        divident = (float(gbce_stock.get('fixed_divident', 0))/100) * \
                            float(gbce_stock.get('par_value', 0)) / float(price)
                    except ZeroDivisionError:
                        divident = 0

                return True, divident

    @classmethod
    def calculate_pe_ratio(self, symbol, price):
        '''
            Calculate P/E Ratio for given stock.
            The initial data about the dividends are static taken from csv file.
            :param symbol: of the stock
            :param price : given price
            :return: value
        '''

        status_code, result = self.calculate_divident(symbol, price)

        if not status_code:
            return status_code, result
        else:
            try:
                pe_ratio = float(price) / float(result)
            except ZeroDivisionError:
                pe_ratio = 0

            return True, pe_ratio

    @classmethod
    def record_trade(self, symbol, quantity, indicator, traded_price):
        '''
            Record a new trade in the stock.

            :param symbol: of the stock
            :param indicator: SELL, BUY
            :param quantity: to trade
            :param traded_price: price of the trade
        '''

        trade_record_file = open("trade_record_file", "r")

        is_file_empty = os.path.getsize("trade_record_file") == 0

        if not is_file_empty:
            list_trade_records = pickle.load(trade_record_file)
        else:
            list_trade_records = []

        stock_symbol = symbol_mapping.get(int(symbol), None)
        quantity = int(quantity)
        indicator = indicator_mapping.get(int(indicator), None)
        traded_price = float(traded_price)

        try:
            trade_record_data = TradeRecord(stock_symbol, quantity, indicator, traded_price, datetime.now())

            trade_record_file = open("trade_record_file", "w")
            list_trade_records.append(trade_record_data)
            pickle.dump(list_trade_records, trade_record_file)
            print "Trade_record ", trade_record_data.trade_details()
            print "----------------------------"
            print "Trade data Recorded !!! "
        except KeyboardInterrupt:
            print "----------------------------"
            print "Trade data Not Added"
        except EOFError:
            print "----------------------------"
            print "Trade data Not Added"
        finally:
            trade_record_file.close()

    @classmethod
    def stock_price(self, symbol):
        '''
            Calculate stock price for given stock based on trades from last 15 min.

            :param symbol: of the stock
            :return: value

        '''

        stock_symbol = symbol_mapping.get(int(symbol), None)
        trade_time = datetime.now() - timedelta(minutes=15)

        trade_record_file = open("trade_record_file", "r")

        is_file_empty = os.path.getsize("trade_record_file") == 0

        quantity_sum = 0
        sum_trade_price = 0

        if not is_file_empty:
            list_trade_records = pickle.load(trade_record_file)

            for trade_record in list_trade_records:
                if trade_record.symbol == stock_symbol and trade_record.created_time >= trade_time:
                    print "Trade_record ", trade_record.trade_details()
                    quantity_sum += trade_record.quantity
                    sum_trade_price += (trade_record.quantity * trade_record.traded_price)

            if sum_trade_price and quantity_sum:
                vol_weight_stock_price = sum_trade_price/quantity_sum
                print "----------------------------"
                print "Volume Weighted Stock Price :  ", float(vol_weight_stock_price)

            else:
                return "Trade record is empty for the stock {0} in the past 15 minutes".format(stock_symbol)

        else:
            print "----------------------------"
            print "Trade Record is empty"

    @classmethod
    def share_index(self):
        '''
            Calculate the GBCE All Share Index using the geometric mean of prices
            for all stocks.

            :return: value
        '''

        trade_time = datetime.now() - timedelta(minutes=15)

        trade_record_file = open("trade_record_file", "r")

        is_file_empty = os.path.getsize("trade_record_file") == 0

        quantity_sum = 0
        sum_trade_price = 0

        if not is_file_empty:
            list_trade_records = pickle.load(trade_record_file)

            for trade_record in list_trade_records:
                if trade_record.created_time >= trade_time:
                    print "trade_record ", trade_record.trade_details()
                    quantity_sum += trade_record.quantity
                    sum_trade_price += (trade_record.quantity * trade_record.traded_price)

            if sum_trade_price and quantity_sum:
                gbce_share_index = sum_trade_price**(1/quantity_sum)
                print "----------------------------"
                print "GBCE Share Index :  ", float(gbce_share_index)

            else:
                return "Trade Record is empty"

        else:
            print "----------------------------"
            print "Trade Record is empty"
