import csv
from src.trade import Trade

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    # skip_missing_columns = True by default, will be able to choose to skip the rows with missing columns or fill in the missing data with 'N/A'
    def load_trades_data(self):
        trades = []
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # column is missing in a specific row, the data in the subsequent columns will be shifted, potentially resulting in incorrect values. 
                # conditional check if skip_missing_columns is true 
                if 'trade_id' not in row or 'symbol' not in row or 'timestamp' not in row or 'quantity' not in row or 'price' not in row:
                    continue

                trade = Trade(
                    trade_id=row['trade_id'],
                    ticker_symbol=row['symbol'],
                    trade_date=row['timestamp'],
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
