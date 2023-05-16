import csv
from src.trade import Trade
from datetime import datetime

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_trades_data(self):
        trades = []
        valid_symbols = {'AAPL', 'GOOGL', 'AMZN', 'TSLA', 'MSFT', 'FB', 'JPM', 'V', 'BRK.B', 'NFLX'}

        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # column is missing in a specific row, the data in the subsequent columns will be shifted, potentially resulting in incorrect values. 
                # conditional check if 
                if 'trade_id' not in row:
                    print("'trade_id' is missing")
                if 'symbol' not in row:
                    print("'symbol' is missing")
                if 'timestamp' not in row:
                    print("'timestamp' is missing")
                if 'quantity' not in row:
                    print("'quantity' is missing")
                if 'price' not in row:
                    print("'price' is missing")
                    continue


                try:
                    # Validate and convert data types
                    trade_id = int(row['trade_id'])
                    ticker_symbol = str(row['symbol'])

                    # Check if the ticker symbol is valid
                    if ticker_symbol not in valid_symbols:
                        continue

                    trade_date = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S').date()
                    quantity = float(row['quantity'])
                    price = float(row['price'])

                    trade = Trade(
                        trade_id=trade_id,
                        ticker_symbol=ticker_symbol,
                        trade_date=trade_date,
                        quantity=quantity,
                        price=price
                    )

                    trades.append(trade)

                except (ValueError, KeyError):
                    # Handle invalid data types or missing keys
                    continue
                
        return trades

    def write_csv(self, trades):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=trades[0].get_field_names())
            writer.writeheader()
            for trade in trades:
                writer.writerow(trade.to_dict())
