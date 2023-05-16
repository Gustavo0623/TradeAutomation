class FinancialInfrastructure:
    def __init__(self, trades):
        self.trades = trades

    def calculate_portfolio_value(self):
        total_value = 0
        for trade in self.trades:
            total_value += trade.quantity * trade.price
        return total_value

    def calculate_portfolio_performance(self, start_date, end_date):
        # Perform calculations to determine portfolio performance
        # based on the trades within the given date range
        return performance_metrics

    def calculate_trade_statistics(self):
        # Perform calculations to determine trade statistics
        # such as average price, total quantity, etc.
        return trade_statistics
