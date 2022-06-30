from datetime import datetime
import pandas as pd
import numpy as np

read_csv = pd.read_csv(r"C:\Users\admin\Desktop\data.csv")
# print(read_csv)
# data_ranges
# date_of_forecast_month
df = pd.DataFrame(read_csv)

# df['date_of_forecast_month'] = pd.to_datetime(df['date_of_forecast_month'], format='%m-%d-%Y')
# df['data_ranges'] = pd.to_datetime(df['data_ranges'], format='%m-%d-%Y')

# if df['date_of_forecast_month'] == df['data_ranges']:
    
df2 = np.where(df.date_of_forecast_month == df.data_ranges, 1,0)
df['diff'] = df2
print(df)






'''




Compare two date columns and validate if DateA is earlier than DateB:(imp)
https://stackoverflow.com/questions/48528084/compare-two-date-columns-and-validate-if-datea-is-earlier-than-dateb
============================================================================
Comparing Timestamp in Python – Pandas:

https://www.geeksforgeeks.org/comparing-timestamp-in-python-pandas/

============================================================================

How to compare two date columns in a dataframe using pandas?
https://stackoverflow.com/questions/71161553/how-to-compare-two-date-columns-in-a-dataframe-using-pandas


Compare 2 columns in same excel sheet in pandas:(imp)
https://stackoverflow.com/questions/71016184/compare-2-columns-in-same-excel-sheet-in-pandas







'''
