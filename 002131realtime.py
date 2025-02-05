#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import tushare as ts

def track_stock_real_time(stock_code='002131'):
    """
    Tracks the real-time stock price of 利欧股份 (Leo Group).
    Args:
        stock_code (str): The stock code without '.SZ' suffix for the Tushare classic API.
    """
    while True:
        try:
            # Get real-time quotes for the given stock code
            df = ts.get_realtime_quotes(stock_code)
            
            # If retrieval is successful, df should have 1 row for a single stock code
            if df is not None and not df.empty:
                # Extract relevant data
                current_price = df.loc[0, 'price']
                bid = df.loc[0, 'bid']
                ask = df.loc[0, 'ask']
                time_str = df.loc[0, 'date'] + " " + df.loc[0, 'time']
                
                print(f"Time: {time_str} | Code: {stock_code} | "
                      f"Current Price: {current_price} | Bid: {bid} | Ask: {ask}")
            else:
                print(f"Failed to retrieve data for {stock_code}")
            
        except Exception as e:
            print(f"Error retrieving stock data: {e}")
        
        # Wait for 60 seconds before querying again
        time.sleep(60)

if __name__ == "__main__":
    # Example usage for 利欧股份 (002131)
    track_stock_real_time('002131')