import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('data.csv')



df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')

#Numaric Columns cleaning
df['price']=df['price'].astype(str).str.replace(',','').astype(float)
df['area']=df['area'].astype(str).str.replace(',','').astype(int)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(',','').astype(float)


#Cleaning Category columns
df['status']=df['status'].str.strip().str.lower()
# df['rera_approval']=df['rera_approval'].str.strip().str.lower().map({'Approved by RERA' : True, 'Not approved by RERA' : False})
df['rera_approval']=df['rera_approval'].str.strip().map({'Approved by RERA' : True, 'Not approved by RERA' : False})
df['flat_type']=df['flat_type'].str.strip().str.lower()

df=df.drop_duplicates()

# print(df)
print(df.info())


#Question 1: Which is the costliest flat?

costliest_flat=df.loc[df['price'].idxmax()]
print(costliest_flat)



#Question 2: Which locality has the highest average price?

highest_avgPrice=df.groupby('locality')['price'].mean().idxmax()

print(f'\n\nlocality with the highest avg price is {highest_avgPrice}')



#Question 3: Which locality has the highest rate per square foot?

highest_rate_per_squarefeet =df.groupby('locality')['rate_per_sqft'].mean().idxmax()

print(f'\n\nlocality with the highest avg price is {highest_rate_per_squarefeet}')


#Question 4: Ready-to-move vs Under-construction pricing

meanReadyToMove=df[df['status']=='ready to move']['price'].mean()
meanUnderConstruction=df[df['status']=='under construction']['price'].mean()


if (meanReadyToMove > meanUnderConstruction):
    print('\nready to move is costlier')
else:
    print('\nunder construction is costlier')
