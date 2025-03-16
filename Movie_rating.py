
import numpy as np 
import pandas as pd 

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import warnings
warnings.filterwarnings('ignore')

data =  pd.read_csv('./IMDB-Movie-Data.csv')

data.head(10)

data.tail(10)

data.shape

print('Number of Rows',data.shape[0])
print('Number of Columns',data.shape[1])

data.info()

data.isnull().sum()

import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(data.isnull())
plt.show()

data = data.dropna(axis=0)

sns.heatmap(data.isnull())
plt.show()

dup_data=data.duplicated().any()
print("Are there any duplicated values in data?",dup_data)

data.describe()

data[data['Runtime (Minutes)']>=180]['Title']

sns.barplot(x='Year',y='Votes',data=data)
plt.title("Votes By Year")
plt.show()

sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.title("Revenue By Year")
plt.show()

data.groupby('Director')['Rating'].mean().sort_values(ascending=False)

le =data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']]. \
set_index('Title')

sns.barplot(x=le['Runtime (Minutes)'],y=le.index)
plt.title('Top 5 Lengthy Movies')
plt.show()

sns.countplot(x='Year',data=data)
plt.title("Number of Movies Per Year")

data.columns

data[data['Revenue (Millions)'].max() == data['Revenue (Millions)']]['Title']

top_10=data.nlargest(10,'Rating')[['Title','Rating','Director']].set_index('Title')

top_10

sns.barplot(x=top_10['Rating'],y=top_10.index)
plt.title("Display Top 10 Highest Rated Movie Titles")

data.columns

data.sort_values(by='Revenue (Millions)',ascending=False).head(10)

top_10 = data.nlargest(10,'Revenue (Millions)')[['Title','Director','Revenue (Millions)']].set_index('Title')

sns.barplot(x=top_10['Revenue (Millions)'],y=top_10.index)
plt.title("Display Top 10 Highest Revenue Movie Titles")
plt.show()

data.columns

data1=data.groupby('Year')[['Year','Rating']].mean().\
sort_values(by='Rating',ascending=False).set_index('Year')

data1

plt.figure(figsize=(10,5))
sns.barplot(x=data1.index,y=data1['Rating'])
plt.show()

sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)

data.columns

def rating(rating):
    if rating>=7.0:
        return 'Excellent'
    elif rating>=6.0:
        return 'Good'
    else:
        return 'Average'

data['rating_cat']=data['Rating'].apply(rating)

data.head(1)

list1=[]
for value in data['Genre']:
    list1.append(value.split(','))

data['temp']=list1

genre=input("Enter Genre you want to count : ").title()
count=0
for value in data['temp']:
    if genre in value:
        count=count+1
print("Total Count is",count)

len(data[data['Genre'].str.contains('action',case=False)])
