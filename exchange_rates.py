import requests 
import pandas as pd
from datetime import datetime
from fast_to_sql import fast_to_sql as fts
from utils import *
import time
import ctypes

def main():

    date = datetime.now().strftime("%Y-%m-%d")
    df = pd.DataFrame(columns=['Amount_FROM','Curr_FROM','Amount_TO','Curr_TO','Update_Date'])

    currencies = ['EUR', 'USD', 'GBP']

    for curr in currencies:
        url = f'https://api.exchangerate.host/latest?base={curr}&v={date}'
        response = requests.get(url)
        data = response.json()
        
        for curr2 in currencies:
            if curr2 != curr:
                temp = {'Amount_FROM' : 1, 'Curr_FROM' : curr, 'Amount_TO' : data['rates'][curr2], 'Curr_TO' : curr2, 'Update_Date': data['date']}
                df = df.append(temp, ignore_index = True)
    
    df['Update_Date'] = pd.to_datetime(df['Update_Date'])

    print(df)
    ctypes.windll.user32.MessageBoxW(0, "Connect to VPN!", "Exchange_rates scrapper", 1)
    
    try:
        conn = init_connection('10.20.29.133','storage_matching_app')
        fts.fast_to_sql(df,'Exchange_Rates',conn,if_exists='append',temp=False)
        commit(conn)
        ctypes.windll.user32.MessageBoxW(0, "Exchange rates are updated", "Exchange_rates scrapper", 1)
    except Exception as e:
        print(e)
        ctypes.windll.user32.MessageBoxW(0, "ERROR", "Exchange_rates scrapper", 1)
        try:
            conn = init_connection('10.20.29.133','storage_matching_app')
            fts.fast_to_sql(df,'Exchange_Rates',conn,if_exists='append',temp=False)
            commit(conn)
            ctypes.windll.user32.MessageBoxW(0, "Exchange rates are updated", "Exchange_rates scrapper", 1)
        except Exception as e:
            print(e)
            ctypes.windll.user32.MessageBoxW(0, "ERROR", "Exchange_rates scrapper", 1)
        
    
if __name__ == '__main__':
    main()
    


