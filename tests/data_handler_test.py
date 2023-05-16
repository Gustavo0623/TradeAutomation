import unittest
from src.data_handler import DataHandler
from datetime import datetime

class TestDataHandler(unittest.TestCase):
    def test_load_trades_data(self):

        self.maxDiff = None

        # Define the expected data
        expected_data = [
            {"trade_id": "1", "ticker_symbol": "AAPL", "trade_date": "2023-05-01", "quantity": "100", "price": "152.50"},
            {"trade_id": "2", "ticker_symbol": "GOOGL", "trade_date": "2023-05-02", "quantity": "50", "price": "2510.25"},
            {"trade_id": "3", "ticker_symbol": "AMZN", "trade_date": "2023-05-03", "quantity": "200", "price": "3450.75"},
            {"trade_id": "4", "ticker_symbol": "TSLA", "trade_date": "2023-05-04", "quantity": "75", "price": "890.50"},
            {"trade_id": "5", "ticker_symbol": "MSFT", "trade_date": "2023-05-05", "quantity": "150", "price": "298.30"},
            {"trade_id": "6", "ticker_symbol": "FB", "trade_date": "2023-05-06", "quantity": "80", "price": "398.15"},
            {"trade_id": "7", "ticker_symbol": "JPM", "trade_date": "2023-05-07", "quantity": "90", "price": "149.75"},
            {"trade_id": "8", "ticker_symbol": "V", "trade_date": "2023-05-08", "quantity": "120", "price": "252.80"},
            {"trade_id": "9", "ticker_symbol": "BRK.B", "trade_date": "2023-05-09", "quantity": "30", "price": "3995.80"},
            {"trade_id": "10", "ticker_symbol": "NFLX", "trade_date": "2023-05-10", "quantity": "65", "price": "555.25"}
        ]



        # Create an instance of the DataHandler class
        data_handler = DataHandler(file_path='data/trades.csv')

        # Call the load_trades_data method
        actual_data = data_handler.load_trades_data()

        # Check if the actual data matches the expected data
        self.assertEqual(len(actual_data), len(expected_data))
        for actual_trade, expected_trade in zip(actual_data, expected_data):
            self.assertEqual(actual_trade.trade_id, expected_trade["trade_id"])
            self.assertEqual(actual_trade.ticker_symbol, expected_trade["ticker_symbol"])
            self.assertEqual(datetime.strptime(actual_trade.trade_date, '%Y-%m-%d %H:%M:%S').date().isoformat(), expected_trade["trade_date"])
            self.assertEqual(actual_trade.quantity, expected_trade["quantity"])
            self.assertEqual(actual_trade.price, expected_trade["price"])

    def test_load_trades_data_empty_file(self):
        # Create a test CSV file with no data
        # file_path = 'path/to/empty_file.csv'

        # Create an instance of the DataHandler class
        data_handler = DataHandler(file_path='data/empty_file.csv')

        # Call the load_trades_data method
        actual_data = data_handler.load_trades_data()

        # Assert that the loaded data is an empty list
        self.assertEqual(actual_data, [])

    def test_load_trades_data_missing_columns(self):
        # Create a test CSV file with missing columns
        # file_path = 'path/to/file_with_missing_columns.csv'

        # Create an instance of the DataHandler class
        # data_handler = DataHandler(file_path='path/to/file_with_missing_columns.csv')

        # Call the load_trades_data method
        # Assert that the appropriate exception is raised or the missing columns are handled correctly
        pass

    def test_load_trades_data_invalid_data(self):
        # Create a test CSV file with invalid data
        # file_path = 'path/to/file_with_invalid_data.csv'

        # Create an instance of the DataHandler class
        # data_handler = DataHandler(file_path='path/to/file_with_invalid_data.csv')

        # Call the load_trades_data method
        # Assert that the appropriate exception is raised or the invalid data is handled correctly
        pass

    def test_load_trades_data_large_file(self):
        # Create a test CSV file with a large number of rows
        # file_path = 'path/to/large_file.csv'

        # Create an instance of the DataHandler class
        # data_handler = DataHandler(file_path='path/to/large_file.csv')

        # Call the load_trades_data method
        # actual_data = data_handler.load_trades_data()

        # Assert that the loaded data is correct and the method performs efficiently
        pass


if __name__ == '__main__':
    unittest.main()
