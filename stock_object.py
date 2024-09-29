from constants import url, headers
import requests
from datetime import datetime

def get_stock_close_date_from_response_json(response_json: dict) -> datetime:
    """The function gets the response json and returns the close date"""

    full_close_date_str: str = response_json['date']

    concated_close_date_str: str = full_close_date_str.split('T')[0]

    close_date: datetime = datetime.strptime(concated_close_date_str, '%Y-%m-%d').date()

    return close_date


def get_stock_close_price_from_response_json(response_json: dict) -> float:
    return response_json['close']


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
    
    
    def init_update_price(self) -> None:
        "The function update the last day close price first time."

        response = requests.get(url.format(symbol=self.symbol), headers=headers)
        stock_data_json = response.json()[0]
        
        self.price = get_stock_close_price_from_response_json(stock_data_json)


    def update_stock(self):
        """The function update the stock's last day close price and last update time."""

        response = requests.get(url.format(symbol=self.symbol), headers=headers)
        stock_data_json = response.json()[0]
        
        last_close_price_from_json: datetime = get_stock_close_price_from_response_json(stock_data_json)
        last_close_date_from_json: float = get_stock_close_date_from_response_json(stock_data_json)
        
        if last_close_date_from_json != self.last_updated_date:
            self.previous_price = self.price
            self.price = last_close_price_from_json
            self.last_updated_date = last_close_date_from_json

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