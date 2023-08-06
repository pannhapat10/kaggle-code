# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os 
i = 1
search_item = 'Province_State'
search_item2 = 'Virginia'
search_item3 = 'China'
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        if filename.endswith('.csv'):
            if i == 200:
                print(namex)
                namex =  dirname+'/'+filename
                train_data = pd.read_csv(namex)
                my_list = list(train_data.columns)
                for index, item in enumerate(my_list):
                    if item == search_item:
                        rslt_df = train_data.loc[train_data['Country_Region'] == search_item3]
                        df_sum = train_data.groupby('Country_Region').agg({'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum'}).reset_index()
                        plt.stackplot(df_sum['Country_Region'], [df_sum['Confirmed'], df_sum['Deaths'], df_sum['Recovered']], labels = ['Confirmed', 'Deaths', 'Recovered'])
                        plt.legend(loc = 'upper left')
                        break
            i+=1

    
