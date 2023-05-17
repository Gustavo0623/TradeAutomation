import unittest
from src.analysis import TradeAnalyzer
from src.trade import Trade

class TestAnalyzer(unittest.TestCase):

    def test_calculate_average_price(self):
        # Create a sample list of trades for testing
        trades = [
            Trade(symbol='AAPL', price=100.0),
            Trade(symbol='AAPL', price=105.0),
            Trade(symbol='AAPL', price=98.0),
            Trade(symbol='AAPL', price=102.0),
            Trade(symbol='AAPL', price=99.0)
        ]
        
        # Create an instance of the Analyzer class
        analyzer = TradeAnalyzer()

        # Call the calculate_average_price method
        average_price = analyzer.calculate_average_price(trades, 'AAPL')

        # Assert that the calculated average price is correct
        self.assertAlmostEqual(average_price, 100.8, places=2)

    def test_get_highest_volume_trades(self):
        # Create a sample list of trades for testing
        trades = [
            Trade(symbol='AAPL', volume=1000),
            Trade(symbol='AAPL', volume=500),
            Trade(symbol='AAPL', volume=2000),
            Trade(symbol='AAPL', volume=1500),
            Trade(symbol='AAPL', volume=800)
        ]
        
        # Create an instance of the Analyzer class
        analyzer = TradeAnalyzer()

        # Call the get_highest_volume_trades method
        highest_volume_trades = analyzer.get_highest_volume_trades(trades, 'AAPL', 3)

        # Assert that the correct number of trades with highest volume is returned
        self.assertEqual(len(highest_volume_trades), 3)
        # Assert that the trades are in the expected order of descending volume
        self.assertEqual(highest_volume_trades[0].volume, 2000)
        self.assertEqual(highest_volume_trades[1].volume, 1500)
        self.assertEqual(highest_volume_trades[2].volume, 1000)

if __name__ == '__main__':
    unittest.main()
