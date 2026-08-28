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



#Question 5: Does RERA approval affect pricing?

reraApprovedMean=df[df['rera_approval']==True]['price'].mean()
reraNotApprovedMean=df[df['rera_approval']==False]['price'].mean()

if (reraApprovedMean > reraNotApprovedMean):
    print('rera approval affect pricing')
else:
    print('rera approval doesnot affect pricing')


#Question 6: How does area impact price?

# sns.scatterplot(data=df, x='area', y='price')
# plt.show()

#Question 7: Which BHK configuration is most expensive?

mostExpensiveBhk=df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f'\n The most expensive bhk is {mostExpensiveBhk}')

#Question 8: Which property type is the costliest?

mostExpensivePropertyType = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f'\n The most expensive property type is {mostExpensivePropertyType}\n')


#Question 9: Do certain builders price higher?

print(df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5))


#Question 10: Are larger homes more expensive per sqft?

sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show()