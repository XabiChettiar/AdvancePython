import pandas as pd

df = pd.DataFrame({
    'order_id': ['ORD-1001', 'ORD-1002', 'ORD-1003', 'ORD-1004', 'ORD-1005', 'ORD-1006'],
    'order_date': ['2026-08-01', '2026-08-02', '2026-08-03', '2026-08-04', '2026-08-05', '2026-08-06'],
    'customer_name': ['Aisha Khan', 'Daniel Brooks', 'Meera Patel', 'Lucas Martin', 'Sofia Garcia', 'Noah Wilson'],
    'product': ['Wireless Headphones', 'Running Shoes', 'Stainless Steel Bottle', 'Laptop Backpack', 'Organic Cotton T-Shirt', 'Smart LED Desk Lamp'],
    'category': ['Electronics', 'Sportswear', 'Home & Kitchen', 'Accessories', 'Clothing', 'Home & Kitchen'],
    'quantity': [1, 2, 3, 1, 2, 1],
    'unit_price': [89.99, 64.50, 22.00, 48.75, 19.99, 35.00],
    'payment_method': ['Credit Card', 'PayPal', 'Debit Card', 'Credit Card', 'Apple Pay', 'PayPal'],
    'order_status': ['Delivered', 'Shipped', 'Processing', 'Delivered', 'Cancelled', 'Shipped'],
    'city': ['New York', 'Austin', 'Chicago', 'Seattle', 'Miami', 'Denver']
})

df2 = pd.DataFrame({
    'order_id': ['ORD-2001', 'ORD-2002', 'ORD-2003', 'ORD-2004', 'ORD-2005', 'ORD-2006'],
    'order_date': ['2026-08-10', '2026-08-11', '2026-08-12', '2026-08-13', '2026-08-14', '2026-08-15'],
    'customer_name': ['Olivia Chen', 'Ethan Miller', 'Fatima Ali', 'James Taylor', 'Emma Johnson', 'Raj Sharma'],
    'product': ['Bluetooth Speaker', 'Yoga Mat', 'Ceramic Coffee Mug', 'Travel Wallet', 'Denim Jacket', 'Wireless Keyboard'],
    'category': ['Electronics', 'Sportswear', 'Home & Kitchen', 'Accessories', 'Clothing', 'Electronics'],
    'quantity': [2, 1, 4, 2, 1, 1],
    'unit_price': [54.99, 28.50, 12.75, 31.25, 79.99, 42.00],
    'payment_method': ['Debit Card', 'Credit Card', 'PayPal', 'Google Pay', 'Credit Card', 'Apple Pay'],
    'order_status': ['Delivered', 'Processing', 'Shipped', 'Delivered', 'Returned', 'Processing'],
    'city': ['Boston', 'Portland', 'San Francisco', 'Atlanta', 'Los Angeles', 'Houston']
})

# df.to_excel('ecomData.xlsx', index=False)

# print(df)


with pd.ExcelWriter('ecommerce.xlsx') as writer:
    df.to_excel(writer,sheet_name='sheet1',index=False)
    df2.to_excel(writer,sheet_name='sheet2',index=False)