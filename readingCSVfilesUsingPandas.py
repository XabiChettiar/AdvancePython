import pandas as pd

# df=pd.read_csv('data.csv')
# df=pd.read_csv('data.csv', usecols=['customer_name' , 'product'])
# print(df)

# deliveredOrders=df[(df['order_status']=='Cancelled') & (df['city']=='Delhi')]

# print(deliveredOrders)


newData = pd.read_excel('newData.xlsx', sheet_name='Sheet2')

print(newData)