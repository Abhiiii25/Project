#!/usr/bin/env python
# coding: utf-8

# Dataset Details
# 
# This dataset has funding information of the Indian startups from January 2015 to August 2017.
# Feature Details :
# SNo - Serial number.
# Date - Date of funding in format DD/MM/YYYY.
# StartupName - Name of the startup which got funded.
# IndustryVertical - Industry to which the startup belongs.
# SubVertical - Sub-category of the industry type.
# CityLocation - City which the startup is based out of.
# InvestorsName - Name of the investors involved in the funding round.
# InvestmentType - Either Private Equity or Seed Funding.
# AmountInUSD - Funding Amount in USD.
# Remarks - Other information, if any.
# Insights -
# Find out what type of startups are getting funded in the last few years?
# Who are the important investors?
# What are the hot fields that get a lot of funding these days?
# Note :
# https://drive.google.com/file/d/1BkfhQfOB9QossPbQ6sFlYa_4SQ5UIu5Q/view
# 

# 1.Number of Fundings
# Send Feedback
# Given File 'startup_funding.csv'
# Problem Statement :
# Check the trend of investments over the years. To check the trend, find -
# Total number of fundings done in each year.
# Plot a line graph between year and number of fundings. Take year on x-axis and number of fundings on y-axis.
# Print year-wise total number of fundings also. Print years in ascending order.
# Note :
# There is some error in the 'Date' feature. Make sure to handle that.
# Output Format :
# year1 TotalFunding1
# year2 TotalFunding2
# . . . 

# In[1]:


import csv
import matplotlib.pyplot as plt
import collections
with open('startup_funding.csv', encoding ='UTF-8') as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace=True)

    dct = {}
    for row in file_data:
        year = row['Date'][-4:]
        if year in dct:
            dct[year] += 1
        else:
            dct[year] = 1
            
    ord_dct = collections.OrderedDict(sorted(dct.items()))                                  
    plt.plot(list(ord_dct.keys()),list(ord_dct.values()))
    plt.xlabel("Year")
    plt.ylabel("Number of Fundings")
    plt.title('Year VS "Number of Fundings"')
    plt.show()
    
    for i in ord_dct.keys():
        print(i,end=" ")
        print(ord_dct[i])


# 2.Top Indian Cities
# 
# Given File 'startup_funding.csv'
# Problem Statement :
# Find out which cities are generally chosen for starting a startup.
# Find top 10 Indian cities which have most number of startups ?
# Plot a pie chart and visualise it.
# Print the city name and number of startups in that city also.
# Note :
# Take city name "Delhi" as "New Delhi".
# Check the case-sensitiveness of cities also. That means - at some place, instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore".
# For few startups multiple locations are given, one Indian and one Foreign. Count those startups in Indian startup also. Indian city name is first.
# Print the city in descending order with respect to the number of startups.
# Output Format :
# city1 number1
# city2 number2
# . . . 
# 

# In[3]:


# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
#df['CityLocation'].dropna(inplace=True)
df.dropna(subset=["CityLocation"],inplace=True)
#df.tail()
def separateCity(city): 
    return city.split('/')[0].strip() 
df['CityLocation']=df['CityLocation'].apply(separateCity) 
df[df['CityLocation']=='bangalore'] = 'Bangalore'
df[df['CityLocation']=='Delhi'] = 'New Delhi'

city = df['CityLocation']
city = city.value_counts()[:10]
city_name = city.index
no_of_str = city.values

plt.pie(no_of_str, labels=city_name, autopct='%.2f%%',counterclock=False)
plt.title('Number of startup in city')
plt.axis("equal")
plt.show()

for i in range(city_name.shape[0]):
    print(city_name[i],no_of_str[i])


# 3.Funding amount
# 
# Given File 'startup_funding.csv'
# Problem Statement :
# Find out if cities play any role in receiving funding.
# Find top 10 Indian cities with most amount of fundings received. Find out percentage of funding each city has got (among top 10 Indian cities only).
# Print the city and percentage with 2 decimal place after rounding off.
# Note:
# Take city name "Delhi" as "New Delhi".
# Check the case-sensitiveness of cities also. That means - at some place, instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore".
# For few startups multiple locations are given, one Indian and one Foreign. Count those startups in Indian startup also. Indian city name is first.
# Print the city in descending order with respect to the percentage of funding.
# Output Format :
# city1 percent1
# city2 percent2
# city3 percent3
# . . . 
# . . .
# . . .

# In[4]:


# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
df.dropna(subset=["CityLocation"],inplace=True)
def separateCity(city):
    return city.split('/')[0].strip()
df['CityLocation'] = df['CityLocation'].apply(separateCity)
df['CityLocation'].replace("Delhi","New Delhi",inplace = True)
df['CityLocation'].replace("bangalore","Bangalore",inplace = True)

df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))
df = df.groupby('CityLocation')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)[0:10]
city = df.index
amount = df.values
explode = [0.2,0.2,0.2,0.2,0.1,0.1,0.2,0.2,0.2,0.2]
plt.pie(amount,labels = city,autopct='%0.2f',counterclock=False,startangle=90,explode =explode,radius=1.5)
plt.show()

percent = np.true_divide(amount,amount.sum())*100
for i in range(len(city)):
    print(city[i],format(percent[i],'0.2f'))


# 4.Investment Type
# 
# Given File 'startup_funding.csv'
# Problem Statement :
# There are 4 different type of investments. Find out percentage of amount funded for each investment type.
# Plot a pie chart to visualise.
# Print the investment type and percentage of amount funded with 2 decimal places after rounding off.
# Note :
# Correct spelling of investment types are - "Private Equity", "Seed Funding", "Debt Funding", and "Crowd Funding". Keep an eye for any spelling mistake. You can find this by printing unique values from this column.
# Print the investment type in descending order with respect to the percentage of the amount funded.
# Output Format :
# investmentType1 percent1
# investmentType2 percent2
# investmentType3 percent3
# . . . 

# In[5]:


# Open and read data file as specified in the question
# Print the required output in given format
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
df['InvestmentType'].replace('SeedFunding','Seed Funding',inplace = True)
df['InvestmentType'].replace('PrivateEquity','Private Equity',inplace = True)
df['InvestmentType'].replace('DebtFunding','Debt Funding',inplace = True)
df['InvestmentType'].replace('Crowd funding','Crowd Funding',inplace = True)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))

df = df.groupby('InvestmentType')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)[:10]
investment = df.index
amount = df.values

plt.pie(amount,labels = investment,autopct='%0.2f',counterclock=False,startangle=110)
plt.show()

percent = np.true_divide(amount,amount.sum())*100
for i in range(len(investment)):
    print(investment[i],format(percent[i],'0.2f'))


# 5.Top Industries
# 
# Given File 'startup_funding.csv'
# Problem Statement :
# Which type of companies got more easily funding. To answer this question, find -
# Top 5 industries and percentage of the total amount funded to that industry. (among top 5 only)
# Print the industry name and percentage of the amount funded with 2 decimal place after rounding off.
# Note :
# Ecommerce is the right word in IndustryVertical, so correct it.
# Print the industry in descending order with respect to the percentage of the amount funded.
# Output Format :
# industry1 percent1
# industry2 percent2
# industry3 percent3
# . . . 
# 

# In[6]:


# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
df['IndustryVertical'].replace('ECommerce','Ecommerce',inplace = True)
df['IndustryVertical'].replace('eCommerce','Ecommerce',inplace = True)
df['IndustryVertical'].replace('ecommerce','Ecommerce',inplace = True)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))
df = df.groupby('IndustryVertical')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)[:5]
industry = df.index
amount = df.values

plt.pie(amount,labels = industry,autopct='%0.2f',counterclock=False,startangle=100)
plt.show()
percent = np.true_divide(amount,amount.sum())*100
for i in range(len(industry)):
    print(industry[i],format(percent[i],'0.2f'))


# 6.Top startups
# 
# Given File 'startup_funding.csv'
# Problem Statement :
# Find top 5 startups with most amount of total funding.
# Print the startup name in descending order with respect to amount of funding.
# Note:
# Ola, Flipkart, Oyo, Paytm are important startups, so correct their names. There are many errors in startup names, ignore correcting all, just handle important ones.
# Output Format :
# startup1
# startup2
# startup3
# . . . 

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
df['StartupName'].replace('Oyorooms','Oyo',inplace = True)
df['StartupName'].replace('OyoRooms','Oyo',inplace = True)
df['StartupName'].replace('Oyo Rooms','Oyo',inplace = True)
df['StartupName'].replace('OYO Rooms','Oyo',inplace = True)
df['StartupName'].replace('Olacabs','Ola',inplace = True)
df['StartupName'].replace('Ola Cabs','Ola',inplace = True)
df['StartupName'].replace('Olacabs','Ola',inplace = True)
df['StartupName'].replace('Flipkart.com','Flipkart',inplace = True)
df['StartupName'].replace('Paytm Marketplace','Paytm',inplace = True)

df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))
df = df.groupby('StartupName')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)[:5]
startup = df.index
for i in range(5):
    print(startup[i])


# 7.Funding rounds
# 
# Given File 'startup_funding.csv'
# Problem Statement :
# Find the top 5 startups who received the most number of funding rounds. That means, startups which got fundings maximum number of times.
# Print the startup name in descending order with respect to the number of funding round as integer value.
# Note:
# Ola, Flipkart, Oyo, Paytm are important startups, so correct their names. There are many errors in startup names, ignore correcting all, just handle important ones.
# Output Format :
# startup1 number1
# startup2 number2
# startup3 number3
# . . . 
# 

# In[8]:


# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np
import collections

df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
df.InvestorsName.fillna("",inplace = True)
investors = df.InvestorsName

investors_name = []
for i in investors:
    if i != "":
        temp = i.split(",")
        for j in temp:
            investors_name.append(j.strip())
dct = {}
for i in investors_name:
    dct[i] = dct.get(i,0) + 1
for i in dct:
    print(i, dct[i])
dct_keys = sorted(dct,key=dct.get,reverse=True)
print(dct_keys[0],dct[dct_keys[0]])


# 8.Top Investor
# 
# Given File 'startup_funding.csv'
# Problem Statement :
# Find the Investors who have invested maximum number of times.
# Print the investor name and number of times invested as integer value.
# Note:
# In startup, multiple investors might have invested. So consider each investor for that startup.
# Ignore the undisclosed investors.
# Output Format :
# investorname number

# In[9]:


# Open and read data file as specified in the question
# Print the required output in given format
import pandas as pd
import numpy as np
import collections

df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
df.InvestorsName.fillna("",inplace = True)
investors = df.InvestorsName

investors_name = []
for i in investors:
    if i != "":
        temp = i.split(",")
        for j in temp:
            investors_name.append(j.strip())
dct = {}
for i in investors_name:
    dct[i] = dct.get(i,0) + 1
#for i in dct:
 
    #print(i, dct[i])
dct_keys = sorted(dct,key=dct.get,reverse=True)
print(dct_keys[0],dct[dct_keys[0]])

