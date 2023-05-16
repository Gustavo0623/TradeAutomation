# Import necessary modules
from src.data_handler import DataHandler
from src.portfolio import Portfolio
from src.report_generator import ReportGenerator

# Create instances of required classes
data_handler = DataHandler()
portfolio = Portfolio()
report_generator = ReportGenerator()

# Load trade data from the CSV file
trade_data = data_handler.load_trade_data('data/trades.csv')

# Process trade data and add trades to the portfolio
portfolio.add_trades(trade_data)

# Generate trade summaries
trade_summaries = portfolio.generate_trade_summaries()

# Generate portfolio performance report
portfolio_performance = portfolio.calculate_performance()

# Generate performance report
performance_report = report_generator.generate_performance_report(trade_summaries, portfolio_performance)

# Display or save the generated reports
performance_report.display()  # Or performance_report.save_as_pdf('reports/performance_report.pdf')
