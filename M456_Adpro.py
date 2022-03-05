#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('seaborn')
sys.path.append(".")

from download import download_file

class Energy:
    
    def __init__(self, link):
        self.link = link 
    
    def dowload(self):
        self.data = download_file(self.link, "Energy.csv")
        return self.data


# In[2]:


x = Energy("https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv")


# In[3]:


DF = x.dowload()


# In[4]:


#DF


# In[5]:


#DF.filter(like = "_consumption")


# ###################
# 
# # METHOD 4 + 5 + 6
# 
# 

# In[6]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('seaborn')


# In[7]:


DF_consumption = DF.filter(like = "_consumption") #get the df of the consumption columns
DF_country = DF[["country"]]#get the df of the country column

#merge the two dfs into 'df' having the columns of country and all the consumptions
df = pd.merge(DF_country, DF_consumption, left_index = True, right_index = True)

#group by countries and compute the averge of each consumption over the years
#'new_df' having index label as country and counsumptions columns
new_df = df.groupby("country").mean()

#compute the sum of all consumptions into TOTAL
new_df["TOTAL_energy_consumption"] = new_df.iloc[:,:].sum(axis = 1)
final_DF = new_df[["TOTAL_energy_consumption"]]
FDF = final_DF.reset_index()


#METHOD 4
def energy_compare (countries):
    
    """
    Takes a list of countries and iterates over it to find the\
    respective value in the dataset for the total energy consumed\
    
    Appends each country element to loca : list
    Appends each value of that country's consumption to val : list
    
    Plot a barchart of each country in the list and their\
    energy consumption for the sake of comparison

    Parameters
    ---------------
    countries: list
        list of country strings
        
    Output
    ---------------
    figure: BarContainer
        compare the total consumption of each country
    """
    
    loca = []
    val = []
    for country in countries:
        e = FDF[FDF["country"] == country]["TOTAL_energy_consumption"].values[0]
        loca.append(country)
        val.append(e)
        
    fig = plt.figure(figsize = (10, 5))
 
    plt.bar(loca, val, color ='purple', width = 0.8)
 
    plt.xlabel("Countries")
    plt.ylabel("Energy Consumption")
    plt.title("Total Energy consumption per Country")
    plt.show()
    
        


# In[8]:


#create new dataframe made of three columns: "country", "year", and "gdp"
gdp_DF = DF[["country", "year", "gdp"]]


#METHOD 5
def gdp_compare(countries):
    
    """
    Takes a list of countries and iterates over it to create a\
    dataframe temp : DataFrame for each country and plots\
    the column "gdp" of that country over the years
    

    Parameters
    ---------------
    countries: list
        list of country strings
        
    Output
    ---------------
    figure: AxesSubplot
        compare the gdp of each country over the years
    """
    
    figure, axis = plt.subplots()
    for country in countries:
        temp = gdp_DF[gdp_DF["country"] == country]
        temp.plot(ax = axis, x = "year", y = "gdp", label = country                 ,title = "GDP of the years")
    plt.show()
    

        


# In[9]:


#'edf' having one column representing the sum of all consumptions per country per year
edf = DF.filter(like = "_consumption").sum(axis = 1).to_frame()
rdf = DF[["country", "year", "gdp", "population"]]
gapminder_df = pd.merge(rdf, edf, left_index = True, right_index = True)

#METHOD 6
def gapminder(year):
    """
    Takes an argument representing the year\
    if the argument is not an int, raises TypeError, else\
    plots scatter plot for the given year with the x-axis\
    the GDP and y-axis the total consumption. 
    the size of the scatters is proportional to the population
    
    Parameters
    ---------------
    year: int
        Year where the energy consumptions are summed and plotted
    
    Output
    ---------------
    figure: ScatterPlot
        In reference to the gapminder tool
    """
    
    if type(year) not in [int]:
        raise TypeError("variable 'Year' is not an int")
        return
    
    t = gapminder_df.groupby("year").get_group(year)
    t = t.set_axis(["country", "year", "gdp", "population", "energy"], axis = 1)
    t = t[t["country"] != "World"]
    t["population"] = (t["population"]/1000000).round(2)
    
    plt.scatter(t["gdp"],t["energy"], s=t["population"], alpha = 0.8)
    plt.xlabel("GDP of countries")
    plt.ylabel("Energy consumption")
    plt.title(f"Gapminder scatter of Energy consumed per GDP of countries in {year}")
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
    


# In[10]:


energy_compare(["Afghanistan", "Albania", "Yemen", "Morocco", "Tunisia"])


# In[11]:


gdp_compare(["Afghanistan", "Albania", "Yemen", "Morocco", "Tunisia"])


# In[12]:


gapminder(2007)


# In[ ]:


#plt.plot(te["gdp"],te["energy"] , "", linestyle='', marker='o', markersize=2) could be used for same scatters size all over


# In[ ]:




