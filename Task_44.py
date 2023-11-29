import random
import pandas as pd 

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)
print()
data[''] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=1, fill_value=0).astype(int)
data.columns = data.columns.droplevel()
print(data)

 