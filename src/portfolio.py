# Import the Trade class from trade.py
from trade import Trade

# Define the Portfolio class
class Portfolio:
    # Constructor
    def __init__(self):
        self.trades = []  # List to store trade objects

    # Method to add a trade to the portfolio
    def add_trade(self, trade):
        if isinstance(trade, Trade):
            self.trades.append(trade)

    # Method to calculate the total value of the portfolio
    def calculate_portfolio_value(self):
        total_value = 0
        for trade in self.trades:
            total_value += trade.calculate_trade_value()
        return total_value

    # Method to generate a trade summary report
    def generate_trade_summary_report(self):
        # Create a report generator object
        report_generator = ReportGenerator()

        # Generate the trade summary report using the trades data
        report = report_generator.generate_trade_summary_report(self.trades)

        # Save the report to a file or display it on the console, based on your requirements

    # Method to generate a portfolio performance report
    def generate_portfolio_performance_report(self):
        # Create a report generator object
        report_generator = ReportGenerator()

        # Generate the portfolio performance report using the trades data
        report = report_generator.generate_portfolio_performance_report(self.trades)

        # Save the report to a file or display it on the console, based on your requirements
