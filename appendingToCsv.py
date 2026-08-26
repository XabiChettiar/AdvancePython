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


df.to_csv('newEcom.csv', mode='a', index=False)