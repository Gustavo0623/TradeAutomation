import csv
from src.trade import Trade

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_trades_data(self):
        trades = []
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                trade = Trade(
                    trade_id=row['trade_id'],
                    ticker_symbol=row['symbol'],
                    trade_date=row['timestamp'],  # Update the parameter name to 'trade_date'
                    quantity=row['quantity'],
                    price=row['price']
                )

                trades.append(trade)
        return trades

    def write_csv(self, trades):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=trades[0].get_field_names())
            writer.writeheader()
            for trade in trades:
                writer.writerow(trade.to_dict())
