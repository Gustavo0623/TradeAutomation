import unittest
from src.analysis import TradeAnalyzer
from src.trade import Trade

class TestAnalyzer(unittest.TestCase):

    # currently set to get average price regardless of stock (needs to be adjusted to only get averages for each stock)
    def test_calculate_average_price(self):
        # Test code for calculate_average_price() method
        # ...

        self.maxDiff = None
        
        # set expected data
        expected_data = [['AAPL', 155.0], ['GOOGL', 2510.25], ['AMZN', 3450.75], ['TSLA', 890.5], ['MSFT', 298.3], ['FB', 398.15], ['JPM', 149.75], ['V', 252.8], ['BRK.B', 3995.8], ['NFLX', 555.25]]

        # create instance of TestAnalyzer class
        analyzer = TradeAnalyzer(file_path='data/trades.csv')

        # call calc avg price method
        actual_data = analyzer.calculate_average_price()
        print(actual_data)

        # check if actual matches expected
        self.assertEqual(actual_data, expected_data)

    def test_get_highest_volume_trades(self):
        # Test code for get_highest_volume_trades() method
        # ...
        pass
        
    def test_calculate_portfolio_returns(self):
        # Create a sample list of trades for testing
        trades = [
            Trade(symbol='AAPL', price=100.0, quantity=10),
            Trade(symbol='AAPL', price=105.0, quantity=5),
            Trade(symbol='AAPL', price=98.0, quantity=7),
            Trade(symbol='AAPL', price=102.0, quantity=12),
            Trade(symbol='AAPL', price=99.0, quantity=8)
        ]

        # Create an instance of the Analyzer class
        analyzer = TradeAnalyzer()

        # Call the calculate_portfolio_returns method
        returns = analyzer.calculate_portfolio_returns(trades)

        # Assert that the calculated returns are correct
        # ...

    def test_calculate_performance_metrics(self):
        # Create a sample list of trades for testing
        trades = [
            Trade(symbol='AAPL', price=100.0, quantity=10),
            Trade(symbol='AAPL', price=105.0, quantity=5),
            Trade(symbol='AAPL', price=98.0, quantity=7),
            Trade(symbol='AAPL', price=102.0, quantity=12),
            Trade(symbol='AAPL', price=99.0, quantity=8)
        ]

        # Create an instance of the Analyzer class
        analyzer = TradeAnalyzer()

        # Call the calculate_performance_metrics method
        metrics = analyzer.calculate_performance_metrics(trades)

        # Assert that the calculated metrics are correct
        # ...

    def test_generate_report(self):
        # Create a sample list of trades for testing
        trades = [
            Trade(symbol='AAPL', price=100.0, quantity=10),
            Trade(symbol='AAPL', price=105.0, quantity=5),
            Trade(symbol='AAPL', price=98.0, quantity=7),
            Trade(symbol='AAPL', price=102.0, quantity=12),
            Trade(symbol='AAPL', price=99.0, quantity=8)
        ]

        # Create an instance of the Analyzer class
        analyzer = TradeAnalyzer()

        # Call the generate_report method
        report = analyzer.generate_report(trades)

        # Assert that the generated report is correct
        # ...


if __name__ == '__main__':
    unittest.main()
