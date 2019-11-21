def buy_and_sell_stock_once(prices):
  min_price_so_far, max_profit = float('inf'), 0.0 # create variables to store minimum price and maximum profit. 
  for price in prices:
    max_profit_sell_today = price - min_price_so_far # maximum profit equal current price minus minum price so far
    max_profit = max(max_profit, max_profit_sell_today) # keep the maximum between current profit and previous maximum
    min_price_so_far = min(min_price_so_far,price)  # keep minimum price so far if it is smaller than current price otherwise keep current price
  return max_profit # return the maximum profit so far among all 
  
import array 

arr = array.array('i', [310,315,275,295,260,270,290,230, 255,250]) # creat array
print(buy_and_sell_stock_once(arr)) # 
