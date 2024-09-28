from constants import url, headers
import requests
from datetime import datetime

class stock:
    
    def __init__(self, company_name, symbol, purchase_price=0.0):
        self.company_name = company_name
        self.symbol = symbol
        self.purchase_price =  purchase_price
        self.previous_price = 0
        self.price = 0
        self.last_updated_date = self.set_init_last_update()
        self.init_update_price()


    def set_init_last_update(self) -> datetime:
        return datetime.now().date()
    

    def get_price(self):
        return self.price


    def get_previous_price(self):
        return self.previous_price


    def get_purchase_price(self):
        return self.purchase_price
    

    def get_stock_change(self):
        """Calculates the price change percentage compared to a purchase price."""

        if self.purchase_price == 0:
            return 0
        change = ((self.price - self.purchase_price) / self.purchase_price) * 100
        return round(change, 2)
    

    def get_last_day_change(self) -> float:
        """The function return the last daily change."""
        
        change = ((self.price - self.previous_price) / self.previous_price) * 100
        return change 
    
    
    def init_update_price(self):
        "The function update the last day close price first time."

        response = requests.get(url.format(symbol=self.symbol), headers=headers)
        stock_data = response.json()
        
        last_close = stock_data[0]['close']
        
        self.price = last_close



    def update_price(self):
        """The function update the last day close price."""
        

        response = requests.get(url.format(symbol=self.symbol), headers=headers)
        stock_data = response.json()
        
        last_close = stock_data[0]['close']
        
        if not ((self.last_updated_date == datetime.now().date()) and not (16 <= datetime.now().hour < 23)) or datetime.now().hour == 23:
            self.previous_price = self.price
            self.price = last_close
            print(f'The last day price was {self.previous_price} and today closed as {self.price}')

        else:
            print('Nothing have changed pal, keep something for tomorrow.')


    def display_info(self):
        """Displays all the stock information in a structured format."""

        stock_change = self.get_stock_change()
        last_day_change = self.get_last_day_change()

        print(f"Stock Information:")
        print(f"Company Name: {self.company_name}")
        print(f"Symbol: {self.symbol}")
        print(f"Purchase Price: ${self.purchase_price:.2f}")
        print(f"Current Price: ${self.price:.2f}")
        print(f"Previous Day's Price: ${self.previous_price:.2f}")
        print(f"Change Since Purchase: {stock_change:.2f}%")
        print(f"Last Day's Change: {last_day_change:.2f}%")