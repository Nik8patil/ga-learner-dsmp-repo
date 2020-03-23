# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
data['Rating'].plot(kind='hist')
data = data[data['Rating']<=5]
data['Rating'].plot(kind='hist')
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = total_null/data.isnull().count()
missing_data = pd.concat([total_null, percent_null], keys = ['Total','Percent'],axis=1)
print(missing_data)

data.dropna(inplace=True)
total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1/data.isnull().count()
missing_data_1 = pd.concat([total_null_1, percent_null_1], keys = ['Total','Percent'],axis=1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here

a = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
a.fig.suptitle('Rating vs Category [BoxPlot]')
a.set_xticklabels(rotation=90)
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
'''
#Code starts here
data.Installs.value_counts()

data['Installs']=data['Installs'].str.replace('+','')
data['Installs']=data['Installs'].str.replace(',','')
#data['Installs'].apply(lambda x: x.strip(','))
#print(data['Installs'])
data['Installs'] = data['Installs'].apply(pd.to_numeric)
#df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)
le = LabelEncoder()
le.fit(data['Installs'])
le.transform(data['Installs'])

b = sns.regplot(x="Installs", y="Rating", data=data).set(title = 'Rating vs Installs [RegPlot]')
#b.fig.suptitle('Rating vs Installs [RegPlot]')

#Code ends here
'''

#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#Removing `,` from the column
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)

#Code ends here




# --------------
#Code starts here

print(data['Price'].value_counts())

data['Price']=data['Price'].str.replace('$','')

data['Price'] = data['Price'].apply(pd.to_numeric)

a = sns.regplot(x="Price", y="Rating", data=data).set(title = 'Rating vs Price [RegPlot]')

#Code ends here


# --------------

#Code starts here
print(data['Genres'].unique)

data['Genres'] = data['Genres'].str.split(";", n = 1, expand = True) 
gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()
gr_mean.describe()
gr_mean = gr_mean.sort_values(by='Rating')
#Code ends here


# --------------

#Code starts here
print(data['Last Updated'])
data['Last Updated'] =  pd.to_datetime(data['Last Updated'])
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated'] ).dt.days

sns.regplot(x="Last Updated Days", y="Rating", color = 'lightpink',data=data )

#Setting the title of the plot
plt.title('Rating vs Last Updated [RegPlot]',size = 20)
#Code ends here


