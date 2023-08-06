import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

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
                        print(rslt_df)   
                        break
            i+=1
