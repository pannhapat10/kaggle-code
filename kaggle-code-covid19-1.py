# File /kaggle/input/covid19
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os 
i = 1
search_item = 'Province_State'
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
#         file_extension = filename.split(".")[-1]
#         print(file_extension)
        if filename.endswith('.csv'):
            if i == 200:
                print(namex)
                namex =  dirname+'/'+filename
                train_data = pd.read_csv(namex)
                my_list = list(train_data.columns)
                if search_item in my_list:
                    print(my_list)
                    display(train_data.head())
#                     print(f"{my_list} found in the list")
            i+=1

