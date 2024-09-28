import pywhatkit as kit
from datetime import datetime
from retrieve_data_only_once_a_day import get_portfolio

def get_relevant_time_variables():
    return datetime.now().hour, datetime.now().minute + 2

def send_message() -> None:

    my_portfolio = get_portfolio()
    hour, minute = get_relevant_time_variables()
    
    # Send a WhatsApp message
    kit.sendwhatmsg('+972548144232', my_portfolio.get_str_display_output() ,hour, minute)