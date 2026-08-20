from statistics import quantiles

import pandas as pd
from datetime import datetime, timedelta

date = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(20)]
categories = ['Electronics', 'Electronics', 'Electronics', 'Accessories'] * 5
location = ['North', 'South', 'West', 'East'] * 5
quantities = [15, 34, 45, 66, 12, 43, 23, 55, 67, 87, 98, 45, 34, 90, 31, 88, 71, 25, 5, 19]
prices = [999.99, 699.99, 459.99, 2999.99] * 5
rating = [10, 4, 5, 6, 3, 2, 4, 5, 6, 3, 2, 4, 5, 6, 3, 2, 7, 8, 9, 10]
 
data = {
     'date' : date,
     'categories' : categories,
     'location' : location,
     'quantities' : quantities,
     'prices' : prices,
     'rating' : rating
 }

df = pd.DataFrame(data)
print(df.head())