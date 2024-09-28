from stock_object import stock
from datetime import datetime

class Portfolio:
    def __init__(self):
        self.stocks = []  # To hold a list of tuples (Stock object, count of stocks)
        self.last_updated_date = self.set_init_last_update()
       

    def set_init_last_update(self) -> datetime:
        return datetime.now().date()
    

    def get_last_update_time(self) -> datetime:
        return self.last_updated_date


    def set_last_update_time(self) -> None:
        self.last_updated_date = datetime.now().date()


    def add_stock(self, stock, count):
        """Adds a stock to the portfolio."""
        self.stocks.append((stock, count))
    

    def get_total_value(self) -> float:
        """Calculates the total value of the portfolio."""
        total = 0
        for stock, count in self.stocks:
            total += stock.get_price() * count
        return round(total, 2)
    

    def get_total_purchase_price(self) -> float:
        total = 0
        for stock, count in self.stocks:
            total += stock.get_purchase_price() * count
        return round(total, 2)


    def get_portfolio_total_change(self) -> float:
        return round((self.get_total_value() - self.get_total_purchase_price())/self.get_total_purchase_price(),4) * 100.0


    def daily_change(self) -> float:
        """
        Calculates the daily change in the portfolio's total value.
        `previous_prices` should be a dictionary with stock symbols as keys and previous prices as values.
        """
        previous_value = 0
        current_value = 0
        
        for stock, count in self.stocks:
            previous_value += stock.get_previous_price() * count
            current_value += stock.get_price() * count
        
        if previous_value == 0:
            return 0
        
        change_percentage = round(((current_value - previous_value) / previous_value) * 100.0,2)
        return change_percentage


    def update_portfolio(self):
        """The function update's the portfolio status."""
        for stock, price in self.stocks:
            stock.update_stock()
        self.set_last_update_time()


    def display_daily_change(self):
        """Displays the portfolio's last day change"""
        daily_change = self.daily_change()
        print(f"Portfolio last day change is: {daily_change} percentages.")


    def get_str_display_output(self):
        """Returns the string of the portfolio's stocks and their values."""
        display_str_output = f"""
            Total portfolio value: ${self.get_total_value()},
            Total portfolio change from purchase: {self.get_portfolio_total_change()}%, 
            Total portfolio last day change: {self.daily_change()} 
        """
        
        return display_str_output

    def display_portfolio(self):
        """Displays the portfolio's stocks and their values."""
        print("Portfolio Summary:")
        for stock, count in self.stocks:
            print(f"{count} shares of {stock.company_name} ({stock.symbol}) at ${stock.price:.2f} each.")
        print(f"Total Portfolio Value: ${self.get_total_value()}")
        print(f"Total Portfolio Change: {self.get_portfolio_total_change()}%")