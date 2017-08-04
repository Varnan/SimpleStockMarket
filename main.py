
from helper import Stock

'''
The main function. Parse the command line parameters,

:param argv: arguments from the command line

'''


option = 0
while True:
    print "---------------------------------------"
    option = raw_input("Enter the number of the Option you want:" +
                       "\n----------------------------------------" +
                       "\n| 1 | Calculate dividend yield" +
                       "\n| 2 | Calculate the P/E Ratio"
                       "\n| 3 | Record Trade" +
                       "\n| 4 | Calculate Volume Weighted Stock Price "
                       "\n| 5 | Calculate the GBCE All Share Index"
                       "\n| 6 | To quit\n" +
                       "----------------------------------------\n>")

    if option == '6':
        break
    elif(option == '1'):
        symbol = raw_input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "----------------------------------------\n>")

        price = raw_input("Enter the stock price \n")
        print "-------------"

        status_code, result = Stock().calculate_divident(symbol, price)

        print "Dividend Yield : ", result

        print "########################################"
        print "\n \n"

    elif(option == '2'):
        symbol = raw_input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "----------------------------------------\n>")

        price = raw_input("Enter the stock price \n")
        print "-------------"

        status_code, result = Stock().calculate_pe_ratio(symbol, price)

        print "P/E Ratio : ", result

        print "########################################"
        print "\n \n"

    elif(option == '3'):
        symbol = raw_input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "----------------------------------------\n>")

        quantity = raw_input("Quantity of shares \n")

        indicator = raw_input("Choose a indicator :" +
                              "\n| 1 | BUY " +
                              "\n| 2 | SELL \n" +
                              "----------------------------------------\n>")

        traded_price = raw_input("Enter traded price \n")

        print "----------------------------"

        Stock().record_trade(symbol, quantity, indicator, traded_price)

        print "########################################"
        print "\n \n"

    elif(option == '4'):
        symbol = raw_input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "----------------------------------------\n>")

        print "-------------"

        Stock().stock_price(symbol)

        print "########################################"
        print "\n \n"

    elif(option == '5'):
        Stock().share_index()

        print "########################################"
        print "\n \n"
