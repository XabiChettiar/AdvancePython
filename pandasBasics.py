import pandas as pd

data={
    'name':['xabi','celina','cupcake','bubu','cutu','putu'],
    'marks':[85,90,75,54,89,98]
}


df=pd.DataFrame(data)

print(df.describe())