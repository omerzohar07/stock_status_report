import pickle
from Portfolio_object import Portfolio
from stock_object import stock
from datetime import datetime

def make_my_portfolio() -> Portfolio:
    my_portfolio= Portfolio()
    CrowdStrike_stock = stock(company_name='CrowdStrike'
                       ,symbol='CRWD'
                       ,purchase_price=282.00)
    my_portfolio.add_stock(CrowdStrike_stock,7)

    google_stock = stock(company_name='Google'
                       ,symbol='GOOG'
                       ,purchase_price=164.56)
    my_portfolio.add_stock(google_stock,7)

    russel2000_stock = stock(company_name='Russel2000'
                       ,symbol='IWM'
                       ,purchase_price=205.69)
    my_portfolio.add_stock(russel2000_stock,6)

    AMD_stock = stock(company_name='AMD'
                       ,symbol='AMD'
                       ,purchase_price=106.19)
    my_portfolio.add_stock(AMD_stock,9)

    adbe_stock = stock(company_name='Adobe'
                       ,symbol='ADBE'
                       ,purchase_price=470.00)
    my_portfolio.add_stock(adbe_stock,2)

    amazon_stock = stock(company_name='Amazon'
                       ,symbol='AMZN'
                       ,purchase_price=160.52)
    my_portfolio.add_stock(amazon_stock,6)

    dis_stock = stock(company_name='Disney'
                       ,symbol='DIS'
                       ,purchase_price=85.56)
    my_portfolio.add_stock(dis_stock,7)

    roku_stock = stock(company_name='Roku'
                       ,symbol='ROKU'
                       ,purchase_price=63.75)
    my_portfolio.add_stock(roku_stock,6)

    shopify_stock = stock(company_name='Shopify'
                       ,symbol='SHOP'
                       ,purchase_price=61)
    my_portfolio.add_stock(shopify_stock,10)

    asts_stock = stock(company_name='AST SpaceMobile'
                       ,symbol='ASTS'
                       ,purchase_price=26.68)
    my_portfolio.add_stock(asts_stock,268)

    return my_portfolio


def is_old_data(loaded_Portfolio: Portfolio) -> bool:
    return loaded_Portfolio.get_last_update_time() != datetime.now().date() or (datetime.now().hour == 23) 


def save_new_data(my_portfolio: Portfolio) -> None:
    portfolio = make_my_portfolio()
    with open('portfolio.pkl', 'wb') as file:
        pickle.dump(my_portfolio, file)


def get_saved_data() -> Portfolio:
    with open('portfolio.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
        
    return loaded_data
    

def get_portfolio() -> Portfolio:
    my_loaded_Portfolio = get_saved_data()
    if (is_old_data(loaded_Portfolio= my_loaded_Portfolio)):
        my_loaded_Portfolio.update_portfolio() 
        save_new_data(my_loaded_Portfolio)
        flag = f'I made new retrieve. This is the most relevant data for the {my_loaded_Portfolio.get_last_update_time()}'

    else:
        flag = f'I used cash. This is the most relevant data for the {my_loaded_Portfolio.get_last_update_time()}'

    print(flag)
    
    return my_loaded_Portfolio